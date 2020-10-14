Making on-sky Sources
---------------------

ScopeSim Templates
++++++++++++++++++
An useful addition to the ScopeSim eco-system is the package ``ScopeSim_templates``.
This python package provides so-called helper functions for generating ScopeSim readable ``Source`` object for common astronomical objects.
The documentation for `ScopeSim templates can be found on Read-The-Docs`__

__ ScopeSim_Templates_

Here is a basic example of creating a star cluster using ``ScopeSim_templates``:

.. code::
    :class: plot
    :name: code-scopesim-templates-example

    from scopesim_templates.basic.stars import cluster

    my_cluster = cluster(mass=1000, distance=50000, half_light_radius=1)

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

    Left: the on-axis K-band (2.15$\mu$m) SCAO PSF for standrard atmospheric conditions.
    Right: the K-band SCAO-PSF at the position (15, -5) arcseconds from the natural guide star.




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
