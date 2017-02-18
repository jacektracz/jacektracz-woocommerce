import sys
import os
import logging
from ... DBG_AdapterBase import *
from ... appcore.memory.DBG_MemoryTools import *
from ... fields.DBG_FieldsMapper import *
from ... appsrc.raidtargets.DBG_RaidDiskIdentityData import * 
from ... appsrc.raidtargets.DBG_EndDeviceTarget import *
from ... appcore.config.DBG_PrintConfig import *

class DBG_RaidportTarget(DBG_AdapterBase):
        def __init__(self,spar,pparent):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_RaidportTarget::__init__::in::")
                self.xx_set_class_name ( "RaidportTarget" )
                self.xx_set_full_class_name ( "iastora!RaidportTarget" )
                self.m_fields = DBG_FieldsMapper("DBG_RaidportTarget",self)
                
                self.m_fields.add_fields_asstr_ints(["mPathId"
                                                     ,"mTargetId"
                                                     ,"mQueueDepth"
                                                     ,"mType"
                                                     ,"mBitLockerWbDisableCount"
                                                     ,"mIsSystemDevice"])
                if(DBG_PrintConfig().getItem().m_is_handled_lun == 1):
                        self.m_fields.add_fields_asstr_ints([
                                "mLun"])
                
                self.xx_dbg("DBG_RaidportTarget::__init__::out::")
               
        
        def prepare_object(self):
                self.xx_dbg("DBG_RaidportTarget::prepare_object::in::")
                if(self.xx_is_object()==1):
                        self.m_fields.initialize_by_parent(self)
                self.xx_dbg("DBG_RaidportTarget::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_RaidportTarget::print_object::in::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):
                        self.m_fields.print_object()
                        
                self.xx_dbg("DBG_RaidportTarget::print_object::out::")
                
        def xx_print_ints(self):
                self.xx_dbg("DBG_RaidportTarget::xx_print_ints::in::")
                #ints = ["mIsSystemDevice"]                
                self.xx_dbg("DBG_RaidportTarget::xx_print_ints::out::")