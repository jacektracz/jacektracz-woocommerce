import sys
import os
from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_MemoryTools import *
from .. ahci.DBG_PortStateMachineN import *
from .. devices.DBG_EndDevice import *
from .. devices.DBG_EndDeviceGeneric import *

from DBG_PortConfigurationInformation import *

class DBG_Port(DBG_AdapterBase):
    
    def __init__(self,spar):
        DBG_AdapterBase.__init__(self,spar)    
        self.xx_set_class_name( "Port" )
        self.xx_set_full_class_name ( "iastora!Port" )
        self.m_psm = DBG_PortStateMachineN("Parent::DBG_Port")
        self.m_enddevice = DBG_EndDevice("Parent::DBG_Port")
        self.m_enddeviceg = DBG_EndDeviceGeneric("Parent::DBG_Port",self)
        self.m_enddeviceg.set_parent(self)
        
    def prepare_object(self):
        self.xx_dbg("DBG_Port::prepare_object")
        
        self.m_psm.xx_inc_tabs_ex(self,1,"DBG_Port")
        self.m_psm.xx_compute_phy_by_parent(self,"mPortStateMachine")
        
        self.m_enddevice.xx_inc_tabs_ex(self,1,"DBG_Port")
        self.m_enddevice.xx_compute_phy_by_parent(self,"mDevice")
        self.m_enddeviceg.set_addr(self,"mDevice")
        
    def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
    def print_object_internal(self,sdbg=""):
            self.prepare_object()
            self.xx_print_ptr("")
            self.m_psm.print_object()
            self.m_enddevice.print_object()
        
