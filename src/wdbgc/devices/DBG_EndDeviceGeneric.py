import sys
import os
import logging
from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_MemoryTools import *
from .. devices.DBG_EndDevice import *
from .. devices.DBG_AtaDeviceN import *
from .. devices.DBG_AtapiDeviceN import *
from .. devices.DBG_ZpoddDeviceN import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *

from .. fields.DBG_FieldsMapper import *
class DBG_EndDeviceGeneric(DBG_AdapterBase):
        def __init__(self,spar,pparent):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "EndDevice" )
                self.xx_set_full_class_name ( "iastora!EndDevice" )
                self.m_parent = pparent                        
                self.m_ata = DBG_AtaDeviceN("Parent::DBG_EndDeviceGeneric")
                self.m_zpodd = DBG_ZpoddDeviceN("Parent::DBG_EndDeviceGeneric")
                self.m_atapi = DBG_AtapiDeviceN("Parent::DBG_EndDeviceGeneric")
                self.m_type = ""
                self.m_fields = DBG_FieldsMapper("DBG_EndDeviceGeneric"
                                         ,self)                                
                self.mDeviceIdType = "";
                self.mSignature = 0
                                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_EndDevices::prepare_object::")
                self.m_parent = pparent

        def prepare_object(self):
                try:
                        if(self.xx_is_object()==1):
                                self.prepare_object_internal()
                except:
                        self.xx_dbg("EXCEPTION::DBG_EndDeviceGeneric::prepare_object::")
                
        def prepare_object_internal(self):
                
                self.xx_dbg("DBG_EndDevices::prepare_object_internal::in::")
                self.mDeviceIdType = DBG_MemoryTools().xx_get_hex(self,"mDeviceIdType")
                self.mSignature = DBG_MemoryTools().xx_get_hex(self,"mSignature")
                self.m_fields.set_fields_parent(self.m_parent)                
                self.m_fields.add_raw_str("mSignature:" + str(self.mSignature))
                self.m_fields.add_raw_str("mDeviceIdType:" + str(self.mDeviceIdType))
                self.m_type = "NOT_COMPUTED"
                if(str(self.mSignature) == '101'):
                        self.m_type = "ata"                                
                        self.m_ata.set_addr(self.m_parent,"mDevice")
                
                if(str(self.mSignature) == 'eb140101'):
                        if(self.mDeviceIdType == '1000'):
                                self.m_type = "atapi"                                
                                self.m_atapi.set_addr(self.m_parent,"mDevice")
                                
                        if(str(self.mDeviceIdType) == '2000'):
                                self.m_type = "zpodd"
                                self.m_zpodd.set_addr(self.m_parent,"mDevice")
                                                
                self.m_fields.add_raw_str("DevType:" + str(self.m_type))
                
                self.xx_dbg("DBG_EndDevices::prepare_object_internal::out::")
                
        
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        if(self.xx_is_object()==1):
                                self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_EndDevices::print_object::")
                
                self.prepare_object()
                self.xx_print_ptr("")
                self.m_fields.print_object()
                if(self.m_type == "ata"):
                        self.m_ata.print_object()
                        
                if(self.m_type == "atapi"):
                        self.m_atapi.print_object()
                        
                if(self.m_type == "zpodd"):
                        self.m_zpodd.print_object()
                        
                self.xx_dbg("DBG_EndDevices::print_object::out::")
                
