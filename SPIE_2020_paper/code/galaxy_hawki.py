from scopesim import rc
rc.__currsys__["!SIM.file.local_packages_path"] = "C:/Work/irdb/"

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm

import scopesim
import scopesim_templates

# ------

spiral = scopesim_templates.basic.galaxy.spiral_two_component(extent=180,       # arcsec
                                                              fluxes=(15, 12))  # mag
hawki = scopesim.OpticalTrain("HAWKI")
hawki.cmds["!OBS.dit"] = 1                      # seconds
hawki.observe(spiral)
hdu = hawki.readout()

# ------

im = hdu[0][1].data
print(np.median(im))

plt.figure(figsize=(12, 12))
plt.imshow(im, norm=LogNorm(), cmap="hot_r",
           vmin=0.97 * np.median(im), vmax=1.07 * np.median(im))

plt.plot([717, 1000], [50, 50], c="k", lw=3)
plt.text(858, 60, '30"', verticalalignment="top", horizontalalignment="center", fontsize=24)
plt.tick_params(axis="both", which="both", bottom=False, labelbottom=False, left=False, labelleft=False)

plt.tight_layout()
plt.savefig("../images/example_2_galaxy_hawki.png")
# plt.show()




