import sys
import os
import logging
from pykd import *
from ... breakp.DBG_BreakpBase import *
from ... breakp.DBG_BreakpUtils import *
from ... appcore.memory.DBG_Utils import *

class DBG_ThreadsError(DBG_BreakpBase):
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
                if(tt == "threads"):
                        return self.get_methods()
                return None
                
        def get_methods(self):
                self.xx_dbg("DBG_BreakpRaidport::get_methods::method_in::")
                pp = ["storport!RaDriverPowerIrp"
                        ,"Transport_CrashdumpDispatchDpcRoutine"
                        ,"Transport_DispatchDpcRoutine"
                        ,"Raidport::suspendSubstateTransitionComplete"
                        #,"Raidport_IsmSuspendCallback+0x2e"
                        ,"RaidIsm::suspend"
                        ,"AhciHwStorAdapterControl"
                        ,"Raidport_IsmSuspendCallback"                
                        ,"Controller::shutdown"
                        ,"Wcdl::Timer::stop"
                        ,"Raidport::stopIsmTimer"
                        ,"Raidport_IsmSuspendCallback"
                        ,"Raidport_IsmSuspendCallbackEx"
                        ,"Raidport_IsmShutdownCallback"
                        ,"Raidport_IsmRemoveCallback"
                        ,"Raidport::suspendIsm"
                        ,"Raidport::~Raidport"
                        ,"RaidIsm::suspend"
                        ,"NvmePort::startIoPower"
                        ,"AhciHwStorAdapterControl"
                        ,"RaidportUnitControl"
                        ,"NvmePort::stop"
                        ,"NvmePort::shutdown"
                        ,"NVMeUnitControl"
                        ,"NvmePort::unitControl"
                        ,"RemapPort::adapterControl"]
                self.xx_dbg("DBG_BreakpRaidport::get_methods::method_out::")
                return pp
