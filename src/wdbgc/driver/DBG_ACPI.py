import sys
import os
from .. appcore.memory.DBG_Utils import *
from .. appcore.memory.DBG_MemoryTools import *
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. driver.DBG_ACPI_CONTROLLER import *
from .. appsrc.acpi.DBG_DEVICE_OBJECT import *

class DBG_ACPI(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_ACPI::__init__::method_in::")
                self.xx_set_class_name ( "Wcdl::ACPI" )
                self.xx_set_full_class_name ( "iastora!Wcdl::ACPI" )
                self.m_parent = self
                
                self.m_fields = DBG_FieldsMapper("DBG_ACPI"
                                         ,self)
                
                self.m_fields.add_fields_int_array([
                        "LINE"
                        ])
                self.mController = DBG_ACPI_CONTROLLER("Parent::DBG_ACPI")
                self.mAcpi = DBG_DEVICE_OBJECT("",self)
                self.mFdo = DBG_DEVICE_OBJECT("",self)
                self.xx_dbg("DBG_ACPI::__init__::method_out::")       
                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_ACPI::set_parent::")
                self.m_parent = pparent
                self.xx_dbg("DBG_ACPI::set_parent::out")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal()                                
                except:
                        self.xx_exception("DBG_ACPI::print_object")
                                        
        def prepare_object_internal(self):
                self.xx_dbg("DBG_ACPI::prepare_object_internal::")
                if(self.xx_is_object()==1):
                        self.m_fields.initialize_by_parent(self)
                        
                        self.mController.set_addr_arr(self,"mController")
                        self.mAcpi.prepare_object()
                        
                        self.mAcpi.set_addr(self,"mAcpi")
                        self.mAcpi.prepare_object()
                        
                        self.mFdo.set_addr(self,"mFdo")
                        self.mFdo.prepare_object()
                        
                self.xx_dbg("DBG_ACPI::prepare_object_internal::out")
                                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_ACPI::print_object")
                        
        def print_object_internal(self):                
                self.xx_dbg("DBG_ACPI::print_object::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object()==1):
                        self.m_fields.print_object()
                        self.mController.print_object()
                        self.mAcpi.print_object()
                        self.mFdo.print_object()
                        
                self.xx_dbg("DBG_ACPI::print_object::out")

                
                
                