import sys
import os
import logging
from ... DBG_AdapterBase import *
from ... appcore.memory.DBG_MemoryTools import *
from ... fields.DBG_FieldsMapper import *
#from DBG_Target import *

from ... appsrc.raidtargets.DBG_RaidDiskIdentityData import * 
from ... appsrc.raidtargets.DBG_EndDeviceTarget import *
from ... raidport.DBG_raiddev import *
from ... appcore.config.DBG_PrintConfig import *

class DBG_RaidTarget(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_RaidTarget::__init__::in::")
                self.xx_set_class_name ( "RaidTarget" )
                self.xx_set_full_class_name ( "iastora!RaidTarget" )
                self.mDiskIdentityData = DBG_RaidDiskIdentityData("Parent::DBG_RaidTarget")
                self.mOriginalPassthroughDisk = DBG_EndDeviceTarget("Parent:DBG_RaidTarget")
                self.m_mRaidDev = DBG_raiddev("Parent:DBG_RaidTarget")
                self.m_fields = DBG_FieldsMapper("DBG_raiddev", self)
                
                self.m_fields.add_fields_asstr_ints([
                        "mPathId"
                        ,"mTargetId"                                                
                        ,"mIsSystemDevice"])
                
                if(DBG_PrintConfig().getItem().m_is_handled_lun == 1):
                        self.m_fields.add_fields_asstr_ints([
                                "mLun"])
                        
                if(DBG_PrintConfig().getItem().m_is_handled_d3 == 1):
                        self.m_fields.add_fields_asstr_ints([
                                "mD3ColdAllowed"])
                        
                self.xx_dbg("DBG_RaidTarget::__init__::out::")               
        
        def prepare_object(self):
                self.xx_dbg("DBG_RaidTarget::prepare_object::in::")
                if(self.prepare_check() == 1):
                        self.xx_dbg("prepare_check::prepared_out::")
                        return
                
                if(self.xx_is_object()==1):
                        self.m_fields.initialize_by_parent(self)
                        self.mDiskIdentityData.set_addr_arr(self,"mDiskIdentityData")
                        self.mOriginalPassthroughDisk.set_addr(self,"mOriginalPassthroughDisk")
                        self.m_mRaidDev.set_addr(self,"mRaidDev")
                #self.m_target.xx_inc_tabs(self);                
                #self.m_target.xx_compute_arr_phy_by_parent(self,"mTarget")
                self.xx_dbg("DBG_RaidTarget::prepare_object::out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self):
                self.xx_dbg("DBG_RaidTarget::print_object::in::")                
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):
                        self.m_fields.print_object()
                        self.mDiskIdentityData.print_object()
                        self.mOriginalPassthroughDisk.print_object()
                        self.m_mRaidDev.print_object()                
                self.xx_dbg("DBG_RaidTarget::print_object::out::")
                
