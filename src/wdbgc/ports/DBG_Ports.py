import sys
import os
from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_MemoryTools import *
from .. ahci.DBG_PortStateMachineN import *
from .. devices.DBG_EndDevice import *
from .. devices.DBG_EndDeviceGeneric import *

from DBG_PortConfigurationInformation import *

        
class DBG_Ports(DBG_AdapterBase):

    def __init__(self,spar,pparent):                
        DBG_AdapterBase.__init__(self,spar)
        self.numPorts = 0
        self.m_Ports =[]
        self.m_parent = pparent
        
    def prepare_object(self):
        self.initialize_ports()
        
    def initialize_ports(self):
        
        self.numPorts = 6
        
        for i in range(self.numPorts):
            dd = DBG_Port("DBG_Ports")
            dd.xx_inc_tabs_ex( self.m_parent,2,"DBG_Ports")                        
            dd.xx_compute_arr_phy_by_parent(
                self.m_parent
                ,"mPort[" +str(i) + "]")
            dd.prepare_object()
            self.m_Ports.append(dd)

    def print_object(self):
        self.prepare_object()
        self.print_ports()
        
    def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
    def print_object_internal(self,sdbg=""):
            self.xx_dbg("DBG_Port::prepare_object")
            for dd_Port in self.m_Ports:
                dd_Port.print_object()
        
