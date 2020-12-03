Summary of Effects in Optical Elements:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table::
    :name: tbl:effects_summary

    =================== ================================ ======================== ======== ===================
          element                     name                        class           included       z_orders     
    =================== ================================ ======================== ======== ===================
              armazones armazones_atmo_skycalc_ter_curve          SkycalcTERCurve     True          [112, 512]
             MICADO_Sci             micado_common_optics                 TERCurve     True      [10, 110, 510]
             MICADO_Sci                     filter_wheel              FilterWheel     True     [124, 224, 524]
    micado_sci_detector           micado_detector_window           DetectorWindow     True [90, 290, 390, 490]
    micado_sci_detector                    h4rg_qe_curve   QuantumEfficiencyCurve     True          [113, 513]
    micado_sci_detector                  exposure_action           SummedExposure     True               [860]
    micado_sci_detector                     dark_current              DarkCurrent     True               [830]
    micado_sci_detector                       shot_noise                ShotNoise     True               [820]
    micado_sci_detector          h4rg_detector_linearity           LinearityCurve    False               [840]
    micado_sci_detector                    readout_noise PoorMansHxRGReadoutNoise     True               [811]
            MICADO_SPEC           micado_adjustable_slit  RectangularApertureMask     True      [80, 280, 380]
            MICADO_SPEC        spectral_trace_3000x50mas        SpectralTraceList     True           [70, 270]
            MICADO_SCAO            scao_relay_optics_ter                 TERCurve     True      [10, 110, 510]
            MICADO_SCAO                   scao_const_psf        AnisocadoConstPSF     True           [42, 652]
            MICADO_MCAO                    maory_mms_ter                 TERCurve     True      [10, 110, 510]
            MICADO_MCAO                  maory_const_psf        AnisocadoConstPSF     True           [42, 652]
    =================== ================================ ======================== ======== ===================
