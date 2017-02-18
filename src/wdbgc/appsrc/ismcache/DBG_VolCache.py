import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
#from ... childdir.DBG_ApstTable import *
from ... appsrc.ismcache.DBG_IsmIoReqList import *
from ... appsrc.ismcache.DBG_LbaLockSet import *
from ... appsrc.ismcache.DBG_IsmIoReq import *
from ... appsrc.ismcache.DBG_CacheWritePolicy import *
from ... appsrc.ismcache.DBG_CacheReadPolicy import *
#@F
class DBG_VolCache(DBG_AdapterBase):
        def __init__(self, spar, pparent):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_VolCache::__init__::m_in::")
                self.xx_set_class_name ( "VolCache" )
                self.xx_set_full_class_name ( "iastora!VolCache" )
                #self.m_child_item = DBG_ApstTable("Parent::DBG_VolCache")
                self.m_fields = DBG_FieldsMapper("DBG_VolCache", self)
                self.pendingReqs = DBG_IsmIoReqList("Parent::DBG_IsmIoReqList",self)
                self.lbaLockSet = DBG_LbaLockSet("Parent::DBG_LbaLockSet",self)
                self.cacheFlushReq = DBG_IsmIoReq("Parent::DBG_IsmIoReq",self)
                self.writePolicy = DBG_CacheWritePolicy("Parent::DBG_CacheWritePolicy",self)
                self.readPolicy = DBG_CacheReadPolicy("Parent::DBG_CacheReadPolicy",self)
                #@I
                self.init_object_fields()
                self.xx_dbg("DBG_VolCache::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_VolCache::init_object_fields::method_in::")                                
                #self.m_fields.add_fields_asstr_ints([])                                                
                self.xx_dbg("DBG_VolCache::init_object_fields::method_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_VolCache::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_VolCache::prepare_object_internal::method_in::")
                
                if(self.xx_is_object()):
                        self.m_fields.set_fields_parent(self)                      
                        #self.m_child_item.set_addr_arr(self,"m_child_item")
                        self.pendingReqs.set_addr_arr(self,"pendingReqs")                
                        self.pendingReqs.prepare_object()                
                        self.lbaLockSet.set_addr_arr(self,"lbaLockSet")                
                        self.lbaLockSet.prepare_object()                
                        self.cacheFlushReq.set_addr(self,"cacheFlushReq")
                        self.cacheFlushReq.prepare_object()                
                        self.writePolicy.set_addr_arr(self,"writePolicy")                
                        self.writePolicy.prepare_object()                
                        self.readPolicy.set_addr_arr(self,"readPolicy")                
                        self.readPolicy.prepare_object()                
                        #@P                
                self.xx_dbg("DBG_VolCache::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_UNICODE_Buffer::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_VolCache::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_is_object()):                
                        self.m_fields.xx_print_fields("")
                        #self.m_child_item.print_object()
                        self.pendingReqs.print_object()                    
                        self.lbaLockSet.print_object()                    
                        self.cacheFlushReq.print_object()                    
                        self.writePolicy.print_object()                    
                        self.readPolicy.print_object()                    
                        #@R                    
                self.xx_dbg("DBG_VolCache::print_object::m_out::")