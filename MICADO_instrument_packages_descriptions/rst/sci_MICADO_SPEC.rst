
OpticalElement: "MICADO_SPEC"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: instrument

**Alias**: INST
        
**Description**: MICADO SPEC mode effects

Global properties
#################
::

             psf : {'wavelength': '!INST.filter_name', 'strehl': 0.4}
        aperture : {'x': 0, 'y': 0, 'width': 3, 'height': 0.05}
    element_name : MICADO_SPEC

        
Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:MICADO_SPEC
   
    =========== ========================= ======================= ======== ==============
      element              name                    class          included    z_orders   
    =========== ========================= ======================= ======== ==============
    MICADO_SPEC    micado_adjustable_slit RectangularApertureMask     True [80, 280, 380]
    MICADO_SPEC spectral_trace_3000x50mas       SpectralTraceList     True      [70, 270]
    =========== ========================= ======================= ======== ==============
 



RectangularApertureMask: "micado_adjustable_slit"
*************************************************
**Included by default**: ``True``

**File Description**: 

**Class Description**: <no docstring>

**Changes**:

- 

Data
++++

.. table::
    :name: tbl:micado_adjustable_slit

    ======= =======
       x       y   
    ======= =======
    -1.5000 -0.0250
     1.5000 -0.0250
     1.5000  0.0250
    -1.5000  0.0250
    ======= =======



Meta-data
+++++++++
::

                 filename : None
                     name : micado_adjustable_slit
                      psf : {'wavelength': 'Ks', 'strehl': 0.4}
                 aperture : {'x': 0, 'y': 0, 'width': 3, 'height': 0.05}
             element_name : MICADO_SPEC
                    width : !INST.aperture.width
                   height : !INST.aperture.height
                        x : !INST.aperture.x
                        y : !INST.aperture.y
                  z_order : [80, 280, 380]
                  include : True
              pixel_scale : !INST.pixel_scale
                  no_mask : True
                    angle : 0
                    shape : rect
           conserve_image : True
                       id : 0
      report_plot_include : False
     report_table_include : True
    report_table_rounding : 4
                   x_unit : arcsec
                   y_unit : arcsec




SpectralTraceList: "spectral_trace_3000x50mas" : 1 traces
*********************************************************
**Included by default**: ``True``

**File Description**: 

**Class Description**: List of spectral trace geometries for the detector plane

**Changes**:

- 

Data
++++

.. figure:: spectral_trace_3000x50mas.png
    :name: fig:spectral_trace_3000x50mas

    

Meta-data
+++++++++
::

                filename : TRACE_SCI_3arcsec.fits
                    name : spectral_trace_3000x50mas
                     psf : {'wavelength': 'Ks', 'strehl': 0.4}
                aperture : {'x': 0, 'y': 0, 'width': 3, 'height': 0.05}
            element_name : MICADO_SPEC
      center_on_wave_mid : True
                  SIMPLE : True
                  BITPIX : 8
                   NAXIS : 0
                  EXTEND : True
                    ECAT : 1
                   EDATA : 2
                 z_order : [70, 270]
                 include : True
             pixel_scale : !INST.pixel_scale
             plate_scale : !INST.plate_scale
                wave_min : !SIM.spectral.wave_min
                wave_mid : !SIM.spectral.wave_mid
                wave_max : !SIM.spectral.wave_max
               x_colname : x
               y_colname : y
               s_colname : s
            wave_colname : wavelength
        col_number_start : 0
                   dwave : 0.002
           invalid_value : None
     report_plot_include : True
    report_table_include : False

