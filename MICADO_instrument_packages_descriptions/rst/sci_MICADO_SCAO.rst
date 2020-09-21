
OpticalElement: "MICADO_SCAO"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: instrument

**Alias**: INST
        
**Description**: MICADO SCAO mode effects

Global properties
#################
::

             psf : {'strehl': 0.4, 'wavelength': 'Ks'}
    element_name : MICADO_SCAO


Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:MICADO_SCAO
   
    =========== ===================== ================= ======== ==============
      element            name               class       included    z_orders   
    =========== ===================== ================= ======== ==============
    MICADO_SCAO scao_relay_optics_ter          TERCurve     True [10, 110, 510]
    MICADO_SCAO        scao_const_psf AnisocadoConstPSF     True           [42]
    =========== ===================== ================= ======== ==============
 



TERCurve: "scao_relay_optics_ter"
*********************************
**Included by default**: ``True``

**File Description**: Combined TER curve for stand-alone relay optics module

**Class Description**: Transmission, Emissivity, Reflection Curve

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

           filename : TER_MICADO_RO.dat
               name : scao_relay_optics_ter
                psf : {'strehl': 0.4, 'wavelength': 'Ks'}
       element_name : MICADO_SCAO
             author : Auto-compiled from source
             source : LIST_RO_SCAO_mirrors.dat
       date_created : 2020-08-25
      date_modified : 2020-08-25
               area : 0.22061834409834324
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




AnisocadoConstPSF: "scao_const_psf"
***********************************
**Included by default**: ``True``

**File Description**: field constant PSF as produced by stand-alone SCAO

**Class Description**: Makes a SCAO on-axis PSF with a desired Strehl ratio at a given wavelength

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

                  filename : MICADO_AnisoCADO_rms_map.fits
                      name : scao_const_psf
                       psf : {'strehl': 0.4, 'wavelength': 'Ks'}
              element_name : MICADO_SCAO
                    strehl : !INST.psf.strehl
                wavelength : !INST.psf.wavelength
           psf_side_length : 256
                    offset : [0, 0]
             rounded_edges : True
             convolve_mode : full
                    SIMPLE : True
                    BITPIX : -64
                     NAXIS : 2
                    NAXIS1 : 35
                    NAXIS2 : 9
                    EXTEND : True
                    CRVAL1 : 0
                    CRVAL2 : 0.8
                    CRPIX1 : 1.0
                    CRPIX2 : 1.0
                    CDELT1 : 20
                    CDELT2 : 0.2
                    CUNIT1 : nm
                    CUNIT2 : um
                    CTYPE1 : LINEAR
                    CTYPE2 : LINEAR
                    LABEL1 : nmRMS
                    LABEL2 : wavelength
                    AUTHOR : Kieran Leschinski
                  DATE_CRE : 2019-07-30
                  DATE_MOD : 2019-07-30
                    SOURCE : AnisoCADO
                    STATUS : Strehl as a function of wavelength and wavefront error (nmRMS)
                     ETYPE : SRMAP
                      ECAT : -1
                     EDATA : 0
                   XOFFSET : 0
                   YOFFSET : 0
                   z_order : [42]
                   include : True
             flux_accuracy : 0.001
            sub_pixel_flag : False
                  wave_key : WAVE0
          normalise_kernel : True
    filter_filename_format : !INST.filename_format

