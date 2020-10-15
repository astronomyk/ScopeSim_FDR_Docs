AnisoCADO
=========
A package for analytically generating SCAO PSFs primarily for the ELT

Documentation: https://anisocado.readthedocs.io/

Code Base: https://github.com/astronomyk/AnisoCADO

Continuous integration : https://travis-ci.org/github/astronomyk/AnisoCADO

Author: Kieran Leschinski

Introduction
------------
- Why AnisoCADO exists
    - Quickly create SCAO PSFs
- Limiting assumptions
    - Long exposure PSFs (> D_M1 / v_wind)
    - No coherence between time steps

Examples
--------

- Basic use case
- Off-axis


.. code::
    :class: execute
    :name: code-anisocado-example

    from anisocado import AnalyticalScaoPsf

    psf = AnalyticalScaoPsf(N=64, wavelength=2.15)  # um
    on_axis = psf.psf_on_axis
    off_axis = psf.shift_off_axis(15, -5)   # arcsec

..
    action: plot
    name: anisocado_basic_example
    ---
    plt.figure(figsize=(10,5))
    plt.subplot(121)
    plt.imshow(on_axis, norm=LogNorm())
    plt.subplot(122)
    plt.imshow(off_axis, norm=LogNorm())



.. figure:: images/anisocado_basic_example.png
    :name: fig-anisocado-basic-example
    :scale: 50 %

    Left: the on-axis K-band (2.15$\\mu$m) SCAO PSF for standrard atmospheric conditions.
    Right: the K-band SCAO-PSF at the position (15, -5) arcseconds from the natural guide star.



Functionality
-------------
- How AnisoCADO creates the SCAO PSFs
- Long / Short exposure PSFs
- Off axis
- Wavelength dependence
