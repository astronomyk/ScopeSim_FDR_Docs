from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


def plot_all_detector_images_IJ():
    plt.figure(figsize=(15,15))

    fname = "E:/SimCADO_archive/ScopeSim_SPEC/temp_speclecado_IJ_det_all.fits"

    with fits.open(fname) as f:
        for i in range(1, 10):
            if isinstance(f[i], fits.ImageHDU):
                plt.subplot(3, 3, i)
                plt.imshow(f[i].data, norm=LogNorm())

    plt.show()


def plot_implane_images_IJ():
    plt.figure(figsize=(15, 15))
    fname = "E:/SimCADO_archive/ScopeSim_SPEC/temp_implane_IJ_det_all.fits"
    plt.imshow(fits.getdata(fname, ext=1), norm=LogNorm())
    plt.show()


plot_implane_images_IJ()

