
OpticalElement: "ELT"
^^^^^^^^^^^^^^^^^^^^^

**Element**: telescope

**Alias**: TEL
        
**Description**: The extremely large telescope

Global properties
#################
::

     temperature : !ATMO.temperature
    element_name : ELT


Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:ELT
   
    ======= ======================= =========== ======== ==============
    element           name             class    included    z_orders   
    ======= ======================= =========== ======== ==============
        ELT      scope_surface_list SurfaceList     True [20, 120, 520]
        ELT         scope_vibration   Vibration     True     [244, 744]
        ELT eso_combined_reflection    TERCurve    False [10, 110, 510]
    ======= ======================= =========== ======== ==============
 



SurfaceList: "scope_surface_list"
*********************************
**Included by default**: ``True``

**File Description**: list of ELT surfaces

**Class Description**: <no docstring>

**Changes**:

- 2018-11-19 (KL) Added meta data, added Action column
- 2019-01-28 (KL) Fixed YAML format in meta data
- 2020-08-17 (KL) Updated M1 and M4 dimensions according to ESO-253082_4 sect 4.7 "all-glass" diameter
- 2020-08-17 (KL) Pegged temperature to the atmosphere

Data
++++

Meta-data
+++++++++
::

              filename : LIST_mirrors_ELT.tbl
                  name : scope_surface_list
           temperature : !ATMO.temperature
          element_name : ELT
                author : Oliver Czoske, Kieran Leschinski
                source : ESO ELT DRM, ESO-253082_4
          date_created : 2018-11-19
         date_modified : 2020-08-17
                status : Design - pre MICADO-FDR mirror list
            outer_unit : m
            inner_unit : m
            angle_unit : degree
      temperature_unit : deg_C
                 notes : ['2020-08-17 (KL) Coatings match those described in ESO-253082_4']
               z_order : [20, 120, 520]
               include : True
          ignore_wings : False
              wave_min : !SIM.spectral.wave_min
              wave_max : !SIM.spectral.wave_max
             wave_unit : !SIM.spectral.wave_unit
              wave_bin : !SIM.spectral.spectral_resolution
    minimum_throughput : !SIM.spectral.minimum_throughput
               etendue : !TEL.etendue




Vibration: "scope_vibration"
****************************
**Included by default**: ``True``

**File Description**: residual vibration of telescope

**Class Description**: Creates a wavelength independent kernel image

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

            filename : None
                name : scope_vibration
         temperature : 7
        element_name : ELT
                fwhm : 0.001
         pixel_scale : 0.004
             z_order : [244, 744]
             include : True
       flux_accuracy : 0.001
      sub_pixel_flag : False
       convolve_mode : full
            wave_key : WAVE0
    normalise_kernel : True
       width_n_fwhms : 4




TERCurve: "eso_combined_reflection"
***********************************
**Included by default**: ``False``

**File Description**: single combined reflection curve for clean ELT 5 mirror combination

**Class Description**: Transmission, Emissivity, Reflection Curve

**Changes**:

- 2019-11-06 (KL) Converted from .xlsx to .dat file, added ScopeSim meta data
- 2020-07-09 (KL) Added inner and outer dimensions to meta, for use with MICADO-Sci
- 2020-08-17 (KL) Added emissivity column according to ESO-253082_4, sect 4.12.2

Data
++++

Meta-data
+++++++++
::

           filename : TER_ELT_system_20190611.dat
               name : eso_combined_reflection
            include : False
        temperature : !ATMO.temperature
       element_name : ELT
         temperture : !ATMO.temperature
             author : R. Holzloehner
             source : See ESO-306070 and ESO-293390 for background.
       date_created : 2018-09-18
      date_modified : 2019-06-11
               type : TERCurve
             status : design
             action : reflection
              outer : 37.3
         outer_unit : m
              inner : 11.1
         inner_unit : m
    wavelength_unit : um
              notes : ['Baseline coatings.', 'Fresh coatings without contamination.', '4nm roughness modeled.', 'Partly based on measured data by Tom Schneider (Gemini).', 'Reflection is for the combined M1-M5 system, not for individual mirrors', 'Emissivity is calculated from ESO-253082_4, sect 4.12.2']
            z_order : [10, 110, 510]
       ignore_wings : False
           wave_min : !SIM.spectral.wave_min
           wave_max : !SIM.spectral.wave_max
          wave_unit : !SIM.spectral.wave_unit
           wave_bin : !SIM.spectral.spectral_resolution

