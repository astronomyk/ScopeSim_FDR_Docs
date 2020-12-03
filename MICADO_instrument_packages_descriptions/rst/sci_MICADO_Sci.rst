
OpticalElement: "MICADO_Sci"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: instrument

**Alias**: INST
        
**Description**: base configuration for MICADO

Global properties
#################
::

           temperature : -190
    filter_file_format : filters/TC_filter_{}.dat
          element_name : MICADO_Sci

        
Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:MICADO_Sci
   
    ========== ==================== =========== ======== ============
     element           name            class    included z_orders [3]
    ========== ==================== =========== ======== ============
    MICADO_Sci micado_common_optics    TERCurve     True    10 .. 510
    MICADO_Sci         filter_wheel FilterWheel     True   124 .. 524
    ========== ==================== =========== ======== ============
 



TERCurve: "micado_common_optics"
********************************
**Included by default**: ``True``

**File Description**: combined transmission for MICADO common optics

**Class Description**: Transmission, Emissivity, Reflection Curve

**Changes**:

- 

Data
++++

.. figure:: micado_common_optics.png
    :name: fig:micado_common_optics

    

Meta-data
+++++++++
::

                filename : TER_MICADO_IMG_common.dat
                    name : micado_common_optics
             temperature : -190
      filter_file_format : filters/TC_filter_{}.dat
            element_name : MICADO_Sci
                  author : Auto-compiled from source
                  source : LIST_MICADO_mirrors_static.dat
            date_created : 2020-08-25
           date_modified : 2020-08-25
                    area : 0.19634954084936207
               area_unit : m2
         wavelength_unit : um
           emission_unit : photlam
                 z_order : [10, 110, 510]
                 include : True
            ignore_wings : False
                wave_min : 0.7
                wave_max : 2.5
               wave_unit : um
                wave_bin : 0.001
     report_plot_include : True
    report_table_include : False




FilterWheel: "filter_wheel"
***************************
**Included by default**: ``True``

**File Description**: 

**Class Description**: Examples

**Changes**:

- 

Data
++++

.. figure:: filter_wheel.png
    :name: fig:filter_wheel

    

.. table::
    :name: tbl:filter_wheel

    ======== ====== ====== =========== ==========
      name   centre width  blue cutoff red cutoff
               um     um        um         um    
    ======== ====== ====== =========== ==========
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
    ======== ====== ====== =========== ==========



Meta-data
+++++++++
::

                 filename : None
                     name : filter_wheel
              temperature : -190
       filter_file_format : filters/TC_filter_{}.dat
             element_name : MICADO_Sci
             filter_names : ['I-long', 'Y', 'J', 'H', 'Ks', 'J-short', 'J-long', 'H-short', 'H-long', 'K-short', 'K-mid', 'Spec_IJ', 'Spec_HK', 'xI1', 'xI2', 'xY1', 'xY2', 'xJ1', 'xJ2', 'xH1', 'xH2', 'xK1', 'xK2', 'blank', 'H-cont', 'FeII', 'H2_1-0S1', 'Br-gamma', 'K-cont', 'K-long', 'He-I', 'Pa-beta', 'ND1', 'ND3']
          filename_format : !INST.filter_file_format
           current_filter : !INST.filter_name
       minimum_throughput : 0.000101
                    outer : 0.2
               outer_unit : m
                  z_order : [124, 224, 524]
                  include : True
                     path : 
      report_plot_include : True
     report_table_include : True
    report_table_rounding : 4

