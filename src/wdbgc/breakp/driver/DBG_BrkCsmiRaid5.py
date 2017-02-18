import sys
import os
import logging
from pykd import *
from ... breakp.DBG_BreakpBase import *
from ... breakp.DBG_BreakpUtils import *
from ... appcore.memory.DBG_Utils import *

class DBG_BrkCsmiRaid5(DBG_BreakpBase):
        def __init__(self,spar, pparent):                
                DBG_BreakpBase.__init__(self,spar)
                self.xx_dbg("DBG_BrkCsmiRaid5::__init__::method_in::")
                self.xx_set_class_name ( "DBG_BrkCsmiRaid5" )
                self.xx_set_full_class_name ( "Wcdl::DBG_BrkCsmiRaid5" )
                self.m_breaks = []
                self.m_handle_io = 0
                self.m_handle_hiber = 0                
                self.xx_dbg("DBG_BrkCsmiRaid5::__init__::method_out::")
                
        def get_dispatch(self,tt):
                if(tt == "CsmiRaid5"):
                        return self.get_methods_entry()
                if(tt == "CsmiRaid5_path_1"):
                        return self.get_methods_path_1()
                
                return None
                
        def get_methods_entry(self):
                self.xx_dbg("DBG_BrkCsmiRaid5::get_methods_entry::method_in::")
                pp=[
                        "raidIsmGetSetParms"
                        ,"RaidIsm::getSetParms"
                        ,"GetRaidConfigCsmiIoctlRequest::build"
                        ,"GetRaidConfigCsmiIoctlRequest::vtableComplete"
                        ,"GetRaidConfigCsmiIoctlRequest::dtableComplete"                
                        ,"CsmiIoctlRequest::construct"
                        ,"RaidIsm::getVolume"
                    ]
                self.xx_dbg("DBG_BrkCsmiRaid5::get_methods::method_out::")
                return pp
        
        def get_methods_path_1(self):
                self.xx_dbg("DBG_BrkCsmiRaid5::get_methods_entry::method_in::")
                pp=[
                    #"SecPortBuildIo+0x1d"
                    #,"secport::SecPort::buildIo+0xc6"
                    "RaidportBuildIo+0x84"
                    ,"IoctlRequest::construct+0x8b"
                    ,"CsmiIoctlRequest::construct"
                    ]
                self.xx_dbg("DBG_BrkCsmiRaid5::get_methods::method_out::")
                return pp
        
        #RaidDev::getCngStates
        
        def get_info(self):
                ii = []
                ii.Append("!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py breakp raidp CsmiRaid5")
                ii.Append("!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py breakp raidp CsmiRaid5 3")
                return ii