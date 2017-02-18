

import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appsrc.ismcache.DBG_RaidMpb import *

#from ... raidism.DBG_RaidIsmDisk import *

#@F
class DBG_ArrayMpbMgr(DBG_AdapterBase):
        def __init__(self, spar, pparent):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_ArrayMpbMgr::__init__::m_in::")
                self.xx_set_class_name ( "ArrayMpbMgr" )
                self.xx_set_full_class_name ( "iastora!ArrayMpbMgr" )
                #self.m_child_item = DBG_ApstTable("Parent::DBG_ArrayMpbMgr")
                self.m_fields = DBG_FieldsMapper("DBG_ArrayMpbMgr", self)
                #self.fastEnumCacheDev = DBG_RaidIsmDisk("DBG_ArrayMpbMgr")
                #@I
                self.init_object_fields()
                self.raidMpb = DBG_RaidMpb("DBG_ArrayMpbMgr",self)
                self.xx_dbg("DBG_ArrayMpbMgr::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_ArrayMpbMgr::init_object_fields::method_in::")                                
                #self.m_fields.add_fields_asstr_ints([])
                #self.m_fields.add_fields_int("mNumPaths")
                self.xx_dbg("DBG_ArrayMpbMgr::init_object_fields::method_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_ArrayMpbMgr::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_ArrayMpbMgr::prepare_object_internal::")
                
                if(self.xx_is_object()):
                        self.m_fields.set_fields_parent(self)                        
                        self.raidMpb.set_addr(self,"raidMpb")
                        self.raidMpb.prepare_object()
                        
                        #@P                
                self.xx_dbg("DBG_ArrayMpbMgr::prepare_object::m_out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_ArrayMpbMgr_PyArray::print_object")
                        
        def print_object_internal(self):
                self.xx_dbg("DBG_ArrayMpbMgr::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_is_object()):                
                        self.m_fields.xx_print_fields("")
                        self.raidMpb.print_object()
                        
                        #@R                    
                self.xx_dbg("DBG_ArrayMpbMgr::print_object::m_out::")
