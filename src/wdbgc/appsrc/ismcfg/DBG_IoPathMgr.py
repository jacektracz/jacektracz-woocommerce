
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.ismcfg.DBG_MPB_SERIAL import *
#from ... appsrc.ismcfg.DBG_DiskMpbMgr import *

#from ... raidism.DBG_RaidIsmDisk import *
from ... appsrc.ismcfg.DBG_VolCache import *
from ... appsrc.ismcfg.DBG_NvCache import *
from ... appsrc.ismcfg.DBG_IoCoalescer import *
from ... appsrc.ismcfg.DBG_HostIoTarget import *
from ... appsrc.ismcache.DBG_FlushSyncInfo import *
from ... appsrc.ismcache.DBG_IsmIoReq import *
from ... appsrc.ismcache.DBG_IsmIoReqFifo import *

class DBG_IoPathMgr(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_IoPathMgr::__init__::m_in::")
                
                self.xx_set_class_name ( "IoPathMgr" )
                self.xx_set_full_class_name ( "iastora!IoPathMgr" )
                
                self.m_fields = DBG_FieldsMapper("DBG_IoPathMgr", self)
                self.init_object_fields()
                #self.serial = DBG_MPB_SERIAL("DBG_IoPathMgr", self)
                #self.mpbMgr = DBG_DiskMpbMgr("DBG_IoPathMgr",self)
                self.hostIoTarget = DBG_HostIoTarget("DBG_IoPathMgr", self)
                self.ioCoalescer = DBG_IoCoalescer("DBG_IoPathMgr", self)
                self.nvCache = DBG_NvCache("DBG_IoPathMgr", self)
                self.volCache = DBG_VolCache("DBG_IoPathMgr", self)
                self.raidDev = DBG_HostIoTarget("DBG_IoPathMgr", self)
                self.flushSyncInfo = DBG_FlushSyncInfo("DBG_IoPathMgr", self)
                self.flushIoReq = DBG_IsmIoReq("DBG_IoPathMgr", self)
                self.blockerIoReq = DBG_IsmIoReq("DBG_IoPathMgr", self)
                self.pendingIoReqs = DBG_IsmIoReqFifo("DBG_IoPathMgr", self)
                self.xx_dbg("DBG_IoPathMgr::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_IoPathMgr::init_object_fields::in::")                                
                #self.m_fields.add_fields_asstr_ints([])                                                
                self.xx_dbg("DBG_IoPathMgr::init_object_fields::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_IoPathMgr::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_IoPathMgr::prepare_object_internal::")                                
                if(self.xx_obj_valid() == 1 ):
                        self.clear_messages()
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        #self.serial.set_addr_arr(self,"serial")
                        #self.serial.prepare_object()
                        
                        self.hostIoTarget.set_addr(self,"hostIoTarget")
                        self.hostIoTarget.prepare_object()                        

                        self.ioCoalescer.set_addr(self,"ioCoalescer")
                        self.ioCoalescer.prepare_object()                        

                        self.nvCache.set_addr(self,"nvCache")
                        self.nvCache.prepare_object()  

                        self.volCache.set_addr(self,"volCache")
                        self.volCache.prepare_object()
                        
                        self.raidDev.set_addr(self,"raidDev")
                        self.raidDev.prepare_object()

                        self.flushSyncInfo.set_addr_arr(self,"flushSyncInfo")
                        self.flushSyncInfo.prepare_object()

                        self.flushIoReq.set_addr_arr(self,"flushIoReq")
                        self.flushIoReq.prepare_object()
                        
                        self.blockerIoReq.set_addr_arr(self,"blockerIoReq")
                        self.blockerIoReq.prepare_object()
                        
                        self.pendingIoReqs.set_addr_arr(self,"blockerIoReq")
                        self.pendingIoReqs.prepare_object()
                        
                        self.prepare_path_info()
                self.xx_dbg("DBG_IoPathMgr::prepare_object::m_out::")
                
        def prepare_path_info(self):
                try:
                        self.xx_dbg("DBG_IoPathMgr::prepare_path_info::in::")
                        self.get_path_info()
                        self.xx_dbg("DBG_IoPathMgr::prepare_path_info::out::")
                except:
                        self.xx_exception("DBG_IoPathMgr::print_object")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_IoPathMgr::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_IoPathMgr::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_obj_valid() == 1 ):                                                        
                        self.m_fields.print_object()                        
                        self.hostIoTarget.print_object()
                        self.ioCoalescer.print_object()
                        self.nvCache.print_object()
                        self.volCache.print_object()
                        self.raidDev.print_object()
                        self.flushSyncInfo.print_object()
                        self.flushIoReq.print_object()
                        self.blockerIoReq.print_object()
                        self.pendingIoReqs.print_object()
                        
                self.xx_dbg("DBG_IoPathMgr::print_object::m_out::")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_IoPathMgr::xx_obj_valid::m_in::")
                i_valid = self.xx_is_object()
                self.xx_dbg("DBG_IoPathMgr::xx_obj_valid::m_out::" + str(i_valid))
                return i_valid
        
        def get_path_info(self):
                try:
                        
                        self.xx_dbg("DBG_IoPathMgr::get_path_info::in::")
                        s_1 = "NONE"
                        host_phy = self.hostIoTarget.xx_get_phy_addr("")
                        s_1 = self.get_obj_name_by_addr(host_phy)
                        
                        self.add_message("hostIoTarget::is:" + s_1)
                        self.add_msg_next(self.hostIoTarget,"hostIoTarget")
                        self.add_msg_next(self.ioCoalescer,"ioCoalescer")
                        self.add_msg_next(self.nvCache,"nvCache")
                        self.add_msg_next(self.volCache,"volCache")
                        self.add_msg_current(self.hostIoTarget,"hostIoTarget")
                        self.xx_dbg("DBG_IoPathMgr::get_path_info::out::")
                except:
                        self.add_message("PATH_ERROR:")

                        
        def add_msg_next(self,p_parent,p_next_name):
                try:
                        
                        self.xx_dbg("DBG_IoPathMgr::get_path_info::in::")
                        
                        s_1 = "NONE"
                        host_phy = p_parent.get_next().xx_get_phy_addr("")
                        s_1 = self.get_obj_name_by_addr( host_phy )
                        
                        self.add_message(p_next_name + "::next_is:" + s_1)
                        
                        self.xx_dbg("DBG_IoPathMgr::get_path_info::out::")
                except:
                        self.add_message("PATH_ERROR:")
                        
        def add_msg_current(self, p_current, p_current_name):
                try:
                        
                        self.xx_dbg("DBG_IoPathMgr::get_path_info::in::")
                        
                        s_1 = "NONE"
                        host_phy = p_current.xx_get_phy_addr("")
                        s_1 = self.get_obj_name_by_addr( host_phy )
                        
                        self.add_message(p_current_name + "::next_is:" + s_1)
                        
                        self.xx_dbg("DBG_IoPathMgr::get_path_info::out::")
                except:
                        self.add_message("PATH_ERROR:")
                                
        def get_obj_name_by_addr(self,tt):
                s_obj = "NONE"
                try:
                        #if( tt == self.hostIoTarget.xx_get_phy_addr("") ):
                        #        s_obj = "hostIoTarget"
                        if( tt == self.ioCoalescer.xx_get_phy_addr("") ):
                                s_obj = "ioCoalescer"
                        if( tt == self.nvCache.xx_get_phy_addr("") ):
                                s_obj = "nvCache"
                        if( tt == self.volCache.xx_get_phy_addr("") ):
                                s_obj = "volCache"
                        if( tt == self.raidDev.xx_get_phy_addr("") ):
                                s_obj = "raidDev"
                        if( tt == self.hostIoTarget.xx_get_phy_addr("") ):
                                s_obj = "hostIoTarget"                                
                        return s_obj
                except:
                        return s_obj + ":EXC"
        
                        