import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. raidism.DBG_CfgRaidDev import *
from .. raidism.DBG_CfgDisk import *
from .. raidism.DBG_CfgDiskList import *
from .. raidism.DBG_CfgRaidDev_PyArray import *
from .. raidism.DBG_CfgArrayList_PyList import *
class DBG_RaidCfgMgr(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_RaidCfgMgr::__init__::in::")
                self.xx_set_class_name ( "RaidCfgMgr" )
                self.xx_set_full_class_name ( "iastora!RaidCfgMgr" )
                
                self.m_cfgraiddevs = DBG_CfgRaidDev_PyArray("Parent::DBG_RaidCfgMgr")
                
                self.m_cfgraiddevs.xx_set_class_name ( "RaidCfgMgr" )
                self.m_cfgraiddevs.xx_set_full_class_name ( "iastora!RaidCfgMgr" )
                
                self.m_selectedDisk = DBG_CfgDisk("Parent::DBG_RaidCfgMgr")
                self.m_arrayList = DBG_CfgArrayList_PyList("Parent::DBG_RaidCfgMgr")
                self.m_fields = DBG_FieldsMapper("DBG_RaidCfgMgr",self)
                
                self.numCfgRaidDevs = 0
                self.m_fields.add_fields_int_array([
                        "initialized"
                        ,"numDisk"
                        ,"numArrays"
                        ,"numCfgRaidDevs"
                        #,"numRaidDevs"
                        ,"createVolFromFreeDisks"
                        ,"inCreateRaidDev"
                        ,"diskActionType"
                        ,"cfgStatus"
                        ,"numBlocksForMigrOpt"
                        ,"rcmConfirm"
                        ,"rcmDiskNum"
                        ,"rcmEnclNum"
                        ,"rcmDomains"
                        ,"rcmArrayNum"
                        ,"rcmRaidLevel"
                        ,"rcmStripKB"
                        ,"rcmDataMB"
                        ,"rcmVolStatus"
                        ,"numMembersPresent"
                        ,"allMembersValid"
                        ,"triggerAction"
                        ,"allMembersUnlocked"                        
                        ])
                
                self.m_fields.add_fields_bool_array([
                        "initialized"                        
                        ])
                                
                self.m_cfgDiskList = DBG_CfgDiskList("DBG_RaidCfgMgr",self)
                
                self.xx_dbg("DBG_RaidCfgMgr::__init__::in::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_RaidCfgMgr::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_RaidCfgMgr::prepare_object_internal::")
                if(self.xx_is_object()==1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.m_selectedDisk.set_addr(self,"selectedDisk")
                        
                        self.m_arrayList.set_addr_arr(self,"arrayList")
                        self.m_arrayList.prepare_object()
                        
                        self.numCfgRaidDevs = self.m_fields.get_fields_int("numCfgRaidDevs")
                        self.m_cfgraiddevs.set_range(self.numCfgRaidDevs)
                        
                        self.m_cfgDiskList.set_addr_arr(self,"cfgDiskList")
                        self.m_cfgDiskList.prepare_object()
                        
                        if(self.numCfgRaidDevs > 0):
                                self.m_cfgraiddevs.set_addr(self,"SELF")
                                self.m_cfgraiddevs.set_parent(self)
                                self.m_cfgraiddevs.prepare_object()
                                
                                
                self.xx_dbg("DBG_RaidCfgMgr::prepare_object_internal::out::")
                
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self,sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,pparent,sdbg=""):

                self.xx_dbg("DBG_RaidCfgMgr::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object()==1):
                        self.m_fields.xx_print_fields("")
                        self.m_arrayList.print_object()
                        self.m_selectedDisk.print_object()
                        self.m_cfgDiskList.print_object()
                        if (self.numCfgRaidDevs > 0):
                                self.m_cfgraiddevs.print_object()
                                                    
                        
                
                self.xx_dbg("DBG_RaidCfgMgr::print_object_internal::out::")                        
                        
                
        def get_class_str(self):
                self.xx_dbg("DBG_RaidCfgMgr::get_class_str::")
                
                ccstr = """
                """
                
                self.xx_dbg("DBG_RaidCfgMgr::get_class_str::")
