
OpticalElement: "default_ro"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Element**: relay_optics

**Alias**: RO
        
**Description**: Simple stand-alone relay optics module

Global properties
#################
::

     temperature : !ATMO.temperature
    psf_filename : None
    element_name : default_ro


Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:default_ro
   
    ========== ================== ================ ======== ==============
     element          name             class       included    z_orders   
    ========== ================== ================ ======== ==============
    default_ro          relay_psf FieldConstantPSF     True     [262, 662]
    default_ro relay_surface_list      SurfaceList     True [20, 120, 520]
    ========== ================== ================ ======== ==============
 



FieldConstantPSF: "relay_psf"
*****************************
**Included by default**: ``True``

**File Description**: SCAO PSF

**Class Description**: <no docstring>

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

            filename : PSF_SCAO_ConstPSF_0_5off.fits
                name : relay_psf
         temperature : 7
        psf_filename : None
        element_name : default_ro
             warning : Default PSF is NOT field varying. See documentation.
              SIMPLE : True
              BITPIX : 8
               NAXIS : 0
              EXTEND : True
              AUTHOR : Kieran Leschinski
            DATE_CRE : 2019-07-30
            DATE_MOD : 2019-07-30
              SOURCE : AnisoCADO
              STATUS : Best guess for a standard observations
               ETYPE : CONSTPSF
                ECAT : -1
               EDATA : 1
             XOFFSET : 0
             YOFFSET : 5
             z_order : [262, 662]
             include : True
       flux_accuracy : 0.001
      sub_pixel_flag : False
       convolve_mode : full
            wave_key : WAVE0
    normalise_kernel : True




SurfaceList: "relay_surface_list"
*********************************
**Included by default**: ``True``

**File Description**: list of surfaces in the relay optics

**Class Description**: <no docstring>

**Changes**:

- 2018-11-19 (KL) Added meta data
- 2019-01-28 (KL) Fixed YAML format in meta data
- 2020-07-18 (KL) Added all 6 mirrors from the CM16 update pdf
- 2020-07-18 (KL) Pegged temperature to atmosphere

Data
++++

Meta-data
+++++++++
::

              filename : LIST_RO_SCAO_mirrors.dat
                  name : relay_surface_list
           temperature : !ATMO.temperature
          psf_filename : None
          element_name : default_ro
                author : Oliver Czoske, Kieran Leschinski
                source : P12_RelayOptics_Status_2020-06-23-MICADO-CM16-RO-v2.pdf
          date_created : 2018-11-19
         date_modified : 2020-08-17
                status : Design - pre FDR list of stand-alone SCAO relay optics mirrors
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

