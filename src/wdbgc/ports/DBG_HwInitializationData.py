import sys
import os

from .. DBG_AdapterBase import *       
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. fields.DBG_FieldsMapper import *
from .. defs.DBG_HwInterfaceType import *
class DBG_HwInitializationData(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_HwInitializationData::__init__::")
                self.xx_set_class_name ( "_HW_INITIALIZATION_DATA" )                
                self.xx_set_full_class_name ( "iastora!_HW_INITIALIZATION_DATA" )
                self.m_fields = DBG_FieldsMapper("DBG_HwInitializationData"
                                                 ,self)
                self.m_fields.add_int("AdapterInterfaceType")
                self.m_fields.add_int("DeviceExtensionSize")                
                self.m_fields.add_int("SpecificLuExtensionSize")
                self.m_fields.add_int("SrbExtensionSize")
                self.m_fields.add_int("NumberOfAccessRanges")
                self.m_fields.add_int("MapBuffers")
                self.m_fields.add_hex("NeedPhysicalAddresses")                
                
                
                self.m_fields.add_hex("TaggedQueuing")
                self.m_fields.add_hex("AutoRequestSense")
                self.m_fields.add_hex("MultipleRequestPerLu")
                self.m_fields.add_hex("DeviceId")
                self.m_AdapterInterfaceType = 0
                self.xx_dbg("DBG_HwInitializationData::__init__::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_HwInitializationData::print_object_internal::")                                
                self.xx_print_ptr("")
                self.prepare_object()
                if(self.xx_is_object() == 1):
                        s_it = DBG_HwInterfaceType("").get_str(self.m_AdapterInterfaceType)
                        self.m_fields.add_raw_str( "AdapterInterfaceType:"+ s_it)
                        self.m_fields.print_object()
                self.xx_dbg("DBG_HwInitializationData::print_object_internal::out::")
                
        def prepare_object(self):
                self.xx_dbg("DBG_HwInitializationData::prepare_object::")
                if(self.xx_is_object() == 0):
                        return                
                self.m_fields.set_parent(self)
                self.m_fields.prepare_object()
                self.m_AdapterInterfaceType = self.m_fields.get_fields_int("AdapterInterfaceType")
                self.xx_dbg("DBG_HwInitializationData::prepare_object::out::")        