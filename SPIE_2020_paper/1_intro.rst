Introduction
------------
ScopeSim is a modular and flexible suite of python packages that enable many common astronomical optical (observatory/telescope/instrument) systems to be simulated.
The suite of packages can be used by a wide audience for a variety of purposes; from the astronomer interested in simulating reduced observational data, to a pipeline developer needing raw calibration data for testing the pipeline.

ScopeSim achieves this level of flexibility by adhering to strict interfaces between the package, e.g: the ScopeSim engine package is completely instrument and object agnostic.
All information and data relating to any specific optical configuration is kept exclusively in the instrument packages hosted in the instrument reference database (IRDB).
The description of the on-sky source is keep exclusively within the target ``templates`` package (see ``scopesim_templates``).
Finally, the engine has no clue about what it is observing until run-time.

Why another instrument simulator
++++++++++++++++++++++++++++++++
Until now most instrument consortia have developed their own simulators.
The general consensus is that every new instrument is sufficiently different from anything that has been previously developed, that it would make little sense to adapt already existing code.
This statement is true to some extent.
Every new instrument must differ in some way from all existing instruments in order for it to be useful to the astronomical community.
However when looked at from a global perspective, every optical system is comprised primarily of elements common to all other systems.
Atmospheric emission, mirror reflectivities, filter transmission curves, point spread functions, read-out noise, detector linearity, hot pixels, are just a few of the effects and artifacts that every astronomical optical system contains.
Furthermore, while the amplitude and shape of each effect differs between optical systems, there are still commonalities in the way each effect can be described programmatically.

ScopeSim's main goal is to provide a framework for modelling (almost) any astronomical optical system by taking advantage of all these commonalities.
What Astropy has done for the general python landscape in astronomy, ScopeSim aims to do for the instrument simulator landscape.
