
OpticalElement: "armazones"
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: atmosphere

**Alias**: ATMO
        
**Description**: Atmosphere and location details for Cerro Armazones

Global properties
#################
::

        altitude : 3060
       longitude : -70.1918
        latitude : -24.5899
     temperature : 7
        humidity : 0.1
        pressure : 0.755
             pwv : 2.5
         airmass : !OBS.airmass
     pupil_angle : !OBS.pupil_angle
     pixel_scale : !INST.pixel_scale
    element_name : armazones


Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:armazones
   
    ========= ================================ ===================== ======== ==========
     element                name                       class         included  z_orders 
    ========= ================================ ===================== ======== ==========
    armazones armazones_atmo_default_ter_curve   AtmosphericTERCurve     True [111, 511]
    armazones        armazones_atmo_dispersion AtmosphericDispersion     True      [231]
    armazones armazones_atmo_skycalc_ter_curve       SkycalcTERCurve    False [112, 512]
    ========= ================================ ===================== ======== ==========
 



AtmosphericTERCurve: "armazones_atmo_default_ter_curve"
*******************************************************
**Included by default**: ``True``

**File Description**: atmospheric emission and transmission

**Class Description**: <no docstring>

**Changes**:

- 2019-07-24 (KL) Created file
- 2019-08-09 (KL) Updated values for airmass 1.2, pwv 2.5

Data
++++

Meta-data
+++++++++
::

           filename : TER_armazones_default_NIR_IMG.dat
               name : armazones_atmo_default_ter_curve
            include : True
           altitude : 3060
          longitude : -70.1918
           latitude : -24.5899
        temperature : 7
           humidity : 0.1
           pressure : 0.755
                pwv : 2.5
            airmass : !OBS.airmass
        pupil_angle : !OBS.pupil_angle
        pixel_scale : !INST.pixel_scale
       element_name : armazones
             author : Kieran Leschinski
             source : skycalc website for standard Armazones conditions
       date_created : 2019-07-24
      date_modified : 2019-08-09
             status : Design
               type : atmosphere:ter_curve
             season : entire year
               time : entire night
             action : transmission
    wavelength_unit : um
      emission_unit : ph s-1 m-2 um-1 arcsec-2
            z_order : [111, 511]
       ignore_wings : False
           wave_min : !SIM.spectral.wave_min
           wave_max : !SIM.spectral.wave_max
          wave_unit : !SIM.spectral.wave_unit
           wave_bin : !SIM.spectral.spectral_resolution
               area : !TEL.area
          area_unit : m2
           position : 0




AtmosphericDispersion: "armazones_atmo_dispersion"
**************************************************
**Included by default**: ``True``

**File Description**: atmospheric dispersion

**Class Description**: Used to generate the wavelength bins based on shifts due to the atmosphere

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

              filename : None
                  name : armazones_atmo_dispersion
              altitude : 3060
             longitude : -70.1918
              latitude : -24.5899
           temperature : 7
              humidity : 0.1
              pressure : 0.755
                   pwv : 2.5
               airmass : !OBS.airmass
           pupil_angle : !OBS.pupil_angle
           pixel_scale : !INST.pixel_scale
          element_name : armazones
               z_order : [231]
               include : True
              wave_min : !SIM.spectral.wave_min
              wave_mid : !SIM.spectral.wave_mid
              wave_max : !SIM.spectral.wave_max
    sub_pixel_fraction : !SIM.sub_pixel.fraction
             num_steps : 1000




SkycalcTERCurve: "armazones_atmo_skycalc_ter_curve"
***************************************************
**Included by default**: ``False``

**File Description**: atmospheric spectra pulled from the skycalc server

**Class Description**: <no docstring>

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

        filename : None
            name : armazones_atmo_skycalc_ter_curve
         include : False
        altitude : 3060
       longitude : -70.1918
        latitude : -24.5899
     temperature : 7
        humidity : 0.1
        pressure : 0.755
             pwv : 2.5
         airmass : !OBS.airmass
     pupil_angle : !OBS.pupil_angle
     pixel_scale : !INST.pixel_scale
    element_name : armazones
     observatory : armazones
            wmin : 699.9999999999999
            wmax : 2499.9999999999995
           wunit : um
          wdelta : 0.09999999999999999
         z_order : [112, 512]
    ignore_wings : False
        wave_min : !SIM.spectral.wave_min
        wave_max : !SIM.spectral.wave_max
       wave_unit : !SIM.spectral.wave_unit
        wave_bin : !SIM.spectral.spectral_resolution
          action : transmission
            area : !TEL.area
       area_unit : m2
        position : 0

