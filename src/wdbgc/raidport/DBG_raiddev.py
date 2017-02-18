import sys
import os
import logging

from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. raidism.DBG_CfgRaidDev_PyPtr import *
#from .. raidport.DBG_RaidCfgArray import *
from .. raidport.DBG_RaidArraySemReq import *
from .. raidport.DBG_RaidAoacInfo import *
from .. appsrc.raidtargets.DBG_RaidDiskIdentityData import *
from .. raidport.DBG_RaidPuisState import *
from .. raidport.DBG_RaidReqList import *
from .. raidport.DBG_RaidVol import *
from .. raidism.DBG_CfgRaidVol import *
from .. fields.DBG_FieldsMapper import *
from .. raidism.DBG_IsmPathTargetLun import *
from .. appsrc.ismcfg.DBG_IoPathMgr import *

class DBG_raiddev(DBG_AdapterBase):
    
    def __init__(self, spar):
        DBG_AdapterBase.__init__(self,spar)
        self.xx_dbg("DBG_raiddev::__init__:method_in::")
        self.xx_set_class_name( "RaidDev" )
        self.xx_set_full_class_name ( "iastora!RaidDev" )
        
        self.m_diskid = DBG_RaidDiskIdentityData("Parent::DBG_raiddev")
        self.m_cfgRaidDev = DBG_CfgRaidDev_PyPtr("Parent::DBG_raiddev")
        self.m_fields = DBG_FieldsMapper("DBG_raiddev",self)
        
        self.m_fields.add_fields_str("serialNo",16)
        self.m_fields.add_fields_int_array(["raidDevNum"])
        self.m_ismPTL = DBG_IsmPathTargetLun("Parent::DBG_raiddev")
        self.m_raidVol = DBG_RaidVol("Parent::DBG_raiddev")
        self.ioPathMgr = DBG_IoPathMgr("Parent::DBG_raiddev",self)
        self.xx_dbg("DBG_raiddev::__init__:method_out::")
        
    def prepare_object(self):
        
        self.xx_dbg("DBG_raiddev::prepare_object:method_in::")
        
        if(self.xx_is_object()==1):
            
            self.m_diskid.set_addr_arr(self,"idData")
            self.m_diskid.prepare_object()    
            
            self.m_cfgRaidDev.set_addr(self,"cfgRaidDev")
            self.m_cfgRaidDev.prepare_object()
            
            self.m_raidVol.set_addr(self,"raidVol")
            self.m_raidVol.prepare_object()
            
            self.m_ismPTL.set_addr_arr(self,"ismPTL")
            self.m_ismPTL.prepare_object()
                        
            self.ioPathMgr.set_addr(self,"ioPathMgr")
            self.ioPathMgr.prepare_object()
            
            self.m_fields.initialize_by_parent(self)
            
        self.xx_dbg("DBG_raiddev::prepare_object:method_out::")
        
    def print_object(self,sdbg=""):
            try:
                    self.xx_print_start("")
                    self.print_object_internal(sdbg)
                    self.xx_print_end("")
            except:
                    self.xx_exception("::print_object")
                    
    def print_object_internal(self,sdbg=""):
        self.xx_dbg("DBG_raiddev::print_object:method_in::")
        self.prepare_object()
        self.xx_print_ptr("")
        
        if(self.xx_is_object()==1):
            self.m_fields.print_object()
            self.m_ismPTL.print_object()            
            self.m_diskid.print_object()            
            self.m_cfgRaidDev.print_object()
            self.m_raidVol.print_object()
            self.ioPathMgr.print_object()
            
        self.xx_dbg("DBG_raiddev::print_object:method_out::")