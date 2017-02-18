import sys
import os
import logging
from pykd import *
from ... breakp.DBG_BreakpBase import *
from ... breakp.DBG_BreakpUtils import *
from ... appcore.memory.DBG_Utils import *

class DBG_BrkEnumHiber(DBG_BreakpBase):
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
                if(tt == "raidport_entry"):
                        return self.get_methods_entry()
                
                if(tt == "raidport_io"):
                        return self.get_methods_io()
                
                if(tt == "raidport_ini_path"):
                        return self.get_methods_ini_path()
                
                return None
                
        def get_methods_entry(self):
                self.xx_dbg("DBG_BreakpRaidport::get_methods::method_in::")
                pp=[
                    "RaidportAdapterControl"                                                
                    ,"RaidportResetBus"                    
                    ,"RaidportAdapterControl"                                                         
                    ,"RaidportInitialize"
                    ,"RaidportFindAdapter"
                    ]
                self.xx_dbg("DBG_BreakpRaidport::get_methods::method_out::")
                return pp
        
        def get_methods_io(self):
                self.xx_dbg("DBG_BreakpRaidport::get_methods_io::method_in::")
                pp=["RaidportBuildIo"
                    ,"RaidportStartIo"
                    ,"RaidportInterrupt"                    
                    ,"RaidportCrashHiberBuildIo"
                    ,"RaidportCrashHiberStartIo"
                    ,"RaidIsm::enumComplete"
                    ]
                self.xx_dbg("DBG_BreakpRaidport::get_methods_io::method_out::")
                return pp


        def get_methods_ini_path(self):
                self.xx_dbg("DBG_BreakpRaidport::get_methods_initialize::method_in::")
                #self.add_bug("storport!RaDriverPowerIrp")                
                pp = [
                        "Transport_CrashdumpDispatchDpcRoutine"
                        ,"Transport_DispatchDpcRoutine"
                        ,"Raidport::suspendSubstateTransitionComplete"                                                
                        ,"Raidport_IsmSuspendCallback"                
                        #,"Controller::shutdown"
                        #,"Wcdl::Timer::stop"
                        #,"Raidport::stopIsmTimer"
                        ,"Raidport_IsmSuspendCallback"
                        #,"Raidport_IsmSuspendCallbackEx"
                        ,"Raidport_IsmShutdownCallback"
                        ,"Raidport_IsmRemoveCallback"
                        ,"Raidport::suspendIsm"
                        ,"Raidport::~Raidport"
                        ,"RaidIsm::suspend"
                        #,"NvmePort::startIoPower"
                        ,"AhciHwStorAdapterControl"
                        ,"RaidportUnitControl"                        
                        #,"MiniportParameters::getSetDefaultRegDword"
                        #,"AhciPort::startIo"
                        #,"AhciController::portStopped"
                        ,"RemapPort::findRemappedAdapters"
                        ,"RemapPort::enableRemappedInterrupts"
                        ,"RaidportInitialize"
                      ]                        
                self.xx_dbg("DBG_BreakpRaidport::get_methods_initialize::method_out::")
                