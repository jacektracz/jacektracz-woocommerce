import sys
import os
import ctypes

c_uint8 = ctypes.c_uint8
c_uint16 = ctypes.c_uint16
c_uint32 = ctypes.c_uint32

from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *


class CAP_fields(ctypes.LittleEndianStructure):
    _fields_ = [
            ("NP_number_of_ports", c_uint8, 4),
            ("SXS_supoorts_external_sata", c_uint8, 1),
            ("EMS_enclosure_management_supported", c_uint8, 1),
            ("CCCS_commad_completion_coalescing_supported", c_uint8, 1),
			("NCS_number_of_command_slots", c_uint8, 5),
			("PSC_partial_state_capable", c_uint8, 1),
			("SSC_slumber_state_capable", c_uint8, 1),
			("PMD_multiple_DRQ_block", c_uint8, 1),
			("FBSS_FIS_based_switching_supported", c_uint8, 1),
			("SPM_supports_port_multiplier", c_uint8, 1),
			("SAM_supports_AHCI_mode_only", c_uint8, 1),
			("RESERVED", c_uint8, 1),
			("ISS_interface_speed_support", c_uint8, 4),
			("SCLO_supoorts_command_list_override", c_uint8, 1),
			("SAL_supports_activity_LED", c_uint8, 1),
			("SALP_supports_aggressive_link_power_management", c_uint8, 1),
			("SSS_supports_staggered_spin_up", c_uint8, 1),
			("SMPS_supports_mechanical_presence_switch", c_uint8, 1),
			("SSNTF_supports_snotification_register", c_uint8, 1),
			("SNCQ_supports_native_command_queuing", c_uint8, 1),
			("S64A_supports_64bit_addressing", c_uint8, 1),
        ]

class CAP(ctypes.Union):
    _fields_ = [("b", CAP_fields),
                ("asbyte", c_uint32)]

class CAP2_fields(ctypes.LittleEndianStructure):
    _fields_ = [
            ("BOH_BIOS_OS_handoff", c_uint8, 1),
            ("NVMP_NVMHCI_present", c_uint8, 1),
            ("APST_automatic_partial_to_slumber_transitions", c_uint8, 1),
            ("SDS_supports_device_sleep", c_uint8, 1),
            ("SADM_supports_aggressive_device_sleep_management", c_uint8, 1),
            ("DESO_devlseep_entrance_from_slumber_only", c_uint8, 1),
            ("RESERVED", c_uint32, 26),
        ]

class CAP2(ctypes.Union):
    _fields_ = [("b", CAP2_fields),
                ("asbyte", c_uint32)]    

class PxCMD_fields(ctypes.LittleEndianStructure):
    _fields_ = [
            ("ST_start", c_uint8, 1),
            ("SUD_spin_up_device", c_uint8, 1),
            ("POD_power_on_device", c_uint8, 1),
            ("CLO_command_list_override", c_uint8, 1),
			("FRE_FIS_receive_enable", c_uint8, 1),
            ("CCS_current_command_slot", c_uint8, 5),
            ("MPSS_mechanical_presence_switch_state", c_uint8, 1),
            ("FR_FIS_receive_running", c_uint8, 1),
            ("CR_command_list_runing", c_uint8, 1),
			("CPS_cold_presence_state", c_uint8, 1),
            ("PMA_port_multiplier_attached", c_uint8, 1),
            ("HPCP_hot_plug_capable_port", c_uint8, 1),
            ("MPSP_mechanical_presence_swithc_attached", c_uint8, 1),
            ("CPD_cold_presence_detection", c_uint8, 1),
			("ESP_external_sata_port", c_uint8, 1),
            ("FBSCPFIS_based_switching_capable_port", c_uint8, 1),
            ("APSTE_automatic_partial_to_slumber_transitions_enabled", c_uint8, 1),
            ("ATAPI_device_is_atapi", c_uint8, 1),
            ("DLAE_drive_led_on_atapi_enable", c_uint8, 1),
			("ALPE_aggressive_link_power_management_enable", c_uint8, 1),
            ("ASP_aggresive_slumber_partial", c_uint8, 1),
			("ICC_interface_communication_control", c_uint8, 4),
        ]

class PxCMD(ctypes.Union):
    _fields_ = [("b", PxCMD_fields),
                ("asbyte", c_uint32)]


class PxSSTS_fields(ctypes.LittleEndianStructure):
    _fields_ = [
            ("DET_device_detection", c_uint8, 4),
            ("SPD_current_interface_speed", c_uint8, 4),
            ("IPM_interface_power_management", c_uint8, 4),
            ("RESERVED", c_uint32, 20),
        ]

class PxSSTS(ctypes.Union):
    _fields_ = [("b", PxSSTS_fields),
                ("asbyte", c_uint32)]
    
    
class PxSCTL_fields(ctypes.LittleEndianStructure):
    _fields_ = [
            ("DET_device_detection", c_uint8, 4),
            ("SPD_speed_allowed", c_uint8, 4),
            ("IPM_interface_power_management_transitions_allowed", c_uint8, 4),
            ("RESERVED", c_uint32, 20),
        ]

class PxSCTL(ctypes.Union):
    _fields_ = [("b", PxSCTL_fields),
                ("asbyte", c_uint32)]
    

class PxDEVSLP_fields(ctypes.LittleEndianStructure):
    _fields_ = [
            ("ADSE_aggresive_device_sleep_enable", c_uint8, 1),
            ("DSP_device_sleep_present", c_uint8, 1),
            ("DETO_device_sleep_exit_timeout", c_uint8, 8),
            ("MDAT_minimum_device_sleep_assertion_time", c_uint8, 5),
            ("DITO_device_sleep_idle_timeout", c_uint16, 10),
            ("DM_DITO_multiplier", c_uint8, 4),
            ("RESERVED", c_uint8, 3),
        ]

class PxDEVSLP(ctypes.Union):
    _fields_ = [("b", PxDEVSLP_fields),
                ("asbyte", c_uint32)]
    
    
class PxSACT_fields(ctypes.LittleEndianStructure):
    _fields_ = [
            ("DS_device_status", c_uint32, 32),
        ]

class PxSACT(ctypes.Union):
    _fields_ = [("b", PxSACT_fields),
                ("asbyte", c_uint32)]
    
class PxCI_fields(ctypes.LittleEndianStructure):
    _fields_ = [
            ("CI_command_issued", c_uint32, 32),
        ]

class PxCI(ctypes.Union):
    _fields_ = [("b", PxCI_fields),
                ("asbyte", c_uint32)]
    
    
