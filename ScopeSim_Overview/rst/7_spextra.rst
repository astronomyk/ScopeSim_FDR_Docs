SpeXtra
=======

``speXtra`` is a tool to manage and manipulate astronomical spectra. 

Documentation: https://spextra.readthedocs.io/

Code Base: https://github.com/miguelverdugo/speXtra

Continuous integration: https://travis-ci.org/github/miguelverdugo/speXtra

Author: Miguel Verdugo


Functionality
-------------

``speXtra`` packages several ``synphot`` workflows in simple-to-use methods that allow the user
to manipulate astronomical spectra. It is intended to be the main spectral engine for ``ScopeSim_templates``
but its design also allows standalone use.

Using ``speXtra``, the user can extract the magnitude from an astronomical spectrum or
scale the spectrum to that magnitude, the spectrum can be redshifted or
blueshifted or smoothed with a velocity kernel, add emission or absorption lines,
rebin the spectra or correct it for an extinction curve, etc. ``speXtra`` however does not perform
measurements, with the sole exception of extracting magnitudes within a passband.

``speXtra`` also comes with a built-in database of spectral templates  that cover many possible user cases.
Loading these templates is as easy as typing ``Spextrum('library_name/template_name')``. The user
can also read their own spectra from a file.
 

Database
++++++++

The ``speXtra`` database contains libraries of spectral templates, extinction curves and filter systems.
The data is downloaded on-the-fly when requested and kept cached in the local hard drive for future use.

The scheme is flexible and additional data can be added.
In the following a short summary of the database contains is provided.

Spectral Templates
++++++++++++++++++

At the time of writing the following libraries are included in the ``speXtra`` database.
Other can be added at request of the user.

* The Kinney-Calzetti Spectral Atlas of Galaxies
* Pickles Stellar Library
* SDSS galaxy composite spectra
* IRTF spectral library
* AGN templates
* Emission line nebulae
* Galaxy SEDs from the UV to the Mid-IR
* Kurucz 1993 Models (subset)
* Supernova Legacy Survey templates (subset)
* Flux/Telluric standards with X-Shooter
* High-Resolution Spectra of Habitable Zone Planets (example)

More templates can be easily added to the database at request of the users.


Extinction Curves
+++++++++++++++++

Extinction curves provided with the database. 

* Gordon LMC/SMC extinction curves
* Cardelli MW extinction curves
* Calzetti starburst attenuation curve

More templates can be easily added to the database at request of the users.


Filter Systems
++++++++++++++

``speXtra`` currently relies on the spanish SVO filter database to download filters transmission curves.
This is done thanksto the ``tynt`` package. However this database is not complete and in particular filters for upcoming
ELT instruments are missing. For that reason we have added some filter management to ``speXtra``.

Filter system currently included

* MICADO filter system
* METIS filter system

More templates can be easily added to the database at request of the users.


Installation
++++++++++++

To install ``speXtra`` simply type:: 

    pip install spextra


Dependencies
++++++++++++

``speXtra`` require the following dependencies to properly work. If they are missing they are automatically
installed.

* ``numpy``
* ``scipy``
* ``astropy``
* ``synphot``
* ``PyYAML``
* ``tynt``


Examples
--------

Load the S0 template from the Kinney-Calzetti library and then plot it for quick examination.

.. plot::
   :context: reset
   :include-source:
   :align: center

    from spextra import Spextrum

    sp = Spextrum("kc96/s0")
    sp.plot()


It is possible to arithmetic operations with spectra

.. plot::
   :context: reset
   :include-source:
   :align: center

    from spextra import Spextrum

    sp1 = Spextrum("kc96/s0")
    sp2 = Spextrum("agn/qso")
    sp = sp1 + 0.3*sp2
    sp.plot()


Scaling the spectra to a magnitude and see what we get afterwards

.. plot::
    :context: reset
    :include-source:
    :align: center

    from spextra import Spextrum

    sp1 = Spextrum("kc96/s0")
    sp2 = sp1.scale_to_magnitude(amplitude=13 * u.ABmag, filter_name="g")

    print(sp2.get_magnitude(filter_name="g")


Adding emission lines

.. plot::
    :context: reset
    :include-source:
    :align: center

    from spextra import Spextrum
    import astropy.units as u

    sp1 = Spextrum("kc96/s0")
    sp2 = sp1.add_emi_lines(center=4000, flux=4e-13, fwhm=5*u.AA)

    sp2.plot()

