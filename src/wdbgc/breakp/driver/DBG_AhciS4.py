import sys
import os
import logging
from pykd import *
from ... breakp.DBG_BreakpBase import *
from ... breakp.DBG_BreakpUtils import *
from ... appcore.memory.DBG_Utils import *

class DBG_AhciS4(DBG_BreakpBase):
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
                if(tt == "ahcis4"):
                        return self.get_methods()
                return None
                
        def get_methods(self):
                self.xx_dbg("DBG_BreakpRaidport::get_methods::method_in::")
                pp = [
                        "ScsiPortInitialize"
                        ,"PopInvokeStateHandlerTargetProcessor"                        
                ]
                
                pp = [
                        "Raidport::completeRaidEnumeration"
                        ,"RaidIsm_FreeIo"
                        ,"TransportRequest::~TransportRequest"
                        ,"TransportDeviceResetRequest"
                        ,"TransportTarget::complete"
                        ,"RpiNotification"
                        ,"AhciController::completeIo"
                        ,"AhciPort::releaseSlot"
                        ,"AhciPort::completeRequests"
                        ,"AhciPort::interruptDpc"
                        ,"AhciHwStorDpcRoutine"
                        ,"AhciHwStorMSInterrupt"
                        ,"AhciHwStorInterrupt"
                        ,"RemapPort::interrupt"
                        ,"RemapPortInterrupt"
                        ,"Transport::interrupt"
                        ,"TransportTarget::dispatchIo"
                        ,"Transport::dispatchIo"
                        ,"Transport_CrashdumpDispatchDpcRoutine"
                        ,"DeferredProcedureCall::execute"
                        ,"CrashdumpHibernateThreadingModel::executePendingDpcs"
                        ,"Library::executePendingDpcs"
                        ,"RaidportPassiveInitialization"
                        ,"Raidport::enablePassiveInitialization"
                        ,"Raidport::initialize"
                        ,"RaidportInitialize"
                        ,"RaidportCrashHiberStartIo"
                
                ]
                self.xx_dbg("DBG_BreakpRaidport::get_methods::method_out::")
                return pp
        
