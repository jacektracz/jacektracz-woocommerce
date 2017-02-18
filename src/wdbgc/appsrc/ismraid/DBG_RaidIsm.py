
import sys
import os


from ... DBG_AdapterBase import *
from ... appcore.memory.DBG_MemoryTools import *
from ... appcore.config.DBG_PrintConfig import *
from ... ports.DBG_PortConfigurationInformation import *
#from ... raidport.DBG_Raiddevs import * 

from ... fields.DBG_FieldsMapper import *
from ... raidism.DBG_RaidIsmInitParams import *
from ... raidism.DBG_RaidIsmDiskTable import *
from ... raidism.DBG_RaidCfgMgr import *
from ... raidism.DBG_RaidMpbMgr import *
from ... raidism.DBG_IsmPathTargetLun import *
from ... appsrc.ismcache.DBG_CacheMgr import *
from ... appsrc.ismcache.DBG_CoalMgr import *
from ... appsrc.ismcache.DBG_NvCacheMgr import *
from ... appsrc.ismcache.DBG_MemoryMgr import *
from ... appsrc.ismevents.DBG_EventQueue import *
from ... appsrc.ismpools.DBG_CkptMgrPool import *
from ... appsrc.ismraid.DBG_RaidDev_PyArray import *
#@F
class DBG_RaidIsm(DBG_AdapterBase):

    def __init__(self,spar):                
        DBG_AdapterBase.__init__(self,spar)
        self.xx_dbg("DBG_RaidIsm::__init__::in::")
        self.xx_set_class_name( "RaidIsm" )
        self.xx_set_full_class_name ( "iastora!RaidIsm" )
        self.xx_set_tabs(1,"DBG_RaidIsm")
        self.m_port_conf = DBG_PortConfigurationInformation("FROM::DBG_RaidIsm")
        self.numRaidDevs = 0
        #self.m_raiddevs = DBG_RaidDevs("Parent::DBG_RaidIsm",self)
        self.m_initParams = DBG_RaidIsmInitParams("Parent::DBG_RaidIsm")
        self.m_diskTable = DBG_RaidIsmDiskTable("Parent::DBG_RaidIsm")
        self.m_cfgMgr = DBG_RaidCfgMgr("Parent::DBG_RaidIsm")
        self.m_mpbMgr = DBG_RaidMpbMgr("Parent::DBG_RaidIsm",self)
        self.m_cacheMgr = DBG_CacheMgr("Parent::DBG_RaidIsm",self)
        self.m_nvCacheMgr = DBG_NvCacheMgr("Parent::DBG_RaidIsm",self)
        self.m_coalMgr = DBG_CoalMgr("Parent::DBG_RaidIsm",self)
        self.m_memoryMgr = DBG_MemoryMgr("Parent::DBG_RaidIsm",self)
        self.m_fields = DBG_FieldsMapper("DBG_RaidIsm",self)
        self.mEventQueue = DBG_EventQueue("DBG_RaidIsm",self)
        
        self.m_systemDevicePtl = DBG_IsmPathTargetLun("Parent::DBG_RaidIsm")
        self.freeCkptMgrPool = DBG_CkptMgrPool("Parent::DBG_CkptMgrPool",self)
        
        self.raiddevs = DBG_RaidDev_PyArray("DBG_RaidMpbTbl",self)
        self.raiddevs.set_parent_names("RaidIsm")
        self.raiddevs.set_selectors("raidDevs ","numRaidDevs ")
        self.raiddevs.init_object_fields()
        
        #@I
        self.prepare_object_fields()
        self.xx_dbg("DBG_RaidIsm::__init__::out::")
        
    def prepare_object(self):
        try:
            self.prepare_object_internal(self)
        except:
            self.xx_exception("DBG_RaidIsmDisk::print_object")
            
    def prepare_object_fields(self):
        """
        """
        self.m_fields.add_fields_int("numScsiAdapters")
        self.m_fields.add_fields_int("numRaidDevs")
        
        self.m_fields.add_fields_asstr_addrs(["numScsiAdapters"
                                              ,"pCachedMemEnd"
                                              ,"pFreeNonCachedMem"
                                              ,"pNonCachedMemEnd"])
        
        self.m_fields.add_fields_asstr_ints(["cachedMemUsed"
                                              ,"nonCachedMemUsed"
                                              ,"nonCachedAlignWaste"
                                              ,"cacheSizeInKB"
                                              ,"disableAllDiskWrites"
                                              ,"neverSpinDownHdd"
                                              ,"sioReqStatus"
                                              ,"sioDetStatus"
                                              ,"numScsiAdapters"
                                              ,"numRaid0Reqs"
                                              ,"numRaid5Reqs"
                                              ,"numRaidDgReqs"
                                              ,"numReserved3050Mdrs"
                                              #,""                                              
                                              ])
        
    def prepare_object_internal(self, pparent):
        self.xx_dbg("DBG_RaidIsm::prepare_object_internal::in::")
        
        if(self.xx_obj_valid() == 1):
            self.m_fields.initialize_by_parent(self)
            
            self.m_port_conf.xx_inc_tabs(self);
            #self.m_port_conf.xx_compute_arr_phy_by_parent(self,"mPortConfiguration")
    
            self.m_initParams.xx_inc_tabs(self);
            self.m_initParams.xx_compute_arr_phy_by_parent(self,"initParms")
            
            self.m_mpbMgr.set_addr(self,"mpbMgr");
    
            self.m_cfgMgr.xx_inc_tabs(self);
            self.m_cfgMgr.xx_compute_phy_by_parent(self,"cfgMgr")
    
            self.m_diskTable.xx_inc_tabs(self);
            self.m_diskTable.xx_compute_arr_phy_by_parent(self,"diskTable")
            #self.m_diskTable.set_parent(self.m_initParams)
            self.m_diskTable.prepare_object()
    
            #self.numRaidDevs = DBG_MemoryTools().xx_get_int(self,"numRaidDevs")        
            #self.m_raiddevs.xx_inc_tabs(self);                 
            #self.m_raiddevs.prepare_object()
            
            self.m_cacheMgr.set_addr(self,"cacheMgr")
            self.m_cacheMgr.prepare_object()
            
            self.m_nvCacheMgr.set_addr(self,"nvCacheMgr")
            self.m_nvCacheMgr.prepare_object()
            
            self.m_coalMgr.set_addr(self,"coalMgr")
            self.m_coalMgr.prepare_object()
            
            self.m_memoryMgr.set_addr(self,"memoryMgr")
            self.m_memoryMgr.prepare_object()
            
            if(DBG_PrintConfig().getItem().get_system_target() == 1):                        
                self.m_systemDevicePtl.set_addr_arr(self,"m_systemDevicePtl")
                
            self.mEventQueue.set_addr_arr(self,"mEventQueue")
            self.mEventQueue.prepare_object()
            self.freeCkptMgrPool.set_addr(self,"freeCkptMgrPool")
            self.freeCkptMgrPool.prepare_object()
            
            self.raiddevs.set_addr(self,"SELF")
            self.raiddevs.prepare_object(self)
            
            #@P
        self.xx_dbg("DBG_RaidIsm::prepare_object_internal::out::")
        
    def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self,sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
    def print_object_internal(self,pparent,sdbg=""):

        self.xx_dbg("DBG_RaidIsm::print_object_internal::in::")
        self.prepare_object()
        self.xx_print_ptr("")
        if(self.xx_obj_valid() == 1):
            self.m_fields.xx_print_fields("")
            if(DBG_PrintConfig().getItem().get_system_target() == 1):
                self.m_systemDevicePtl.print_object()
            
            #self.m_port_conf.print_object()
            #self.m_raiddevs.print_object()
            self.m_initParams.print_object()
            self.m_diskTable.print_object()
            self.m_cfgMgr.print_object()
            self.m_mpbMgr.print_object()
            self.m_cacheMgr.print_object()
            self.m_nvCacheMgr.print_object()
            self.m_coalMgr.print_object()
            self.m_memoryMgr.print_object()
            self.mEventQueue.print_object()
            self.freeCkptMgrPool.print_object()
            self.raiddevs.print_object()
            
            #@R
        self.xx_dbg("DBG_RaidIsm::print_object_internal::in::")

    
    def xx_obj_valid(self):
        
            self.xx_dbg("DBG_RaidIsm::xx_obj_valid::m_in::")
            
            i_valid = 1
            if(i_valid == 1):
                if(self.xx_is_object() != 1):
                    i_valid = 0
                    
            if(i_valid == 1):
                if(self.xx_check_int(self,"numRaidDevs")!= 1):
                    i_valid = 0
                
            self.xx_dbg("DBG_RaidIsm::xx_obj_valid::m_out::" + str(i_valid))
            return i_valid
    
    def get_class_str(self):
        ccs = """        
        """
        
        return ccs