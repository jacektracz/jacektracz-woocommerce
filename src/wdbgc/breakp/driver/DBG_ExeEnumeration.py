import sys
import os
import logging
from pykd import *
from ... breakp.DBG_BreakpBase import *
from ... breakp.DBG_BreakpUtils import *
from ... appcore.memory.DBG_Utils import *
#!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py breakp raidp enumeration_entry 3
class DBG_ExeEnumeration(DBG_BreakpBase):
        def __init__(self,spar,pparent):                
                DBG_BreakpBase.__init__(self,spar)
                self.xx_dbg("DBG_ExeEnumeration::__init__::method_in::")
                self.xx_set_class_name ( "DBG_ExeEnumeration" )
                self.xx_set_full_class_name ( "Wcdl::DBG_ExeEnumeration" )
                self.m_breaks = []
                self.m_handle_io = 0
                self.m_handle_hiber = 0                
                self.xx_dbg("DBG_ExeEnumeration::__init__::method_out::")
                
        def get_dispatch(self,tt):
                if(tt == "enumeration_entry"):
                        return self.get_methods_entry()
                
                return None
                
        
        def get_methods_entry(self):
                self.xx_dbg("DBG_ExeEnumeration::get_methods::method_in::")
                pp=[
                    "Raidport::transportEnumerationComplete"
                    ,"Raidport::startEnumeration"
                    ,"Transport::enumerate"
                    ,"TransportPath::issueReportLuns"
                    ,"TransportPath::targetIdentifyComplete"
                    ,"EndDeviceTarget::identify"
                    ,"EndDeviceTarget::issueInquiry"
                    ,"RaidIsm::enumComplete"
                    ,"ReadCfgMgr::readConfig"
                    ,"Raidport::handleReportLuns"
                    ,"TransportRequest::finalizeCompletion"                    
                    ,"Raidport::transportEnumerationComplete"
                    ,"Raidism::enumComplete"
                    ,"TransportPath::completionCallback"
                    ,"AhciController::completeIo"
                    ,"NvmePort::buildIo"
                    ,"AhciController::buildIo"
                    ,"AhciPort::buildIo"
                    ,"Raidport::deviceAdded"
                    ,"EndDeviceTarget::identify"
                    ,"RaidIsm::diskAdded"
                    ,"ReadCfgMgr::readConfig2"
                    ,"iaStorA!IoPathMgr::startIo+0xba"
                    ]
                self.xx_dbg("DBG_ExeEnumeration::get_methods::method_out::")
                return pp

