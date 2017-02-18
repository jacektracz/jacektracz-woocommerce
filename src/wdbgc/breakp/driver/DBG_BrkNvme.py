import sys
import os
import logging
from pykd import *
from ... breakp.DBG_BreakpBase import *
from ... breakp.DBG_BreakpUtils import *
from ... appcore.memory.DBG_Utils import *

class DBG_BrkNvme(DBG_BreakpBase):
        def __init__(self,spar, pparent):                
                DBG_BreakpBase.__init__(self,spar)
                self.xx_dbg("DBG_BrkNvme::__init__::method_in::")
                self.xx_set_class_name ( "DBG_BrkNvme" )
                self.xx_set_full_class_name ( "Wcdl::DBG_BrkNvme" )
                self.m_breaks = []
                self.m_handle_io = 0
                self.m_handle_hiber = 0                
                self.xx_dbg("DBG_BrkNvme::__init__::method_out::")
                
        def get_dispatch(self,tt):
                if(tt == "nvme_entry"):
                        return self.get_methods_entry()
                
                if(tt == "nvme_io"):
                        return self.get_methods_io()
                                
                return None
                
        def get_methods_entry(self):
                self.xx_dbg("DBG_BrkNvme::get_methods::method_in::")
                pp=[
                    "NVMeAdapterControl"
                    ,"NVMeInitialize"                                        
                    ,"NVMeResetBus"                                                                
                    ,"NVMeInitialize"
                    ,"NVMeFindAdapter"
                    ]
                self.xx_dbg("DBG_BrkNvme::get_methods::method_out::")
                return pp
        
        def get_methods_io(self):
                self.xx_dbg("DBG_BrkNvme::get_methods_io::method_in::")
                pp=["NVMeBuildIo"
                    ,"NVMeStartIo"
                    ,"NVMeInterrupt"
                    ,"NVMeCrashHiberBuildIo"
                    ,"NVMeCrashHiberStartIo"
                    ,"NVMeCrashHiberInterrupt"
                    ]
                self.xx_dbg("DBG_BrkNvme::get_methods_io::method_out::")
                return pp
