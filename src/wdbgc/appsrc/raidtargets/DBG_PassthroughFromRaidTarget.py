import sys
import os
import logging
from ... DBG_AdapterBase import *
from ... appcore.memory.DBG_MemoryTools import *
#from DBG_Target import *
from ... fields.DBG_FieldsMapper import *
from ... appsrc.raidtargets.DBG_RaidDiskIdentityData import * 
from ... appsrc.raidtargets.DBG_EndDeviceTarget import *

class DBG_PassthroughFromRaidTarget(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_PassthroughFromRaidTarget::__init__::in::")
                self.xx_set_class_name ( "PassthroughFromRaidTarget" )
                self.xx_set_full_class_name ( "iastora!PassthroughFromRaidTarget" )
                self.mDiskIdentityData = DBG_RaidDiskIdentityData("Parent::DBG_PassthroughFromRaidTarget")
                self.mEndDeviceTarget = DBG_EndDeviceTarget("Parent:DBG_PassthroughFromRaidTarget")
                self.m_fields = DBG_FieldsMapper("DBG_PassthroughFromRaidTarget",self)
                
                self.m_fields.add_fields_str("mVolumeId",8)
                #self.m_target = DBG_Target("FROM::DBG_PassthroughFromRaidTarget")
                self.xx_dbg("DBG_PassthroughFromRaidTarget::__init__::out::")
               
        
        def prepare_object(self):
                self.xx_dbg("DBG_PassthroughFromRaidTarget::prepare_object::in::")
                if(self.xx_is_object()==1):
                        self.m_fields.initialize_by_parent(self)
                        self.mDiskIdentityData.set_addr_arr(self,"mDiskIdentityData")
                        self.mEndDeviceTarget.set_addr(self,"mEndDeviceTarget")
                #self.m_target.xx_inc_tabs(self);                
                #self.m_target.xx_compute_arr_phy_by_parent(self,"mTarget")
                self.xx_dbg("DBG_PassthroughFromRaidTarget::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_PassthroughFromRaidTarget::print_object::in::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):
                        self.m_fields.print_object()
                        self.mDiskIdentityData.print_object()
                        self.mEndDeviceTarget.print_object()
                        
                #self.xx_print_ints()
                #self.m_target.print_object()
                self.xx_dbg("DBG_PassthroughFromRaidTarget::print_object::out::")
                
        def xx_print_ints(self):
                self.xx_dbg("DBG_PassthroughFromRaidTarget::xx_print_ints::in::")
                ints = ["mIsSystemDevice"]                
                self.xx_dbg("DBG_PassthroughFromRaidTarget::xx_print_ints::out::")