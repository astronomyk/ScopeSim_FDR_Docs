
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
      background : {'filter_name': 'Ks', 'value': 13.6, 'unit': 'mag'}
        spectrum : {'filename': 'TER_armazones_default_FULL_IMG.dat'}
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
    armazones        armazones_atmo_dispersion AtmosphericDispersion    False      [231]
    armazones armazones_atmo_skycalc_ter_curve       SkycalcTERCurve    False [112, 512]
    ========= ================================ ===================== ======== ==========
 



AtmosphericTERCurve: "armazones_atmo_default_ter_curve"
*******************************************************
**Included by default**: ``True``

**File Description**: atmospheric emission and transmission

**Class Description**: <no docstring>

**Changes**:

- 2020-10-29 (MV) Created file

Data
++++

.. figure:: armazones_atmo_default_ter_curve.png
    :name: fig:armazones_atmo_default_ter_curve

    

Meta-data
+++++++++
::

                filename : TER_armazones_default_FULL_IMG.dat
                    name : armazones_atmo_default_ter_curve
                 include : True
                altitude : 3060
               longitude : -70.1918
                latitude : -24.5899
             temperature : 7
                humidity : 0.1
                pressure : 0.755
                     pwv : 2.5
                 airmass : 1.2
             pupil_angle : 0
             pixel_scale : 0.004
              background : {'filter_name': 'Ks', 'value': 13.6, 'unit': 'mag'}
                spectrum : {'filename': 'TER_armazones_default_FULL_IMG.dat'}
            element_name : armazones
                    area : 0
        rescale_emission : {'filter_name': 'Ks', 'filename_format': 'filters/TC_filter_{}.dat', 'value': 13.6, 'unit': 'mag'}
                  author : Miguel Verdugo
                  source : skycalc_ipy tool for standard Armazones conditions
            date_created : 2020-10-29
           date_modified : 2020-10-29
                  status : Design
                    type : atmosphere:ter_curve
                  wdelta : 10
                    wmin : 300
                    wmax : 15000
                  season : entire year
                    time : entire night
                  action : transmission
         wavelength_unit : um
           emission_unit : ph s-1 m-2 um-1 arcsec-2
                 z_order : [111, 511]
            ignore_wings : False
                wave_min : 0.7
                wave_max : 2.5
               wave_unit : um
                wave_bin : 0.0001
     report_plot_include : True
    report_table_include : False
                position : 0




AtmosphericDispersion: "armazones_atmo_dispersion"
**************************************************
**Included by default**: ``False``

**File Description**: atmospheric dispersion

**Class Description**: Used to generate the wavelength bins based on shifts due to the atmosphere

**Changes**:

- 

Data
++++

.. figure:: armazones_atmo_dispersion.png
    :name: fig:armazones_atmo_dispersion

    

Meta-data
+++++++++
::

                filename : None
                    name : armazones_atmo_dispersion
                 include : False
                altitude : 3060
               longitude : -70.1918
                latitude : -24.5899
             temperature : 7
                humidity : 0.1
                pressure : 0.755
                     pwv : 2.5
                 airmass : 1.2
             pupil_angle : 0
             pixel_scale : 0.004
              background : {'filter_name': 'Ks', 'value': 13.6, 'unit': 'mag'}
                spectrum : {'filename': 'TER_armazones_default_FULL_IMG.dat'}
            element_name : armazones
                 z_order : [231]
     report_plot_include : True
    report_table_include : False
                wave_min : 0.7
                wave_mid : 1.6
                wave_max : 2.5
      sub_pixel_fraction : 1
               num_steps : 1000
                      z0 : 33.55730976192071
                    temp : 7
                 rel_hum : 10.0
                    pres : 755.0
                     lat : -24.5899
                       h : 3060




SkycalcTERCurve: "armazones_atmo_skycalc_ter_curve"
***************************************************
**Included by default**: ``False``

**File Description**: atmospheric spectra pulled from the skycalc server

**Class Description**: <no docstring>

**Changes**:

- 

Data
++++

.. figure:: armazones_atmo_skycalc_ter_curve.png
    :name: fig:armazones_atmo_skycalc_ter_curve

    

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
                 airmass : 1.2
             pupil_angle : 0
             pixel_scale : 0.004
              background : {'filter_name': 'Ks', 'value': 13.6, 'unit': 'mag'}
                spectrum : {'filename': 'TER_armazones_default_FULL_IMG.dat'}
            element_name : armazones
             observatory : armazones
                    wmin : 699.9999999999999
                    wmax : 2499.9999999999995
                   wunit : um
                  wdelta : 0.09999999999999999
                 z_order : [112, 512]
            ignore_wings : False
                wave_min : 0.7
                wave_max : 2.5
               wave_unit : um
                wave_bin : 0.0001
     report_plot_include : True
    report_table_include : False
                  action : transmission
                position : 0

