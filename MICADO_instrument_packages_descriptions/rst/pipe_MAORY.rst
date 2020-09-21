
OpticalElement: "MAORY"
^^^^^^^^^^^^^^^^^^^^^^^

**Element**: relay_optics

**Alias**: RO
        
**Description**: MAORY AO relay module

Global properties
#################
::

     temperature : !ATMO.temperature
    psf_filename : None
    element_name : MAORY


Effects
#######

Summary of Effects included in this optical element:

.. table::
    :name: tbl:MAORY
   
    ======= ================== ================ ======== ==============
    element        name             class       included    z_orders   
    ======= ================== ================ ======== ==============
      MAORY maory_surface_list      SurfaceList     True [20, 120, 520]
      MAORY  maory_generic_psf FieldConstantPSF     True     [262, 662]
    ======= ================== ================ ======== ==============
 



SurfaceList: "maory_surface_list"
*********************************
**Included by default**: ``True``

**File Description**: list of surfaces in MAORY

**Class Description**: <no docstring>

**Changes**:

- 2018-11-19 (KL) Added meta data, changed Dichr. filename
- 2019-01-28 (KL) Fixed YAML format in meta data
- 2020-06-22 (KL) Obsolete. Use LIST_mirrors_maory_mms.tbl from now on.

Data
++++

Meta-data
+++++++++
::

              filename : LIST_mirrors_MCAO_MAORY.tbl
                  name : maory_surface_list
           temperature : !ATMO.temperature
          psf_filename : None
          element_name : MAORY
                author : Kieran Leschinski
                source : Ciliegi+ 2018 SPIE, "MAORY for ELT - preliminary design overview"
          date_created : 2018-11-19
         date_modified : 2018-11-19
                status : Design - pre PDR list of MAORY mirrors
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




FieldConstantPSF: "maory_generic_psf"
*************************************
**Included by default**: ``True``

**File Description**: MAORY field varying MCAO PSF

**Class Description**: <no docstring>

**Changes**:

- 

Data
++++

Meta-data
+++++++++
::

            filename : PSF_MCAO_ConstPSF_40_18_6.fits
                name : maory_generic_psf
         temperature : 7
        psf_filename : None
        element_name : MAORY
             warning : Default PSF is not Field Varying. See Documentation
              SIMPLE : True
              BITPIX : 8
               NAXIS : 0
              EXTEND : True
              AUTHOR : Kieran Leschinski
            DATE_CRE : 2019-07-30
            DATE_MOD : 2019-07-30
              SOURCE : AnisoCADO
              STATUS : Best guess for a MAORY ConstantPSF with AnisoCADO
               ETYPE : CONSTPSF
                ECAT : -1
               EDATA : 1
             XOFFSET : 0
             YOFFSET : 0
             z_order : [262, 662]
             include : True
       flux_accuracy : 0.001
      sub_pixel_flag : False
       convolve_mode : full
            wave_key : WAVE0
    normalise_kernel : True

