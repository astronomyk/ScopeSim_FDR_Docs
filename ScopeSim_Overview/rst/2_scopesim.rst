The ScopeSim engine
-------------------
        
Documentation: https://scopesim.readthedocs.io/

Code Base: https://github.com/astronomyk/ScopeSim

Continuous integration: https://travis-ci.org/github/astronomyk/ScopeSim

Author: Kieran Leschinski

Updated: 06.11.2020

Installation::

    pip install scopesim


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

Using this method, ScopeSim attempts to replicate as efficiently as possible the actual physical processes within a spectrograph, while not using ray-tracing or fourier-optics methods.
This enables the spectroscopic mode of ScopeSim to be applied to all major spectrograph types: long slit, integral field unit, and multi-object spectrographs.
This is done by providing a simplified mapping between apertures and spectral traces on the detector.
For example, a simple long-slit spectrograph will have a single aperture and a single spectral trace on the detector plane.
IFUs and MOS can be seen as a collection of simple long slits with coherent and incoherent aperture images.


Explanation of Effect objects
+++++++++++++++++++++++++++++

The Effect objects are the main building blocks used by ScopeSim to describe the artefacts introduced by an imperfect optical system.
These cover a wide range of mathematical operations (addition, multiplication, convolution, distortion, translation, rotation, etc) which alter the distribution and amplitude of the flux maps (or cubes) produced by the on-sky target objects.
All effect objects are based on an underlying ``Effect`` operator class.
An operator class returns the same object as passed via the function call.
However during the function call, the effect object may apply changes to the input object's internal data.

A good example of this is the PSF effect class.
It accepts a field-of-view object and returns a field-of-view-object.
However while acting on the field-of-view object, the PSF effect convolves the field-of-view's internal flux map with the PSF kernel.

Effect object must contain a description of what needs to happen to any incoming object.
This may take the form of a purely mathematical operation, or is use an empirical external data set.
The ``ShotNoise`` effect for example, applies a Poisson noise filter to the ideal flux map contained within an ``ImagePlane`` object.
In contrast, the ``FilterCurve`` effect must read in an ASCII file containing wavelength dependent transmission information.
How the contained information is applied to the incoming object it unique to each Effect object.
The only requirement is that the incoming object is returned once the effect object is finished.

While ScopeSim contains a library of effect objects common to many astronomical instruments, the user is also free to create and include their own custom build effect objects.

.. warning:: Include code snippet of custom effect


Explanation of observation workflow
+++++++++++++++++++++++++++++++++++

.. warning:: Add visual representation here

During an observation simulation the flux description of the on-sky target is passed through a series of management layer objects: ``Source``, ``FieldOfView``, ``ImagePlane``, ``Detector``.
The effects specific to each management layer object are iteratively applied to these objects before moving onto the next step.

The following pieces of pseudo-code describe the workflow followed by ScopeSim when simulating an observation::

    sky_object = copy(user_sky_object)

    for effect in sky_object_effects:
        sky_object = effect.apply_to(sky_object)

Here the user's target is copied and all effects relating solely to the target description are applied.
These are primarily (but not exclusively) the purely spectral effects like mirror transmission curves.::

    field_of_view.extract_flux_from(sky_object)

    for effect in field_of_view_effects:
        field_of_view = effect.apply_to(field_of_view)

In the second step a field-of-view object extracts flux information from the user's target that matches the spatial and spectral borders of the field-of-view object.
All effects relating to this field-of-view object are applied.
These are generally the complex effects which have both a wavelength- and a spatial dependency, e.g.: PSFs, NCPAs, atmospheric dispersion, etc.::

    image_plane.add_flux_from(field_of_view)

    for effect in image_plane_effects:
        image_plane = effect.apply_to(image_plane)

The third step involves projecting all fields of view onto a two dimensional image plane.
This creates an 'expectation' image.
Essentially this is the noiseless signal map directly above the array of detectors.
All remaining spatial effects (e.g. vibration, rotation, offsets, etc) are applied during this step.::

    detector.extract_flux_from(image_plane)

    for effect in detector_effects:
        detector = effect.apply_to(detector)

    detector.write_to(filename)

The final step involves extracting the flux map that each detector chip will see and applying all the electronic effects.
For example: shot and read noise, dark current, linearity, exposure stacking, etc

The output of the observation simulation is a FITS object containing detector read-out images for all the detectors modelled by the optical train.
This can be passed on in memory for further use or saved to disk using the standard FITS write out method.


Reducing the complexity of simulations
++++++++++++++++++++++++++++++++++++++

The observation workflow described above depicts the full process of simulating an observation.
It allows for a complete description and treatment of all optical artefacts within an optical train.
For many applications however such a complete description is not needed.
For science case feasibility studies, many of the effects contained in the raw readout frames are removed in by the data processing pipelines.
The modular nature of ScopeSim allows for many levels of complexity in the optical train.
For example, the wavelength and spatial extent of simulations can be restricted to only those areas that are interesting to the user.
Effect objects can be turned on or off on-the-fly.
Large and complex effect objects can be replaced by more light-weight versions.
For the MICADO simulator, we have provided three packages with increasing levels of simplicity: ``MICADO_pipe``, ``MICADO_sci``, and ``MICADO_etc``.
As the names suggest, each package contains only the effects and simulation parameter spaces relevant to the package's scope.
These three packages are described in greater detail in ELT-TRE-MCD-56306-0059

Documentation
+++++++++++++
User documentation can be found online at https://scopesim.readthedocs.io/en/latest/.
The online documentation primarily focuses on how to control ScopeSim.
A series of shorter tutorials (so called 5-liners) describe very specific aspects of the software.
There are also a few longer tutorials which guide a potential user through the process of running observation simulations from start to finish.

.. warning:: Add some 5 liners

.. warning:: generate a nice 3 colour image with everything scopesim can do.







    
    
    
    



