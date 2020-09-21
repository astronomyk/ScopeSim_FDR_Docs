Summary of Effects in Optical Elements:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table::
    :name: tbl:effects_summary

    =================== ===================== ======================== ======== ===================
          element                name                  class           included       z_orders     
    =================== ===================== ======================== ======== ===================
                 MICADO         micado_filter              FilterCurve     True     [114, 214, 514]
                 MICADO  micado_common_optics                 TERCurve     True      [10, 110, 510]
    micado_sci_detector       detector_window           DetectorWindow     True [90, 290, 390, 490]
    micado_sci_detector              qe_curve   QuantumEfficiencyCurve     True          [113, 513]
    micado_sci_detector       exposure_action           SummedExposure     True               [860]
    micado_sci_detector          dark_current              DarkCurrent     True               [830]
    micado_sci_detector            shot_noise                ShotNoise     True               [820]
    micado_sci_detector         readout_noise PoorMansHxRGReadoutNoise     True               [811]
            MICADO_SCAO scao_relay_optics_ter                 TERCurve     True      [10, 110, 510]
            MICADO_SCAO        scao_const_psf        AnisocadoConstPSF     True                [42]
            MICADO_MCAO         maory_mms_ter                 TERCurve     True      [10, 110, 510]
            MICADO_MCAO       maory_const_psf        AnisocadoConstPSF     True                [42]
    =================== ===================== ======================== ======== ===================
