Science package use case examples
---------------------------------

- 4mas MCAO field constat PSF, windowed detector --.> a resolved spiral galaxy (FITS image) with background elliptical galaxies (analytical profiles)
- 4mas SCAO field varying PSF, full detector --> a resolved star cluster (e.g. 30 Dor in LMC)
- 1.5mas SCAO astrometric imaging --> two epoch observations of a resolved star cluster with sub-pixel level shifts in the star positions
- IJ SPEC 3000x20mas slit, (quick rectified ) science-team mode, --> target TBD, possible binary star system
- HK SPEC 15000x50mas slit, (slow) pipeline mode --> TBD , possible elliptical galaxy with velocity gradient
- possibly a HCI example with a large warning sign that HCI is a complex monster and that this example is purely for illustrative purposes.


IMG: Extended Sources (4mas, MCAO, Ks filter)
+++++++++++++++++++++++++++++++++++++++++++++
- View a galaxy with star formation regions over the middle MICADO detector
- Use a strehl ratio of 35% in the Ks-filter
- Observe for 60 x 60s DITs and stack them

IMG: Point sources (1.5mas, SCAO, Pa-Beta filter)
+++++++++++++++++++++++++++++++++++++++++++++++++
- View a cluster of stars in the central detector
- Use a field varying PSF, with strehl of 20% in J, dropping off with radius from centre

IMG: Astrometric sub-pixel shifts (1.5mas, SCAO, J filter)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
- Generate a group of stars with different velocities
- Observe the group at two epochs
- Extract the positions and show change in position

SPEC 50x15000, HK, slit aligned with parallactic angle, no ADC
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


SPEC 20x3000, J, slit at 45 deg to zenith
+++++++++++++++++++++++++++++++++++++++++

HCI (not yet implemented)
+++++++++++++++++++++++++
- possible hack to get this working




.. _SimCADO: https://simcado.readthedocs.io/en/latest/
.. _ScopeSim: https://scopesim.readthedocs.io/en/latest/
.. _IRDB: https://github.com/astronomyk/irdb
.. _ScopeSim_Templates: https://scopesim-templates.readthedocs.io/en/latest/
