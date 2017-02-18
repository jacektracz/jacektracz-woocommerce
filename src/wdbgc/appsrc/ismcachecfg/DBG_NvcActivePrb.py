
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.ismcachecfg.DBG_NvcPrbEntry import *
from ... appsrc.ismcache.DBG_NvCacheFrameHdr import *
from ... appsrc.ismcache.DBG_NvCacheFrameHdr_PyArray import *
class DBG_NvcActivePrb(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_NvcActivePrb::__init__::m_in::")
                
                self.xx_set_class_name ( "NvcActivePrb" )
                self.xx_set_full_class_name ( "iastora!NvcActivePrb" )
                
                self.m_fields = DBG_FieldsMapper("DBG_NvcActivePrb", self)
                self.init_object_fields()
                
                self.activePrbe  = DBG_NvcPrbEntry("DBG_RaidMpbTbl",self)
                self.firstFrame   = DBG_NvCacheFrameHdr("DBG_RaidMpbTbl",self)
                self.freeFrame   = DBG_NvCacheFrameHdr("DBG_RaidMpbTbl",self)
                
                self.m_frames  = DBG_NvCacheFrameHdr_PyArray("DBG_RaidMpbTbl",self)
                self.m_frames.set_parent_names("NvcActivePrb")                
                self.m_frames.set_selectors("firstFrame ","numFramesLeft")
                self.m_frames.init_object_fields()
                
                self.xx_dbg("DBG_NvcActivePrb::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_NvcActivePrb::init_object_fields::in::")                                
                #self.m_fields.add_fields_asstr_u32("mIntervalInMilliseconds")
                self.xx_dbg("DBG_NvcActivePrb::init_object_fields::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_NvcActivePrb::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_NvcActivePrb::prepare_object_internal::")                                
                if(self.xx_obj_valid() == 1 ):
                        self.clear_messages()
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.activePrbe.set_addr(self,"activePrbe")
                        self.activePrbe.prepare_object()
                        
                        self.firstFrame.set_addr(self,"firstFrame")
                        self.firstFrame.prepare_object()
                        
                        self.freeFrame.set_addr(self,"freeFrame")
                        self.freeFrame.prepare_object()
                        
                        self.m_frames.set_addr(self,"SELF")
                        self.m_frames.prepare_object(self)
                        
                self.xx_dbg("DBG_NvcActivePrb::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_NvcActivePrb::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_NvcActivePrb::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_obj_valid() == 1 ):                                                        
                        self.m_fields.print_object()
                        self.activePrbe.print_object()
                        self.firstFrame.print_object()
                        self.freeFrame.print_object()
                        self.m_frames.print_object()
                self.xx_dbg("DBG_NvcActivePrb::print_object::m_out::")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_NvcActivePrb::xx_obj_valid::m_in::")
                i_valid = self.xx_is_object()
                self.xx_dbg("DBG_NvcActivePrb::xx_obj_valid::m_out::" + str(i_valid))
                return i_valid
        
