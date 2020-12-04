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

im = fits_hdulists[0][1].data
plt.figure(figsize=(12, 12))
plt.imshow(im, norm=LogNorm(), cmap="hot",
           vmin=0.7 * np.median(im), vmax=3 * np.median(im))

plt.plot([744, 1000], [50, 50], c="k", lw=3)
plt.text(872, 60, '1"', verticalalignment="top", horizontalalignment="center", fontsize=24)
plt.tick_params(axis="both", which="both", bottom=False, labelbottom=False, left=False, labelleft=False)

plt.tight_layout()
plt.savefig("../images/example_1_star_cluster_micado.png")
# plt.show()




