import sys
import os
import logging
from .. DBG_AdapterBase import *

from .. devices.DBG_EndDevice import *
from .. devices.DBG_EndDeviceGeneric import *
from .. ports.DBG_PortConfigurationInformation import *
from .. ahci.DBG_PortStateMachineN import *        
from .. ahci.DBG_AhciPort import *
from .. fields.DBG_FieldsMapper import *
from .. appcore.config.DBG_PrintConfig import *                
class DBG_AhciPortsGeneric(DBG_AdapterBase):

    def __init__(self,spar,pparent):                
        DBG_AdapterBase.__init__(self,spar)
        self.xx_dbg("DBG_AhciPortsGeneric::__init__::in::")
        self.xx_set_class_name ( "AhciController" )
        self.xx_set_full_class_name ( "iastora!AhciController" )        
        self.numPorts = 0
        self.m_ports =[]
        self.m_parent = pparent
        self.m_fields = DBG_FieldsMapper("DBG_AhciPortsGeneric"
                                 ,self)
        
        self.m_fields_ports = DBG_FieldsMapper("DBG_AhciPortsGeneric"
                                 ,self)                
        
        self.xx_dbg("DBG_AhciPortsGeneric::__init__::out::")
        
    def prepare_object(self):
        self.xx_dbg("DBG_AhciPortsGeneric::prepare_object")
        self.m_fields.initialize_by_parent(self.m_parent)
        self.m_fields_ports.initialize_by_parent(self.m_parent)
        #self.m_fields.xx_inc_tabs_ex( self.m_parent,2)
        self.prepare_ports()
        self.xx_dbg("DBG_AhciPortsGeneric::prepare_object::out::")
        
    def prepare_ports(self):
        self.xx_dbg("DBG_AhciPortsGeneric::prepare_ports")
        self.numPorts = 6
        self.m_ports =[]
        for i in range(self.numPorts):
            self.create_port_item_cpp(i)
        self.xx_dbg("DBG_AhciPortsGeneric::prepare_ports::out::")

    def create_port_item(self,ii_port):
        try:
            self.xx_dbg("DBG_AhciPortsGeneric::create_port_item")            
            dd = DBG_AhciPort("Parent::DBG_AhciPortsGeneric")            
            dd.set_addr_arr(self.m_parent,"mPort[" +str(ii_port) + "]")
            dd.prepare_object()
            self.m_ports.append(dd)
            self.xx_dbg("DBG_AhciPortsGeneric::create_port_item::out::")            
        except:
            self.xx_exception("[create_port_item][exception]")
        
    def create_port_item_cpp(self,ii_port):
        try:
            self.xx_dbg("DBG_AhciPortsGeneric::create_port_item")
            
            dd = DBG_AhciPort("Parent::DBG_AhciPortsGeneric")
            dd.xx_inc_tabs_ex( self.m_parent,2,"DBG_AhciPortsGeneric")                        
            dd.xx_compute_cpp_phy_by_parent(
                self.m_parent
                ,"mPort[" +str(ii_port) + "]")
            dd.prepare_object()
            self.m_ports.append(dd)
            self.xx_dbg("DBG_AhciPortsGeneric::create_port_item::out::")            
        except:
            self.xx_exception("[create_port_item][exception]")

    def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
    def print_object_internal(self,sdbg=""):
            self.xx_dbg("DBG_AhciPortsGeneric::print_object")
            self.prepare_object()
            self.xx_print_ptr("")
            self.m_fields.xx_print_fields("") 
            self.print_ports()
            self.m_fields_ports.xx_print_fields("") 
            self.xx_dbg("DBG_AhciPortsGeneric::print_object::out")
        
    def print_ports(self):
        self.xx_dbg("DBG_AhciPortsGeneric::print_ports")
        ii = 0
        for dd_port in self.m_ports:
            self.print_port_item(dd_port,ii)
            ii = ii + 1
        self.xx_dbg("DBG_AhciPortsGeneric::print_ports::out")
        
    def print_port_item(self,dd_port,dd_ii):        
        self.xx_dbg("DBG_AhciPortsGeneric::print_port_item::in::")
        try:
            if(dd_port.xx_device_is_object() == 1):
                self.m_fields_ports.add_raw_str( "ahci_port_is_used:" + str(dd_ii),1)
                dd_port.print_object()
            else:
                self.xx_dbg("not used port" + str(dd_ii))                
                self.m_fields_ports.add_raw_str( "ahci_port_not_used:" + str(dd_ii),1)
                
                if(DBG_PrintConfig().getItem().m_print_all_ahci_ports == 1):
                    dd_port.print_object()
                    
            self.xx_dbg("DBG_AhciPortsGeneric::print_port_item::out::")
        except:
            self.xx_exception("[print_port_item][exception]")

        