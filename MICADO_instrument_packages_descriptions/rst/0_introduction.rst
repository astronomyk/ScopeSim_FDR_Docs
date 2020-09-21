Overview of the Instrument Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The MICADO instrument simulator has moved from using the stand alone SimCADO package to using the generic astronomical instrument simulator ScopeSim.
As the ScopeSim code is instrument agnostic, all data related to creating instrument models are contained inside instrument packages, which are hosted on the `instrument reference database (IRDB)`__.

__ IRDB_


Primary MICADO packages
#######################

This document is primarily concerned with describing the contents of the two major MICADO instrument descriptions: ``MICADO`` and ``MICADO_Sci``.
These two packages serve two different audiences:

1. The ``MICADO`` package contains all information available pertaining to the optical effects expected for the MICADO optical system.
   The primary user of this package will be the data flow system.
   The primary use case for this package is the creation of raw data frames for testing the algorithms of the reduction pipelines for the different modes of MICADO.
   This package is large and therefore computationally expensive and slow.
2. The ``MICADO_Sci`` package contains a subset of the effects in the ``MICADO`` package.
   The primary users of this package will be the science team and outside astronomers interested in simulating observations with the future MICADO instrument.
   The goal of this package is enable observations to be simulated quickly, so that the user can quickly iterate on observation strategies and/or target choices.
   As such this package contains only the effects which cause the major optical aberrations.
   It is by nature not complete, but aims to provide a level of detail sufficient for the majority of observation feasibility studies for MICADO


Support packages
################
The MICADO packages, as the names suggest, only describe the contents of the MICADO instrument.
Observations with MICADO will however rely on the ELT infrastructure, which can be decomposed into several parts: Location, Telescope, Relay optics.
Each of these additional parts can be considered as closed optical elements in the full observational optical system.
Indeed the relay optics element is a replacable element in the optical path (with MAORY vs stand-alone mode)
Hence each of these optical elements have been given their own instrument package, and are referred to as support packages.

The support packages needed to simulate MICADO observations are also described in this document. Specifically these are:

- Armazones
- ELT
- MAORY
- Stand-alone relay optics

For each observation the Armazones and ELT packages are required. However only one of MAORY or the stand-alone relay optics packages are required.


Adding content to the packages
##############################

The contents of the packages are currently in the public domain.
The raw data is `hosted on Github`__.

__ IRDB_

Periodically this data is compiled into an instrument package and uploaded to the ScopeSim server.
It is these packages which are downloaded by ScopeSim when setting up an observation simulation.

New data or Effect objects can be added by submitting a pull request to the `Github repository`__.

__ IRDB_


Contents of packages
^^^^^^^^^^^^^^^^^^^^

Each package contains three types of files:

1. configuration,
2. effect descriptions, and
3. raw data

The configuration files are responsible for controlling which effects and which parameters and values are used when generating the optical model for an observation simulation
The effect files describe which classes and which values should be used when applying an effect to the photon flux of the target object, e.g. which PSF kernel should be applied at which wavelength
The raw dta files provide the raw data needed by the Effect objects, e.g. the bitmaps of the PSF kernels

In the following sections each optical element is described.
Each optical elements contains a description of all the optical Effects associated with it, as well as a list of the configuration keywords and values required by the effect.
If an Effect required data from an external file (e.g. PSF kernels, linearity curves, etc), these data are presented as part of each Effect object - either in the ``Table`` or ``Data`` sections.

.. note:: The raw data will not always be displayed directly.

   A representation of the data will be presented where available.
   For further details the reader is directed to the view the data directly on the IRDB_


.. _IRDB: https://github.com/astronomyk/irdb