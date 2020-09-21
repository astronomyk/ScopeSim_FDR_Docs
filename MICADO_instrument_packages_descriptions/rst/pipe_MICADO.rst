
OpticalElement: "MICADO"
^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: instrument

**Alias**: INST
        
**Description**: Effects from the MICADO common optics

Global properties
#################
::

     temperature : -190
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
     MICADO          micado_filter             FilterCurve     True [114, 214, 514]
     MICADO       micado_ncpas_psf NonCommonPathAberration     True      [241, 641]
    ======= ====================== ======================= ======== ===============
 



SurfaceList: "micado_static_surfaces"
*************************************
**Included by default**: ``True``

**File Description**: surfaces list for wide field optics

**Class Description**: <no docstring>

**Changes**:

- {datetime.date(2019, 1, 28): '(KL) Changed column names and added units to header'}
- {datetime.date(2019, 7, 10): '(KL) Shortened the list to only the swappable mirrors'}
- {datetime.date(2020, 8, 25): '(KL) Updated angle_unit to degree from degrees (why has astropy not complained until now?)'}

Data
++++

Meta-data
+++++++++
::

              filename : LIST_MICADO_mirrors_static.dat
                  name : micado_static_surfaces
           temperature : -190
          element_name : MICADO
                author : Kieran Leschinski
                source : Ric's SPIE 2018 PPT presentation
          date_created : 2018-11-19
         date_modified : 2019-07-10
                status : Design - pre PDR list of all static MICADO surfaces
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
    minimum_throughput : !SIM.spectral.minimum_throughput
               etendue : !TEL.etendue




FilterCurve: "micado_filter"
****************************
**Included by default**: ``True``

**File Description**: transmission curve for filter

**Class Description**: Other Parameters

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

              filename : filters/TC_filter_Spec_HK.dat
                  name : micado_filter
           temperature : -190
          element_name : MICADO
           filter_name : !OBS.filter_name
       filename_format : filters/TC_filter_{}.dat
    minimum_throughput : 0.000101
                 outer : 0.2
            outer_unit : m
                author : Ric Davies
                source : Ric Davies
          date_created : 2017-11-20
         date_modified : 2017-11-20
                status : Design - pre PDR list of filters
               z_order : [114, 214, 514]
               include : True
          ignore_wings : False
              wave_min : !SIM.spectral.wave_min
              wave_max : !SIM.spectral.wave_max
             wave_unit : !SIM.spectral.wave_unit
              wave_bin : !SIM.spectral.spectral_resolution
                action : transmission
              position : -1
       wing_flux_level : None




NonCommonPathAberration: "micado_ncpas_psf"
*******************************************
**Included by default**: ``True``

**File Description**: Effective NCPA induced PSF kernel

**Class Description**: Needed: pixel_scale

**Changes**:

- 2018-11-19 (KL) updated meta data to new format

Data
++++

Meta-data
+++++++++
::

            filename : INST_MICADO_wavefront_error_budget.dat
                name : micado_ncpas_psf
         temperature : -190
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
        kernel_width : None
        strehl_drift : 0.02
            wave_min : !SIM.spectral.wave_min
            wave_max : !SIM.spectral.wave_max

