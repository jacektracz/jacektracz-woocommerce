import sys
import os

from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appsrc.raidtargets.DBG_RaidDiskIdentityData import *

class DBG_TransportTarget(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_TransportTarget::__init__::in::")
                self.xx_set_class_name ( "TransportTarget" )
                self.xx_set_full_class_name ( "iastora!TransportTarget" )
                self.m_fields = DBG_FieldsMapper("DBG_TransportTarget",self)                                
                
                self.init_fields()
                self.xx_dbg("DBG_TransportTarget::__init__::in::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_TransportTarget::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_TransportTarget::prepare_object_internal::")
                
                if(self.xx_is_object() == 1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        self.xx_dbg("DBG_TransportTarget::prepare_object_internal::on::")
                        
                self.xx_dbg("DBG_TransportTarget::prepare_object::out::")
                
        def init_fields(self):
                try:
                        self.m_fields.add_fields_asstr_u32("mTransportTargetState")
                except:
                        self.xx_exception("DBG_TransportTarget::print_object")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_TransportTarget::print_object")
                        
                
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_TransportTarget::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):
                        self.xx_dbg("DBG_TransportTarget::print_object_internal::on::")
                        self.m_fields.xx_print_fields("")
                        
                self.xx_dbg("DBG_TransportTarget::print_object_internal::out::")                        
                        
                
        def get_class_str(self):
                self.xx_dbg("DBG_TransportTarget::get_class_str::")
                
                ccstr = """
"""
                self.xx_dbg("DBG_TransportTarget::get_class_str::")
