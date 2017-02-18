
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *

class DBG_PowerState(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_PowerState::__init__::m_in::")
                
                self.xx_set_class_name ( "PowerState" )
                self.xx_set_full_class_name ( "iastora!PowerState" )
                
                self.m_fields = DBG_FieldsMapper("DBG_PowerState", self)
                self.init_object_fields()
                
                self.xx_dbg("DBG_PowerState::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_PowerState::init_object_fields::in::")                                
                #self.m_fields.add_fields_asstr_ints([])                                                
                self.xx_dbg("DBG_PowerState::init_object_fields::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_PowerState::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_PowerState::prepare_object_internal::")                                
                if(self.xx_obj_valid() == 1 ):
                        self.clear_messages()
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                self.xx_dbg("DBG_PowerState::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_PowerState::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_PowerState::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_obj_valid() == 1 ):                                                        
                        self.m_fields.print_object()
                                
                self.xx_dbg("DBG_PowerState::print_object::m_out::")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_PowerState::xx_obj_valid::m_in::")
                i_valid = self.xx_is_object()
                self.xx_dbg("DBG_PowerState::xx_obj_valid::m_out::" + str(i_valid))
                return i_valid
        
