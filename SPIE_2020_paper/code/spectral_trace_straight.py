from scopesim import rc
rc.__currsys__["!SIM.file.local_packages_path"] = "C:/Work/irdb/"

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
# from matplotlib import rcParams
# rcParams['axes.formatter.useoffset'] = False

from astropy import units as u
from astropy.io import fits

import scopesim
import scopesim_templates

# ------

stars = scopesim_templates.basic.stars.stars(filter_name="Ks",
                                             amplitudes=np.linspace(18, 23, 6)*u.mag,
                                             spec_types=["A0V"]*6,
                                             x=np.linspace(-1, 1, 6),
                                             y=[0]*6)
cmds = scopesim.UserCommands(use_instrument="MICADO_Sci",
                             set_modes=["SCAO", "SPEC"],
                             properties={"!OBS.dit": 3600,
                                         "!SIM.spectral.wave_mid": 1.578,
                                         "!SIM.spectral.spectral_resolution": 0.00001,
                                         "!DET.height": 2048,
                                         "!DET.width": 800})
micado_spec = scopesim.OpticalTrain(cmds)
# micado_spec.observe(stars)
# hdu = micado_spec.readout(filename="basic_spectral_trace.fits")

# ------
# im = hdu[0][1].data.T
im = fits.getdata("basic_spectral_trace.fits").T

waves = [fov.wavelength.value for fov in micado_spec.fov_manager.fovs]

plt.figure(figsize=(12, 8))

ax2 = plt.subplot(212)
ax2.set_position([0.05, 0.07, 0.9, 0.33])
bg = np.median(im, axis=0)
plt.semilogy(waves, bg, "k:", label="Atmosphere")

flux = np.sum(im[145:158, :], axis=0) / 13 - bg
plt.semilogy(waves, flux, "b", label="A0V @ Ks=18$^m$")
flux = np.sum(im[349:354, :], axis=0) / 5 - bg
plt.semilogy(waves, flux, "r--", label="A0V @ Ks=20$^m$")

plt.ylim(ymin=0.5*min(bg))
plt.xlim(min(waves), max(waves))
plt.tick_params(axis="y", which="both", left=False, labelleft=False)
plt.xlabel("Wavelength [um]")
plt.legend(loc=1, fontsize=12)

ax1 = plt.subplot(211)
ax1.set_position([0.05, 0.4, 0.9, 0.55])

plt.imshow(im, norm=LogNorm(), cmap="Greys", vmin=np.min(im), vmax=10 * np.min(im), aspect="auto")
plt.tick_params(axis="both", which="both", bottom=False, labelbottom=False, left=False, labelleft=False)

plt.savefig("../images/example_3_spectra.png")
plt.savefig("../images/example_3_spectra.pdf", format="pdf")
# plt.show()




