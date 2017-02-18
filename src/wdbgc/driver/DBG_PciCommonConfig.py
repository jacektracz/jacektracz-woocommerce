import sys
import os
from .. appcore.memory.DBG_Utils import *
from .. appcore.memory.DBG_MemoryTools import *
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
                
class DBG_PciCommonConfig(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_PciCommonConfig::__init__::method_in::")
                self.xx_set_class_name ( "_PCI_COMMON_CONFIG" )
                self.xx_set_full_class_name ( "iastora!_PCI_COMMON_CONFIG" )
                self.m_parent = self
                
                self.m_fields = DBG_FieldsMapper("DBG_PciCommonConfig"
                                         ,self)
                
                self.m_fields.add_fields_str("DeviceSpecific",192)
                self.m_fields.add_fields_int_array([
                        "VendorID"
                        ,"DeviceID"
                        ,"Status"
                        ,"RevisionID"
                        ])
                
                self.xx_dbg("DBG_PciCommonConfig::__init__::method_out::")       
                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_PciCommonConfig::set_parent::")
                self.m_parent = pparent
                self.xx_dbg("DBG_PciCommonConfig::set_parent::out")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal()                                
                except:
                        self.xx_exception("DBG_PciCommonConfig::print_object")
                                        
        def prepare_object_internal(self):
                self.xx_dbg("DBG_PciCommonConfig::prepare_object_internal::")
                if(self.xx_is_object()==1):                
                        self.m_fields.initialize_by_parent(self)                
                self.xx_dbg("DBG_PciCommonConfig::prepare_object_internal::out")
                                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):               
                self.xx_dbg("DBG_PciCommonConfig::print_object::")
                self.xx_print_ptr("")
                self.prepare_object()
                if(self.xx_is_object()==1):
                        self.m_fields.print_object() 
                self.xx_dbg("DBG_PciCommonConfig::print_object::out")

                
                
                