import sys
import os
import logging
from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_MemoryTools import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from DBG_EndDeviceConcrete import *
from .. fields.DBG_FieldsMapper import *

class DBG_EndDevice(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "EndDevice" )
                self.xx_set_full_class_name ( "iastora!EndDevice" )               
                self.mDeviceIdType = "";
                self.mSignature = 0
                self.m_fields = DBG_FieldsMapper("DBG_EndDevice"
                                         ,self)                                
                
                
                
        def prepare_object(self):
                self.xx_dbg("DBG_EndDevice::prepare_object::")
                try:
                        
                        if(self.xx_is_object()==1):
                                self.mDeviceIdType = DBG_MemoryTools().xx_get_hex(self,"mDeviceIdType")
                                self.mSignature = DBG_MemoryTools().xx_get_int(self,"mSignature")
                                self.m_fields.initialize_by_parent(self)
                        
                        #self.m_fields.add_fields_int_array(["mDeviceIdType","mSignature"])
                                
                except:
                        self.xx_dbg("EXCEPTION_IN_END_DEVICE::prepare_object::")
                        
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:                        
                        self.xx_dbg("DBG_EndDevice::print_object::")
                        self.prepare_object()
                        self.xx_print_ptr("")
                        if(self.xx_is_object()==1):
                                self.m_fields.add_str_raw("DeviceIdType:" + str(self.mDeviceIdType))
                                self.m_fields.add_str_raw("Signature:" + str(self.mSignature))
                                self.m_fields.add_str_raw("DEVICE_IS_USED")
                                self.m_fields.print_onject()
                        
                except:
                        self.xx_dbg("EXCEPTION_IN_END_DEVICE::print_object::")
                
        def print_object_raw(self):
                try:
                        self.xx_dbg("DBG_EndDevice::print_object_raw::in::")
                        self.prepare_object()
                        self.xx_print_start("")
                        self.xx_print_ptr("")
                        self.xx_print_end("")
                        self.xx_dbg("DBG_EndDevice::print_object_raw::out::")
                        #self.m_fields.xx_print_fields("")
                except:
                        self.xx_dbg("EXCEPTION_IN_END_DEVICE::print_object_raw::")
                
