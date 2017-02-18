

import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
#used in CfgRaidMap
from ... raidism.DBG_RaidIsmDisk import *
#from ... childdir.DBG_ApstTable import *
#@F
class DBG_DiskMpbMgr(DBG_AdapterBase):
        def __init__(self, spar, pparent):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_DiskMpbMgr::__init__::m_in::")
                self.xx_set_class_name ( "DiskMpbMgr" )
                self.xx_set_full_class_name ( "iastora!DiskMpbMgr" )
                #self.m_child_item = DBG_ApstTable("Parent::DBG_DiskMpbMgr")
                self.m_fields = DBG_FieldsMapper("DBG_DiskMpbMgr", self)
                self.fastEnumCacheDev = DBG_RaidIsmDisk("DBG_DiskMpbMgr")
                self.fastEnumAccelDev = DBG_RaidIsmDisk("DBG_DiskMpbMgr")
                self.m_handle_disks = 0
                #@I
                self.init_object_fields()
                self.xx_dbg("DBG_DiskMpbMgr::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_DiskMpbMgr::init_object_fields::method_in::")                                
                #self.m_fields.add_fields_asstr_ints([])
                #self.m_fields.add_fields_int("mNumPaths")
                self.xx_dbg("DBG_DiskMpbMgr::init_object_fields::method_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_DiskMpbMgr::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_DiskMpbMgr::prepare_object_internal::")
                
                if(self.xx_is_object()):
                        self.m_fields.set_fields_parent(self)
                        if(self.m_handle_disks==1):
                                self.fastEnumCacheDev.set_addr(self,"fastEnumCacheDev")
                                self.fastEnumCacheDev.prepare_object()
                                
                                self.fastEnumAccelDev.set_addr(self,"fastEnumAccelDev")
                                self.fastEnumAccelDev.prepare_object()
                        
                        #self.m_child_item.set_addr_arr(self,"m_child_item")
                        #@P                
                self.xx_dbg("DBG_DiskMpbMgr::prepare_object::m_out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_DiskMpbMgr_PyArray::print_object")
                        
        def print_object_internal(self):
                self.xx_dbg("DBG_DiskMpbMgr::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_is_object()):                
                        self.m_fields.xx_print_fields("")
                        if(self.m_handle_disks==1):
                                self.fastEnumCacheDev.print_object()
                                self.fastEnumAccelDev.print_object()
                        #self.m_child_item.print_object()
                        #@R                    
                self.xx_dbg("DBG_DiskMpbMgr::print_object::m_out::")
