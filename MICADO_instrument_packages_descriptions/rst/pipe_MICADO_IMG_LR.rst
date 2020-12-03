
OpticalElement: "MICADO_IMG_LR"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: instrument

**Alias**: INST
        
**Description**: additional effects for the wide-field imaging mode

Global properties
#################
::

     pixel_scale : 0.004
     plate_scale : 0.26666666666
    element_name : MICADO_IMG_LR

        
Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:MICADO_IMG_LR
   
    ============= ============================= =============================== ======== ==============
       element                 name                          class              included    z_orders   
    ============= ============================= =============================== ======== ==============
    MICADO_IMG_LR micado_wide_field_mirror_list                     SurfaceList     True [20, 120, 520]
    MICADO_IMG_LR           micado_adc_3D_shift AtmosphericDispersionCorrection    False     [632, 232]
    ============= ============================= =============================== ======== ==============
 



SurfaceList: "micado_wide_field_mirror_list"
********************************************
**Included by default**: ``True``

**File Description**: list of extra mirrors needed for the wide field mode

**Class Description**: <no docstring>

**Changes**:

- 2019-01-28 (KL) Changed column names and added units to header
- 2019-07-10 (KL) Shortened the list to only the swappable mirrors

Data
++++

.. figure:: micado_wide_field_mirror_list.png
    :name: fig:micado_wide_field_mirror_list

    

.. table::
    :name: tbl:micado_wide_field_mirror_list

    ======= ===== ===== ===== =========== ========== ===================
      name  outer inner angle temperature   action         filename     
    ======= ===== ===== ===== =========== ========== ===================
    I08_SM5   0.2   0.0     0        -190 reflection TER_mirror_gold.dat
    I09_SM6   0.2   0.0     0        -190 reflection TER_mirror_gold.dat
    ======= ===== ===== ===== =========== ========== ===================

The list of surfaces from the rotating optics wheel that are added to the optical train when observing in the wide field mode

Meta-data
+++++++++
::

                filename : LIST_MICADO_mirrors_wide.dat
                    name : micado_wide_field_mirror_list
             pixel_scale : 0.004
             plate_scale : 0.26666666666
            element_name : MICADO_IMG_LR
                  author : Kieran Leschinski
                  source : Ric's SPIE 2018 PPT presentation
            date_created : 2018-11-19
           date_modified : 2019-07-10
                  status : Design, pre PDR list of MICADO mirrors for wide-field mode
                    type : mirror:list
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




AtmosphericDispersionCorrection: "micado_adc_3D_shift"
******************************************************
**Included by default**: ``False``

**File Description**: atmospheric disperson corrector

**Class Description**: <no docstring>

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

                filename : None
                    name : micado_adc_3D_shift
                 include : False
             pixel_scale : 0.004
             plate_scale : 0.26666666666
            element_name : MICADO_IMG_LR
                altitude : !ATMO.altitude
               longitude : !ATMO.longitude
                latitude : !ATMO.latitude
                 airmass : !OBS.airmass
             temperature : !ATMO.temperature
                humidity : !ATMO.humidity
                pressure : !ATMO.pressure
             pupil_angle : !OBS.pupil_angle
              efficiency : 1
                wave_mid : !SIM.spectral.wave_mid
               quick_adc : True
                 z_order : [632, 232]
     report_plot_include : True
    report_table_include : False

