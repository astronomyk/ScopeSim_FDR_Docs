
OpticalElement: "micado_sci_detector"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: detector

**Alias**: DET
        
**Description**: List of MICADO detector effects relevant for astronomers

Global properties
#################
::

    image_plane_id : 0
       temperature : -230
               dit : !OBS.dit
              ndit : !OBS.ndit
             width : 4096
            height : 4096
                 x : 0
                 y : 0
      element_name : micado_sci_detector

        
Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:micado_sci_detector
   
    =================== ======================= ======================== ======== ===================
          element                 name                   class           included       z_orders     
    =================== ======================= ======================== ======== ===================
    micado_sci_detector  micado_detector_window           DetectorWindow     True [90, 290, 390, 490]
    micado_sci_detector           h4rg_qe_curve   QuantumEfficiencyCurve     True          [113, 513]
    micado_sci_detector         exposure_action           SummedExposure     True               [860]
    micado_sci_detector            dark_current              DarkCurrent     True               [830]
    micado_sci_detector              shot_noise                ShotNoise     True               [820]
    micado_sci_detector h4rg_detector_linearity           LinearityCurve    False               [840]
    micado_sci_detector           readout_noise PoorMansHxRGReadoutNoise     True               [811]
    =================== ======================= ======================== ======== ===================
 



DetectorWindow: "micado_detector_window"
****************************************
**Included by default**: ``True``

**File Description**: 

**Class Description**: For when a full DetectorList if too cumbersome

**Changes**:

- 

Data
++++

.. figure:: micado_detector_window.png
    :name: fig:micado_detector_window

    

.. table::
    :name: tbl:micado_detector_window

    === ====== ====== ========== =========== ===== ==== ==========
     id x_cen  y_cen    x_size      y_size   angle gain pixel_size
    === ====== ====== ========== =========== ===== ==== ==========
      0 !DET.x !DET.y !DET.width !DET.height     0    1      0.015
    === ====== ====== ========== =========== ===== ==== ==========



Meta-data
+++++++++
::

                filename : None
                    name : micado_detector_window
              orig_units : pixel
              x_cen_unit : pixel
              y_cen_unit : pixel
             x_size_unit : pixel
             y_size_unit : pixel
         pixel_size_unit : mm
              angle_unit : deg
               gain_unit : electron/adu
          image_plane_id : 0
             temperature : -230
                     dit : !OBS.dit
                    ndit : !OBS.ndit
            element_name : micado_sci_detector
                 z_order : [90, 290, 390, 490]
                 include : True
             pixel_scale : !INST.pixel_scale
        active_detectors : all
     report_plot_include : True
    report_table_include : True




QuantumEfficiencyCurve: "h4rg_qe_curve"
***************************************
**Included by default**: ``True``

**File Description**: Quantum efficiency curves for each detector

**Class Description**: <no docstring>

**Changes**:

- 2018-11-19 (KL) updated meta data to new format
- 2019-08-09 (KL) Added action keyword to meta data

Data
++++

.. figure:: h4rg_qe_curve.png
    :name: fig:h4rg_qe_curve

    

Meta-data
+++++++++
::

                filename : QE_detector_H2RG.dat
                    name : h4rg_qe_curve
          image_plane_id : 0
             temperature : -230
                     dit : 60
                    ndit : 1
                   width : 4096
                  height : 4096
                       x : 0
                       y : 0
            element_name : micado_sci_detector
                  author : Kieran Leschinski
                 sources : Finger+ 2008 SPIE
            date_created : 2016-01-01
           date_modified : 2019-08-09
                    type : detector:quantum_efficiency
                  status : Design, guestimated by reading off the graph in Finger+ 2008
         wavelength_unit : um
                  action : transmission
                 z_order : [113, 513]
                 include : True
            ignore_wings : False
                wave_min : 0.7
                wave_max : 2.5
               wave_unit : um
                wave_bin : 0.001
     report_plot_include : True
    report_table_include : False
                position : -1




SummedExposure: "exposure_action"
*********************************
**Included by default**: ``True``

**File Description**: Summing up sky signal for all DITs and NDITs

**Class Description**: Simulates a summed stack of ``ndit`` exposures

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

          filename : None
              name : exposure_action
    image_plane_id : 0
       temperature : -230
               dit : !OBS.dit
              ndit : !OBS.ndit
             width : 4096
            height : 4096
                 x : 0
                 y : 0
      element_name : micado_sci_detector
           z_order : [860]
           include : True




DarkCurrent: "dark_current"
***************************
**Included by default**: ``True``

**File Description**: MICADO dark current

**Class Description**: required: dit, ndit, value

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

          filename : None
              name : dark_current
    image_plane_id : 0
       temperature : -230
               dit : !OBS.dit
              ndit : !OBS.ndit
             width : 4096
            height : 4096
                 x : 0
                 y : 0
      element_name : micado_sci_detector
             value : 0.1
           z_order : [830]
           include : True




ShotNoise: "shot_noise"
***********************
**Included by default**: ``True``

**File Description**: apply poisson shot noise to images

**Class Description**: <no docstring>

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

          filename : None
              name : shot_noise
    image_plane_id : 0
       temperature : -230
               dit : !OBS.dit
              ndit : !OBS.ndit
             width : 4096
            height : 4096
                 x : 0
                 y : 0
      element_name : micado_sci_detector
           z_order : [820]
           include : True
       random_seed : !SIM.random.seed




LinearityCurve: "h4rg_detector_linearity"
*****************************************
**Included by default**: ``False``

**File Description**: Linearity characteristics of H4RG chips

**Class Description**: <no docstring>

**Changes**:

- 2018-11-19 (KL) updated meta data to new format
- 2019-08-14 (KL) replaced long 1000000000 with 1e99

Data
++++

.. figure:: h4rg_detector_linearity.png
    :name: fig:h4rg_detector_linearity

    

Meta-data
+++++++++
::

                filename : FPA_linearity.dat
                    name : h4rg_detector_linearity
                 include : False
          image_plane_id : 0
             temperature : -230
                     dit : !OBS.dit
                    ndit : !OBS.ndit
                   width : 4096
                  height : 4096
                       x : 0
                       y : 0
            element_name : micado_sci_detector
                  author : Kieran Leschinski
                 sources : Ingraham+ 2014 - Gemini Calibrations II for H2RG
            date_created : 2016-01-01
           date_modified : 2018-11-19
                    type : detector:linearity
                  status : Design, approximated from the H2RG
           incident_unit : ph
           measured_unit : ph
                 z_order : [840]
     report_plot_include : True
    report_table_include : False




PoorMansHxRGReadoutNoise: "readout_noise"
*****************************************
**Included by default**: ``True``

**File Description**: Readout noise frames

**Class Description**: <no docstring>

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

                filename : None
                    name : readout_noise
          image_plane_id : 0
             temperature : -230
                     dit : !OBS.dit
                    ndit : !OBS.ndit
                   width : 4096
                  height : 4096
                       x : 0
                       y : 0
            element_name : micado_sci_detector
               noise_std : 12
              n_channels : 64
                 z_order : [811]
                 include : True
       pedestal_fraction : 0.3
           read_fraction : 0.4
           line_fraction : 0.25
        channel_fraction : 0.05
             random_seed : !SIM.random.seed
     report_plot_include : False
    report_table_include : False

