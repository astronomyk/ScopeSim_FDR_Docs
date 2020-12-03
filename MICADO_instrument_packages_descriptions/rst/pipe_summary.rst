Summary of Effects in Optical Elements:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table::
    :name: tbl:effects_summary

    ===================== ================================ =============================== ======== ===================
           element                      name                            class              included       z_orders     
    ===================== ================================ =============================== ======== ===================
                armazones armazones_atmo_default_ter_curve             AtmosphericTERCurve     True          [111, 511]
                armazones        armazones_atmo_dispersion           AtmosphericDispersion    False               [231]
                armazones armazones_atmo_skycalc_ter_curve                 SkycalcTERCurve    False          [112, 512]
                      ELT               scope_surface_list                     SurfaceList     True      [20, 120, 520]
                      ELT                  scope_vibration                       Vibration     True          [244, 744]
                      ELT          eso_combined_reflection                        TERCurve    False      [10, 110, 510]
                   MICADO           micado_static_surfaces                     SurfaceList     True      [20, 120, 520]
                   MICADO                 micado_ncpas_psf         NonCommonPathAberration     True          [241, 641]
                   MICADO                   filter_wheel_1                     FilterWheel     True     [124, 224, 524]
                   MICADO                   filter_wheel_2                     FilterWheel     True     [124, 224, 524]
                   MICADO                      pupil_wheel                     FilterWheel     True     [124, 224, 524]
    micado_detector_array              full_detector_array                    DetectorList    False [90, 290, 390, 490]
    micado_detector_array                  detector_window                    DetectorList     True [90, 290, 390, 490]
    micado_detector_array                         qe_curve          QuantumEfficiencyCurve     True          [113, 513]
    micado_detector_array                  exposure_action                  SummedExposure     True               [860]
    micado_detector_array                     dark_current                     DarkCurrent     True               [830]
    micado_detector_array               detector_linearity                  LinearityCurve     True               [840]
    micado_detector_array                       shot_noise                       ShotNoise     True               [820]
    micado_detector_array                    readout_noise        PoorMansHxRGReadoutNoise     True               [811]
               default_ro                        relay_psf                FieldConstantPSF     True          [262, 662]
               default_ro               relay_surface_list                     SurfaceList     True      [20, 120, 520]
                    MAORY               maory_surface_list                     SurfaceList     True      [20, 120, 520]
                    MAORY                maory_generic_psf                FieldConstantPSF     True          [262, 662]
            MICADO_IMG_LR    micado_wide_field_mirror_list                     SurfaceList     True      [20, 120, 520]
            MICADO_IMG_LR              micado_adc_3D_shift AtmosphericDispersionCorrection    False          [632, 232]
            MICADO_IMG_HR                 zoom_mirror_list                     SurfaceList     True      [20, 120, 520]
            MICADO_IMG_HR              micado_adc_3D_shift AtmosphericDispersionCorrection    False          [632, 232]
              MICADO_SPEC                 spec_mode_optics                     SurfaceList     True      [20, 120, 520]
              MICADO_SPEC      spectroscopic_slit_aperture                    ApertureMask     True      [80, 280, 380]
              MICADO_SPEC           micado_spectral_traces               SpectralTraceList     True           [70, 270]
    ===================== ================================ =============================== ======== ===================
