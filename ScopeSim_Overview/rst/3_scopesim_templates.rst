On-sky target templates: ScopeSim_templates
-------------------------------------------

Documentation: https://scopesim-templates.readthedocs.io/

Code Base: https://github.com/astronomyk/ScopeSim_templates

Continuous integration: https://travis-ci.org/github/astronomyk/ScopeSim_Templates

Author: Kieran Leschinski

Functionality
-------------

``ScopeSim_templates`` creates astronomical sources in a format (``Source`` objects)
that can be used by the instrument simulator ``ScopeSim``.

It is designed to be agnostic regarding the instrument/telescope details. At the moment
only the most representative astronomical sources are included, however more
can be added with relative ease.


Source object interface
+++++++++++++++++++++++

A ``ScopeSim.Source`` object is a 2+1D (x, y, lambda) description of an on-sky object.
As such, it needs to contain the following information:

* A spatial description of the flux distribution on the sky. Either in table form (point sources)
  or in image/bitmap form (extended sources). The spatial description is internally stored as
  an ``astropy.table.Table`` object (in case of point sources) or as a ``astropy.io.fits.ImageHDU`` object
  (extended sources).

* A spectral description with the absolute flux per unit of wavelength of the objects. The spectral
  description is stored as a ``synphot.SourceSpectrum`` object.


We plan to add support for fits datacubes in the near future.

Composition of sources are possible, for example creating an stellar field around a galaxy.


What is included in the package
++++++++++++++++++++++++++++++++

``ScopeSim_Templates`` contains several functions to generate ``ScopeSim.Source`` objects.
In general, the most basic and more used functions are currently included in the package.
We expect to collaborate with the community to increase the breath of possible astronomical
sources.

The ``Source`` functions are organized in subpackages for a better accessibility.
They include a

* A ``.basic`` subpackage that contains functions to generate stars, stellar compositions
  (clusters, grids, etc) and basic galaxy descriptions

* An ``.advanced`` subpackage that contains - mostly - community contributions. In this package
  however, is possible to find advanced galaxy definitions, including a 3D velocity field.

* A ``.micado`` subpackage which contains MICADO specific sources with the main purpose of pipeline
  testing



Installation
++++++++++++

To install ``ScopeSim_templates`` simply type::

    pip install scopesim_templates

For the development version please visit the github repository.

``ScopeSim_templates`` should run with ``Python`` versions 3.5 and above.


Dependencies
++++++++++++

The following dependencies are necessary to run ScopeSim_templates``
installed.

* ``numpy``
* ``scipy``
* ``astropy``
* ``synphot``
* ``PyYAML``
* ``pyckles``
* ``scopesim``
* ``spextra``
* ``synphot``


Example
+++++++

1. A stellar cluster with a mass of 100 Msun, located at 1000pc and a core radius of 1pc. Currently only
   age=0 is supported.

.. plot::
    :context: reset
    :include-source:
    :align: center

    import matplotlib.pyplot as plt
    from templates.basic import star_cluster

    # This creates the source
    cluster = star_cluster(mass=100, distance=1000, core_radius=1)

    # Let's examine the fields
    table = star_cluster.fields[0]
    print(table)

    # And now the positions
    plt.plot(table["x"], table["y"], ".")


2. A two component galaxy, with a younger component described by a star-forming spectra and an older by a
   passive evolving spectral energy distribution

.. plot::
    :context: reset
    :include-source:
    :align: center

    from scopesim_templates.basic.galaxy import spiral_two_component
    import matplotlib.pyplot as plt
    import astropy.units as u

    gal = spiral_two_component(fluxes=(20*u.ABmag, 21*u.ABmag))

    plt.subplot(121)
    plt.imshow(gal.fields[0].data)
    plt.subplot(122)
    plt.imshow(gal.fields[1].data)


Above only the flux distribution on the sky can be appreciated. The description regarding the total flux
and its dependence with wavelength is contained in the ``.spectra`` property.

.. plot::
    :context: reset
    :include-source:
    :align: center

    from scopesim_templates.basic.galaxy import spiral_two_component
    import matplotlib.pyplot as plt
    import astropy.units as u

    gal = spiral_two_component(fluxes=(20*u.ABmag, 21*u.ABmag))
    gal.spectra[0].plot(left=3000, right=8000, flux_unit="FLAM")

    

Documentation
+++++++++++++

- scopesim_templates main documentation
- source object interface documentation from scopesim-templates
- converting from simcado to scopesim

