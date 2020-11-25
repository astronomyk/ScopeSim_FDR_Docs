Building blocks
---------------




Description of on-sky targets
- Spatial + spectral descriptions
- ScopeSim_templates package

Optical Model data
- What is an Instrument packages
- What do they contain
- Where are they found

Observation simulator engine
- Uses data from packge to cerate a model
- Manages the transport of photons from the on-sky object to the detector plane
- Sequentially alters the distrobution of flux according to the instrumentions in the inst pkg
- Outputs the final photon distibution in FITS format for the end user

