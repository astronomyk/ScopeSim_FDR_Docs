On-sky target templates: ScopeSim_templates
-------------------------------------------

Documentation: scopesim-templates.readthedocs.io

Code Base: github.io/astronomyk/scopesim_templates

Continuous integration : travis-ci

.. todo:: update link


What is included in the package
++++++++++++++++++++++++++++++++
- Functions to generate ``Source`` objects. 
- .basic subpackage written by us
- .micado subpackage written by micado pipeline team (HB)

- can add packages for any other topic if anyone has code for this 
- functions do not necessarily need spectra. stars for example need mags/fluxes


Source object interface
+++++++++++++++++++++++
- spatial description
    - ascii
    - fits ImageHDU
    - fits cube (3D ImageHDU)
- spectral description
    - synphot.SourceSpectrum

    
Example
+++++++

.. todo:: code to make images for here

- clusters
- galaxies with velocity gradients
    

Documentation
+++++++++++++

- scopesim_templates main documentation
- source object interface documentation from scopesim-templates
- converting from simcado to scopesim
