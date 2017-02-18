import sys
import os
import logging
from pykd import *
from ... breakp.DBG_BreakpBase import *
from ... breakp.DBG_BreakpUtils import *
from ... appcore.memory.DBG_Utils import *

class DBG_BrkScsi(DBG_BreakpBase):
        def __init__(self,spar, pparent):                
                DBG_BreakpBase.__init__(self,spar)
                self.xx_dbg("DBG_BrkAhci::__init__::method_in::")
                self.xx_set_class_name ( "DBG_BrkAhci" )
                self.xx_set_full_class_name ( "Wcdl::DBG_BrkAhci" )
                self.m_breaks = []
                self.m_handle_io = 0
                self.m_handle_hiber = 0                
                self.xx_dbg("DBG_BrkAhci::__init__::method_out::")
                
        def get_dispatch(self,tt):
                if(tt == "scsi"):
                        return self.get_methods_entry()
                                
                return None
                
        def get_methods_entry(self):
                self.xx_dbg("DBG_BrkAhci::get_methods_entry::method_in::")
                pp=[
                    "ScsiDiskIoctlRequest::construct"
                    ,"AhciPort::initializeScsiUnitPoFxPowerInfo"
                    ,"Raidport::unitControl"
                    ,"AhciHwStorStartIo"
                    ,"AHCI_PublicIoControl"
                    ]
                self.xx_dbg("DBG_BrkAhci::get_methods::method_out::")
                return pp
        
