ScopeSim is a flexible multipurpose instrument data simulation ecosystem built in python.
It enables both raw and reduced observation data to be simulated for a wide range of telescopes and instruments quickly and efficiently on regular laptops.
The software is currently being used to generate simulated raw input data for developing the data reduction pipelines for the MICADO and METIS instruments at the ELT.

The ScopeSim environment consists of three main packages which are responsible for providing on-sky target templates (ScopeSim_templates), the data to built the optical models of various telescops and instruments (instrument reference database), and the simulation engine (ScopeSim).
This strict division of responsibilities allows ScopeSim to be used to simulate observation data for many different instrument and telescope configurations for both imaging and spectroscopic instruments.
ScopeSim has been built to avoid redundant calculations where ever possible.
As such it is able to deliver simulated observations on times scales of seconds to minutes.

All the code and data is open source and hosted on Github.
The community is also most welcome, and indeed encouraged to contribute to code ideas, target templates, and instrument packages.
