from astropy.io import fits
import scopesim as sim
import scopesim_templates as sim_tp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import scipy.ndimage as spi


def source_from_image(image, amplitude, pixel_scale, scale_factor=1,
                      offset=(0, 0), threshold=0):

    im_full = spi.zoom(image, scale_factor)
    im = im_full**2
    im[im < threshold] = 0
    im = im / np.sum(im)

    spec = sim_tp.utils.general_utils.vega_spectrum(amplitude)

    hdu = fits.ImageHDU(data=im)
    hdu.header["CDELT1"] = pixel_scale / 3600
    hdu.header["CDELT2"] = pixel_scale / 3600
    hdu.header["CUNIT1"] = "deg"
    hdu.header["CUNIT2"] = "deg"
    hdu.header["CRPIX1"] = im.shape[1] // 2
    hdu.header["CRPIX2"] = im.shape[0] // 2
    hdu.header["CRVAL1"] = offset[0] / 3600
    hdu.header["CRVAL2"] = offset[1] / 3600

    src = sim.Source(image_hdu=hdu, spectra=spec)

    return src


def get_sombrero():
    m101 = plt.imread("input/sombrero.jpg").sum(axis=2)
    src_m101 = source_from_image(m101, 14, 0.004, 1, (-11, 9), 3E4)
    return src_m101


def get_m101():
    m101 = plt.imread("input/m101.jpg").sum(axis=2)
    src_m101 = source_from_image(m101, 15.5, 0.004, 1, (11, -8), 3E4)
    return src_m101


def get_vesta():
    vesta_full = plt.imread("input/vesta.png")[:, :, :3].sum(axis=2)
    src_vesta = source_from_image(vesta_full, 13, 0.004, 0.16, (7, -4), 0)
    return src_vesta


# ----------------------------------- saturn
def get_saturn():
    saturn_full = plt.imread("input/saturn2.jpg").sum(axis=2)[::-1, :]
    src_saturn = source_from_image(saturn_full, 12.5, 0.004, 1, (0, 0), 1E4)
    return src_saturn


# ----------------------------------- cluster of ellipicals
def get_galaxy_cluster():
    width = 2048 * 0.004
    n_gals = 50
    x_off, y_off = (np.random.normal(0, 3, size=(2, n_gals)))
    x_off += 10
    y_off += 10
    half_lights = np.random.random(n_gals) * 10
    ellips = np.random.random(n_gals) * 0.7
    angles = np.random.random(n_gals) * 180
    sersic_n = np.random.random(n_gals) * 2 + 2
    mags = np.random.random(n_gals) * 4 + 13

    ellips = [sim_tp.basic.galaxy.elliptical(hlr, 0.004, "Ks", amplitude=m,
                                             width=width, height=width,
                                             n=n, ellipticity=e,
                                             x_offset=dx, y_offset=dy, angle=ang)
              for hlr, n, e, m, dx, dy, ang in zip(half_lights, sersic_n, ellips,
                                                   mags, x_off, y_off, angles)]

    gal_cluster = ellips[0]
    for ellip in ellips:
        gal_cluster += ellip

    return gal_cluster


# ----------------------------------- star cluster
def get_star_cluster():
    cluster = sim_tp.basic.stars.cluster(core_radius=0.3, distance=20000,
                                         mass=10000)
    cluster.fields[0]["x"] += -11
    cluster.fields[0]["y"] += -7

    return cluster


# ----------------------------------- field stars
def get_field_stars():
    fov_width_arcsec = FOV_WIDTH * 0.004
    n_bg_stars = 1000
    x, y = (np.random.random((2, n_bg_stars)) - 0.5) * fov_width_arcsec
    mags = 25 - 12 * np.random.random(n_bg_stars)**2
    bg_stars = sim_tp.basic.stars.stars("Ks", mags, ["A0V"]*n_bg_stars, x, y)
    mask = (x ** 2 + y ** 2 > 1500 * 0.004)
    bg_stars.fields[0] = bg_stars.fields[0][mask]

    return bg_stars


# make micado simulation
FOV_WIDTH = 8192
src_combined = get_vesta() + \
               get_m101() + \
               get_sombrero() + \
               get_saturn() + \
               get_star_cluster() + \
               get_galaxy_cluster() + \
               get_field_stars()


sim.rc.__currsys__["!SIM.file.local_packages_path"] = "C:/Work/irdb/"
cmds = sim.UserCommands(use_instrument="MICADO_Sci", use_modes=["SCAO", "4mas"],
                        properties={"!DET.width": FOV_WIDTH,
                                    "!DET.height": FOV_WIDTH,
                                    "!OBS.dit": 3600})
micado = sim.OpticalTrain(cmds)
micado.observe(src_combined)
hdus = micado.readout()

im = hdus[0][1].data
im = spi.zoom(im, 0.5)

plt.imsave("test.png", im, origin="lower", cmap="viridis",
           vmin=0.9 * np.median(im), vmax=10 * np.median(im))

hdus[0].writeto("TEST.fits", clobber=True)
