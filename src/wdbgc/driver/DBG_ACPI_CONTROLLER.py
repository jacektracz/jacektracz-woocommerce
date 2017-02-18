import sys
import os
from .. appcore.memory.DBG_Utils import *
from .. appcore.memory.DBG_MemoryTools import *
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. appsrc.acpi.DBG_AcpiMethods import *
from .. appcore.config.DBG_PrintConfig import *
class DBG_ACPI_CONTROLLER(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_ACPI_CONTROLLER::__init__::method_in::")
                self.xx_set_class_name ( "Wcdl::ACPI::ACPI_CONTROLLER" )
                self.xx_set_full_class_name ( "iastora!Wcdl::ACPI::ACPI_CONTROLLER" )
                self.m_parent = self
                
                self.m_fields = DBG_FieldsMapper("DBG_ACPI_CONTROLLER"
                                         ,self)
                
                self.m_fields.add_fields_int_array([
                        "mLength"
                        ])
                
                self.m_fields.add_fields_str("mName",256)
                self.mMethods = DBG_AcpiMethods("DBG_ACPI_CONTROLLER",self)
                self.xx_dbg("DBG_ACPI_CONTROLLER::__init__::method_out::")       
                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_ACPI_CONTROLLER::set_parent::")
                self.m_parent = pparent
                self.xx_dbg("DBG_ACPI_CONTROLLER::set_parent::out")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal()                                
                except:
                        self.xx_exception("DBG_ACPI_CONTROLLER::print_object")
                                        
        def prepare_object_internal(self):
                self.xx_dbg("DBG_ACPI_CONTROLLER::prepare_object_internal::")
                if(self.xx_is_object() == 1):
                        self.m_fields.initialize_by_parent(self)
                        if (DBG_PrintConfig().getItem().m_handle_methods == "1"):
                                self.mMethods.set_addr_arr(self,"mMethods")
                                self.mMethods.prepare_object()
                self.xx_dbg("DBG_ACPI_CONTROLLER::prepare_object_internal::out")
                                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")                                
                except:
                        self.xx_exception("DBG_ACPI_CONTROLLER::print_object")
                        
        def print_object_internal(self):                
                self.xx_dbg("DBG_ACPI_CONTROLLER::print_object::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):
                        self.m_fields.print_object()
                        if (DBG_PrintConfig().getItem().m_handle_methods == "1"):
                                self.mMethods.print_object()
                self.xx_dbg("DBG_ACPI_CONTROLLER::print_object::out")

                
                
                