


import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appsrc.ismcache.DBG_NvCacheFrameHdrSet import *
#from ... childdir.DBG_ApstTable import *
#from ... appsrc.ismcfg.DBG_MemberDiskInfo_PyArray import *
#@F
class DBG_NvCrashDmp(DBG_AdapterBase):
        def __init__(self, spar, pparent):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_NvCrashDmp::__init__::m_in::")
                self.xx_set_class_name ( "NvCrashDmp" )
                self.xx_set_full_class_name ( "iastora!NvCrashDmp" )
                #self.m_child_item = DBG_ApstTable("Parent::DBG_NvCrashDmp")
                self.m_fields = DBG_FieldsMapper("DBG_NvCrashDmp", self)
                self.cacheFrameSet = DBG_NvCacheFrameHdrSet("DBG_MemoryMgr", self)                
                #self.m_disks_info = DBG_MemberDiskInfo_PyArray("Parent::DBG_MemberDiskInfo_PyArray",self)
                #@I
                self.init_object_fields()
                self.xx_dbg("DBG_NvCrashDmp::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_NvCrashDmp::init_object_fields::method_in::")                                
                #self.m_fields.add_fields_asstr_ints([])                                                
                self.xx_dbg("DBG_NvCrashDmp::init_object_fields::method_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_NvCrashDmp::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_NvCrashDmp::prepare_object_internal::")
                
                if(self.xx_is_object()):
                        self.m_fields.set_fields_parent(self)
                        self.cacheFrameSet.set_addr_arr(self,"cacheFrameSet")                
                        self.cacheFrameSet.prepare_object()                
                        
                        #self.m_child_item.set_addr_arr(self,"m_child_item")
                        #self.m_disks_info.set_addr(self,"SELF")
                        #self.m_disks_info.prepare_object(self)
                        #@P                
                self.xx_dbg("DBG_NvCrashDmp::prepare_object::m_out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_NvCrashDmp::print_object")
                        
        def print_object_internal(self):
                self.xx_dbg("DBG_NvCrashDmp::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_is_object()):                
                        self.m_fields.xx_print_fields("")
                        self.cacheFrameSet.print_object()
                        #self.m_child_item.print_object()
                        #self.m_disks_info.print_object()                    
                        #@R                    
                self.xx_dbg("DBG_NvCrashDmp::print_object::m_out::")