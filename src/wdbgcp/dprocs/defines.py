

import ctypes
c_uint8 = ctypes.c_uint8
c_uint16 = ctypes.c_uint16
c_uint32 = ctypes.c_uint32

disk_state_map = {}
disk_state_map['SPARE_DISK'] = 0x01  
disk_state_map['CONFIGURED_DISK'] = 0x02  
disk_state_map['FAILED_DISK'] = 0x04
disk_state_map['USABLE_DISK'] = 0x08
disk_state_map['DETECTED_DISK'] = 0x10
disk_state_map['CLAIMED_DISK'] = 0x20 
disk_state_map['PASSTHRU_DISK'] = 0x40
disk_state_map['OFFLINE_DISK'] = 0x80 
disk_state_map['CONFIG_ON_DISK'] = 0x100
disk_state_map['DISK_SMART_EVENT_TRIGGERED'] = 0x200 
disk_state_map['DISK_SMART_EVENT_SUPPORTED'] = 0x400 
disk_state_map['FORMATTING_DISK'] = 0x800
disk_state_map['FORMAT_SUCCEEDED'] = 0x1000
disk_state_map['FORMAT_FAILED'] = 0x2000
disk_state_map['ELIGIBLE_FOR_SPARE'] = 0x4000
disk_state_map['OFFLINE_ARRAY_MEMBER'] = 0x8000
disk_state_map['CONFIG_IS_UPREV'] = 0x10000
disk_state_map['DISK_WRITE_CACHE_DISABLED'] = 0x20000
disk_state_map['UNKNOWN_DISK_FAILURE'] = 0x40000
disk_state_map['DO_READ_CONFIG'] = 0x80000 
disk_state_map['POWERED_OFF_DISK'] = 0x100000
disk_state_map['BOOTABLE_DISK'] = 0x200000
disk_state_map['CLONE_DISK_MODIFIED'] = 0x400000
disk_state_map['PASSTHRU_DISK_WMPB'] = 0x800000
disk_state_map['LOCKED_DISK'] = 0x1000000
disk_state_map['NVM_DEVICE'] = 0x2000000 
disk_state_map['NVMHCI_HEALTH_FAILED'] = 0x4000000 
disk_state_map['NVMHCI_HEALTH_READONLY'] = 0x8000000
disk_state_map['PORT_IN_D3'] = 0x10000000
disk_state_map['SDR0_IS_HIDDEN'] = 0x20000000      
disk_state_map['CVFD_ELIGIBLE_DISK'] = 0x40000000  
disk_state_map['NEWLY_ADDED_DISK'] = 0x80000000 

srb_functions_map = {}
srb_functions_map[0x0] = 'SRB_FUNCTION_EXECUTE_SCSI'
srb_functions_map[0x01] = 'SRB_FUNCTION_CLAIM_DEVICE'
srb_functions_map[0x02] = 'SRB_FUNCTION_IO_CONTROL'
srb_functions_map[0x03] = 'SRB_FUNCTION_RECEIVE_EVENT'
srb_functions_map[0x04] = 'SRB_FUNCTION_RELEASE_QUEUE'
srb_functions_map[0x05] = 'SRB_FUNCTION_ATTACH_DEVICE'
srb_functions_map[0x06] = 'SRB_FUNCTION_RELEASE_DEVICE'
srb_functions_map[0x07] = 'SRB_FUNCTION_SHUTDOWN'
srb_functions_map[0x08] = 'SRB_FUNCTION_FLUSH'
srb_functions_map[0x10] = 'SRB_FUNCTION_ABORT_COMMAND'
srb_functions_map[0x11] = 'SRB_FUNCTION_RELEASE_RECOVERY'
srb_functions_map[0x12] = 'SRB_FUNCTION_RESET_BUS'
srb_functions_map[0x13] = 'SRB_FUNCTION_RESET_DEVICE'
srb_functions_map[0x14] = 'SRB_FUNCTION_TERMINATE_IO'
srb_functions_map[0x15] = 'SRB_FUNCTION_FLUSH_QUEUE'
srb_functions_map[0x16] = 'SRB_FUNCTION_REMOVE_DEVICE'
srb_functions_map[0x17] = 'SRB_FUNCTION_WMI'
srb_functions_map[0x18] = 'SRB_FUNCTION_LOCK_QUEUE'
srb_functions_map[0x19] = 'SRB_FUNCTION_UNLOCK_QUEUE'
srb_functions_map[0x1a] = 'SRB_FUNCTION_QUIESCE_DEVICE'
srb_functions_map[0x20] = 'SRB_FUNCTION_RESET_LOGICAL_UNIT'
srb_functions_map[0x21] = 'SRB_FUNCTION_SET_LINK_TIMEOUT'
srb_functions_map[0x22] = 'SRB_FUNCTION_LINK_TIMEOUT_OCCURRED'
srb_functions_map[0x23] = 'SRB_FUNCTION_LINK_TIMEOUT_COMPLETE'
srb_functions_map[0x24] = 'SRB_FUNCTION_POWER'
srb_functions_map[0x25] = 'SRB_FUNCTION_PNP'
srb_functions_map[0x26] = 'SRB_FUNCTION_DUMP_POINTERS'
srb_functions_map[0x27] = 'SRB_FUNCTION_FREE_DUMP_POINTERS'
srb_functions_map[0x28] = 'SRB_FUNCTION_STORAGE_REQUEST_BLOCK'

srb_status_map = {}
srb_status_map[0x00] = 'SRB_STATUS_PENDING'
srb_status_map[0x01] = 'SRB_STATUS_SUCCESS'
srb_status_map[0x02] = 'SRB_STATUS_ABORTED'
srb_status_map[0x03] = 'SRB_STATUS_ABORT_FAILED'
srb_status_map[0x04] = 'SRB_STATUS_ERROR'
srb_status_map[0x05] = 'SRB_STATUS_BUSY'
srb_status_map[0x06] = 'SRB_STATUS_INVALID_REQUEST'
srb_status_map[0x07] = 'SRB_STATUS_INVALID_PATH_ID'
srb_status_map[0x08] = 'SRB_STATUS_NO_DEVICE'
srb_status_map[0x09] = 'SRB_STATUS_TIMEOUT'
srb_status_map[0x0A] = 'SRB_STATUS_SELECTION_TIMEOUT'
srb_status_map[0x0B] = 'SRB_STATUS_COMMAND_TIMEOUT'
srb_status_map[0x0D] = 'SRB_STATUS_MESSAGE_REJECTED'
srb_status_map[0x0E] = 'SRB_STATUS_BUS_RESET'
srb_status_map[0x0F] = 'SRB_STATUS_PARITY_ERROR'
srb_status_map[0x10] = 'SRB_STATUS_REQUEST_SENSE_FAILED'
srb_status_map[0x11] = 'SRB_STATUS_NO_HBA'
srb_status_map[0x12] = 'SRB_STATUS_DATA_OVERRUN'
srb_status_map[0x13] = 'SRB_STATUS_UNEXPECTED_BUS_FREE'
srb_status_map[0x14] = 'SRB_STATUS_PHASE_SEQUENCE_FAILURE'
srb_status_map[0x15] = 'SRB_STATUS_BAD_SRB_BLOCK_LENGTH'
srb_status_map[0x16] = 'SRB_STATUS_REQUEST_FLUSHED'
srb_status_map[0x20] = 'SRB_STATUS_INVALID_LUN'
srb_status_map[0x21] = 'SRB_STATUS_INVALID_TARGET_ID'
srb_status_map[0x22] = 'SRB_STATUS_BAD_FUNCTION'
srb_status_map[0x23] = 'SRB_STATUS_ERROR_RECOVERY'
srb_status_map[0x24] = 'SRB_STATUS_NOT_POWERED'
srb_status_map[0x25] = 'SRB_STATUS_LINK_DOWN'
srb_status_map[0x30] = 'SRB_STATUS_INTERNAL_ERROR'


# 6-byte commands:
srb_scsiop_map = {}
srb_scsiop_map[0x00] = 'SCSIOP_TEST_UNIT_READY'
srb_scsiop_map[0x01] = 'SCSIOP_REZERO_UNIT'
srb_scsiop_map[0x01] = 'SCSIOP_REWIND'
srb_scsiop_map[0x02] = 'SCSIOP_REQUEST_BLOCK_ADDR'
srb_scsiop_map[0x03] = 'SCSIOP_REQUEST_SENSE'
srb_scsiop_map[0x04] = 'SCSIOP_FORMAT_UNIT'
srb_scsiop_map[0x05] = 'SCSIOP_READ_BLOCK_LIMITS'
srb_scsiop_map[0x07] = 'SCSIOP_REASSIGN_BLOCKS'
srb_scsiop_map[0x07] = 'SCSIOP_INIT_ELEMENT_STATUS'
srb_scsiop_map[0x08] = 'SCSIOP_READ6'
srb_scsiop_map[0x08] = 'SCSIOP_RECEIVE'
srb_scsiop_map[0x0A] = 'SCSIOP_WRITE6'
srb_scsiop_map[0x0A] = 'SCSIOP_PRINT'
srb_scsiop_map[0x0A] = 'SCSIOP_SEND'
srb_scsiop_map[0x0B] = 'SCSIOP_SEEK6'
srb_scsiop_map[0x0B] = 'SCSIOP_TRACK_SELECT'
srb_scsiop_map[0x0B] = 'SCSIOP_SLEW_PRINT'
srb_scsiop_map[0x0B] = 'SCSIOP_SET_CAPACITY'
srb_scsiop_map[0x0C] = 'SCSIOP_SEEK_BLOCK'
srb_scsiop_map[0x0D] = 'SCSIOP_PARTITION'
srb_scsiop_map[0x0F] = 'SCSIOP_READ_REVERSE'
srb_scsiop_map[0x10] = 'SCSIOP_WRITE_FILEMARKS'
srb_scsiop_map[0x10] = 'SCSIOP_FLUSH_BUFFER'
srb_scsiop_map[0x11] = 'SCSIOP_SPACE'
srb_scsiop_map[0x12] = 'SCSIOP_INQUIRY'
srb_scsiop_map[0x13] = 'SCSIOP_VERIFY6'
srb_scsiop_map[0x14] = 'SCSIOP_RECOVER_BUF_DATA'
srb_scsiop_map[0x15] = 'SCSIOP_MODE_SELECT'
srb_scsiop_map[0x16] = 'SCSIOP_RESERVE_UNIT'
srb_scsiop_map[0x17] = 'SCSIOP_RELEASE_UNIT'
srb_scsiop_map[0x18] = 'SCSIOP_COPY'
srb_scsiop_map[0x19] = 'SCSIOP_ERASE'
srb_scsiop_map[0x1A] = 'SCSIOP_MODE_SENSE'
srb_scsiop_map[0x1B] = 'SCSIOP_START_STOP_UNIT'
srb_scsiop_map[0x1B] = 'SCSIOP_STOP_PRINT'
srb_scsiop_map[0x1B] = 'SCSIOP_LOAD_UNLOAD'
srb_scsiop_map[0x1C] = 'SCSIOP_RECEIVE_DIAGNOSTIC'
srb_scsiop_map[0x1D] = 'SCSIOP_SEND_DIAGNOSTIC'
srb_scsiop_map[0x1E] = 'SCSIOP_MEDIUM_REMOVAL'

# 10-byte commands
srb_scsiop_map[0x23] = 'SCSIOP_READ_FORMATTED_CAPACITY'
srb_scsiop_map[0x25] = 'SCSIOP_READ_CAPACITY'
srb_scsiop_map[0x28] = 'SCSIOP_READ'
srb_scsiop_map[0x2A] = 'SCSIOP_WRITE'
srb_scsiop_map[0x2B] = 'SCSIOP_SEEK'
srb_scsiop_map[0x2B] = 'SCSIOP_LOCATE'
srb_scsiop_map[0x2B] = 'SCSIOP_POSITION_TO_ELEMENT'
srb_scsiop_map[0x2E] = 'SCSIOP_WRITE_VERIFY'
srb_scsiop_map[0x2F] = 'SCSIOP_VERIFY'
srb_scsiop_map[0x30] = 'SCSIOP_SEARCH_DATA_HIGH'
srb_scsiop_map[0x31] = 'SCSIOP_SEARCH_DATA_EQUAL'
srb_scsiop_map[0x32] = 'SCSIOP_SEARCH_DATA_LOW'
srb_scsiop_map[0x33] = 'SCSIOP_SET_LIMITS'
srb_scsiop_map[0x34] = 'SCSIOP_READ_POSITION'
srb_scsiop_map[0x35] = 'SCSIOP_SYNCHRONIZE_CACHE'
srb_scsiop_map[0x39] = 'SCSIOP_COMPARE'
srb_scsiop_map[0x3A] = 'SCSIOP_COPY_COMPARE'
srb_scsiop_map[0x3B] = 'SCSIOP_WRITE_DATA_BUFF'
srb_scsiop_map[0x3C] = 'SCSIOP_READ_DATA_BUFF'
srb_scsiop_map[0x3F] = 'SCSIOP_WRITE_LONG'
srb_scsiop_map[0x40] = 'SCSIOP_CHANGE_DEFINITION'
srb_scsiop_map[0x41] = 'SCSIOP_WRITE_SAME'
srb_scsiop_map[0x42] = 'SCSIOP_READ_SUB_CHANNEL'
srb_scsiop_map[0x42] = 'SCSIOP_UNMAP'
srb_scsiop_map[0x43] = 'SCSIOP_READ_TOC'
srb_scsiop_map[0x44] = 'SCSIOP_READ_HEADER'
srb_scsiop_map[0x44] = 'SCSIOP_REPORT_DENSITY_SUPPORT'
srb_scsiop_map[0x45] = 'SCSIOP_PLAY_AUDIO'
srb_scsiop_map[0x46] = 'SCSIOP_GET_CONFIGURATION'
srb_scsiop_map[0x47] = 'SCSIOP_PLAY_AUDIO_MSF'
srb_scsiop_map[0x48] = 'SCSIOP_PLAY_TRACK_INDEX'
srb_scsiop_map[0x48] = 'SCSIOP_SANITIZE'
srb_scsiop_map[0x49] = 'SCSIOP_PLAY_TRACK_RELATIVE'
srb_scsiop_map[0x4A] = 'SCSIOP_GET_EVENT_STATUS'
srb_scsiop_map[0x4B] = 'SCSIOP_PAUSE_RESUME'
srb_scsiop_map[0x4C] = 'SCSIOP_LOG_SELECT'
srb_scsiop_map[0x4D] = 'SCSIOP_LOG_SENSE'
srb_scsiop_map[0x4E] = 'SCSIOP_STOP_PLAY_SCAN'
srb_scsiop_map[0x50] = 'SCSIOP_XDWRITE'
srb_scsiop_map[0x51] = 'SCSIOP_XPWRITE'
srb_scsiop_map[0x51] = 'SCSIOP_READ_DISK_INFORMATION'
srb_scsiop_map[0x51] = 'SCSIOP_READ_DISC_INFORMATION'
srb_scsiop_map[0x52] = 'SCSIOP_READ_TRACK_INFORMATION'
srb_scsiop_map[0x53] = 'SCSIOP_XDWRITE_READ'
srb_scsiop_map[0x53] = 'SCSIOP_RESERVE_TRACK_RZONE'
srb_scsiop_map[0x54] = 'SCSIOP_SEND_OPC_INFORMATION'
srb_scsiop_map[0x55] = 'SCSIOP_MODE_SELECT10'
srb_scsiop_map[0x56] = 'SCSIOP_RESERVE_UNIT10'
srb_scsiop_map[0x56] = 'SCSIOP_RESERVE_ELEMENT'
srb_scsiop_map[0x57] = 'SCSIOP_RELEASE_UNIT10'
srb_scsiop_map[0x57] = 'SCSIOP_RELEASE_ELEMENT'
srb_scsiop_map[0x58] = 'SCSIOP_REPAIR_TRACK'
srb_scsiop_map[0x5A] = 'SCSIOP_MODE_SENSE10'
srb_scsiop_map[0x5B] = 'SCSIOP_CLOSE_TRACK_SESSION'
srb_scsiop_map[0x5C] = 'SCSIOP_READ_BUFFER_CAPACITY'
srb_scsiop_map[0x5D] = 'SCSIOP_SEND_CUE_SHEET'
srb_scsiop_map[0x5E] = 'SCSIOP_PERSISTENT_RESERVE_IN'
srb_scsiop_map[0x5F] = 'SCSIOP_PERSISTENT_RESERVE_OUT'

# 12-byte commands
srb_scsiop_map[0xA0] = 'SCSIOP_REPORT_LUNS'
srb_scsiop_map[0xA1] = 'SCSIOP_BLANK'
srb_scsiop_map[0xA1] = 'SCSIOP_ATA_PASSTHROUGH12'
srb_scsiop_map[0xA2] = 'SCSIOP_SEND_EVENT'
srb_scsiop_map[0xA2] = 'SCSIOP_SECURITY_PROTOCOL_IN'
srb_scsiop_map[0xA3] = 'SCSIOP_SEND_KEY'
srb_scsiop_map[0xA3] = 'SCSIOP_MAINTENANCE_IN'
srb_scsiop_map[0xA4] = 'SCSIOP_REPORT_KEY'
srb_scsiop_map[0xA4] = 'SCSIOP_MAINTENANCE_OUT'
srb_scsiop_map[0xA5] = 'SCSIOP_MOVE_MEDIUM'
srb_scsiop_map[0xA6] = 'SCSIOP_LOAD_UNLOAD_SLOT'
srb_scsiop_map[0xA6] = 'SCSIOP_EXCHANGE_MEDIUM'
srb_scsiop_map[0xA7] = 'SCSIOP_SET_READ_AHEAD'
srb_scsiop_map[0xA7] = 'SCSIOP_MOVE_MEDIUM_ATTACHED'
srb_scsiop_map[0xA8] = 'SCSIOP_READ12'
srb_scsiop_map[0xA8] = 'SCSIOP_GET_MESSAGE'
srb_scsiop_map[0xA9] = 'SCSIOP_SERVICE_ACTION_OUT12'
srb_scsiop_map[0xAA] = 'SCSIOP_WRITE12'
srb_scsiop_map[0xAB] = 'SCSIOP_SEND_MESSAGE'
srb_scsiop_map[0xAB] = 'SCSIOP_SERVICE_ACTION_IN12'
srb_scsiop_map[0xAC] = 'SCSIOP_GET_PERFORMANCE'
srb_scsiop_map[0xAD] = 'SCSIOP_READ_DVD_STRUCTURE'
srb_scsiop_map[0xAE] = 'SCSIOP_WRITE_VERIFY12'
srb_scsiop_map[0xAF] = 'SCSIOP_VERIFY12'
srb_scsiop_map[0xB0] = 'SCSIOP_SEARCH_DATA_HIGH12'
srb_scsiop_map[0xB1] = 'SCSIOP_SEARCH_DATA_EQUAL12'
srb_scsiop_map[0xB2] = 'SCSIOP_SEARCH_DATA_LOW12'
srb_scsiop_map[0xB3] = 'SCSIOP_SET_LIMITS12'
srb_scsiop_map[0xB4] = 'SCSIOP_READ_ELEMENT_STATUS_ATTACHED'
srb_scsiop_map[0xB5] = 'SCSIOP_REQUEST_VOL_ELEMENT'
srb_scsiop_map[0xB5] = 'SCSIOP_SECURITY_PROTOCOL_OUT'
srb_scsiop_map[0xB6] = 'SCSIOP_SEND_VOLUME_TAG'
srb_scsiop_map[0xB6] = 'SCSIOP_SET_STREAMING'
srb_scsiop_map[0xB7] = 'SCSIOP_READ_DEFECT_DATA'
srb_scsiop_map[0xB8] = 'SCSIOP_READ_ELEMENT_STATUS'
srb_scsiop_map[0xB9] = 'SCSIOP_READ_CD_MSF'
srb_scsiop_map[0xBA] = 'SCSIOP_SCAN_CD'
srb_scsiop_map[0xBA] = 'SCSIOP_REDUNDANCY_GROUP_IN'
srb_scsiop_map[0xBB] = 'SCSIOP_SET_CD_SPEED'
srb_scsiop_map[0xBB] = 'SCSIOP_REDUNDANCY_GROUP_OUT'
srb_scsiop_map[0xBC] = 'SCSIOP_PLAY_CD'
srb_scsiop_map[0xBC] = 'SCSIOP_SPARE_IN'
srb_scsiop_map[0xBD] = 'SCSIOP_MECHANISM_STATUS'
srb_scsiop_map[0xBD] = 'SCSIOP_SPARE_OUT'
srb_scsiop_map[0xBE] = 'SCSIOP_READ_CD'
srb_scsiop_map[0xBE] = 'SCSIOP_VOLUME_SET_IN'
srb_scsiop_map[0xBF] = 'SCSIOP_SEND_DVD_STRUCTURE'
srb_scsiop_map[0xBF] = 'SCSIOP_VOLUME_SET_OUT'
srb_scsiop_map[0xE7] = 'SCSIOP_INIT_ELEMENT_RANGE'

# 16-byte commands
srb_scsiop_map[0x80] = 'SCSIOP_XDWRITE_EXTENDED16'
srb_scsiop_map[0x80] = 'SCSIOP_WRITE_FILEMARKS16'
srb_scsiop_map[0x81] = 'SCSIOP_REBUILD16'
srb_scsiop_map[0x81] = 'SCSIOP_READ_REVERSE16'
srb_scsiop_map[0x82] = 'SCSIOP_REGENERATE16'
srb_scsiop_map[0x83] = 'SCSIOP_EXTENDED_COPY'
srb_scsiop_map[0x83] = 'SCSIOP_POPULATE_TOKEN'
srb_scsiop_map[0x83] = 'SCSIOP_WRITE_USING_TOKEN'
srb_scsiop_map[0x84] = 'SCSIOP_RECEIVE_COPY_RESULTS'
srb_scsiop_map[0x84] = 'SCSIOP_RECEIVE_ROD_TOKEN_INFORMATION'
srb_scsiop_map[0x85] = 'SCSIOP_ATA_PASSTHROUGH16'
srb_scsiop_map[0x86] = 'SCSIOP_ACCESS_CONTROL_IN'
srb_scsiop_map[0x87] = 'SCSIOP_ACCESS_CONTROL_OUT'
srb_scsiop_map[0x88] = 'SCSIOP_READ16'
srb_scsiop_map[0x8A] = 'SCSIOP_WRITE16'
srb_scsiop_map[0x8C] = 'SCSIOP_READ_ATTRIBUTES'
srb_scsiop_map[0x8D] = 'SCSIOP_WRITE_ATTRIBUTES'
srb_scsiop_map[0x8E] = 'SCSIOP_WRITE_VERIFY16'
srb_scsiop_map[0x8F] = 'SCSIOP_VERIFY16'
srb_scsiop_map[0x90] = 'SCSIOP_PREFETCH16'
srb_scsiop_map[0x91] = 'SCSIOP_SYNCHRONIZE_CACHE16'
srb_scsiop_map[0x91] = 'SCSIOP_SPACE16'
srb_scsiop_map[0x92] = 'SCSIOP_LOCK_UNLOCK_CACHE16'
srb_scsiop_map[0x92] = 'SCSIOP_LOCATE16'
srb_scsiop_map[0x93] = 'SCSIOP_WRITE_SAME16'
srb_scsiop_map[0x93] = 'SCSIOP_ERASE16'
srb_scsiop_map[0x9E] = 'SCSIOP_READ_CAPACITY16'
srb_scsiop_map[0x9E] = 'SCSIOP_GET_LBA_STATUS'
srb_scsiop_map[0x9E] = 'SCSIOP_SERVICE_ACTION_IN16'
srb_scsiop_map[0x9F] = 'SCSIOP_SERVICE_ACTION_OUT16'

# 32-byte commands
srb_scsiop_map[0x7F] = 'SCSIOP_OPERATION32'

unit_control_map = {}
unit_control_map[0] = 'ScsiQuerySupportedUnitControlTypes'
unit_control_map[1] = 'ScsiUnitUsage'
unit_control_map[2] = 'ScsiUnitStart'
unit_control_map[3] = 'ScsiUnitPower'
unit_control_map[4] = 'ScsiUnitPoFxPowerInfo'
unit_control_map[5] = 'ScsiUnitPoFxPowerRequired'
unit_control_map[6] = 'ScsiUnitPoFxPowerActive'
unit_control_map[7] = 'ScsiUnitPoFxPowerSetFState'
unit_control_map[8] = 'ScsiUnitPoFxPowerControl'
unit_control_map[9] = 'ScsiUnitRemove'
unit_control_map[10] = 'ScsiUnitSurpriseRemoval'
unit_control_map[11] = 'ScsiUnitControlMax'
unit_control_map[0xffffffff] = 'MakeUnitControlTypeSizeOfUlong'

adapter_control_map = {}
adapter_control_map[0] = 'ScsiQuerySupportedControlTypes'
adapter_control_map[1] = 'ScsiStopAdapter'
adapter_control_map[2] = 'ScsiRestartAdapter'
adapter_control_map[3] = 'ScsiSetBootConfig'
adapter_control_map[4] = 'ScsiSetRunningConfig'
adapter_control_map[5] = 'ScsiPowerSettingNotification'
adapter_control_map[6] = 'ScsiAdapterPower'
adapter_control_map[7] = 'ScsiAdapterPoFxPowerRequired'
adapter_control_map[8] = 'ScsiAdapterPoFxPowerActive'
adapter_control_map[9] = 'ScsiAdapterPoFxPowerSetFState'
adapter_control_map[10] = 'ScsiAdapterPoFxPowerControl'
adapter_control_map[11] = 'ScsiAdapterPrepareForBusReScan'
adapter_control_map[12] = 'ScsiAdapterSystemPowerHints'
adapter_control_map[13] = 'ScsiAdapterFilterResourceRequirements'
adapter_control_map[14] = 'ScsiAdapterPoFxMaxOperationalPower'
adapter_control_map[15] = 'ScsiAdapterPoFxSetPerfState'
adapter_control_map[16] = 'ScsiAdapterSurpriseRemoval'
adapter_control_map[17] = 'ScsiAdapterControlMax'
adapter_control_map[0xffffffff] = 'MakeAdapterControlTypeSizeOfUlong'

ahci_controller_version_map = {}
ahci_controller_version_map[0x0]='Unknown'
ahci_controller_version_map[0x2822]='DESKTOP_SATA'
ahci_controller_version_map[0x282A]='MOBILE_SATA'
ahci_controller_version_map[0x2826]='SERVER_SATA'

    # Ibex Peak (5 Series/3400 Series)
ahci_controller_version_map[0x3B22]='DESKTOP_IBX_AHCI'
ahci_controller_version_map[0x3B23]='DESKTOP_IBX_AHCI_4P'
ahci_controller_version_map[0x3B24]='DESKTOP_IBX_PREM_RAID'
ahci_controller_version_map[0x3B25]='DESKTOP_IBX_RAID'
ahci_controller_version_map[0x3B29]='MOBILE_IBX_AHCI_4P'
ahci_controller_version_map[0X3B2B]='MOBILE_IBX_PREM_RAID'
ahci_controller_version_map[0x3B2C]='MOBILE_IBX_RAID'
ahci_controller_version_map[0x3B2F]='MOBILE_IBX_AHCI'

    # Cougar Point (6 Series/C200 Series)
ahci_controller_version_map[0x1C02]='DESKTOP_CPT_AHCI'
ahci_controller_version_map[0x1C03]='MOBILE_CPT_AHCI'
ahci_controller_version_map[0x1C04]='DESKTOP_CPT_RAID'
ahci_controller_version_map[0x1C05]='MOBILE_CPT_RAID'
ahci_controller_version_map[0x1C06]='DESKTOP_CPT_PREM_RAID'
ahci_controller_version_map[0x1C07]='MOBILE_CPT_PREM_RAID'

    # Cougar Point Refresh (CPT-R) - not productized
ahci_controller_version_map[0x1C84]='DESKTOP_CPTR_RAID'
ahci_controller_version_map[0x1C85]='MOBILE_CPTR_RAID'
ahci_controller_version_map[0x1C86]='DESKTOP_CPTR_PREM_RAID'
ahci_controller_version_map[0x1C87]='MOBILE_CPTR_PREM_RAID'

    # Panther Point (7 Series/C216)
ahci_controller_version_map[0x1E02]='DESKTOP_PPT_AHCI'
ahci_controller_version_map[0x1E03]='MOBILE_PPT_AHCI'
ahci_controller_version_map[0x1E04]='DESKTOP_PPT_RAID'
ahci_controller_version_map[0x1E05]='MOBILE_PPT_RAID'
ahci_controller_version_map[0x1E06]='DESKTOP_PPT_PREM_RAID'
ahci_controller_version_map[0x1E07]='MOBILE_PPT_PREM_RAID'
ahci_controller_version_map[0x1E0E]='DESKTOP_PPT_Q75_RAID'

    # Patsburg HEDT (X79)
ahci_controller_version_map[0x1D02]='DESKTOP_PBG_AHCI'
ahci_controller_version_map[0x1D04]='DESKTOP_PBG_RAID'
ahci_controller_version_map[0x1D06]='DESKTOP_PBG_PREM_RAID'

    # Lynxpoint
ahci_controller_version_map[0x8C02]='DESKTOP_LPT_AHCI'
ahci_controller_version_map[0x8C03]='MOBILE_LPT_AHCI'
ahci_controller_version_map[0x8C04]='DESKTOP_LPT_RAID'
ahci_controller_version_map[0x8C05]='MOBILE_LPT_RAID'
ahci_controller_version_map[0x8C06]='DESKTOP_LPT_PREM_RAID'
ahci_controller_version_map[0x8C07]='MOBILE_LPT_PREM_RAID'
ahci_controller_version_map[0x8C0E]='DESKTOP_LPT_R1ONLY_RAID'
ahci_controller_version_map[0x8C0F]='MOBILE_LPT_R1ONLY_RAID'

    # Lynxpoint Refresh
ahci_controller_version_map[0x8C82]='DESKTOP_LPT_R_AHCI'
ahci_controller_version_map[0x8C83]='MOBILE_LPT_R_AHCI'
ahci_controller_version_map[0x8C84]='DESKTOP_LPT_R_RAID'
ahci_controller_version_map[0x8C85]='MOBILE_LPT_R_RAID'
ahci_controller_version_map[0x8C86]='DESKTOP_LPT_R_PREM_RAID'
ahci_controller_version_map[0x8C87]='MOBILE_LPT_R_PREM_RAID'
ahci_controller_version_map[0x8C8E]='DESKTOP_LPT_R_R1ONLY_RAID'
ahci_controller_version_map[0x8C8F]='MOBILE_LPT_R_R1ONLY_RAID'

    # Lynx Point Low Power
ahci_controller_version_map[0x9C03]='MOBILE_LPT_LP_AHCI'
ahci_controller_version_map[0x9C05]='MOBILE_LPT_LP_RAID'
ahci_controller_version_map[0x9C07]='MOBILE_LPT_LP_PREM_RAID'
ahci_controller_version_map[0x9C0F]='MOBILE_LPT_LP_R1_RAID'

    # Wellsburg HEDT (X99) RPIDs
ahci_controller_version_map[0x8D04]='DESKTOP_WBG_RAID'
ahci_controller_version_map[0x8D06]='DESKTOP_WBG_PREM_RAID'

    # Wildcat Point Low Power
ahci_controller_version_map[0x9C87]='MOBILE_WPT_LP_PREM_RAID'

    # Sunrise Point Low Power (SPT-LP) RPIDs
ahci_controller_version_map[0x9D03]='MOBILE_SPT_LP_AHCI'
ahci_controller_version_map[0x9D05]='MOBILE_SPT_LP_RAID'
ahci_controller_version_map[0x9D07]='MOBILE_SPT_LP_PREM_RAID'
ahci_controller_version_map[0x9D0F]='MOBILE_SPT_LP_R1_RAID'

    # Sunrise Point H (SPT-H) RPIDs
ahci_controller_version_map[0xA102]='DESKTOP_SPT_H_AHCI'
ahci_controller_version_map[0xA103]='MOBILE_SPT_H_AHCI'
ahci_controller_version_map[0xA105]='DESKTOP_SPT_H_RAID'
ahci_controller_version_map[0xA106]='DESKTOP_SPT_H_PREM_RAID2'
ahci_controller_version_map[0xA107]='DESKTOP_SPT_H_PREM_RAID'
ahci_controller_version_map[0xA10F]='DESKTOP_SPT_H_R1_RAID'

    # August Ridge
ahci_controller_version_map[0xF1A5]='AUG'


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
    
    
    

