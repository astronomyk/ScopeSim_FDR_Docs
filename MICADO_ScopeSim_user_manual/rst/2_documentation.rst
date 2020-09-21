Essentials: Documentation and Downloads
---------------------------------------

Online Documentation
++++++++++++++++++++

Online documentation for the main packages in the ScopeSim environment can be found here:

- ScopeSim: https://scopesim.readthedocs.io/en/latest/
- ScopeSim_Templates: https://scopesim-templates.readthedocs.io/en/latest/
- IRDB: https://github.com/astronomyk/irdb

The original SimCADO package is described here:

- SimCADO: https://simcado.readthedocs.io/en/latest/

.. note:: In the near future we will release a wrapper for the ScopeSim engine and the MICADO instrument package.

    The doumentation for this will be added to the original SimCADO_ read-the-docs page


Downloading ScopeSim and the MICADO package
+++++++++++++++++++++++++++++++++++++++++++

The ScopeSim engine is installed using pip::

    $ pip install scopesim

The casual user will also probably want to install the templates package, which contains helper functions for generating descriptions of on-sky targets like elliptical galaxies or star clusters::

    $ pip install scopesim_templates

Once ScopeSim is available to the local Python (version >= 3.5) installation, the user must download **ALL** the required instrument packages from the server::

    from scopesim.server import download_package
    scopesim.download_package(["locations/Armazones",
                               "telescopes/ELT",
                               "instruments/MAORY",
                               "instruments/MICADO"])

.. note:: There are two (2) MICADO packages available

    ``MICADO`` and ``MICADO_Sci``.

    For those interested in quick results, ``MICADO_Sci`` provides a reduced version of the MICADO package that contains all the major effects expected from the MICADO optical system.
    For those more concerned with accuracy, the standard ``MICADO`` package contains all expected optical effects.
    ``MICADO`` was originally developed for the development of the reduction pipeline, and therefore contains many effects that are beyond the scope of normal science case feasability studies.


Primary vs Support packages
+++++++++++++++++++++++++++

``MICADO`` and ``MICADO_Sci`` are primary packages.
This means they contain detector modules that enable an on-sky target to be observed

Armazones, ELT, and MAORY are support packages.
They do not contain detector modules.

Just like in real life, observing with only MICADO would be a difficult task.
Therefore we encourage the user to also download the support packages needed by MICADO.



.. _SimCADO: https://simcado.readthedocs.io/en/latest/
.. _ScopeSim: https://scopesim.readthedocs.io/en/latest/
.. _IRDB: https://github.com/astronomyk/irdb
.. _ScopeSim_Templates: https://scopesim-templates.readthedocs.io/en/latest/
