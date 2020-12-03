
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
          season : 0
            time : 0
      background : {'filter_name': 'Ks', 'value': 13.6, 'unit': 'mag'}
    element_name : armazones

        
Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:armazones
   
    ========= ================================ =============== ======== ============
     element                name                    class      included z_orders [2]
    ========= ================================ =============== ======== ============
    armazones armazones_atmo_skycalc_ter_curve SkycalcTERCurve     True   112 .. 512
    ========= ================================ =============== ======== ============
 



SkycalcTERCurve: "armazones_atmo_skycalc_ter_curve"
***************************************************
**Included by default**: ``True``

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
                  season : 0
                    time : 0
              background : {'filter_name': 'Ks', 'value': 13.6, 'unit': 'mag'}
            element_name : armazones
             observatory : armazones
                    wmin : 699.9999999999999
                    wmax : 2499.9999999999995
                   wunit : um
                  wdelta : 0.9999999999999999
        rescale_emission : {'filter_name': 'Ks', 'filename_format': 'filters/TC_filter_{}.dat', 'value': 13.6, 'unit': 'mag'}
                 z_order : [112, 512]
            ignore_wings : False
                wave_min : 0.7
                wave_max : 2.5
               wave_unit : um
                wave_bin : 0.001
     report_plot_include : True
    report_table_include : False
                  action : transmission
                position : 0

