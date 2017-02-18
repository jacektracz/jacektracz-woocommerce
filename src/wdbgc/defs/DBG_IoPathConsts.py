import sys
import os
from .. DBG_AdapterBase import *
        
        
class DBG_IoPathConsts(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_SrbFunctions::__init__::in::")
                self.xx_set_class_name ( "DBG_SrbFunctions" )
                self.xx_set_full_class_name ( "iastora!Wcdl::Chipset" )
                self.xx_dbg("DBG_Chipset::__init__::out")
                self.ahci_controller_version_map = {}
                self.IO_PATH_UNINITIALIZED  = 0
                self.IO_PATH_HAS_COALESCER = 1
                self.IO_PATH_HAS_VOL_CACHE = 2
                self.IO_PATH_HAS_NV_CACHE  = 4
                self.IO_PATH_HAS_RAIDDEV   = 8
                
        def create_map(self):            
            ""
