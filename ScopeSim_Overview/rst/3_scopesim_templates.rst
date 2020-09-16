On-sky target templates: ScopeSim_templates
-------------------------------------------

Documentation: https://scopesim-templates.readthedocs.io/

Code Base: https://github.com/astronomyk/ScopeSim_templates

Continuous integration: https://travis-ci.org/github/astronomyk/ScopeSim_Templates

Author: Kieran Leschinski

Functionality
-------------

``ScopeSim_templates`` creates astronomical sources in a format (``Source`` objects)
that can be used with the instrument simulator ``ScopeSim``. It is designed to
be agnostic regarding the instrument/telescope details. It is also possible to add
new sources with relative ease.


What is included in the package
++++++++++++++++++++++++++++++++


- Functions to generate ``Source`` objects.
- .basic subpackage written by us
- .advanced subpackage for community contributions
- .micado subpackage written by micado pipeline team (HB)

- can add packages for any other topic if anyone has code for this 
- functions do not necessarily need spectra. stars for example need mags/fluxes


Source object interface
+++++++++++++++++++++++

A ScopeSim ``Source`` object is essentially a 2+1D (x, y, lambda) description of an on-sky object.
As such it contains the following information.

* A spatial description: Either in table form (point sources) or in image/bitmap form (extended source).

* A spectral description: Basically a spectrum with wavelength and flux information.



- spatial description
    - ascii
    - fits ImageHDU
    - fits cube (3D ImageHDU)
- spectral description
    - synphot.SourceSpectrum


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

.. warning:: code to make images for here

- clusters
- galaxies with velocity gradients
    

Documentation
+++++++++++++

- scopesim_templates main documentation
- source object interface documentation from scopesim-templates
- converting from simcado to scopesim

