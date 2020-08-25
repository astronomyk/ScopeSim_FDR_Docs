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
- The effect of each optical artefact is indenpendent of all other artefacts

If we follow these to Ans�tze to their logical conclusion we end up with a situation where optical artefacts can be treated as a series of "lego bricks" and any digital optical model can be constructed much in the same way as a lego model; by stacking the correct combination of effect "bricks" together in the right order.

The ScopeSim engine is therefore comprised of two types of objects: a collection of ``Effect`` object subclasses, and a series of "management" classes.

The ``Effect`` object is a lightweight class that acts as a simple operator class.
Object goes in, object comes out. 
Albeit with the flux distribution slightly altered in one way or another.
Here the object in question can be any one of the 4 main flux distribution classes: 

- ``Source``: (x, y, lambda)
- ``FieldOfView``: (x, y, lambda_0)
- ``ImagePlane``: (x, y, sum(lambda))
- ``DetectorPlane``: (x, y, e-)

.. todo:: finish section
    
    
Optical system capabilities
+++++++++++++++++++++++++++
- Imaging
- Spectroscopy (LS, MOS, IFU)
- Simultaneous readouts on multiple image planes


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





    
    
    
    



