
OpticalElement: "MICADO_IMG_HR"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: instrument

**Alias**: INST
        
**Description**: additional effects for the zoom imaging mode

Global properties
#################
::

     pixel_scale : 0.0015
     plate_scale : 0.1
    element_name : MICADO_IMG_HR


Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:MICADO_IMG_HR
   
    ============= =================== =============================== ======== ==============
       element            name                     class              included    z_orders   
    ============= =================== =============================== ======== ==============
    MICADO_IMG_HR    zoom_mirror_list                     SurfaceList     True [20, 120, 520]
    MICADO_IMG_HR micado_adc_3D_shift AtmosphericDispersionCorrection     True     [632, 232]
    ============= =================== =============================== ======== ==============
 



SurfaceList: "zoom_mirror_list"
*******************************
**Included by default**: ``True``

**File Description**: list of extra mirror needed for the zoom imaging mode

**Class Description**: <no docstring>

**Changes**:

- {datetime.date(2019, 1, 28): '(KL) Changed column names and added units to header'}
- {datetime.date(2019, 7, 10): '(KL) Shortened the list to only the swappable mirrors'}

Data
++++

Meta-data
+++++++++
::

              filename : LIST_MICADO_mirrors_zoom.dat
                  name : zoom_mirror_list
           pixel_scale : 0.0015
           plate_scale : 0.1
          element_name : MICADO_IMG_HR
                author : Kieran Leschinski
                source : Ric's SPIE 2018 PPT presentation
          date_created : 2018-11-19
         date_modified : 2019-07-10
                status : Design - pre PDR list of swappable mirrors for zoom mode
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
    minimum_throughput : !SIM.spectral.minimum_throughput
               etendue : !TEL.etendue




AtmosphericDispersionCorrection: "micado_adc_3D_shift"
******************************************************
**Included by default**: ``True``

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
     pixel_scale : 0.0015
     plate_scale : 0.1
    element_name : MICADO_IMG_HR
        altitude : !ATMO.altitude
       longitude : !ATMO.longitude
        latitude : !ATMO.latitude
         airmass : !OBS.airmass
     temperature : !ATMO.temperature
        humidity : !ATMO.humidity
        pressure : !ATMO.pressure
     pupil_angle : !OBS.pupil_angle
        wave_mid : !SIM.spectral.wave_mid
      efficiency : 1
       quick_adc : True
         z_order : [632, 232]
         include : True

