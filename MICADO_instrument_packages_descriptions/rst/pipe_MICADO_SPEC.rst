
OpticalElement: "MICADO_SPEC"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: instrument

**Alias**: INST
        
**Description**: additional effects for the spectroscopy mode

Global properties
#################
::

     pixel_scale : 0.004
     plate_scale : 0.2666666667
    element_name : MICADO_SPEC

        
Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:MICADO_SPEC
   
    =========== =========================== ================= ======== ==============
      element               name                  class       included    z_orders   
    =========== =========================== ================= ======== ==============
    MICADO_SPEC            spec_mode_optics       SurfaceList     True [20, 120, 520]
    MICADO_SPEC spectroscopic_slit_aperture      ApertureMask     True [80, 280, 380]
    MICADO_SPEC      micado_spectral_traces SpectralTraceList     True      [70, 270]
    =========== =========================== ================= ======== ==============
 



SurfaceList: "spec_mode_optics"
*******************************
**Included by default**: ``True``

**File Description**: list of extra mirrors needed for the spectroscopy mode

**Class Description**: <no docstring>

**Changes**:

- 2019-01-28 (KL) Changed column names and added units to header
- 2019-07-10 (KL) Shortened the list to only the swappable gratings

Data
++++

.. figure:: spec_mode_optics.png
    :name: fig:spec_mode_optics

    

.. table::
    :name: tbl:spec_mode_optics

    ======= ===== ===== ===== =========== ========== ===============
      name  outer inner angle temperature   action       filename   
    ======= ===== ===== ===== =========== ========== ===============
    I08_SM7   0.2   0.0     0        -190 reflection TER_grating.dat
    I09_SM8   0.2   0.0     0        -190 reflection TER_grating.dat
    ======= ===== ===== ===== =========== ========== ===============



Meta-data
+++++++++
::

                filename : LIST_MICADO_mirrors_spec.dat
                    name : spec_mode_optics
             pixel_scale : 0.004
             plate_scale : 0.2666666667
            element_name : MICADO_SPEC
                  author : Kieran Leschinski
                  source : Ric's SPIE 2018 PPT presentation
            date_created : 2018-11-19
           date_modified : 2019-07-10
                  status : Design, pre PDR list of swappable optics for spectroscopy
                    type : mirror:list
                   ETYPE : SURFLIST
                    EDIM : 1
              outer_unit : m
              inner_unit : m
              angle_unit : degree
        temperature_unit : deg_C
                 z_order : [20, 120, 520]
                 include : True
            ignore_wings : False
                wave_min : !SIM.spectral.wave_min
                wave_max : !SIM.spectral.wave_max
               wave_unit : !SIM.spectral.wave_unit
                wave_bin : !SIM.spectral.spectral_resolution
     report_plot_include : True
    report_table_include : True
      minimum_throughput : !SIM.spectral.minimum_throughput
                 etendue : !TEL.etendue




ApertureMask: "spectroscopic_slit_aperture"
*******************************************
**Included by default**: ``True``

**File Description**: Slit mask for the short, wide slit  (3 arcsec x 50 mas)

**Class Description**: Only provides the on-sky window coords of the Aperture

**Changes**:

- 2019-07-10 (KL) Created the file
- 2020-03-24 (KL) Changed geometry to 3000x50mas

Data
++++

.. table::
    :name: tbl:spectroscopic_slit_aperture

    ======= =======
       x       y   
    ======= =======
    -1.5000 -0.0250
     1.5000 -0.0250
     1.5000  0.0250
    -1.5000  0.0250
    ======= =======



Meta-data
+++++++++
::

                 filename : !OBS.slit_file
                     name : spectroscopic_slit_aperture
              pixel_scale : 0.004
              plate_scale : 0.2666666667
             element_name : MICADO_SPEC
                   author : Kieran Leschinski
                   source : My imagination
             date_created : 2019-07-10
            date_modified : 2019-07-10
                   status : Guess - in the train on the way home from CM13
                     type : aperture:slit_geometry
                   x_unit : arcsec
                   y_unit : arcsec
                  z_order : [80, 280, 380]
                  include : True
                  no_mask : True
                    angle : 0
                    shape : rect
           conserve_image : True
                       id : 0
      report_plot_include : False
     report_table_include : True
    report_table_rounding : 4




SpectralTraceList: "micado_spectral_traces" : 17 traces
*******************************************************
**Included by default**: ``True``

**File Description**: list of spectral order trace geometry on the focal plane

**Class Description**: List of spectral trace geometries for the detector plane

**Changes**:

- 

Data
++++

.. figure:: micado_spectral_traces.png
    :name: fig:micado_spectral_traces

    

Meta-data
+++++++++
::

                filename : !OBS.trace_file
                    name : micado_spectral_traces
             pixel_scale : 0.004
             plate_scale : 0.2666666667
            element_name : MICADO_SPEC
            wave_colname : lam
               s_colname : xi
        col_number_start : 1
           invalid_value : 0
                  SIMPLE : True
                  BITPIX : 8
                   NAXIS : 0
                  EXTEND : True
                FILETYPE : Spectral Layout Definition
                  AUTHOR : Oliver Czoske
                    DATE : 2018-09-16
                  SOURCE : Frank Grupp
                ORIGDATE : 2018-06-29
                  STATUS : Design PDR
                    ECAT : 1
                   EDATA : 2
                DESCRIPT : Maps spectral traces from long slit aperture to detector image plane
                DATE_CRE : 2018-06-29
                DATE_MOD : 2019-09-16
                 HISTORY : 2019-09-16 : (KL) Added aperture-imagePlane table to EXT 1
                 z_order : [70, 270]
                 include : True
                wave_min : !SIM.spectral.wave_min
                wave_mid : !SIM.spectral.wave_mid
                wave_max : !SIM.spectral.wave_max
               x_colname : x
               y_colname : y
      center_on_wave_mid : False
                   dwave : 0.002
     report_plot_include : True
    report_table_include : False

