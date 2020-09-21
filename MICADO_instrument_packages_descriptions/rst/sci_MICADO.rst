
OpticalElement: "MICADO"
^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: instrument

**Alias**: INST
        
**Description**: base configuration for MICADO

Global properties
#################
::

        temperature : -190
    filename_format : filters/TC_filter_{}.dat
       element_name : MICADO


Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:MICADO
   
    ======= ==================== =========== ======== ============
    element         name            class    included z_orders [3]
    ======= ==================== =========== ======== ============
     MICADO        micado_filter FilterCurve     True   114 .. 514
     MICADO micado_common_optics    TERCurve     True    10 .. 510
    ======= ==================== =========== ======== ============
 



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

              filename : filters/TC_filter_Ks.dat
                  name : micado_filter
           temperature : -190
       filename_format : !INST.filename_format
          element_name : MICADO
           filter_name : !INST.filter_name
    minimum_throughput : 0.000101
                 outer : 0.2
            outer_unit : m
                author : Ric Davies
                source : Ric Davies
          date_created : 2017-11-20
         date_modified : 2017-11-20
                status : Design - pre PDR list of filters
                  type : filter:transmission
                center : 2.144876984095012
                 width : 0.3470169216021642
           blue_cutoff : 1.97136852329393
            red_cutoff : 2.3183854448960943
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




TERCurve: "micado_common_optics"
********************************
**Included by default**: ``True``

**File Description**: combined transmission for MICADO common optics

**Class Description**: Transmission, Emissivity, Reflection Curve

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

           filename : TER_MICADO_IMG_common.dat
               name : micado_common_optics
        temperature : -190
    filename_format : filters/TC_filter_{}.dat
       element_name : MICADO
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
           wave_min : !SIM.spectral.wave_min
           wave_max : !SIM.spectral.wave_max
          wave_unit : !SIM.spectral.wave_unit
           wave_bin : !SIM.spectral.spectral_resolution

