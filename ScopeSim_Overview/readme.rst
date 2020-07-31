ScopeSim
========
A modular astronomical instrument data simulation environment


Authors
-------
Kieran Leschinski
Hugo Buddelmeijer
Oliver Czoske
Miguel Verdugo
Gijs Verdoes-Kleijn
Werner Zeilinger

For each of the package sections, provide a reference to documentation and the
github repository

Contents
--------
- The ScopeSim environment overview
    - How everything is connected
    - Rationale for splitting everything
    - Community involvement
    - Documentation and Code base overview
    
- Core packages
    - ScopeSim engine
        - Possible functionality
            - Imaging
            - Spectroscopy (LS, MOS, IFU)
            - Simultaneous readouts on multiple image planes
        - Effects
            - Effect as an operator
            - Principles of chaining effects
            - Sub-classing easily doing

    - ScopeSim templates
        - Basic Source interface
        - Basic functions provided
        - Higher level functions open to community contributions

    - IRDB
        - Main packages vs support packages
        - List of available packages
        - Custom effects plugins possible

- Support Packages
    - AnisoCADO
        - SCAO PSFs for the ELT
        - Extendable for VLT
    - SkyCalc_ipy
        - iPython wrapper based on the skycalc_cli package
    - SpeXtra
        - Library for spectra
    - Pyckles
        - Basic Library for pyckles / brown
