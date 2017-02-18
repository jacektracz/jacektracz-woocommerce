
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.acpi.DBG_UNICODE_STRING import *

class DBG_DRIVER_OBJECT(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_DRIVER_OBJECT::__init__::m_in::")
                
                self.xx_set_class_name ( "_DRIVER_OBJECT" )
                self.xx_set_full_class_name ( "iastora!_DRIVER_OBJECT" )
                
                self.m_fields = DBG_FieldsMapper("DBG_DRIVER_OBJECT", self)
                self.init_object_fields()
                self.m_DriverName = DBG_UNICODE_STRING("",self)
                self.m_HardwareDatabase = DBG_UNICODE_STRING("",self)
                self.xx_dbg("DBG_DRIVER_OBJECT::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_DRIVER_OBJECT::init_object_fields::in::")
                self.m_fields.add_fields_asstr_addr("DriverStart")
                self.m_fields.add_fields_asstr_addr("DriverInit")
                self.m_fields.add_fields_asstr_addr("DriverStartIo")
                self.m_fields.add_fields_asstr_addr("DriverUnload")
                self.xx_dbg("DBG_DRIVER_OBJECT::init_object_fields::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_DRIVER_OBJECT::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_DRIVER_OBJECT::prepare_object_internal::")                                
                if(self.xx_obj_valid() == 1 ):
                        self.clear_messages()
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.m_DriverName.set_addr_arr(self,"DriverName")
                        self.m_DriverName.prepare_object()
                        
                        self.m_HardwareDatabase.set_addr(self,"HardwareDatabase")
                        self.m_HardwareDatabase.prepare_object()
                        
                self.xx_dbg("DBG_DRIVER_OBJECT::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_DRIVER_OBJECT::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_DRIVER_OBJECT::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_obj_valid() == 1 ):                                                        
                        self.m_fields.print_object()
                        self.m_DriverName.print_object()
                        self.m_HardwareDatabase.print_object()
                self.xx_dbg("DBG_DRIVER_OBJECT::print_object::m_out::")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_DRIVER_OBJECT::xx_obj_valid::m_in::")
                i_valid = self.xx_is_object()
                self.xx_dbg("DBG_DRIVER_OBJECT::xx_obj_valid::m_out::" + str(i_valid))
                return i_valid
        
