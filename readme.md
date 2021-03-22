# Documents for the MICADO final design review

All documents are to be written in LaTeX, and will be linked to overleaf.com

The overleaf session can be access using this link:

https://www.overleaf.com/8196534261ndmvhvrfzmyn

Therefore ALWAYS sync a session (pull, push) with Github at the START AND END
of a writing session. 

## Sphinx and Latex

The docs can be written in RST format, and include graphics generated directly 
from python code. However the sphinx conversion create a single latex file
which isn't as nice to edit as it could be.

Some setting can be altered with the ``latex_elements`` object:

- https://www.sphinx-doc.org/en/master/latex.html
- https://sphinxguide.readthedocs.io/en/latest/sphinx_basics/settings.html


## Overview

| Document Title                                                            | Document Number        | Version | responsible author | JIRA username of responsible author |
|---|---|---|---|---|
| SimCADO User Manual                                                       | ELT-MAN-MCD-56306-0058 | 1.0     | Leschinski/Verdugo | NN |
| Instrument data packages for the MICADO simulation environment            | ELT-TRE-MCD-56306-0059 | 1.0     | Leschinski/Verdugo | NN |
| ScopeSim - A modular astronomical instrument data simulation environment  | ELT-TRE-MCD-56306-0060 | 1.0     | Leschinski/Verdugo | NN |


## Three ScopeSim documents

1. **ScopeSim technical manual**
   
   A wrapper document for the ScopeSim environment. This document will contain
   a description of all the packages included in this environment and links to
   the main online documentation. 
   
   This document will NOT contain technical information about any specific 
   package

2. **MICADO instrument packages descriptions**

   This document will describe the data contained inside the three MICADO 
   instrument packages that will be delivered at FDR. These include:
   
   - The pipeline package, with all possible effects
   - The science package, with several "short cut" for quick science-grade 
     simulations
   - The ETC package, with only the absolutely necessary amount of information
     for generating super quick SNR and EXPTIME estimates
     
   Ideally this document will generate itself from the contents of the IRDB
   packages with the appropriate python scripts.

3. **MICADO ScopeSim user manual**

   This document is aimed at the general user of ScopeSim for simulating MICADO
   observations. It will contain a description of how to install ScopeSim and
   invoke the MICADO instrument packages. It will also contain worked examples
   for each of the main MICADO observing modes, including:
   
   - IMG : A series of examples covering the MCAO and SCAO modes, at 4mas and 
     1.5mas, using wide and narrow band filters. For example:
     - SCAO @ 4mas in J of a star cluster
     - SCAO @ 1.5mas in BrGamma of an Supernova in an elliptical galaxy
     - MCAO @ 4mas in Ks of a spiral galaxy
   - SPEC : A series of example covering the 3 slit configuration with the 
     three blocking filters
     - 0.05x15" with HK along the parallactic angle of three stars
     - 0.05x3" with IJ of an extended source
     - 0.02x3" with J rotated at angle X w.r.t. parallactic angle of a single 
       star
   - HCI : The high contrast imager. Still T.B.D
   - Astrometry : An example of using the sub-pixel functionality with the
     1.5mas mode in MCAO and SCAO


## Primer on package documentation

A basic list of things that all packages should cover in their online 
documentation.

E.g:
- Short introduction
    - What does the package do
    - Installation instructions (i.e. pip install <pkg-name>)
    - 5-liner code example
    - List of dependencies
- Quick-start guide
- Use case examples
- Misc end user information
- Deep dive
    - Technical manual for maintainers
        - Description of code
            - Major classes and how they interact   
        - Inheritence diagramme
        - File Interfaces
        - Sub-classing (if appropriate)
        
I will add more to this list soon, like:
- how to set up ReadTheDocs
- How to automatically generate and include matplotlib plots with Sphinx          

## Other FDR documents

Feel free to add other documents to this repository as needed, e.g: 
- for the ETC, 
- or pipeline algorithms, etc
