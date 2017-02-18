import sys
import os
import logging
from ... DBG_AdapterBase import *
from ... appcore.memory.DBG_MemoryTools import *
from ... fields.DBG_FieldsMapper import *
from ... defs.DBG_RaidTargetMap import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.raidtargets.DBG_PassthroughTarget import *
from ... appsrc.raidtargets.DBG_PassthroughFromRaidTarget  import *
from ... appsrc.raidtargets.DBG_RaidTarget import *
from ... appsrc.raidtargets.DBG_RaidportTarget import *

class DBG_RaidportTarget_PyManager(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_RaidportTarget_PyManager::__init__::in::")
                self.xx_set_class_name ( "RaidportTarget" )
                self.xx_set_full_class_name ( "iastora!RaidportTarget" )
                self.m_fields = DBG_FieldsMapper("DBG_raiddev"
                                         ,self)
                
                self.m_fields.add_fields_int("mIsSystemDevice")
                self.m_fields.add_fields_int("mType")
                
                self.m_fields.add_fields_int("mPathId")
                self.m_fields.add_fields_int("mTargetId")
                self.m_fields.add_fields_int("mLun")
                
                self.mIsSystemDevice = 0
                self.mType = 1
                self.mPathId = 0
                self.mTargetId = 0
                self.mLun = 0
                
                self.m_pass_target = DBG_PassthroughTarget("Parent:DBG_RaidportTarget_PyManager")
                self.m_raid_target = DBG_RaidTarget("Parent:DBG_RaidportTarget_PyManager")
                self.m_pass_from_raid_target = DBG_PassthroughFromRaidTarget("Parent:DBG_RaidportTarget_PyManager")
                self.m_raidport_target = DBG_RaidportTarget("Parent:DBG_RaidportTarget_PyManager", self)
                self.xx_dbg("DBG_RaidportTarget_PyManager::__init__::out::")
                       
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_RaidportTarget_PyManager::prepare_object::in::")
                        if(self.prepare_check() == 1):
                                self.xx_dbg("prepare_check::prepared_out::")
                                return
                        
                        if(self.xx_is_object() == 0):
                                return
                        
                        self.clear_messages()                
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.mIsSystemDevice = self.m_fields.get_fields_int("mIsSystemDevice")
                        self.mType = self.m_fields.get_fields_int("mType")
                        self.mPathId = self.m_fields.get_fields_int("mPathId")
                        self.mTargetId = self.m_fields.get_fields_int("mTargetId")
                        self.mLun = self.m_fields.get_fields_int("mLun")
                        
                        self.m_raidport_target.set_addr(self,"SELF")
                        self.m_raidport_target.prepare_object()
                        
                        
                        if(self.mType == 0 ):
                                self.xx_dbg("DBG_RaidportTarget_PyManager::prepare_object::self::")
                                self.m_pass_target.set_addr(self,"SELF")
                                self.m_pass_target.prepare_object()
                                #self.mEndDeviceTarget.set_addr_arr(self,"mEndDeviceTarget")

                        if(self.mType == 2):
                                self.xx_dbg("DBG_RaidportTarget_PyManager::prepare_object::self::")
                                self.m_raid_target.set_addr(self,"SELF")
                                self.m_raid_target.prepare_object()
                                
                        if(self.mType == 4):
                                self.xx_dbg("DBG_RaidportTarget_PyManager::prepare_object::self::")                                
                                self.m_pass_from_raid_target.set_addr(self,"SELF")
                                self.m_raid_target.prepare_object()
                                
                        self.xx_dbg("DBG_RaidportTarget_PyManager::prepare_object::out::")
                except:
                        self.xx_exception("DBG_RaidportTarget_PyManager::prepare_object")
                
        def print_object(self):
                try:
                        self.prepare_object()
                        show_all = DBG_PrintConfig().getItem().m_print_all_targets
                        
                                
                        if((self.mIsSystemDevice == 1) or (show_all==1) or ( self.mType != 1 )):                                                        
                                self.xx_print_start("")
                                self.print_object_internal()
                                self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def raidport_target_is_used(self):
                try:                        
                        is_used = 0        
                        if((self.mIsSystemDevice == 1) or ( self.mType != 1 )):
                                is_used = 1
                                
                        return is_used                                
                except:
                        self.xx_exception("DBG_RaidportTarget_PyManager::raidport_target_is_used")
                        
        def print_object_internal(self):
                try:
                        self.xx_dbg("DBG_RaidportTarget_PyManager::print_object::in::")                        
                        self.prepare_object()
                        show_all = DBG_PrintConfig().getItem().m_print_all_targets
                        
                                
                        if((self.mIsSystemDevice == 1) or (show_all==1) or ( self.mType != 1 )):                                
                                self.xx_print_ptr("")
                                self.m_fields.add_raw_str( "Type:" + DBG_RaidTargetMap("").get_str(self.mType))
                                self.m_fields.print_object()
                                self.m_raidport_target.print_object()
                                if(self.mType == 0 ):
                                        self.m_pass_target.print_object()
                                        
                                if(self.mType == 2):
                                        self.m_raid_target.print_object()

                                if(self.mType == 4):
                                        self.m_pass_from_raid_target.print_object()
                                        
                        self.xx_dbg("DBG_RaidportTarget_PyManager::print_object::out::")
                except:
                        self.xx_exception("DBG_RaidportTarget_PyManager::print_object")
                        
        def print_object_header(self):
                try:
                        self.xx_dbg("DBG_RaidportTarget_PyManager::print_object::in::")
                        self.prepare_object()
                        self.xx_print_start("")
                        self.xx_print_ptr("")
                        self.xx_print_end("")
                        self.xx_dbg("DBG_RaidportTarget_PyManager::print_object::out::")
                except:
                        self.xx_exception("DBG_RaidportTarget_PyManager::print_object")
                        
                