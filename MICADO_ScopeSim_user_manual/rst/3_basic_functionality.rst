Basic functionality
-------------------

A basic simulation of an ELT/MICADO observation using the MICADO_Sci package would look something like this::

    # Setup everything
    import scopesim_templates
    from scopesim.server.database import download_package
    import scopesim

    scopesim.download_package(["locations/Armazones",
                               "telescopes/ELT",
                               "instruments/MICADO_Sci"])

    # Make the on-sky target
    src = scopesim_templates.basic.stars.cluster()

    # Load the model of MICADO and the ELT
    cmd = scopesim.UserCommands(use_instrument="MICADO_Sci",
                                properties={"!OBS.dit": 60, "!OBS.ndit": 10,
                                            "!INST.filter_name": "Ks"})
    micado = scopesim.OpticalTrain(cmd)

    # Run the simulation
    micado.observe(src)
    micado.readout(filename="my_image.fits")







General Workflow
++++++++++++++++
The general workflow for simulating observations can be seen in the code in the previous section.
There are three (four) major components of any simulation workflow:

1. the target description,
2. the telescope/instrument model, and
3. the observation.

The zeroth (or fourth) step is the setup stage which include the import statements and the package downloads.

The first step of any simulation run is defining the on-sky target.
This is probably the most time intensive step and requires the user to know what they want to observe.
In the code above we make use of the ScopeSim_Templates_ package to create a ``Source`` object for an open cluster with default values (i.e. 1000 Msun at 50 kpc).::

    src = scopesim_templates.basic.stars.cluster()

``Source`` objects are discussed in a later chapter.
Here it is sufficient to note that ``Source`` objects can be created from scratch if the user has both spectral and spatial data available.
Otherwise the ScopeSim_Templates_ package contains various helper functions to aid the user in quickly generating "standard" objects.

The second step required creating an in-memory model of the optical system.
This model contains a list of effects that are applied to the incoming photon description (similar to a flux cube).::

    cmd = scopesim.UserCommands(use_instrument="MICADO_Sci",
                                properties={"!OBS.dit": 60, "!OBS.ndit": 10,
                                            "!INST.filter_name": "Ks"})
    micado = scopesim.OpticalTrain(cmd)

In this code we initialise a series of command dictionaries that control how the optical model will be built.
Any default values that we wish to override can be set by passing a dictionary to the ``properties`` keyword.
The `controlling-the-simulation`_ section goes into more detail on how to adjust these parameters.
The command dictionary (``cmd``) is used to initialise an ``OpticalTrain`` object which acts as the in-memory model of MICADO.
Here we use the ``MICADO_Sci`` optical model rather than the generic ``MICADO`` package, as the ``MICADO_Sci`` package has been optimised for speedy simulations.

The third step executes the simulation by passing the ``Source`` object through the ``OpticalTrain`` model.::

    micado.observe(src)
    micado.readout(filename="my_image.fits")

This step involves two commands:
``.observe`` generates an photon flux image (or images) on the focal plane(s) of the instrument.
``.readout`` converts the photon flux image into electrons inside the detector, and ultimately into the FITS objects that all astronomers know (and love?).
The output of this step is a FITS object available either as an ``astropy.fits.HDUList`` object inside the python environment, or as a ``.fits`` file saved to the hard drive.



.. _SimCADO: https://simcado.readthedocs.io/en/latest/
.. _ScopeSim: https://scopesim.readthedocs.io/en/latest/
.. _IRDB: https://github.com/astronomyk/irdb
.. _ScopeSim_Templates: https://scopesim-templates.readthedocs.io/en/latest/
