The ScopeSim engine
-------------------
        
Documentation: https://scopesim.readthedocs.io/

Code Base: https://github.com/astronomyk/ScopeSim

Continuous integration: https://travis-ci.org/github/astronomyk/ScopeSim

Author: Kieran Leschinski


How the ScopeSim engine works
+++++++++++++++++++++++++++++

The scopesim engine is the core of the scopesim environment.
At the heart of scopesim are two major concepts. 

- The observed output is the target input plus a series of optical artefacts
- The effect of each optical artefact is independent of all other artefacts

If we follow these to concepts to their logical conclusion we end up with a situation where optical artefacts can be treated as a series of "lego bricks" and any digital optical model can be constructed much in the same way as a lego model; by stacking the correct combination of effect "bricks" together in the right order.

The ScopeSim engine is therefore comprised of two types of objects: a collection of ``Effect`` object subclasses, and a series of "management" classes.

The ``Effect`` object is a lightweight class that acts as a simple operator class.
Object goes in, object comes out. 
Albeit with the flux distribution slightly altered in one way or another.
Here the object in question can be any one of the 4 main flux distribution classes: 

- ``Source``: (x, y, lambda)
- ``FieldOfView``: (x, y, lambda_0)
- ``ImagePlane``: (x, y, sum(lambda))
- ``DetectorPlane``: (x, y, e-)

.. warning:: finish section
    
    
Optical system capabilities
+++++++++++++++++++++++++++
ScopeSim is able to simulate raw detector data for the majority of the currently. available imaging and spectroscopic instruments.

Imagers
*******
In theory there is no limit to the size of a focal plane that ScopeSim can simulate.
ScopeSim uses a puzzle like approach to populating the final image plane canvas.
It generates a series of smaller fields-of-view objects which each cover a unique region of the spatial and spectral domain available to the instrument.
Each of these field-of-view objects observe only the parts of the on-sky target that fit within each fields-of-view's spectro-spatial limits.
The images contained within each field-of-view are broadcast onto their corresponding region of the image plane canvas.

In this manner, ScopeSim can simulate focal plane images up to half as large as the available amount of RAM on the host machine.

Spectroscopes
*************
The use of field-of-view objects with a restricted spectro-spatial range allows ScopeSim to also simulated a range of different spectroscopic modes.
Instead of splitting the field of view in the spatial dimensions, ScopeSim can also split along the spectral dimension.
To simulate raw spectroscope detector outputs, ScopeSim sets the allowable spatial field equal to the dimensions of the aperture mask.
It then creates spatially identical field-of-view objects for each narrow wavelength bin within the desired wavelength range of the instrument.
As with the imager mode, these field-of-view objects observe the on-sky target within each field-of-view's spectro-spatial limits.
The detector coordinates of each field-of-view are set such that they mimic the instrument's raw dispersion pattern.
Simulated raw detector images must then be reduced or analysed with the common suite of spectroscopic data tools.

Using this method, ScopeSim attempts to replicate as efficiently as possible the actual physical processes within a spectrograph.
This enables the spectroscopic mode of ScopeSim to be applied to all major spectrograph types: long slit, integral field unit, and multi-object spectrographs.
This is done by providing a simplified mapping between apertures and spectral traces on the detector. For example, a simple long-slit spectrograph will have a single aperture and a single spectral trace on the detector plane.
IFUs and MOS can be seen as a collection of simple long slits with coherent and incoherent aperture images.


Explanation of Effect objects
+++++++++++++++++++++++++++++
- effects are operators, what is passed, is returned
- effect classes can alter the object in a variety of ways:
    - intensity (mult, add, sub) in x,y and/or lambda
    - shifts 
    - convolutions
    - spreads
    
effects are applied one after the other, first lam, then xylam, then xy
- effects can also be electronic in nature, 
- examples of effects, psf, linearity, exposure


Explanation of observation workflow
+++++++++++++++++++++++++++++++++++
- pseudo code for loop
- description of 4 objects, and why they are important


Documentation
+++++++++++++
- Tutorials on read the docs





    
    
    
    



