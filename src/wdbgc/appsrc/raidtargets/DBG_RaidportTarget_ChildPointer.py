import sys
import os
import logging
from ... DBG_AdapterBase import *
from ... appcore.memory.DBG_MemoryTools import *
from ... fields.DBG_FieldsMapper import *
from ... defs.DBG_RaidTargetMap import *
from ... appcore.config.DBG_PrintConfig import *

class DBG_RaidportTarget_ChildPointer(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_RaidportTarget_ChildPointer::__init__::in::")
                self.xx_set_class_name ( "RaidportTarget" )
                self.xx_set_full_class_name ( "iastora!RaidportTarget" )
                self.m_fields = DBG_FieldsMapper("DBG_raiddev"
                                         ,self)
                
                self.m_fields.add_fields_int("mIsSystemDevice")
                self.m_fields.add_fields_int("mType")
                #self.m_fields.add_fields_int_array(["mPathId","mtargetId","mLunId"])
                self.m_fields.add_fields_int("mPathId")
                self.m_fields.add_fields_int("mTargetId")
                self.m_fields.add_fields_int("mLun")
                
                self.mIsSystemDevice = 0
                self.mType = 1
                self.mPathId = 0
                self.mTargetId = 0
                self.mLun = 0
                #self.mEndDeviceTarget = DBG_EndDeviceTarget("Parent:DBG_RaidportTarget_ChildPointer")
                #self.m_target = DBG_Target("FROM::DBG_RaidportTarget_ChildPointer")
                self.xx_dbg("DBG_RaidportTarget_ChildPointer::__init__::out::")
                       
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_RaidportTarget_ChildPointer::prepare_object::in::")
                        if(self.xx_is_object() == 0):
                                return
                        self.m_fields.initialize_by_parent(self)
                        self.mIsSystemDevice = self.m_fields.get_fields_int("mIsSystemDevice")
                        self.mType = self.m_fields.get_fields_int("mType")
                        self.mPathId = self.m_fields.get_fields_int("mPathId")
                        self.mTargetId = self.m_fields.get_fields_int("mTargetId")
                        self.mLun = self.m_fields.get_fields_int("mLun")
                        
                        self.xx_dbg("DBG_RaidportTarget_ChildPointer::prepare_object::out::")
                except:
                        self.xx_exception("DBG_RaidportTarget_ChildPointer::prepare_object")
                
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
                        self.xx_exception("DBG_RaidportTarget_ChildPointer::raidport_target_is_used")
                        
        def print_object_internal(self):
                try:
                        self.xx_dbg("DBG_RaidportTarget_ChildPointer::print_object::in::")                        
                        self.prepare_object()
                        show_all = DBG_PrintConfig().getItem().m_print_all_targets
                        
                        #if( self.mPathId == 0 and self.mTargetId == 0 and self.mLun == 0):
                        #        show_all = 1
                        #        show_all = 0
                                
                        if((self.mIsSystemDevice == 1) or (show_all==1) or ( self.mType != 1 )):                                
                                self.xx_print_ptr("")
                                self.m_fields.add_raw_str( "Type:" + DBG_RaidTargetMap("").get_str(self.mType))
                                self.m_fields.print_object()
                                
                        self.xx_dbg("DBG_RaidportTarget_ChildPointer::print_object::out::")
                except:
                        self.xx_exception("DBG_RaidportTarget_ChildPointer::print_object")
                        
        def print_object_header(self):
                try:
                        self.xx_dbg("DBG_RaidportTarget_ChildPointer::print_object::in::")
                        self.prepare_object()
                        self.xx_print_start("")
                        self.xx_print_ptr("")
                        self.xx_print_end("")
                        self.xx_dbg("DBG_RaidportTarget_ChildPointer::print_object::out::")
                except:
                        self.xx_exception("DBG_RaidportTarget_ChildPointer::print_object")
                        
        def is_valid_object(self):
                is_valid = DBG_RaidTargetMap("").is_valid(self.mType)
                return is_valid