Making on-sky Sources
---------------------

On-sky target source objects for ScopeSim can be created in two ways:
by using the helper functions provided in the ScopeSim_Templates_ package, or by creating a ``Source`` object from scratch.
The latter requires the user to have both the spatial and spectral data needed to describe the object.


ScopeSim Templates
++++++++++++++++++

A useful addition to the ScopeSim eco-system is the package ``ScopeSim_templates``.
This python package provides so-called helper functions for generating ScopeSim readable ``Source`` object for common astronomical objects.
The ``basic`` subpackage contains functions for generating star clusters and grids of stars, as well as analytical and numerical representations of galaxies.
The documentation for `ScopeSim templates can be found on Read-The-Docs`__.

__ ScopeSim_Templates_

Here is a basic example of creating a star cluster using ``ScopeSim_templates``:

.. code::
    :class: plot
    :name: code-scopesim-templates-example

    from scopesim_templates.basic.stars import cluster

    my_cluster = cluster(mass=1000, distance=50000,
                         half_light_radius=1)

..
    action: plot
    name: scopesim_templates_cluster_example
    ---
    plt.figure(figsize=(10,10))
    my_cluster.plot()
    plt.xlabel("x [arcsec]")
    plt.ylabel("y [arcsec]")


.. figure:: images/scopesim_templates_cluster_example.png
    :name: fig-scopesim-templates-cluster-example
    :scale: 50 %

In section 7, various helper functions are used to create the source objects observed in the presented use cases.

The ScopeSim Source object
++++++++++++++++++++++++++

The ``Source`` object is the underlying python class that contains the spatial and spectral descriptions of the on-sky target.
The spatial description can be either a table of point source positions, or a 2D intensity map (image) of an extended object.

Point source tables must contain the following columns:

=========   ===
Column      Description
=========   ===
x           [arcsec] position of source relative to centre of FOV
y
ref         index of spectrum associated with the point source
(weight)    [default=1] scaling factor if multiple point sources reference the same spectrum
=========   ===

Extended objects intensity maps (images) must be ``astropy.fits.HDUImage`` objects that display a the extent of similar spectral regions.
Each image may only be linked to one spectrum.
An extended ``Source`` may however contain multiple images that reference different spectra.
To illustrate the point, a spiral galaxy may be split into two intensity maps (images).
The first shows the distribution of the new stellar population, while the second shows the distribution of the old stellar population.
Each of these images is linked to a generic spectrum for the given population.
Conceivably a third image showing the distribution of warm gas and the spectrum for warm gas could be added to the ``Source`` object.

Each ImageHDU must contain the following information in the header:

==============  ===
Header Keyword  Description
==============  ===
CDELT1, CDELT2  Pixel scale of the image
CUNIT1, CUNIT2  Unit of the pixel scale value.
SPEC_REF        Spectrum associated with the image
==============  ===

All ``Source`` objects require list of one or more spectra to be passed to the ``Source`` object when it is created.
Spectra can either be ``synphot.SourceSpectrum`` objects or numpy arrays.
If they are passed as numpy arrays, a corresponding wavelength array must also be passed.

.. note:: The ScopeSim affiliate packages ``Spextra`` and ``Pyckles`` provide access to many standard spectral libraries.

    These python packages return spectra in a variety of formats including the ``synphot.SourceSpectrum`` format.

The following code shows the process of creating a simple binary star system from scratch::

    # Get two spectra
    from pyckles import SpectralLibrary
    pickles = SpectralLibrary("pickles", return_style="synphot")
    spec = [pickles.A0V, pickles.G2V]

    # Make a table
    from astropy.table import Table
    tbl = Table(names=["x", "y", "ref"],
                data=[[-2, 2], [0, 0], [0, 1]])

    # Combine spectra and positions in the Source object
    from scopesim import Source
    binary = Source(table=tbl, spectra=spec)

Source objects can also be combined using the ``+`` operator::

    star = Source(x=[0], y=[10], ref=[0], spectra=[pickles.M0III])
    trinary = binary + star

The ``trinary`` Source object now contains two tables with the positions of the stars and three spectra.
This can be verified by looking at the ``<Source>.fields`` and ``<Source>.spectra`` attributes.

We can also combine point source with extended source objects.
Each object remains intact inside the new ``Source`` container.




.. Contents
    - What is inside a Source object
    - How to make source objects to observe
        - Star cluster
        - Custom point source
        - Elliptical galaxy
        - Custom extended source
        - Combining sources



.. _SimCADO: https://simcado.readthedocs.io/en/latest/
.. _ScopeSim: https://scopesim.readthedocs.io/en/latest/
.. _IRDB: https://github.com/astronomyk/irdb
.. _ScopeSim_Templates: https://scopesim-templates.readthedocs.io/en/latest/
