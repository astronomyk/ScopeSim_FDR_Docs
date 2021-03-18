Science package use case examples
---------------------------------




Pipeline package use case examples
----------------------------------



IMG: Extended Sources (4mas, MCAO, Ks filter)
+++++++++++++++++++++++++++++++++++++++++++++
Should show how to use the science package (MICADO_Sci)

- a resolved spiral galaxy (FITS image) with ~10 background elliptical galaxies (analytical profiles)
    - scopesim_templates.basicgalaxy.two_component_spiral
    - MICADO_Sci package
    - windowed detector
    - 4mas MCAO field constant PSF
    - Ks filter
    - NDIT = 60
    - DIT = 60

IMG: Point source (4mas, SCAO, J filter, Field-varying PSFs)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Should show how to use the pipeline package (MICADO). Therefore should also show detector characteristics like linearity, and noise, etc

- a resolved star cluster (e.g. similar 30 Dor in LMC)
    - scopesim_templates.basic.stars.cluster
    - MICADO package
    - full detector layout
    - 4mas SCAO field varying PSF
    - J filter
    - NDIT = 1
    - DIT = 60

IMG: Astrometric sub-pixel shifts (1.5mas, SCAO, Pa-Beta  filter)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Astrometry use case with MICADO_Sci package.
Two epoch observations of a resolved star cluster with sub-pixel level shifts in the star positions
This will need a tiny field of view (like 64x64 pixels)

- a resolved star cluster (e.g. similar 30 Dor in LMC)
    - scopesim_templates.basic.stars.stars - random distribution of stars in both spatial and brightness
    - MICADO_Sci package
    - tiny window layout (64x64 pixel)
    - 1.5mas SCAO CONSTANT PSF
    - PaBeta filter
    - NDIT = 1
    - DIT = 60

- Generate a group of stars with different velocities
- Observe the group at two epochs
- Extract the positions and show change in position


SPEC 20x3000, J, slit at 45 deg to zenith
+++++++++++++++++++++++++++++++++++++++++
Binary stars with MICADO_Sci producing spectra

- binary star system of two A0V stars with shifted spectral features
    - scopesim_templates.basic.stars.stars - 2 stars
    - IJ_SPEC filter
    - 3000x20mas slit
    - NDIT = 1
    - DIT = 3600


SPEC 50x15000, HK, slit aligned with parallactic angle, no ADC
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
possible elliptical galaxy with velocity gradient
- HK SPEC 15000x50mas slit, (slow) pipeline mode --> TBD , possible elliptical galaxy with velocity gradient




HCI (not yet implemented)
+++++++++++++++++++++++++
- possibly a HCI example with a large warning sign that HCI is a complex monster and that this example is purely for illustrative purposes.




.. _SimCADO: https://simcado.readthedocs.io/en/latest/
.. _ScopeSim: https://scopesim.readthedocs.io/en/latest/
.. _IRDB: https://github.com/astronomyk/irdb
.. _ScopeSim_Templates: https://scopesim-templates.readthedocs.io/en/latest/
