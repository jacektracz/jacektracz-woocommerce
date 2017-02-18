import sys
import os
import logging
from pykd import *
from ... breakp.DBG_BreakpBase import *
from ... breakp.DBG_BreakpUtils import *
from ... appcore.memory.DBG_Utils import *

class DBG_BrkRemapPort(DBG_BreakpBase):
        def __init__(self,spar,pparent):                
                DBG_BreakpBase.__init__(self,spar)
                self.xx_dbg("DBG_BreakpRaidport::__init__::method_in::")
                self.xx_set_class_name ( "DBG_BreakpRaidport" )
                self.xx_set_full_class_name ( "Wcdl::DBG_BreakpRaidport" )
                self.m_breaks = []
                self.m_handle_io = 0
                self.m_handle_hiber = 0                
                self.xx_dbg("DBG_BreakpRaidport::__init__::method_out::")
                
        def get_dispatch(self,tt):
                if(tt == "remap_ini_path"):
                        return self.get_methods_ini_path()
                if(tt == "remap_entry"):
                        return self.get_methods_entry()
                if(tt == "remap_io"):
                        return self.get_methods_io()
                
                return None
                
        
        def get_methods_entry(self):
                self.xx_dbg("DBG_BrkAhci::get_methods::method_in::")
                pp=[
                    "RemapPortAdapterControl"
                    ,"RemapPortInitialize"                                        
                    ,"RemapPortResetBus"                    
                    ,"RemapPortAdapterControl"                                                         
                    ,"RemapPortInitialize"
                    ,"RemapPortFindAdapter"
                    ]
                self.xx_dbg("DBG_BrkAhci::get_methods::method_out::")
                return pp

        def get_methods_io(self):
                self.xx_dbg("DBG_BrkAhci::get_methods_io::method_in::")
                pp=["RemapPortBuildIo"
                    ,"RemapPortStartIo"
                    ,"RemapPortInterrupt"
                    ,"RemapPortCrashHiberBuildIo"
                    ,"RemapPortCrashHiberStartIo"
                    ,"RemapPortCrashHiberInterrupt"
                    ]
                self.xx_dbg("DBG_BrkAhci::get_methods_io::method_out::")
                return pp

        def get_methods_ini_path(self):
                self.xx_dbg("DBG_BreakpRaidport::set_breakpoints_storport_full::method_in::")                
                pp = [
                        "RemapPortInterrupt"
                        ,"RemapPort::findRemappedAdapters"
                        ,"RemapPort::enableRemappedInterrupts"
                        ,"RaidportInitialize"]
                return pp
