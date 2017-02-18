
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
#from ... appsrc.ismevents.DBG_IsmQueue import *
from ... appcore.printers.DBG_MethodByAddrPrinter import *
class DBG_Ism_Event(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_Ism_Event::__init__::m_in::")
                
                self.xx_set_class_name ( "Event" )
                self.xx_set_full_class_name ( "iastora!Event" )
                
                self.m_fields = DBG_FieldsMapper("DBG_Ism_Event", self)
                self.m_handler_method = DBG_MethodByAddrPrinter("DBG_Ism_Event", self)
                self.init_object_fields()
                #self.mQueue = DBG_IsmQueue("DBG_Ism_Event", self)
                self.xx_dbg("DBG_Ism_Event::__init__::m_out::")

        def init_object_fields(self):
                """                """
                self.xx_dbg("DBG_Ism_Event::init_object_fields::in::")                                
                self.m_fields.add_fields_asstr_addr_method("handler")
                self.m_fields.add_fields_asstr_addr_memory("context")
                self.m_fields.add_fields_asstr_addr_class("_next")
                self.m_fields.add_fields_asstr_ints([
                        "arg"
                        ])
                
                self.xx_dbg("DBG_Ism_Event::init_object_fields::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_Ism_Event::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_Ism_Event::prepare_object_internal::")                                
                if(self.xx_obj_valid() == 1 ):
                        self.clear_messages()
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        s_addr = self.m_fields.get_fields_string("handler")
                        self.m_handler_method.set_parent(self)
                        self.m_handler_method.set_addr_string(s_addr)
                        self.m_handler_method.prepare_object()
                        #self.mQueue.set_addr_arr(self,"mQueue")
                        #self.mQueue.prepare_object()
                        
                self.xx_dbg("DBG_Ism_Event::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_Ism_Event::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_Ism_Event::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_obj_valid() == 1 ):                                                        
                        self.m_fields.print_object()
                        self.m_handler_method.print_object()
                        #self.mQueue.print_object()
                self.xx_dbg("DBG_Ism_Event::print_object::m_out::")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_Ism_Event::xx_obj_valid::m_in::")
                i_valid = self.xx_is_object()
                self.xx_dbg("DBG_Ism_Event::xx_obj_valid::m_out::" + str(i_valid))
                return i_valid
        
