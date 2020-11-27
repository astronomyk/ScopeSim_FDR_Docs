Building blocks
---------------

.. figure:: Ecosystem.png
    :name: fig-ecosystem
    :scale: 90 %

The ScopeSim ecosystem has been designed to maintain strict boundaries between the simulation code, the optical model data, and the user input.
As with real systems, the astronomical objects and the light they emit exist regardless of the telescope or astronomer.
The telescope and instruments also exist independently of the astronomer.
Only when an astronomer uses a telescope to observe a celestial object are the three connected.
A similar philosophy has been applied to the development of the ScopeSim ecosystem.

The ScopeSim ecosystem consists of three main packages:

- ScopeSim: the core simulation engine,
- ScopeSim_templates: a library of functions for generating descriptions of on-sky objects,
- IRDB: The instrument reference database containing the data and configuration files needed to generate the digital models of a range of telescope and instrument optical system.

Figure \ref{fig-ecosystem} illustrates the relationship between these three packages.
Although there is a strict delineation between the scopes of each package, the interfaces between the packages allows them to interact almost seamlessly with each other.
This can be seen in the code examples from section \ref{sec-examples}.
The main code pattern for simulating observations with a specific instrument is the same for all use cases:

1. download the required instrument packages from the instrument reference database (IRDB) using scopesim,
2. create a description of the astronomical object using scopesim_templates,
3. generate a model of the desired optical system using scopesim and referencing the IRDB package,
4. simulate and output the observed data using scopesim.

The following subsections briefly describe each of these 3 packages:

ScopeSim: the observation simulator engine
++++++++++++++++++++++++++++++++++++++++++
The ScopeSim core package, also referred to as the ScopeSim engine, contains the code necessary for running observations simulations.
The code has been written in such a way as to be completely agnostic to the instrument setup as well as agnostic towards the on-sky target.
At its heart the code transports flux from a description of the on-sky target to a detector focal plane.
During the process it applies any optical aberrations contained in the optical model to the flux description.
Section \ref{sec-scopesim-architecture} describes this process in more detail.
ScopeSim attempts to remove as much redundancy and inefficiency from observation simulations as possible by recognising the fact that there is little need to redo the majority of the calculations executed in high-fidelity simulations.
In other words, the ScopeSim engine does not work with ray-tracing methods or use fourier optics, except in isolated cases.
Instead it uses the fact that the observed image is a linear combination of independent optical aberrations applied to an incoming spectro-spatial flux distribution.

This focus on removing as many redundant calculations as possible results in very quick execution times.
The images from the code examples were generated on a standard laptop in around 10 seconds.
Such speed makes ScopeSim suitable for use cases with short iteration times, such a quick look feasibility studies, e.g. "playing" with a science case, or advanced exposure time calculators.
At the other end of the scale, ScopeSim is also useful for generating simulated raw data needed during the development of instrument data reduction pipelines.
As the ScopeSim engine takes its cues from the instrument packages, the fidelity of simulations is limited only the number and accuracy of the Effects listed in these packages.


ScopeSim_templates: Description sof on-sky targets
++++++++++++++++++++++++++++++++++++++++++++++++++

The scopesim_templates package provides a series of functions to help the user create a description of the on-sky targets they wish to observe in the format required by the ScopeSim engine.
These helper function populate one or more instances of the ScopeSim "Source" class with the data needed to best describe the target.

Format of a Source object
*************************

In order to optimise memory usage the Source objects split the spatial and spectral characteristics of a target.

**!!!** reference Schmalzl+2010 (old METIS simulator paper)

These are held separately in two list: fields and spectra.
A spatial field can be either a table of coordinated and flux scaling factors (e.g. the positions of stars in cluster) or a 2D weight map (e.g. an image of a galaxy).
Each entry in a field must reference one of the entries in the list of spectra, however there is no requirement for a one-to-one relationship between field entries and spectral list entries.
For example in the case of star cluster, all A0V stars can reference a single A0V spectrum.
Scopsim memory requirement are further reduces by taking advantage of this redundancy.

Galaxies and similar extended objects can also be adequately represented in this manner.
A galaxy generally contains populations of stars (new, old, high-, low-metalicity, etc.) and in most cases observations do not resolve individual stars.
Hence it can be assumed that if each component is represented by a unique flux weight map (i.e. an image) then each stellar population can be represented by a single spectrum.
As an example, the scopesim_templates function ``galaxy.spiral_two_component`` uses the B filter image of the galaxy NGC\,1232L to represent the young population and the I filter image for the old population.
Each image references a spectrum for a young or old population.

The extreme limit for this type of representation would be the case where every single pixel in an image is associated with a unique spectrum.
An example might be the turbulent motions of gas in a star forming region, although it is still arguable that even here there will still be spectrally redundant regions.
In this case the spectral and spatial components can still be split, however the result will be that each spatial field entry will consist of an image with only a single pixel and referencing the associated spectrum from the list of spectra.
Such a use case would be particularly computationally expensive.
It is therefore highly recommended in such cases to search for possible spectral redundancy before creating a "Source" object from a spectral cube.

**!!!** insert image of these use cases


Structure of ScopeSim-templates package
***************************************

Currently ScopeSim-templates splits the helper functions into categories based on the complexity of the Source object that is produced.
The ``basic`` subpackage contains helper function which are useful for quick look investigations, but which should not be used for in depth feasibility studies.
For example the ``stars.cluster`` function does not allow age or metallicity to be set.
In contrast the ``advanced`` subpackage contains functions that can be useful for very specific science cases, but are not adapted for general use.

In addition to the general functions, it is possible to add helper functions for objects used by specific instruments.
The ``micado`` subpackage for example contains functions that produce objects specific to the MICADO instrument at the ELT.

Community participation is most welcome to help expand the number of object template function in the ScopeSim_templates package.


Instrument Reference Database: The optical model data
+++++++++++++++++++++++++++++++++++++++++++++++++++++

ScopeSim aims to be a general purpose instrument data simulator that can be used to simulate the output of many different optical systems.
To make this goal a reality it was mandatory that the scopesim engine be completely instrument agnostic.
There is however a large amount of instrument specific data that is need to accurately model the optical aberrations inherent in any optical system.
For ScopeSim this data is stored in instrument packages in a separate instrument reference database (IRDB).
Instrument packages can be created for any self contained section of an optical train.
For example the telescope, the atmosphere, the relay optics, and the instrument are generally assumed to be self contained optical sections.
For small observatories like the University fo Vienna's 1.5m telescope there is no benefit to splitting the optical elements into separate packages.
However for large observatories like the VLT where multiple instruments can be attached to a single telescope, it makes sense to split the telescope optical system from the instrument description.
Not only does this avoid multiple versions of a single optical element (e.g. telescope) becoming unsynchronised when one instrument package is updated and another is not, it also reduces the scope of responsibility for maintaining packages.
For example this means that instrument consortia need only concentrate on maintaining their own instrument package, while the telescope operator is responsible for maintaining the telescope package.
It also means a telescope or relay optics package can be updated without needing (theoretically) to inform the maintainers of all instrument packages that use those subsystem.


Instrument package format
*************************
Each instrument package contains two main types of data:

1. A series of configuration files describing which optical aberrations should be modelled by scopesim, and
2. The empirical data files needed for scopesim to apply the aberrations to the incoming photon flux.

The configuration files are written in YAML.
They contain lists of Effect object descriptions as well as global properties that are common to all Effect objects in the subsystem.
The Effect object descriptions must call an existing Effect class from the ScopeSim core package.
Effect objects are discussed in more detail in section \ref{subsec-effects}.
For the Effects which rely on external empirical data, these files must also be contained in the instrument package.
The empirical data files must be either ASCII tables or FITS images/tables.
Examples of empirical data files include the filter response curves or pre-computed sets of PSF kernels.

The raw instrument data currently resides in the instrument reference database on Github.
Periodically, or when explicitly needed, the data on this repository are compiled into packages and uploaded onto the ScopeSim server.
It is from here that ScopeSim downloads a package when asked to do so by the user (as seen in the code examples).
Packages are downloaded using Astropy, and hence are saved locally in the Astropy cache.
This allows the packages to be used offline.
Updated packages can be downloaded by either clearing the Astropy cache, or by forcing scopesim to redownload a package via the RC parameters.
An example of this is available in the online documentation.

For readers interested in creating their own instrument packages for a local telescope or instrument, the authors recommend looking inside the LFOA (Leopold-Figl Observatory for Astrophysics) package on the IRDB Github page.
This contains everything needed to simulate observations with the Viennese 1.5m telescope.

**!!!** add link here
