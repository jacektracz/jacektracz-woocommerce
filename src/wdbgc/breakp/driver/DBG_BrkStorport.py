import sys
import os
import logging
from pykd import *
from ... breakp.DBG_BreakpBase import *
from ... breakp.DBG_BreakpUtils import *
from ... appcore.memory.DBG_Utils import *

class DBG_BrkStorport(DBG_BreakpBase):
        def __init__(self,spar, pparent):                
                DBG_BreakpBase.__init__(self,spar)
                self.xx_dbg("DBG_BreakpRaidport::__init__::method_in::")
                self.xx_set_class_name ( "DBG_BreakpRaidport" )
                self.xx_set_full_class_name ( "Wcdl::DBG_BreakpRaidport" )
                self.m_breaks = []
                self.m_handle_io = 0
                self.m_handle_hiber = 0                
                self.xx_dbg("DBG_BreakpRaidport::__init__::method_out::")
                
        def get_dispatch(self,tt):
                if(tt == "storport"):
                        return self.get_methods()
                
                if(tt == "storportexe"):
                        self.set_execution()                
                return None
                
        def get_methods(self):
                self.xx_dbg("DBG_BreakpRaidport::set_breakpoints_storport_full::method_in::")                
                pp = ["StorPortCompleteServiceIrp"
                      ,"StorPortGetSystemAddress"
                      ,"StorPortInitialize"
                      ,"StorPortGetDeviceBase"
                      ,"StorPortGetLogicalUnit"
                      ,"StorPortGetScatterGatherList"
                      ,"StorPortGetPhysicalAddress"
                      ,"StorPortGetVirtualAddress"
                      ,"StorPortPauseDevice"
                      ,"StorPortResumeDevice"
                      ,"StorPortPause"
                      ,"StorPortResume"
                      ,"StorPortDeviceBusy"
                      ,"StorPortDeviceReady"
                      ,"StorPortBusy"
                      ,"StorPortReady"
                      ,"StorPortNotification"
                      ,"StorPortCompleteRequest"
                      ,"StorPortStallExecution"
                      ,"StorPortSynchronizeAccess"
                      ,"StorPortReadPortUchar"
                      ,"StorPortReadPortUshort"
                      ,"StorPortReadPortUlong"
                      ,"StorPortReadRegisterUchar"
                      ,"StorPortReadRegisterUshort"
                      ,"StorPortReadRegisterUlong"
                      ,"StorPortWritePortUshort"
                      ,"StorPortWritePortUlong"
                      ,"StorPortWriteRegisterUchar"
                      ,"StorPortWriteRegisterUshort"
                      ,"StorPortWriteRegisterUlong"
                      ,"StorPortInitializeDpc"
                      ]
                return pp
        
        def set_execution(self):
                self.xx_dbg("DBG_BreakpRaidport::set_breakpoints_storport::method_in::")
                
                pp = ["storport!RaidAdapterPowerDownDevice"]
                self.xx_set_bpreakpoint_arr_raw(pp)
                
                pp = ["ed kd_default_mask f"
                      ,"ed kd_storminiport_mask f"]
                self.xx_set_commands_arr_raw(pp)
                
                pp = ["StorPortCompleteServiceIrp"
                      ,"StorPortGetSystemAddress"]
                
                self.xx_set_bpreakpoint_arr( pp )
                self.xx_dbg("DBG_BreakpRaidport::set_breakpoints_storport::method_in::")
        
                