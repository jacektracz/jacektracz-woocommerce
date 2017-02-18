
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.ismcache.DBG_CacheMpb import *
from ... appsrc.ismcache.DBG_AccelMpb import *

from ... appsrc.ismcache.DBG_RaidMpb import *
from ... appsrc.ismcache.DBG_MdDeltaLogRecord import *
from ... appsrc.ismcache.DBG_NvcPrbEntry import *
from ... appsrc.ismcache.DBG_NvCacheConfigMdHeader import *

from ... appsrc.ismcache.DBG_NvCacheControlData import *
from ... appsrc.ismcache.DBG_NvcCleanAreaMap import *
from ... appsrc.ismcache.DBG_Disk_PyPtr import *
from ... appsrc.ismcache.DBG_ISM_SGE_PAGE_ELEMENT import *
from ... appsrc.ismcachecfg.DBG_SegNumHeap import *
from ... appsrc.ismevents.DBG_Ism_Event import *
class DBG_NvCacheMdMgr(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_NvCacheMdMgr::__init__::m_in::")
                
                self.xx_set_class_name ( "NvCacheMdMgr" )
                self.xx_set_full_class_name ( "iastora!NvCacheMdMgr" )
                
                self.m_fields = DBG_FieldsMapper("DBG_NvCacheMdMgr", self)
                self.init_object_fields()
                
                self.cacheMpb = DBG_CacheMpb("DBG_MemoryMgr", self)
                
                self.accelMpb = DBG_RaidMpb("DBG_MemoryMgr", self)
                #self.raidMpb = DBG_RaidMpb("DBG_MemoryMgr", self)                
                self.currMdLogBlock = DBG_MdDeltaLogRecord("DBG_MemoryMgr", self)                
                self.currMdLogRec = DBG_MdDeltaLogRecord("DBG_MemoryMgr", self)                
                self.currPrbe = DBG_NvcPrbEntry("DBG_MemoryMgr", self)
                self.cacheCfg = DBG_NvCacheConfigMdHeader("DBG_MemoryMgr", self)
                self.cacheMdHdr = DBG_NvCacheControlData("DBG_MemoryMgr", self)
                self.cacheMdHdrBuff = DBG_NvCacheControlData("DBG_MemoryMgr", self)
                self.cleanAreaMap = DBG_NvcCleanAreaMap("DBG_MemoryMgr", self)
                self.nvCacheTarget = DBG_Disk_PyPtr("DBG_MemoryMgr", self)
                self.mdLogSgl = DBG_ISM_SGE_PAGE_ELEMENT("DBG_MemoryMgr", self)
                self.segNumHeap = DBG_SegNumHeap("DBG_MemoryMgr", self)
                self.readComp = DBG_Ism_Event("DBG_MemoryMgr", self)
                self.moveFramesComp = DBG_Ism_Event("DBG_MemoryMgr", self)
                self.writeComp = DBG_Ism_Event("DBG_MemoryMgr", self)
                self.flushComp = DBG_Ism_Event("DBG_MemoryMgr", self)
                self.readBuffComp = DBG_Ism_Event("DBG_MemoryMgr", self)
                self.memAllocComp = DBG_Ism_Event("DBG_MemoryMgr", self)
                self.writePackedMdUnitDoneNotify = DBG_Ism_Event("DBG_MemoryMgr", self)
                self.writeCleanAreaMapComp = DBG_Ism_Event("DBG_MemoryMgr", self)
                
                self.xx_dbg("DBG_NvCacheMdMgr::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_NvCacheMdMgr::init_object_fields::in::")                                
                #self.m_fields.add_fields_asstr_u32("mIntervalInMilliseconds")
                self.xx_dbg("DBG_NvCacheMdMgr::init_object_fields::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_NvCacheMdMgr::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_NvCacheMdMgr::prepare_object_internal::")                                
                if(self.xx_obj_valid() == 1 ):
                        self.clear_messages()
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.cacheMpb.set_addr_arr(self,"cacheMpb")                
                        self.cacheMpb.prepare_object()                

                        self.accelMpb.set_addr_arr(self,"accelMpb")
                        self.accelMpb.prepare_object()
                        
                        #self.raidMpb.set_addr_arr(self,"raidMpb")                
                        #self.raidMpb.prepare_object()
                        
                        self.currMdLogBlock.set_addr(self,"currMdLogBlock")                
                        self.currMdLogBlock.prepare_object()
                        
                        self.currMdLogRec.set_addr(self,"currMdLogRec")                
                        self.currMdLogRec.prepare_object()
                        
                        
                        self.currPrbe.set_addr(self,"currPrbe")                
                        self.currPrbe.prepare_object()
                        
                        self.cacheCfg.set_addr(self,"cacheCfg")                
                        self.cacheCfg.prepare_object()
                        
                        
                        self.cacheMdHdr.set_addr_arr(self,"cacheMdHdr")                
                        self.cacheMdHdr.prepare_object()
                        
                        self.cacheMdHdrBuff.set_addr(self,"cacheMdHdrBuff")                
                        self.cacheMdHdrBuff.prepare_object()
                        
                        self.cleanAreaMap.set_addr_arr(self,"cleanAreaMap")                
                        self.cleanAreaMap.prepare_object()
                                                
                        self.nvCacheTarget.set_addr_arr(self,"nvCacheTarget")                
                        self.nvCacheTarget.prepare_object()
                        
                        
                        self.mdLogSgl.set_addr_arr(self,"mdLogSgl")                
                        self.mdLogSgl.prepare_object()
                        
                        
                        self.segNumHeap.set_addr_arr(self,"segNumHeap")                
                        self.segNumHeap.prepare_object()

                        self.readComp.set_addr_arr(self,"readComp")                
                        self.readComp.prepare_object()
                        
                        self.moveFramesComp.set_addr_arr(self,"moveFramesComp")                
                        self.moveFramesComp.prepare_object()
                        
                        self.writeComp.set_addr_arr(self,"writeComp")                
                        self.writeComp.prepare_object()
                        
                        self.flushComp.set_addr_arr(self,"flushComp")                
                        self.flushComp.prepare_object()
                        
                        self.readBuffComp.set_addr_arr(self,"readBuffComp")                
                        self.readBuffComp.prepare_object()
                        
                        self.memAllocComp.set_addr_arr(self,"memAllocComp")                
                        self.memAllocComp.prepare_object()

                        self.writePackedMdUnitDoneNotify.set_addr_arr(self,"writePackedMdUnitDoneNotify")                
                        self.writePackedMdUnitDoneNotify.prepare_object()

                        self.writeCleanAreaMapComp.set_addr_arr(self,"writeCleanAreaMapComp")                
                        self.writeCleanAreaMapComp.prepare_object()
                                             
                self.xx_dbg("DBG_NvCacheMdMgr::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_NvCacheMdMgr::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_NvCacheMdMgr::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_obj_valid() == 1 ):                                                        
                        self.m_fields.print_object()
                        self.cacheMdHdr.print_object()
                        self.cacheMdHdrBuff.print_object()
                        self.cacheCfg.print_object()
                        self.accelMpb.print_object()
                        self.cacheMpb.print_object()
                        #self.raidMpb.print_object()
                        self.currMdLogBlock.print_object()
                        self.currMdLogRec.print_object()
                        self.currPrbe.print_object()
                        self.cleanAreaMap.print_object()
                        self.nvCacheTarget.print_object()
                        self.mdLogSgl.print_object()
                        self.segNumHeap.print_object()
                        self.readComp.print_object()
                        self.moveFramesComp.print_object()
                        self.writeComp.print_object()
                        self.flushComp.print_object()
                        self.readBuffComp.print_object()
                        self.memAllocComp.print_object()
                        self.writePackedMdUnitDoneNotify.print_object()
                        self.writeCleanAreaMapComp.print_object()
                        
                self.xx_dbg("DBG_NvCacheMdMgr::print_object::m_out::")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_NvCacheMdMgr::xx_obj_valid::m_in::")
                i_valid = self.xx_is_object()
                self.xx_dbg("DBG_NvCacheMdMgr::xx_obj_valid::m_out::" + str(i_valid))
                return i_valid
        
