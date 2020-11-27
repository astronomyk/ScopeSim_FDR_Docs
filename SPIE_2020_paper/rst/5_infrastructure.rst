Package Ecosystem
-----------------

**!!!** add Figure showing the relation ship between packages

At its core the ScopeSim environment contains three packages:

- ``ScopeSim``: the simulation engine
- ``ScopeSim_templates``: descriptions of the on-sky sources
- ``IRDB``: the instrument reference database, which contains the data files used to build the instrument models as well as the conguration files which tell the ScopeSim engine how to simulate observations.

In addition to the core package, there are several support packages:

- ``AnisoCADO``: simulates SCAO PSFs for the ELT
- ``SkyCalc_ipy``: queries the ESO skycalc service for atmospheric spectral curves
- ``SpeXtra``: provides easy access to many well-known spectral libraries
- ``Pyckles``: a light-weight wrapper for the Pickles (1998) and Brown (2010) catalogues.

These package are not direct dependencies of ScopeSim, but do help provide additional functionality to the simulation engine.
Table \ref{tbl-list-of-packages} contains a list of the relevant links to both documentation and code-bases for these packages.

.. list-table:: Links to the open source documentation and code bases
    :name: tbl-list-of-packages

    *   - Package
        - Documentation
        - Code base
    *   - ScopeSim
        - https://scopesim.readthedocs.io/
        - https://github.io/astronomyk/scopesim
    *   - ScopeSim_templates
        - https://scopesim-templates.readthedocs.io/
        - https://github.com/astronomyk/ScopeSim_templates
    *   - IRDB
        - https://irdb.readthedocs.io/en/latest/
        - https://github.com/astronomyk/IRDB
    *   - AnisoCADO
        - https://anisocado.readthedocs.io/
        - https://github.com/astronomyk/AnisoCADO
    *   - SkyCalc_ipy
        - https://skycalc-ipy.readthedocs.io/en/latest/
        - https://github.com/astronomyk/SkyCalc_iPy
    *   - SpeXtra
        - https://spextra.readthedocs.io/en/latest/
        - https://github.com/miguelverdugo/speXtra
    *   - Pyckles
        - https://pyckles.readthedocs.io/en/latest/
        - https://github.com/astronomyk/Pyckles


Community involvement
+++++++++++++++++++++
**Community involvement is highly encouraged!**
The whole ScopeSim ecosystem is open source and the developers welcome any contributions, both code and comments, by members of the astronomical community.
The astronomical object templates package is one area which will benefit greatly from community contributions.
There is a wide variety of astronomical objects for which the authors have not yet created templates.
Galaxy clusters, gravitational lenses, supernovae, exoplanets, solar system objects are all still missing from the scopesim_templates package.
The instrument reference database also currently only contains the instruments directly relevant to the authors.
There is no limit to the size of telescopes or number of instruments that can be hosted on the server.
Readers interested in submitting a package for their own telescope or instrument are very welcome to make a pull request on the IRDB github page.
