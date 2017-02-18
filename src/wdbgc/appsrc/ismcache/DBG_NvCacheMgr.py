
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.ismcache.DBG_NvCacheFrameHdr import *
from ... appsrc.ismcache.DBG_NvCacheFrameHdrSet import *
from ... appsrc.ismcache.DBG_NvCacheMdMgr import *
from ... appsrc.ismcache.DBG_NvActiveFrameReqsRbTree import *
from ... appsrc.ismcache.DBG_LbaLockPool import *
from ... appsrc.ismcachecfg.DBG_NvcPromoBlkSet import *
class DBG_NvCacheMgr(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_NvCacheMgr::__init__::m_in::")
                
                self.xx_set_class_name ( "NvCacheMgr" )
                self.xx_set_full_class_name ( "iastora!NvCacheMgr" )
                
                self.m_fields = DBG_FieldsMapper("DBG_NvCacheMgr", self)
                self.init_object_fields()
                
                self.cacheFrameSet = DBG_NvCacheFrameHdrSet("DBG_MemoryMgr", self)                
                self.bootListBookMark = DBG_NvCacheFrameHdr("DBG_MemoryMgr", self)
                self.trimFreeListCurrentFrame = DBG_NvCacheFrameHdr("DBG_MemoryMgr", self)
                self.bgCleanCursorFrame = DBG_NvCacheFrameHdr("DBG_MemoryMgr", self)
                self.cacheLockPool = DBG_LbaLockPool("DBG_MemoryMgr", self)
                self.cacheMdMgr = DBG_NvCacheMdMgr("DBG_MemoryMgr", self)
                self.afrRbTree = DBG_NvActiveFrameReqsRbTree("DBG_MemoryMgr", self)
                self.promoBlkSet = DBG_NvcPromoBlkSet("DBG_MemoryMgr", self)
                self.xx_dbg("DBG_NvCacheMgr::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_NvCacheMgr::init_object_fields::in::")                                
                #self.m_fields.add_fields_asstr_u32("mIntervalInMilliseconds")
                self.xx_dbg("DBG_NvCacheMgr::init_object_fields::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_NvCacheMgr::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_NvCacheMgr::prepare_object_internal::")                                
                if(self.xx_obj_valid() == 1 ):
                        self.clear_messages()
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        

                        self.cacheFrameSet.set_addr_arr(self,"cacheFrameSet")                
                        self.cacheFrameSet.prepare_object()                

                        self.bootListBookMark.set_addr(self,"bootListBookMark")                
                        self.bootListBookMark.prepare_object()
                        
                        self.trimFreeListCurrentFrame.set_addr(self,"trimFreeListCurrentFrame")                
                        self.trimFreeListCurrentFrame.prepare_object()                

                        self.cacheMdMgr.set_addr(self,"cacheMdMgr")                
                        self.cacheMdMgr.prepare_object()                

                        self.cacheLockPool.set_addr_arr(self,"cacheLockPool")                
                        self.cacheLockPool.prepare_object()                

                        self.afrRbTree.set_addr_arr(self,"afrRbTree")                
                        self.afrRbTree.prepare_object()                
                        
                        self.promoBlkSet.set_addr_arr(self,"promoBlkSet")                
                        self.promoBlkSet.prepare_object()                
                        
                self.xx_dbg("DBG_NvCacheMgr::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_NvCacheMgr::print_object")
                        
        def print_object_internal(self, sdbg=""):
                self.xx_dbg("DBG_NvCacheMgr::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_obj_valid() == 1 ):                                                        
                        self.m_fields.print_object()                        
                        self.cacheFrameSet.print_object()                
                        self.bootListBookMark.print_object()
                        self.trimFreeListCurrentFrame.print_object()                
                        self.cacheMdMgr.print_object()                
                        self.cacheLockPool.print_object()                                        
                        self.afrRbTree.print_object()                
                        self.promoBlkSet.print_object()
                        
                self.xx_dbg("DBG_NvCacheMgr::print_object::m_out::")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_NvCacheMgr::xx_obj_valid::m_in::")
                i_valid = self.xx_is_object()
                self.xx_dbg("DBG_NvCacheMgr::xx_obj_valid::m_out::" + str(i_valid))
                return i_valid
        
