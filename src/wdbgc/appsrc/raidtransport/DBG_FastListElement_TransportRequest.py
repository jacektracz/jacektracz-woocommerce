import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.raidtransport.DBG_TransportRequest import *

class DBG_FastListElement_TransportRequest(DBG_AdapterBase):
        def __init__(self, spar, pparent):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_FastListElement_TransportRequest::__init__::in::")
                self.xx_set_class_name ( "FastListElement<TransportRequest>" )
                self.xx_set_full_class_name ( "iastora!FastListElement<TransportRequest>" )
                
                self.m_fields = DBG_FieldsMapper("DBG_FastListElement_TransportRequest", self)
                self.mObject = DBG_TransportRequest("DBG_FastListElement_TransportRequest",self)
                
                self.create_fields()
                                
                self.xx_dbg("DBG_FastListElement_TransportRequest::__init__::in::")

        def create_fields(self):
                try:
                        self.xx_dbg("DBG_FastListElement_TransportRequest::create_fields::method_in::")
                        #self.m_fields.add_fields_int("mElementCount")
                        self.xx_dbg("DBG_FastListElement_TransportRequest::create_fields::method_out::")
                except:
                        self.xx_exception("DBG_FastListElement_TransportRequest::create_fields")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_FastListElement_TransportRequest::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_FastListElement_TransportRequest::prepare_object::")
                if(self.xx_is_object() == 1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        self.mObject.set_addr(self,"mObject")
                        self.mObject.prepare_object()
                                                                        
                self.xx_dbg("DBG_FastListElement_TransportRequest::prepare_object::out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_FastListElement_TransportRequest::print_object")                                        
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_FastListElement_TransportRequest::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):                
                        self.m_fields.xx_print_fields("")
                        self.mObject.print_object()
                        
                        
                self.xx_dbg("DBG_FastListElement_TransportRequest::print_object_internal::out::")                        
                        
                
        def get_class_str(self):
                self.xx_dbg("DBG_FastListElement_TransportRequest::get_class_str::")
                
                ccstr = """
"""
                self.xx_dbg("DBG_FastListElement_TransportRequest::get_class_str::")
