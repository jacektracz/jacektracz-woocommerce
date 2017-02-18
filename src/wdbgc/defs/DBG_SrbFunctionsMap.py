import sys
import os
from .. DBG_AdapterBase import *
        
        
class DBG_SrbFunctionsMap(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_SrbFunctions::__init__::in::")
                self.xx_set_class_name ( "DBG_SrbFunctions" )
                self.xx_set_full_class_name ( "iastora!Wcdl::Chipset" )
                self.xx_dbg("DBG_Chipset::__init__::out")
                self.srb_functions_map = {}
                
        def create_map(self):
            self.srb_functions_map[0x0] = 'SRB_FUNCTION_EXECUTE_SCSI'
            self.srb_functions_map[0x01] = 'SRB_FUNCTION_CLAIM_DEVICE'
            self.srb_functions_map[0x02] = 'SRB_FUNCTION_IO_CONTROL'
            self.srb_functions_map[0x03] = 'SRB_FUNCTION_RECEIVE_EVENT'
            self.srb_functions_map[0x04] = 'SRB_FUNCTION_RELEASE_QUEUE'
            self.srb_functions_map[0x05] = 'SRB_FUNCTION_ATTACH_DEVICE'
            self.srb_functions_map[0x06] = 'SRB_FUNCTION_RELEASE_DEVICE'
            self.srb_functions_map[0x07] = 'SRB_FUNCTION_SHUTDOWN'
            self.srb_functions_map[0x08] = 'SRB_FUNCTION_FLUSH'
            self.srb_functions_map[0x10] = 'SRB_FUNCTION_ABORT_COMMAND'
            self.srb_functions_map[0x11] = 'SRB_FUNCTION_RELEASE_RECOVERY'
            self.srb_functions_map[0x12] = 'SRB_FUNCTION_RESET_BUS'
            self.srb_functions_map[0x13] = 'SRB_FUNCTION_RESET_DEVICE'
            self.srb_functions_map[0x14] = 'SRB_FUNCTION_TERMINATE_IO'
            self.srb_functions_map[0x15] = 'SRB_FUNCTION_FLUSH_QUEUE'
            self.srb_functions_map[0x16] = 'SRB_FUNCTION_REMOVE_DEVICE'
            self.srb_functions_map[0x17] = 'SRB_FUNCTION_WMI'
            self.srb_functions_map[0x18] = 'SRB_FUNCTION_LOCK_QUEUE'
            self.srb_functions_map[0x19] = 'SRB_FUNCTION_UNLOCK_QUEUE'
            self.srb_functions_map[0x1a] = 'SRB_FUNCTION_QUIESCE_DEVICE'
            self.srb_functions_map[0x20] = 'SRB_FUNCTION_RESET_LOGICAL_UNIT'
            self.srb_functions_map[0x21] = 'SRB_FUNCTION_SET_LINK_TIMEOUT'
            self.srb_functions_map[0x22] = 'SRB_FUNCTION_LINK_TIMEOUT_OCCURRED'
            self.srb_functions_map[0x23] = 'SRB_FUNCTION_LINK_TIMEOUT_COMPLETE'
            self.srb_functions_map[0x24] = 'SRB_FUNCTION_POWER'
            self.srb_functions_map[0x25] = 'SRB_FUNCTION_PNP'
            self.srb_functions_map[0x26] = 'SRB_FUNCTION_DUMP_POINTERS'
            self.srb_functions_map[0x27] = 'SRB_FUNCTION_FREE_DUMP_POINTERS'
            self.srb_functions_map[0x28] = 'SRB_FUNCTION_STORAGE_REQUEST_BLOCK'
