import sys
import os

from ... DBG_AdapterBase import *
from ... appcore.config.DBG_PrintConfig import *
#from ... nvme.DBG_AdminIdentifyControllerData import *
from ... fields.DBG_FieldsMapper import *
from ... appsrc.raidtargets.DBG_RaidDiskIdentityData import *
from ... appsrc.raidtargets.DBG_RaidportTarget_ChildPointer import *
from ... appsrc.raidtransport.DBG_EnddeviceTarget_TransportPath_PyPointer import *
from ... appsrc.raidtargets.DBG_InquiryData import *
from ... defs.DBG_TargetIdentifyState import *

class DBG_EndDeviceTarget(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_EndDeviceTarget::__init__::in::")
                self.xx_set_class_name ( "EndDeviceTarget" )
                self.xx_set_full_class_name ( "iastora!EndDeviceTarget" )
                self.m_fields = DBG_FieldsMapper("DBG_EndDeviceTarget", self)                                
                self.mDiskIdentityData = DBG_RaidDiskIdentityData("Parent::DBG_EndDeviceTarget")
                self.init_value_fields()
                self.mRaidportTarget = DBG_RaidportTarget_ChildPointer("Parent::DBG_EndDeviceTarget")
                self.mPath = DBG_EnddeviceTarget_TransportPath_PyPointer("Parent::DBG_EndDeviceTarget",self)
                self.mInquiryData  = DBG_InquiryData("Parent::DBG_EndDeviceTarget",self)
                self.xx_dbg("DBG_EndDeviceTarget::__init__::in::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_EndDeviceTarget::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_EndDeviceTarget::prepare_object::")
                
                if(self.is_valid_object() == 1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.mDiskIdentityData.set_addr_arr(self,"mDiskIdentityData")
                        
                        self.mRaidportTarget.set_addr(self,"mRaidportTarget")
                        self.mRaidportTarget.prepare_object()
                        
                        self.mPath.set_addr(self,"mPath")
                        self.mPath.prepare_object()
                        
                        self.init_mapped_fields()
                        
                        self.mInquiryData.set_addr_arr(self,"mInquiryData")
                        self.mInquiryData.prepare_object()
                                                
                self.xx_dbg("DBG_EndDeviceTarget::prepare_object::out::")
                
        def init_mapped_fields(self):
                
                try:
                        sstate = self.m_fields.get_fields_string("mIdentifyState")                        
                        if(sstate != ""):
                                state = int(sstate)
                                xst = DBG_TargetIdentifyState("").get_str(state)
                                self.m_fields.add_raw_str("mIdentifyState:" + xst)
                        
                except:
                        self.xx_exception("DBG_EndDeviceTarget::init_mapped_fields")
                
        def init_value_fields_test(self):
                try:
                        self.m_fields.add_fields_asstr_ints([
                                                            "mIdentifyState"
                                                            ])
                        
                except:
                        self.xx_exception("DBG_EndDeviceTarget::print_object")

        def init_value_fields(self):
                try:
                        self.xx_dbg("DBG_EndDeviceTarget::init_value_fields::in::")
                        self.m_fields.add_fields_int_array(["mPathId","mTargetId","mLun"])
                        self.m_fields.add_fields_asstr_int("mTransportTargetState")
                        self.m_fields.add_fields_asstr_int("mSasAddress")
                        self.m_fields.add_fields_asstr_int("mDeviceType")
                        self.m_fields.add_fields_asstr_int("mIsDiskClaimable")
                        self.m_fields.add_fields_asstr_ints(["mRequestsToComplete"
                                                            ,"mPausedPathId"
                                                            ,"mPausedTargetId"                                                            
                                                            ,"mPuisStandby"
                                                            ,"mPuisEnabled"
                                                            ,"mPuisSupported"
                                                            ,"mSpinupDisk"
                                                            ,"mIdentifyState"
                                                            ,"mQueueDepth"
                                                            ,"mIsInReset"
                                                            ])
                        if(DBG_PrintConfig().getItem().m_is_handled_lun == 1):
                                self.m_fields.add_fields_asstr_ints(["mPausedLun"])
                                
                        self.xx_dbg("DBG_EndDeviceTarget::init_value_fields::end_method::")
                except:
                        self.xx_exception("DBG_EndDeviceTarget::print_object")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_EndDeviceTarget::print_object")
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_EndDeviceTarget::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.is_valid_object() == 1):
                        self.m_fields.xx_print_fields("")
                        self.mDiskIdentityData.print_object()                
                        self.mRaidportTarget.print_object()
                        self.mPath.print_object()
                        self.mInquiryData.print_object()
                self.xx_dbg("DBG_EndDeviceTarget::print_object_internal::out::")
                
        def is_valid_object(self):
                self.xx_dbg("DBG_EndDeviceTarget::is_valid_object::in")        
                is_c = 1
                if(is_c == 1):
                        is_c = self.xx_check_int(self,"mTargetId")
                        
                if(is_c == 1):
                        is_c = self.xx_is_object()
                self.xx_dbg("DBG_EndDeviceTarget::is_valid_object::out::" + str(is_c))        
                return is_c
                        
        def is_raidtarget_attached(self):
                self.xx_dbg("DBG_EndDeviceTarget::is_raidtarget_attached::in::")
                is_c = 1
                if(is_c == 1):                
                        is_c = self.xx_check_int(self,"mTargetId")
                if(is_c == 1):
                        is_c = self.xx_is_object()
                        
                if(is_c == 1):
                        is_c = self.mRaidportTarget.is_valid_object()
                        
                self.xx_dbg("DBG_EndDeviceTarget::is_raidtarget_attached::out::" + str(is_c))
                
                return is_c

                
        def get_class_str(self):
                self.xx_dbg("DBG_EndDeviceTarget::get_class_str::")
                
                ccstr = """
"""
                self.xx_dbg("DBG_EndDeviceTarget::get_class_str::")
