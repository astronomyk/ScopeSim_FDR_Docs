
OpticalElement: "MICADO"
^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: instrument

**Alias**: INST
        
**Description**: Effects from the MICADO common optics

Global properties
#################
::

           temperature : -190
    filter_file_format : filters/TC_filter_{}.dat
          element_name : MICADO

        
Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:MICADO
   
    ======= ====================== ======================= ======== ===============
    element          name                   class          included     z_orders   
    ======= ====================== ======================= ======== ===============
     MICADO micado_static_surfaces             SurfaceList     True  [20, 120, 520]
     MICADO       micado_ncpas_psf NonCommonPathAberration     True      [241, 641]
     MICADO         filter_wheel_1             FilterWheel     True [124, 224, 524]
     MICADO         filter_wheel_2             FilterWheel     True [124, 224, 524]
     MICADO            pupil_wheel             FilterWheel     True [124, 224, 524]
    ======= ====================== ======================= ======== ===============
 



SurfaceList: "micado_static_surfaces"
*************************************
**Included by default**: ``True``

**File Description**: surfaces list for wide field optics

**Class Description**: <no docstring>

**Changes**:

- 2019-01-28 (KL) Changed column names and added units to header
- 2019-07-10 (KL) Shortened the list to only the swappable mirrors
- 2020-08-25 (KL) Updated angle_unit to degree from degrees (why has astropy not complained until now?)
- 2020-10-10 (KL) Added SCAO pick-off dichroic after CM17 conversation

Data
++++

.. figure:: micado_static_surfaces.png
    :name: fig:micado_static_surfaces

    

.. table::
    :name: tbl:micado_static_surfaces

    =========== ===== ===== ===== =========== ============ =======================
        name    outer inner angle temperature    action            filename       
    =========== ===== ===== ===== =========== ============ =======================
    I00_EntrWin   0.5   0.0     0           0 transmission TER_entrance_window.dat
    I09_SCAO_PO   0.5   0.0    45        -190   reflection   TER_SCAO_dichroic.dat
      I01_Fold1   0.5   0.0    45        -190   reflection     TER_mirror_gold.dat
      I02_Coli1   0.4   0.0    10        -190   reflection     TER_mirror_gold.dat
      I03_Coli2   0.2   0.0    10        -190   reflection     TER_mirror_gold.dat
      I04_Coli3   0.2   0.0    10        -190   reflection     TER_mirror_gold.dat
      I05_Fold2   0.2   0.0    45        -190   reflection     TER_mirror_gold.dat
        I07_ADC   0.2   0.0     0        -190 transmission        TER_full_adc.dat
      I10_Fold3   0.2   0.0    45        -190   reflection     TER_mirror_gold.dat
      I11_ReIm1   0.2   0.0    10        -190   reflection     TER_mirror_gold.dat
      I12_ReIm2   0.2   0.0    10        -190   reflection     TER_mirror_gold.dat
      I13_ReIm3   0.2   0.0    10        -190   reflection     TER_mirror_gold.dat
    =========== ===== ===== ===== =========== ============ =======================



Meta-data
+++++++++
::

                filename : LIST_MICADO_mirrors_static.dat
                    name : micado_static_surfaces
             temperature : -190
      filter_file_format : filters/TC_filter_{}.dat
            element_name : MICADO
                  author : Kieran Leschinski
                  source : Ric's SPIE 2018 PPT presentation
            date_created : 2018-11-19
           date_modified : 2019-07-10
                  status : Design, pre PDR list of all static MICADO surfaces
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




NonCommonPathAberration: "micado_ncpas_psf"
*******************************************
**Included by default**: ``True``

**File Description**: Effective NCPA induced PSF kernel

**Class Description**: Needed: pixel_scale

**Changes**:

- 2018-11-19 (KL) updated meta data to new format

Data
++++

.. figure:: micado_ncpas_psf.png
    :name: fig:micado_ncpas_psf

    

Meta-data
+++++++++
::

                filename : INST_MICADO_wavefront_error_budget.dat
                    name : micado_ncpas_psf
             temperature : -190
      filter_file_format : filters/TC_filter_{}.dat
            element_name : MICADO
             pixel_scale : 0.004
                  author : Kieran Leschinski
                 sources : Ric Davies email
            date_created : 2016-11-21
           date_modified : 2018-11-19
                    type : instrument:wavefront_errors_list
                  status : Idea - based on the WFE budget and emails with Ric
            wfe_rms_unit : nm
                 z_order : [241, 641]
                 include : True
           flux_accuracy : 0.001
          sub_pixel_flag : False
           convolve_mode : full
                wave_key : WAVE0
        normalise_kernel : True
     report_plot_include : True
    report_table_include : False
            kernel_width : None
            strehl_drift : 0.02
                wave_min : !SIM.spectral.wave_min
                wave_max : !SIM.spectral.wave_max




FilterWheel: "filter_wheel_1"
*****************************
**Included by default**: ``True``

**File Description**: 

**Class Description**: Examples

**Changes**:

- 

Data
++++

.. figure:: filter_wheel_1.png
    :name: fig:filter_wheel_1

    

.. table::
    :name: tbl:filter_wheel_1

    ======= ====== ====== =========== ==========
      name  centre width  blue cutoff red cutoff
    ======= ====== ====== =========== ==========
     I-long 0.8689 0.1340      0.8019     0.9359
          Y 1.0396 0.1550      0.9621     1.1171
          J 1.2502 0.1950      1.1527     1.3477
          H 1.6395 0.2900      1.4945     1.7845
         Ks 2.1500 0.3500      1.9750     2.3250
    J-short 1.1902 0.0490      1.1657     1.2147
     J-long 1.2702 0.0490      1.2457     1.2947
    H-short 1.5830 0.0850      1.5405     1.6255
     H-long 1.6937 0.1120      1.6377     1.7497
    K-short 2.0602 0.0600      2.0302     2.0902
      K-mid 2.1005 0.1000      2.0505     2.1505
    Spec_IJ 1.1663 0.6990      0.8168     1.5158
    Spec_HK 2.0345 1.0200      1.5245     2.5445
      blank 2.7545 2.7000      1.4045     4.1045
    ======= ====== ====== =========== ==========



Meta-data
+++++++++
::

                 filename : None
                     name : filter_wheel_1
              temperature : -190
       filter_file_format : filters/TC_filter_{}.dat
             element_name : MICADO
             filter_names : ['I-long', 'Y', 'J', 'H', 'Ks', 'J-short', 'J-long', 'H-short', 'H-long', 'K-short', 'K-mid', 'Spec_IJ', 'Spec_HK', 'blank']
          filename_format : !INST.filter_file_format
           current_filter : !OBS.filter_name_fw1
       minimum_throughput : 0.000101
                    outer : 0.2
               outer_unit : m
                  z_order : [124, 224, 524]
                  include : True
                     path : 
      report_plot_include : True
     report_table_include : True
    report_table_rounding : 4




FilterWheel: "filter_wheel_2"
*****************************
**Included by default**: ``True``

**File Description**: 

**Class Description**: Examples

**Changes**:

- 

Data
++++

.. figure:: filter_wheel_2.png
    :name: fig:filter_wheel_2

    

.. table::
    :name: tbl:filter_wheel_2

    ===== ====== ====== =========== ==========
     name centre width  blue cutoff red cutoff
    ===== ====== ====== =========== ==========
      xI1 0.8355 0.0680      0.8015     0.8695
      xI2 0.9005 0.0680      0.8665     0.9345
      xY1 1.0006 0.0800      0.9606     1.0406
      xY2 1.0756 0.0800      1.0356     1.1156
      xJ1 1.2009 0.1100      1.1459     1.2559
      xJ2 1.3007 0.1000      1.2507     1.3507
      xH1 1.5465 0.1600      1.4665     1.6265
      xH2 1.7064 0.1600      1.6264     1.7864
      xK1 2.0612 0.1600      1.9812     2.1412
      xK2 2.2211 0.1600      2.1411     2.3011
    blank 2.7545 2.7000      1.4045     4.1045
    ===== ====== ====== =========== ==========



Meta-data
+++++++++
::

                 filename : None
                     name : filter_wheel_2
              temperature : -190
       filter_file_format : filters/TC_filter_{}.dat
             element_name : MICADO
             filter_names : ['xI1', 'xI2', 'xY1', 'xY2', 'xJ1', 'xJ2', 'xH1', 'xH2', 'xK1', 'xK2', 'blank']
          filename_format : !INST.filter_file_format
           current_filter : !OBS.filter_name_fw2
       minimum_throughput : 0.000101
                    outer : 0.2
               outer_unit : m
                  z_order : [124, 224, 524]
                  include : True
                     path : 
      report_plot_include : True
     report_table_include : True
    report_table_rounding : 4




FilterWheel: "pupil_wheel"
**************************
**Included by default**: ``True``

**File Description**: 

**Class Description**: Examples

**Changes**:

- 

Data
++++

.. figure:: pupil_wheel.png
    :name: fig:pupil_wheel

    

.. table::
    :name: tbl:pupil_wheel

    ======== ====== ====== =========== ==========
      name   centre width  blue cutoff red cutoff
    ======== ====== ====== =========== ==========
      H-cont 1.5701 0.0220      1.5591     1.5811
        FeII 1.6495 0.0210      1.6390     1.6600
    H2_1-0S1 2.1289 0.0280      2.1149     2.1429
    Br-gamma 2.1734 0.0280      2.1594     2.1874
      K-cont 2.2019 0.0270      2.1884     2.2154
      K-long 2.3081 0.0440      2.2861     2.3301
        He-I 2.0656 0.0270      2.0521     2.0791
     Pa-beta 1.2865 0.0170      1.2780     1.2950
         ND1 2.7529 0.0000      2.7529     2.7529
         ND3 2.7529 0.0000      2.7529     2.7529
       blank 2.7545 2.7000      1.4045     4.1045
    ======== ====== ====== =========== ==========



Meta-data
+++++++++
::

                 filename : None
                     name : pupil_wheel
              temperature : -190
       filter_file_format : filters/TC_filter_{}.dat
             element_name : MICADO
             filter_names : ['H-cont', 'FeII', 'H2_1-0S1', 'Br-gamma', 'K-cont', 'K-long', 'He-I', 'Pa-beta', 'ND1', 'ND3', 'blank']
          filename_format : !INST.filter_file_format
           current_filter : !OBS.filter_name_pupil
       minimum_throughput : 0.000101
                    outer : 0.2
               outer_unit : m
                  z_order : [124, 224, 524]
                  include : True
                     path : 
      report_plot_include : True
     report_table_include : True
    report_table_rounding : 4

