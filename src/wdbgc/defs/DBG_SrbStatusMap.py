import sys
import os
from .. DBG_AdapterBase import *
        
        
class DBG_SrbStatusMap(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_SrbFunctions::__init__::in::")
                self.xx_set_class_name ( "DBG_SrbFunctions" )
                self.xx_set_full_class_name ( "iastora!Wcdl::Chipset" )
                self.xx_dbg("DBG_Chipset::__init__::out")
                self.srb_status_map = {}
                
        def create_map(self):            
            self.srb_status_map[0x00] = 'SRB_STATUS_PENDING'
            self.srb_status_map[0x01] = 'SRB_STATUS_SUCCESS'
            self.srb_status_map[0x02] = 'SRB_STATUS_ABORTED'
            self.srb_status_map[0x03] = 'SRB_STATUS_ABORT_FAILED'
            self.srb_status_map[0x04] = 'SRB_STATUS_ERROR'
            self.srb_status_map[0x05] = 'SRB_STATUS_BUSY'
            self.srb_status_map[0x06] = 'SRB_STATUS_INVALID_REQUEST'
            self.srb_status_map[0x07] = 'SRB_STATUS_INVALID_PATH_ID'
            self.srb_status_map[0x08] = 'SRB_STATUS_NO_DEVICE'
            self.srb_status_map[0x09] = 'SRB_STATUS_TIMEOUT'
            self.srb_status_map[0x0A] = 'SRB_STATUS_SELECTION_TIMEOUT'
            self.srb_status_map[0x0B] = 'SRB_STATUS_COMMAND_TIMEOUT'
            self.srb_status_map[0x0D] = 'SRB_STATUS_MESSAGE_REJECTED'
            self.srb_status_map[0x0E] = 'SRB_STATUS_BUS_RESET'
            self.srb_status_map[0x0F] = 'SRB_STATUS_PARITY_ERROR'
            self.srb_status_map[0x10] = 'SRB_STATUS_REQUEST_SENSE_FAILED'
            self.srb_status_map[0x11] = 'SRB_STATUS_NO_HBA'
            self.srb_status_map[0x12] = 'SRB_STATUS_DATA_OVERRUN'
            self.srb_status_map[0x13] = 'SRB_STATUS_UNEXPECTED_BUS_FREE'
            self.srb_status_map[0x14] = 'SRB_STATUS_PHASE_SEQUENCE_FAILURE'
            self.srb_status_map[0x15] = 'SRB_STATUS_BAD_SRB_BLOCK_LENGTH'
            self.srb_status_map[0x16] = 'SRB_STATUS_REQUEST_FLUSHED'
            self.srb_status_map[0x20] = 'SRB_STATUS_INVALID_LUN'
            self.srb_status_map[0x21] = 'SRB_STATUS_INVALID_TARGET_ID'
            self.srb_status_map[0x22] = 'SRB_STATUS_BAD_FUNCTION'
            self.srb_status_map[0x23] = 'SRB_STATUS_ERROR_RECOVERY'
            self.srb_status_map[0x24] = 'SRB_STATUS_NOT_POWERED'
            self.srb_status_map[0x25] = 'SRB_STATUS_LINK_DOWN'
            self.srb_status_map[0x30] = 'SRB_STATUS_INTERNAL_ERROR'
