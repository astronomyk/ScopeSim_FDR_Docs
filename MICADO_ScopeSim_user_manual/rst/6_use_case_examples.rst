Use case examples using the MICADO_Sci and MICADO instrument packages
---------------------------------------------------------------------
This section presents a series of 5 use case examples for both the science-team oriented ``MICADO_Sci`` package and the pipeline oriented ``MICADO`` package.
All example are available as iPython notebooks as part of the ScopeSim_ online documentation.
Please note that no scientifically relevant information is extracted from these simulations.
The sole purpose of the attached notebooks is to illustrate how to run ScopeSim with the two MICADO packages.

- Observing a galaxy with MICADO_Sci in wide-field MCAO mode:

  This example shows how to use the science package to observe a resolved spiral galaxy using the ``scopesim_templates.basicgalaxy.two_component_spiral`` function.
  It uses a windowed detector object to avoid simulating the full MICADO detector array.
  The pixel scale is set to 4mas (low resolution imaging) and a MCAO field constant PSF is used.
  The galaxy is observed for 1 hour (60x 60s images) in the J filter.


IMG: Point source (4mas, SCAO, J filter, Field-varying PSFs)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
