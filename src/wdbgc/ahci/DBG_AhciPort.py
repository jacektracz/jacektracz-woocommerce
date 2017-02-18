import sys
import os
import logging
from .. DBG_AdapterBase import *


from .. devices.DBG_EndDevice import *
from .. devices.DBG_EndDeviceGeneric import *

from .. ports.DBG_PortConfigurationInformation import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. ahci.DBG_PortStateMachineN import *        
from .. fields.DBG_FieldsMapper import *
from .. appsrc.ahciintl.DBG_AHCI_PORT import *

class DBG_AhciPort(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_AhciPort::__init__::in::")
                self.xx_set_class_name ( "AhciPort" )
                self.xx_set_full_class_name ( "iastora!AhciPort" )
                #self.m_ports = DBG_Ports("PARENT::DBG_AhciPort",self)
                self.m_psm = DBG_PortStateMachineN("Parent::DBG_AhciPort")
                self.m_enddevice = DBG_EndDevice("Parent::DBG_AhciPort")
                self.m_enddeviceg = DBG_EndDeviceGeneric("Parent::DBG_AhciPort",self)
                self.m_enddeviceg.set_parent(self)
                self.m_fields = DBG_FieldsMapper("DBG_AhciPort"
                                         ,self)                
                self.m_fields.add_fields_int_array(["ChannelNumber"
                                                    ,"aoacSpinupDrive"
                                                    ,"mSerialAbortedCommandCount"
                                                    ,"aoacState"
                                                    ,"aoacTime"
                                                    ,"aoacFlag"
                                                    ,"aoacSpinupDrive"
                                                    ,"mTaskFileIndx"
                                                    ,"mPortStateFlags"
                                                    ,"mPortSupportsZpodd"
                                                    ,"mZpoddAcpiCapable"
                                                    ,"mAsrCount"
                                                    ,"mPortPowerState"])
                
                self.m_Px = DBG_AHCI_PORT("PArent::DBG_AhciPort")
                
                self.xx_dbg("DBG_AhciPort::__init__::out")
                
        def prepare_object(self):
                try:
                        
                        self.xx_dbg("DBG_AhciPort::prepare_object")        
                        if(self.xx_is_object() == 0):
                                self.m_fields.set_fields_parent(self)
                                self.xx_dbg("DBG_AhciPort::ahci_port_not_used")                
                                #self.print_object_not_used("ahci port in prepare")                                
                        else:
                                #self.print_object_is_used("ahci port in prepare")
                                self.m_fields.set_fields_parent(self)                                                                                        
                                self.m_psm.set_addr(self,"mStateMachine")                                                        
                                self.m_enddevice.set_addr(self,"mDevice")                                
                                self.m_enddeviceg.set_addr(self,"mDevice")
                                self.m_Px.set_addr(self,"Px")
                                self.m_Px.prepare_object()
                                
                        self.xx_dbg("DBG_AhciPort::prepare_object::out")
                except:
                        self.xx_exception("DBG_AhciPort::prepare_object")
            
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_AhciPort::print_object")        
                        self.prepare_object()
                        self.xx_print_ptr("")
                        if(self.xx_is_object() == 1 ):                                
                                self.m_fields.xx_print_fields("")
                                
                                if(self.m_enddevice.xx_is_object()==1):
                                        self.m_enddevice.print_object()
                                else:
                                        self.m_enddevice.print_object_raw()                                
                                
                                if(self.m_enddeviceg.xx_is_object()==1):
                                        self.m_enddeviceg.print_object()
                                else:
                                        self.xx_dbg("end_device_generic_u_not_used")
                                
                                if(self.m_psm.xx_is_object() == 1):
                                        self.m_psm.print_object()
                                else:
                                        self.xx_dbg("psm_u_not_used")
                                        
                                self.m_Px.print_object()
                                
                        self.xx_dbg("DBG_AhciPort::print_object::out")
                except:
                        self.xx_exception("DBG_AhciPort::print_object")

        def print_object_raw(self):
                try:
                        self.xx_dbg("DBG_AhciPort::print_object_raw")        
                        self.prepare_object()
                        self.xx_print_ptr("")
                                                
                        self.xx_dbg("DBG_AhciPort::print_object::out")
                except:
                        self.xx_exception("DBG_AhciPort::print_object")

        def print_object_no_print(self):
                try:
                        self.xx_dbg("DBG_AhciPort::print_object_raw")        
                        #self.prepare_object()
                        #self.xx_print_ptr("")
                                                
                        self.xx_dbg("DBG_AhciPort::print_object::out")
                except:
                        self.xx_exception("DBG_AhciPort::print_object")

        def xx_device_is_object(self):
                self.xx_dbg("DBG_AhciPort::xx_device_is_object::in::")
                is_obj = 1
                if(is_obj == 1):                                                
                        if(self.xx_is_object() == 0):
                                is_obj = 0
                if(is_obj == 1):                                                
                        if(self.xx_check_int(self,"ChannelNumber") < 0):
                                is_obj = 0
                if(is_obj == 1):                                                                                
                        if(self.m_enddevice.xx_is_object() == 0 ):
                                is_obj = 0
                self.xx_dbg("DBG_AhciPort::xx_device_is_object::out::")        
                return is_obj
                        