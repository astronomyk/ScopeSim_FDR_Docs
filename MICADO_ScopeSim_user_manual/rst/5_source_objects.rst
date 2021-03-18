Making on-sky Sources
---------------------

On-sky target source objects for ScopeSim can be created in two ways:
by using the helper functions provided in the ScopeSim_Templates_ package, or by creating a ``Source`` object from scratch.
The latter requires the user to have both the spatial and spectral data needed to describe the object.


ScopeSim Templates
++++++++++++++++++
An useful addition to the ScopeSim eco-system is the package ``ScopeSim_templates``.
This python package provides so-called helper functions for generating ScopeSim readable ``Source`` object for common astronomical objects.
The ``basic`` subpackage contains functions for generating star clusters and grids of stars, as well as analytical and numerical representations of galaxies.
The documentation for `ScopeSim templates can be found on Read-The-Docs`__.
In section 7, various helper functions are used to create the source objects observed in the presented use cases.

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
