Use case examples using the MICADO_Sci and MICADO instrument packages
---------------------------------------------------------------------

Notes regarding the worked examples
+++++++++++++++++++++++++++++++++++

.. note:: All examples listed here are available online as part of the ScopeSim_ documentation.


This section presents a series of 5 use case examples for both the science-team oriented ``MICADO_Sci`` package and the pipeline oriented ``MICADO`` package.
All example are available as iPython notebooks as part of the ScopeSim_ online documentation.
Please note that no scientifically relevant information is extracted from these simulations.
The sole purpose of the attached notebooks is to illustrate how to run ScopeSim with the two MICADO packages.

- Observing a galaxy with MICADO_Sci in wide-field MCAO mode:

  This example shows how to use the science package to observe a resolved spiral galaxy using the ``scopesim_templates.basicgalaxy.two_component_spiral`` function.
  It uses a windowed detector object to avoid simulating the full MICADO detector array.
  The pixel scale is set to 4mas (low resolution imaging) and a MCAO field constant PSF is used.
  The galaxy is observed for 1 hour (60x 60s images) in the J filter.

- Astrometric observations of an open cluster in zoom SCAO mode:

  This example shows how to enable sub-pixel resolution for simulations with the ``MICADO_Sci`` package.
  Two basic examples are shown: the sub-pixel motions of a grid of 4 stars, and the proper motions of stars in an open cluster.
  Both MICADO pixel scales (4mas and 1.5mas) are used for the example, together with the SCAO mode.
  The observations are in the J filter with an exposure time of 1 hour (1x 3600s).
  This example also makes use of the variable size of a theoretical detector sub-frame readout (window).

- Field variations in the PSF using a star cluster and wide-field SCAO mode (advanced level):

  This example shows the effects of of field dependent variations in the shape of the PSF for off-axis stars using the pipeline-oriented ``MICADO`` package.
  A standard open cluster is observed in the Ks filter for 10 minutes (1x 600s).
  The use of various detector window sizes as well as the use of the full MICADO detector array are described.
  This example also illustrates how ``Effect`` objects can be exchanged for more realistic simulation outputs.

- Basic spectroscopy observation of a galaxy core with MICADO_Sci:

  This example shows how to generate rectified images of spectra for a desired wavelength range using the ``SPEC`` mode of the ``MICADO_Sci`` package.
  The 3 arcsec slit is placed over the centre of the galaxy and observed for 1 hour using the ``Spec_IJ`` filter.
  The final output image shows distance along the slit on the horizontal axis and wavelength on the vertical axis.
  ScopeSim **does not** provide functionality for extracting spectra from the images.
  Hence it is up to the user to extract the regions corresponding to their desired spectra from this image.

- Advanced spectroscopy observation of a binary star system with MICADO:

  This example shows how to use the pipeline-oriented ``MICADO`` package to generate raw detector readouts for the MICADO spectroscopy mode.
  The spectroscopy modes in this package are not aimed towards the casual user, but rather are meant to simulate realistic raw data frames for the data reduction pipeline.
  There may however be science users who wish to have such data for their feasibility studies.
  The example observes a binary star system with the 3000x50 slit and the ``Spec_HK`` filter for 10 minutes.
  Each star ha a K-band brightness of 18 magnitudes.


A note on High Contrast Imaging simulations
+++++++++++++++++++++++++++++++++++++++++++

High contrast imaging has been described as an Artform.
It is almost impossible to define a "standard" HCI PSF.
ScopeSim and the MICADO packages work with data models that can be standardised, or at the very least be described by a low-dimensional parameter space.
As the high contrast imaging PSFs do not fit this definition, we concluded that a HCI mode was outside the scope of the ``MICADO`` and ``MICADO_Sci`` packages.
Separate HCI simulation packages are being developed by the HCI work package.
Readers interested in simulating HCI use cases should contact the relevant work package leaders.


.. _SimCADO: https://simcado.readthedocs.io/en/latest/
.. _ScopeSim: https://scopesim.readthedocs.io/en/latest/
.. _IRDB: https://github.com/astronomyk/irdb
.. _ScopeSim_Templates: https://scopesim-templates.readthedocs.io/en/latest/
