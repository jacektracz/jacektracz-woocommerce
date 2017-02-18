import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *

class DBG_Generics_ISM_LINK(DBG_AdapterBase):
        def __init__(self, spar, pparent):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_Generics_ISM_LINK::__init__::m_in::")
                self.xx_set_class_name ( "_ISM_LINK" )
                self.xx_set_full_class_name ( "iastora!_ISM_LINK" )                
                self.m_fields = DBG_FieldsMapper("DBG_Generics_ISM_LINK"
                                         ,self)
                
                self.m_fields.add_fields_int_array([
                        "EMPTY"
                        ])                
                
                self.xx_dbg("DBG_Generics_ISM_LINK::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_Generics_ISM_LINK::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_Generics_ISM_LINK::prepare_object_internal::")
                if(self.xx_is_object()==1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                
                
                self.xx_dbg("DBG_Generics_ISM_LINK::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_Generics_ISM_LINK::print_object::m_in::")
                self.prepare_object()
                self.xx_print_ptr("")
                
                if(self.xx_is_object()==1):
                        self.m_fields.xx_print_fields("")
                self.xx_dbg("DBG_Generics_ISM_LINK::print_object::m_out::")
