import sys
import os

from ... DBG_AdapterBase import *
from ... appsrc.raidtargets.DBG_RaidDiskIdentityData import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
#from ... appsrc.raidtargets.DBG_EndDeviceTarget_PyArray import *
from ... appsrc.raidtransport.DBG_FastList_TransportRequest import *

#from ... appsrc.raidtargets.DBG_TransportTarget import *

class DBG_EnddeviceTarget_TransportPath_PyPointer(DBG_AdapterBase):
        def __init__(self, spar, pparent):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_EnddeviceTarget_TransportPath_PyPointer::__init__::in::")
                self.xx_set_class_name ( "TransportPath" )
                self.xx_set_full_class_name ( "iastora!TransportPath" )
                
                #self.m_diskid = DBG_RaidDiskIdentityData("Parent::DBG_EnddeviceTarget_TransportPath_PyPointer")
                #self.m_diskid.set_use_object(0)
                self.m_fields = DBG_FieldsMapper("DBG_EnddeviceTarget_TransportPath_PyPointer",self)
                                
                #self.mIoQueue = DBG_FastList_TransportRequest("DBG_EnddeviceTarget_TransportPath_PyPointer",self)
                #self.mRetryQueue  = DBG_FastList_TransportRequest("DBG_EnddeviceTarget_TransportPath_PyPointer",self)
                #self.mDispatchedIoList  = DBG_FastList_TransportRequest("DBG_EnddeviceTarget_TransportPath_PyPointer",self)
                
                self.init_object_fields()
                #self.m_devices = DBG_EndDeviceTarget_PyArray("Parent::DBG_EnddeviceTarget_TransportPath_PyPointer",self)
                self.xx_dbg("DBG_EnddeviceTarget_TransportPath_PyPointer::__init__::in::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_EnddeviceTarget_TransportPath_PyPointer::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_EnddeviceTarget_TransportPath_PyPointer::prepare_object::")
                
                if(self.is_valid_object()==1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        #i_num_targets = self.m_fields.get_fields_int("mNumTargets")
                        #self.m_diskid.xx_inc_tabs(self)
                        #self.m_diskid.xx_compute_arr_phy_by_parent(self,"mOldDiskIdentityData")
                                                
                        #self.mIoQueue.set_addr_arr(self,"mIoQueue")
                        #self.mIoQueue.prepare_object()                        
                        
                        #self.mRetryQueue.set_addr_arr(self,"mRetryQueue")
                        #self.mRetryQueue.prepare_object()                        
                        
                        #self.mDispatchedIoList.set_addr_arr(self,"mDispatchedIoList")
                        #self.mDispatchedIoList.prepare_object()
                        
                self.xx_dbg("DBG_EnddeviceTarget_TransportPath_PyPointer::prepare_object::out::")
                
        def print_object(self):
                try:
                        self.xx_print_start()
                        self.print_object_internal(self)
                        self.xx_print_end()
                except:
                        self.xx_exception("DBG_EnddeviceTarget_TransportPath_PyPointer::print_object")
                        
        def init_object_fields(self):
                try:
                        self.xx_dbg("DBG_EnddeviceTarget_TransportPath_PyPointer::init_object_fields::in::")
                        sver = DBG_PrintConfig().getItem().get_version()                        
                        
                        self.m_fields.add_fields_int_array(
                                [
                                "mPathId"
                                ,"mCurrentTargetId"                                        
                                ,"mNumTargets"                                
                                ])
                        if(DBG_PrintConfig().getItem().m_is_handled_lun == 1):
                                self.m_fields.add_fields_int_array(                                
                                [
                                "mCurrentLun"                                 
                                ,"mCurrentLunIndex"                                
                                ,"mNumLuns"
                                ,"mReportedLunsCount"
                                ])                        
                except:
                        self.xx_exception("DBG_EnddeviceTarget_TransportPath_PyPointer::print_object")
                
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_EnddeviceTarget_TransportPath_PyPointer::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                
                if(self.is_valid_object()==1):
                        self.m_fields.xx_print_fields("")                        
                        #self.m_diskid.print_object()
                        #self.m_devices.print_object()
                        #self.mIoQueue.print_object()
                        #self.mRetryQueue.print_object()
                        #self.mDispatchedIoList.print_object()
                        self.add_message_global("path_is_valid:" + self.xx_get_full_path())
                        #if(self.m_diskid.get_use_object() == 1):
                else:
                        self.add_message_global("path_is_not_valid:" +  self.xx_get_full_path())
                self.xx_dbg("DBG_EnddeviceTarget_TransportPath_PyPointer::print_object_internal::out::")                        
                        

        def is_valid_object(self):
                self.xx_dbg("DBG_EndDeviceTarget::is_raidtarget_attached::in::")
                is_c = 1
                
                if(is_c == 1):
                        is_c = self.xx_is_object()                                                
                
                if(is_c == 1):                
                        is_c = self.xx_check_int(self,"mPathId")
                self.xx_dbg("DBG_EndDeviceTarget::is_raidtarget_attached::out::" + str(is_c))
                
                return is_c
                
        def get_class_str(self):
                self.xx_dbg("DBG_EnddeviceTarget_TransportPath_PyPointer::get_class_str::")
                
                ccstr = """
"""
                self.xx_dbg("DBG_EnddeviceTarget_TransportPath_PyPointer::get_class_str::")
