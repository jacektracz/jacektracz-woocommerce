
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.ismcache.DBG_CacheCandidate import *
from ... appsrc.ismcache.DBG_CacheEntryHdr import *
from ... appsrc.ismcache.DBG_CacheEntryHdrPool import *
from ... appsrc.ismcache.DBG_CacheEntryPool import *
from ... appsrc.ismcache.DBG_CacheEntryHdrSet import *
from ... appsrc.ismcache.DBG_CacheEntryHdrList import *
from ... appsrc.generics.DBG_Generics_PyList import *
from ... appsrc.generics.DBG_Generics_PyHashTable import *
class DBG_CacheMgr(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_CacheMgr::__init__::m_in::")
                
                self.xx_set_class_name ( "CacheMgr" )
                self.xx_set_full_class_name ( "iastora!CacheMgr" )
                
                self.m_fields = DBG_FieldsMapper("DBG_CacheMgr", self)
                self.init_object_fields()
                
                self.cacheCandLru_PyList = DBG_Generics_PyHashTable("DBG_CacheMgr", self,"")
                self.cacheCandLru_PyList.m_item_type = "CacheCandidate"
                self.cacheCandLru_PyList.set_parent_names("CacheCandidate")
                self.cacheCandLru_PyList.set_selectors("_not_set","_not_set")
                
                self.cacheCandLru_PyList.init_object_fields()
                
                self.cacheCandLru = DBG_CacheCandidate("DBG_CacheMgr", self)
                self.mruCleanCacheCand = DBG_CacheEntryHdr("DBG_CacheMgr", self)
                self.cacheCandSet = DBG_CacheEntryHdrSet("DBG_CacheMgr", self)
                self.cachedCandList = DBG_CacheEntryHdrList("DBG_CacheMgr", self)
                self.fullCacheEntryPool = DBG_CacheEntryPool("DBG_CacheMgr", self)
                self.emptyCacheEntryPool  = DBG_CacheEntryPool("DBG_CacheMgr", self)
                
                self.xx_dbg("DBG_CacheMgr::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_CacheMgr::init_object_fields::in::")                                
                #self.m_fields.add_fields_asstr_u32("mIntervalInMilliseconds")
                self.xx_dbg("DBG_CacheMgr::init_object_fields::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_CacheMgr::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_CacheMgr::prepare_object_internal::")                                
                if(self.xx_obj_valid() == 1 ):
                        self.clear_messages()
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.cacheCandLru.set_addr(self,"cacheCandLru")
                        self.cacheCandLru.prepare_object()
                        
                        self.mruCleanCacheCand.set_addr(self,"mruCleanCacheCand")
                        self.mruCleanCacheCand.prepare_object()
                        
                        
                        self.cacheCandSet.set_addr_arr(self,"cacheCandSet")
                        self.cacheCandSet.prepare_object()
                        
                        #(((iastora!CacheEntryHdrList*)&((((iastora!CacheMgr*)0xffffe000e4d9a8c0))->cacheCandList)))
                        #(((iastora!CacheEntryHdrList*)((((iastora!CacheMgr*)0xffffe000e4d9a8c0))->cacheCandList)))
                        self.cachedCandList.set_addr_arr(self,"cachedCandList")
                        self.cachedCandList.prepare_object()
                        
                        self.fullCacheEntryPool.set_addr_arr(self,"fullCacheEntryPool")
                        self.fullCacheEntryPool.prepare_object()
                        
                        self.emptyCacheEntryPool.set_addr_arr(self,"emptyCacheEntryPool")
                        self.emptyCacheEntryPool.prepare_object()
                        
                        self.cacheCandLru_PyList.set_addr(self,"cacheCandLru")
                        self.cacheCandLru_PyList.prepare_object()
                        
                self.xx_dbg("DBG_CacheMgr::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_CacheMgr::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_CacheMgr::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_obj_valid() == 1 ):                                                        
                        self.m_fields.print_object()
                        self.cacheCandLru.print_object()
                        self.mruCleanCacheCand.print_object()
                        self.cacheCandSet.print_object()
                        self.cachedCandList.print_object()
                        
                        self.fullCacheEntryPool.print_object()                        
                        self.emptyCacheEntryPool.print_object()
                        self.cacheCandLru_PyList.print_object()
                self.xx_dbg("DBG_CacheMgr::print_object::m_out::")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_CacheMgr::xx_obj_valid::m_in::")
                i_valid = self.xx_is_object()
                self.xx_dbg("DBG_CacheMgr::xx_obj_valid::m_out::" + str(i_valid))
                return i_valid
        
