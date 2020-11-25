from scopesim import rc
rc.__currsys__["!SIM.file.local_packages_path"] = "C:/Work/irdb/"

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm

import scopesim
import scopesim_templates

# ------

cluster = scopesim_templates.basic.stars.cluster(mass=3e3,          # solar masses
                                                 distance=50e3,     # parsec
                                                 core_radius=0.3)   # parsec
micado = scopesim.OpticalTrain("MICADO_Sci")
micado.cmds["!OBS.dit"] = 3600      # seconds
micado.observe(cluster)
fits_hdulists = micado.readout()

# ------


plt.figure(figsize=(12, 6))
plt.subplots_adjust(hspace=0.)

ax2 = plt.subplot(122)
# ax2.set_position([0.5, 0.05, 0.45, 0.9])

im = fits_hdulists[0][1].data
plt.imshow(im, norm=LogNorm(), cmap="hot",
           vmin=0.9 * np.median(im), vmax=3 * np.median(im))

plt.plot([718, 974], [50, 50], c="w", lw=3)
plt.text(846, 60, '1"', verticalalignment="top", horizontalalignment="center", fontsize=24, color="w")
plt.tick_params(axis="both", which="both", bottom=False, labelbottom=False, left=False, labelleft=False)

# ------

spiral = scopesim_templates.basic.galaxy.spiral_two_component(extent=180, fluxes=(15, 12))  # arcsec
hawki = scopesim.OpticalTrain("HAWKI")
hawki.cmds["!OBS.dit"] = 1                      # seconds
hawki.observe(spiral)
hdu = hawki.readout()

# ------

ax1 = plt.subplot(121)
# ax1.set_position([0.05, 0.05, 0.45, 0.9])

im = hdu[0][1].data

plt.imshow(im, norm=LogNorm(), cmap="hot_r",
           vmin=0.97 * np.median(im), vmax=1.07 * np.median(im))

plt.plot([50, 333], [50, 50], c="k", lw=3)
plt.text(178, 60, '30"', verticalalignment="top", horizontalalignment="center", fontsize=24)
plt.tick_params(axis="both", which="both", bottom=False, labelbottom=False, left=False, labelleft=False)

plt.tight_layout()
plt.savefig("../images/combined_1_2.png")
plt.savefig("../images/combined_1_2.pdf", format="pdf")
plt.show()
