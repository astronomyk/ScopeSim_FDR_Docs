
OpticalElement: "micado_detector_array"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: detector

**Alias**: DET
        
**Description**: A set of 9 H4RG detectors

Global properties
#################
::

    image_plane_id : 0
       temperature : -230
               dit : !OBS.dit
              ndit : !OBS.ndit
      element_name : micado_detector_array


Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:micado_detector_array
   
    ===================== =================== ======================== ======== ===================
           element                name                 class           included       z_orders     
    ===================== =================== ======================== ======== ===================
    micado_detector_array full_detector_array             DetectorList    False [90, 290, 390, 490]
    micado_detector_array     detector_window             DetectorList     True [90, 290, 390, 490]
    micado_detector_array            qe_curve   QuantumEfficiencyCurve     True          [113, 513]
    micado_detector_array     exposure_action           SummedExposure     True               [860]
    micado_detector_array        dark_current              DarkCurrent     True               [830]
    micado_detector_array  detector_linearity           LinearityCurve     True               [840]
    micado_detector_array          shot_noise                ShotNoise     True               [820]
    micado_detector_array       readout_noise PoorMansHxRGReadoutNoise     True               [811]
    ===================== =================== ======================== ======== ===================
 



DetectorList: "full_detector_array"
***********************************
**Included by default**: ``False``

**File Description**: MICADO detector array list

**Class Description**: A description of detector positions and properties

**Changes**:

- {datetime.date(2017, 8, 12): '(OC) id changed to conform with spectroscopy report'}
- {datetime.date(2018, 7, 26): '(OC) large gap (chips 5 and 6) reduced to 8 mm'}
- {datetime.date(2018, 11, 19): '(KL) updated meta data to new format'}
- {datetime.date(2019, 1, 28): '(KL) moved units into header'}

Data
++++

.. figure:: full_detector_array.png
    :name: fig:full_detector_array

    

.. table::
    :name: tbl:full_detector_array

    === ====== ====== ====== ====== ===== ===== ========== ===== ====
     id x_cen  y_cen  x_size y_size x_len y_len pixel_size angle gain
    === ====== ====== ====== ====== ===== ===== ========== ===== ====
      1 -63.84  63.84  61.44  61.44  4096  4096      0.015   0.0  1.0
      2    0.0  63.84  61.44  61.44  4096  4096      0.015   0.0  1.0
      3  63.84  63.84  61.44  61.44  4096  4096      0.015   0.0  1.0
      4  63.84    0.0  61.44  61.44  4096  4096      0.015   0.0  1.0
      5    0.0    0.0  61.44  61.44  4096  4096      0.015   0.0  1.0
      6 -69.44    0.0  61.44  61.44  4096  4096      0.015   0.0  1.0
      7 -63.84 -63.84  61.44  61.44  4096  4096      0.015   0.0  1.0
      8    0.0 -63.84  61.44  61.44  4096  4096      0.015   0.0  1.0
      9  63.84 -63.84  61.44  61.44  4096  4096      0.015   0.0  1.0
    === ====== ====== ====== ====== ===== ===== ========== ===== ====



Meta-data
+++++++++
::

                filename : FPA_array_layout.dat
                    name : full_detector_array
                 include : False
          image_plane_id : 0
             temperature : -230
                     dit : !OBS.dit
                    ndit : !OBS.ndit
            element_name : micado_detector_array
        active_detectors : all
                  author : Oliver Czoske
                 sources : E-MCD-FPA-572089EB.uda, ELT-TRE-MCD-56300-0011
            date_created : 2017-06-28
           date_modified : 2018-07-26
                    type : detector:chip_list
              x_cen_unit : mm
              y_cen_unit : mm
                xhw_unit : mm
                yhw_unit : mm
              x_len_unit : pix
              y_len_unit : pix
            pixsize_unit : mm
              angle_unit : deg
               gain_unit : electron/adu
                 z_order : [90, 290, 390, 490]
             pixel_scale : !INST.pixel_scale
     report_plot_include : True
    report_table_include : True
             x_size_unit : mm
             y_size_unit : mm




DetectorList: "detector_window"
*******************************
**Included by default**: ``True``

**File Description**: 

**Class Description**: A description of detector positions and properties

**Changes**:

- 

Data
++++

.. figure:: detector_window.png
    :name: fig:detector_window

    

.. table::
    :name: tbl:detector_window

    === ========== ===== ==== ===== ===== ====== ======
     id pixel_size angle gain x_cen y_cen x_size y_size
    === ========== ===== ==== ===== ===== ====== ======
      1      0.015   0.0  1.0   0.0   0.0  15.36  15.36
    === ========== ===== ==== ===== ===== ====== ======



Meta-data
+++++++++
::

                filename : None
                    name : detector_window
                 include : True
          image_plane_id : 0
             temperature : -230
                     dit : !OBS.dit
                    ndit : !OBS.ndit
            element_name : micado_detector_array
              x_cen_unit : mm
              y_cen_unit : mm
                xhw_unit : mm
                yhw_unit : mm
            pixsize_unit : mm
              angle_unit : deg
               gain_unit : electron/adu
                 z_order : [90, 290, 390, 490]
              array_dict : {'id': [1], 'pixsize': [0.015], 'angle': [0.0], 'gain': [1.0], 'x_cen': [0.0], 'y_cen': [0.0], 'xhw': [7.68], 'yhw': [7.68]}
             pixel_scale : !INST.pixel_scale
        active_detectors : all
     report_plot_include : True
    report_table_include : True
             x_size_unit : mm
             y_size_unit : mm




QuantumEfficiencyCurve: "qe_curve"
**********************************
**Included by default**: ``True``

**File Description**: Quantum efficiency curves for each detector

**Class Description**: <no docstring>

**Changes**:

- {datetime.date(2018, 11, 19): '(KL) updated meta data to new format'}
- {datetime.date(2019, 8, 9): '(KL) Added action keyword to meta data'}

Data
++++

Meta-data
+++++++++
::

           filename : QE_detector_H2RG.dat
               name : qe_curve
     image_plane_id : 0
        temperature : -230
                dit : !OBS.dit
               ndit : !OBS.ndit
       element_name : micado_detector_array
             author : Kieran Leschinski
            sources : Finger+ 2008 SPIE
       date_created : 2016-01-01
      date_modified : 2019-08-09
               type : detector:quantum_efficiency
             status : Design - guestimated by reading off the graph in Finger+ 2008
    wavelength_unit : um
             action : transmission
            z_order : [113, 513]
            include : True
       ignore_wings : False
           wave_min : !SIM.spectral.wave_min
           wave_max : !SIM.spectral.wave_max
          wave_unit : !SIM.spectral.wave_unit
           wave_bin : !SIM.spectral.spectral_resolution
           position : -1




SummedExposure: "exposure_action"
*********************************
**Included by default**: ``True``

**File Description**: Summing up sky signal for all DITs and NDITs

**Class Description**: <no docstring>

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
      element_name : micado_detector_array
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
      element_name : micado_detector_array
             value : 0.1
           z_order : [830]
           include : True




LinearityCurve: "detector_linearity"
************************************
**Included by default**: ``True``

**File Description**: Linearity characteristics of H4RG chips

**Class Description**: <no docstring>

**Changes**:

- 2018-11-19 (KL) updated meta data to new format
- 2019-08-14 (KL) replaced long 1000000000 with 1e99

Data
++++

Meta-data
+++++++++
::

          filename : FPA_linearity.dat
              name : detector_linearity
    image_plane_id : 0
       temperature : -230
               dit : !OBS.dit
              ndit : !OBS.ndit
      element_name : micado_detector_array
            author : Kieran Leschinski
           sources : Ingraham+ 2014 - Gemini Calibrations II for H2RG
      date_created : 2016-01-01
     date_modified : 2018-11-19
              type : detector:linearity
            status : Design - approximated from the H2RG
     incident_unit : ph
     measured_unit : ph
           z_order : [840]
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
      element_name : micado_detector_array
           z_order : [820]
           include : True
       random_seed : !SIM.random.seed




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
         element_name : micado_detector_array
            noise_std : 12
           n_channels : 64
              z_order : [811]
              include : True
    pedestal_fraction : 0.3
        read_fraction : 0.4
        line_fraction : 0.25
     channel_fraction : 0.05
          random_seed : !SIM.random.seed

