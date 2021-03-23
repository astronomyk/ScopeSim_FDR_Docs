Controlling a simulation
------------------------

A note on the two MICADO packages
+++++++++++++++++++++++++++++++++

It should be noted that there are two MICADO packages available:

1. MICADO_Sci: optimised for quick run times to enable rapid iterations of science feasibility use cases
2. MICADO: the generalised package containing all the known optical effects needed by the pipeline development team.

In general science team members are recommended to use the MICADO_Sci package as the generalised MICADO is slower and exposes many more configuration parameters to the user.

Both packages **still** require all upstream support packages, namely: Armazones, ELT, and MAORY.


Available MICADO observing modes
++++++++++++++++++++++++++++++++

As mentioned in the previous sections there are two MICADO models available: MICADO_Sci and MICADO.
The desired model is selected with the ``use_instrument=`` parameter::

    cmd = scopesim.UserCommands(use_instrument="MICADO_Sci", ...)

The choice of observing modes can be set when the ``UserCommand`` object is initialised by passing a list of mode names to the ``set_mode=`` parameter.
Note that multiple keywords can be passed as different modes for different optical sections can be combined.
For example, using the MAORY relay optics with the MICADO wide-field imaging mode requires the following input::

    cmd = scopesim.UserCommands(..., set_modes=["MCAO", "IMG_4mas"])

In contrast, to use the MICADO internal SCAO mode with the zoom imaging mode, the following input is required::

    cmd = scopesim.UserCommands(..., set_modes=["SCAO", "IMG_1.5mas"])

The following table lists all available mode keywords for MICADO.

============= ===
Keyword       Description
============= ===
MCAO          MAORY relay optics model is included
SCAO          MICADO SCAO relay optics module is included
IMG_4mas      Wide-field imaging optics included. Images have 4mas pixel scale.
IMG_1.5mas    Zoom imaging optics included. Images have 1.5mas pixel scale.
SPEC          'MICADO_Sci' package only. Produces rectified spectroscopic images.
SPEC_3000x20  'MICADO' package only. Produces full raw detector traces for the short-narrow slit (3000x20mas)
SPEC_3000x50  'MICADO' package only. Produces full raw detector traces for the short-wide slit (3000x50mas)
SPEC_15000x50 'MICADO' package only. Produces full raw detector traces for the long-wide slit (15000x50mas)
============= ===

.. note::  while the imaging mode names are consistent between the MICADO_Sci and MICADO packages, the spectroscopy mode names differ.


Setting top level observation parameters
++++++++++++++++++++++++++++++++++++++++

The ``UserCommands`` object is built on several hierarchical (YAML-style) nested dictionaries which contain all the information needed to build the optical model of MICADO.
Checking and changing parameters in these dictionaries is done using the so-called "bang-string" notation.
Bang-strings shorten the syntax for accessing nested dictionaries.
E.g. ``cmd["!OBS.ndit"]`` is the equivalent of ``cmd["OBS"]["ndit"]``

Alternatively, a dictionary of bang-string keyword-value pairs can be passed to the ``UserCommands`` object when initialising via the ``properties`` keyword::

    scopesim.UserCommands(..., ..., properties={"!OBS.dit": 60, "!OBS.ndit": 10})

The following table describes the top level parameter categories.

===== ===
Alias Description
===== ===
OBS   Instrument specific parameters. E.g. exposure time and number (DIT, NDIT), filter name, etc
ATMO  Atmospheric specific parameters. E.g. air temperature, background brightness, location, etc
TEL   Telescope specific parameters. E.g. Dome temperature, etc
RO    Relay optics specific parameters. E.g. RO module temperature, etc
INST  Instrument specific parameters. E.g. plate scale, strehl ratio (MICADO_Sci only), etc
DET   Detector specific parameters. E.g. windowing dimensions and position (MICADO_Sci only), etc
SIM   Instrument specific parameters. E.g. spectral range, computing parameters, file locations, etc
===== ===

.. note:: Important parameters like which filter to use and how long to observe for are generally kept in the ``"!OBS"`` dictionary

The whole parameter dictionary can be shown by simply printing the ``UserCommand`` object::

    print(cmd)

Specific categories can be shown by using the category alias in the bang string format::

    print(cmd["!OBS"])

A specific parameter (or sub-group thereof) can be shown by following the hierarchy in bang-string format::

    print(cmd["!INST.psf.strehl"])

Parameter values can also be set in this manner.
For example, to set which filter to use with MICADO, we call the ``"OBS.filter_name`` keyword::

    cmd["!OBS.filter_name"] = "Ks"

.. note:: The full list of filters available in MICADO is kept in the ``OpticalTrain`` object. This will be discussed below.

The following list contains some commonly used parameters for the ``MICADO_Sci`` package::

    MICADO_Sci
    ==========

    OBS.filter_name: "J"                    # MICADO filter name
    OBS.dit: 60                             # [s] Length of exposure
    OBS.ndit: 1                             # Number of exposures to stack
    OBS.airmass: 1.2

    ATMO.background.filter_name: "Ks"
    ATMO.background.value: 13.6             # Amplitude of background flux
    ATMO.background.unit: "mag"             # Unit of background flux

    INST.psf.strehl: 0.8                    # Desired Strehl ratio (as far as physically possible)
    INST.psf.wavelength: "Ks"               # Either wavelength [um] or common broadband filter name
    INST.aperture.x: 0                      # [arcsec] (MICADO_Sci only) The slit position relative to FOV centre
    INST.aperture.y: 0
    INST.aperture.width: 3                  # [arcsec] (MICADO_Sci only) The slit dimensions
    INST.aperture.height: 0.05

    DET.width: 1024                         # [pixel] Detector dimensions
    DET.height: 1024
    DET.x: 0                                # [pixel] Position of window centre relative to detector plane centre
    DET.y: 0

    SIM.spectral.wave_min: 0.7              # [um] Spectral borders of simulation
    SIM.spectral.wave_mid: 1.6              # [um] Central wavelength for SPEC mode
    SIM.spectral.wave_max: 2.5
    SIM.sub_pixel.flag: False               # Turn on for astrometry observation
    SIM.random.seed: 9001                   # Random seed for numpy to aid reproducibility
    SIM.file.use_cached_downloads: True     # Turn off when checking for updates

The spectroscopy mode of the ``MICADO_Sci`` package contains a configurable slit and detector window.
This allows the user to choose only the spectral range that is relevant to their science case.
Restricting the spectral range like this speeds up the computation time by order and allows for fast iterations of science use cases.
The pipeline-oriented ``MICADO`` package contains fixed slit dimensions and spectral trace layouts.
Simulations run using this setup are slow and memory intensive.


The MICADO filter settings
++++++++++++++++++++++++++

To set the filter name, we use the ``!OBS.filter_name`` bang-string.

To find out which filters are included in the MICADO_Sci and MICADO packages, we must create an OpticalTrain model for MICADO::

    cmd = scopesim.UserCommands(use_instrument="MICADO_Sci")
    micado = scopesim.OpticalTrain(cmd)

In the ``MICADO_Sci`` package all filters are contained in a single ``filter_wheel`` object::

    micado["filter_wheel"].data["name"]

For the pipeline-oriented ``MICADO`` package, the filters are distributed among the three filter wheels:
``filter_wheel_1``, ``filter_wheel_2``, and ``pupil_wheel``.
Hence there is no central list of all filters for the ``MICADO`` package.


The MICADO_Sci PSF model
++++++++++++++++++++++++

The ``MICADO_Sci`` package uses the AnisoCADO python package to generate ELT-like PSFs on the fly.
The Strehl ratio can therefore be set (within reason) to whatever the user desires.
The global bang-string keywords for this are ``!OBS.psf.strehl`` and ``!OBS.psf.wavelength``::

    cmd["!OBS.psf.strehl"] = 0.35
    cmd["!OBS.psf.wavelength"] = 2.15

These settings will create an on-axis PSF with a 35% Strehl ratio at 2.15um.
At shorter wavelengths the Strehl ratio will scale as expected.
If a Strehl ratio is physically impossible (e.g. 80% at 0.9um), the largest PSF will be generated with the best physically possible Strehl ratio.

It is possible to also create PSF models for off-axis positions in SCAO mode.
The offset can only be specified after the ``OpticalTrain`` model has been created by accessing the PSF object inside the model.
The relevant MICADO ``OpticalTrain`` objects are ``scao_const_psf`` for SCAO observations and ``maory_const_psf`` for MCAO observations::

    cmd = scopesim.UserCommands(use_instrument="MICADO_Sci", set_modes=["SCAO", "IMG_4mas"])
    cmd["!OBS.psf.strehl"] = 0.35
    cmd["!OBS.psf.wavelength"] = 2.15

    micado = scopesim.OpticalTrain(cmd)
    micado["scao_const_psf"].meta["offset"] = [10, 0]

This will create an on-axis PSF with a 35% Strehl ratio at 2.15um, and then shift the 10 arcseconds off axis.
The form and Strehl ratio of the PSF will be adjusted to match what is expected for the off-axis position.

.. note:: While the ``MICADO_Sci`` PSF model is configurable, the ``MICADO`` PSF model is not.

    The ``MICADO``-package uses pre-computed PSF files. These are available on the ScopeSim server: https://www.univie.ac.at/simcado/InstPkgSvr/psfs/


..
    - Other major configuration parameters
    - filter
    - dit / ndit
    - slit size
    - zenith distance
    - psf model


.. _SimCADO: https://simcado.readthedocs.io/en/latest/
.. _ScopeSim: https://scopesim.readthedocs.io/en/latest/
.. _IRDB: https://github.com/astronomyk/irdb
.. _ScopeSim_Templates: https://scopesim-templates.readthedocs.io/en/latest/
