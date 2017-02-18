import sys
import os

from ... DBG_AdapterBase import *
from ... appsrc.raidtargets.DBG_RaidDiskIdentityData import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.raidtargets.DBG_EndDeviceTarget_PyArray import *
from ... appsrc.raidtransport.DBG_FastList_TransportRequest import *

class DBG_TransportPath(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_TransportPath::__init__::in::")
                self.xx_set_class_name ( "TransportPath" )
                self.xx_set_full_class_name ( "iastora!TransportPath" )
                
                self.m_diskid = DBG_RaidDiskIdentityData("Parent::DBG_TransportPath")
                self.m_diskid.set_use_object(0)
                self.m_fields = DBG_FieldsMapper("DBG_TransportPath",self)
                
                self.mIoQueue = DBG_FastList_TransportRequest("DBG_TransportPath",self)
                self.mRetryQueue  = DBG_FastList_TransportRequest("DBG_TransportPath",self)
                self.mDispatchedIoList  = DBG_FastList_TransportRequest("DBG_TransportPath",self)
                
                self.create_init()
                self.m_devices = DBG_EndDeviceTarget_PyArray("Parent::DBG_TransportPath",self)
                self.m_childs_count = 0
                self.xx_dbg("DBG_TransportPath::__init__::in::")
                
        def get_childs_count(self):
                return self.m_childs_count
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_TransportPath::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_TransportPath::prepare_object::")
                
                if(self.xx_is_object() == 1):                
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        i_num_targets = self.m_fields.get_fields_int("mNumTargets")
                        self.m_diskid.xx_inc_tabs(self)
                        self.m_diskid.xx_compute_arr_phy_by_parent(self,"mOldDiskIdentityData")
                        
                        
                        self.mIoQueue.set_addr_arr(self,"mIoQueue")
                        self.mIoQueue.prepare_object()                        
                        
                        self.mRetryQueue.set_addr_arr(self,"mRetryQueue")
                        self.mRetryQueue.prepare_object()                        
                        
                        self.mDispatchedIoList.set_addr_arr(self,"mDispatchedIoList")
                        self.mDispatchedIoList.prepare_object()

                        #if(DBG_PrintConfig().getItem().get_handle_devices_in_transport_path() == 1):
                        self.m_devices.set_addr(self,"SELF")                        
                        self.m_devices.set_range(i_num_targets,1)
                        self.m_devices.prepare_object()
                        self.m_childs_count = self.m_devices.get_items_count()
                self.xx_dbg("DBG_TransportPath::prepare_object::out::")
                
        def print_object(self):
                try:
                        self.xx_print_start()
                        self.print_object_internal(self)
                        self.xx_print_end()
                except:
                        self.xx_exception("DBG_TransportPath::print_object")
                        
        def create_init(self):
                try:
                        self.xx_dbg("DBG_TransportPath::create_init::in::")
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
                                ])                        
                except:
                        self.xx_exception("DBG_TransportPath::print_object")
                
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_TransportPath::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.is_valid_object() == 1 ):                        
                        self.m_fields.xx_print_fields("")                        
                        self.m_diskid.print_object()
                                
                        self.mIoQueue.print_object()
                        self.mRetryQueue.print_object()
                        self.mDispatchedIoList.print_object()
                        
#                        if(DBG_PrintConfig().getItem().get_handle_devices_in_transport_path() == 1):
                        self.m_devices.print_object()
                        
                        #if(self.m_diskid.get_use_object() == 1):
                        
                self.xx_dbg("DBG_TransportPath::print_object_internal::out::")                        
                        
        def is_valid_object(self):
                self.xx_dbg("DBG_TransportPath::is_valid_object::in::")
                is_c = 1
                
                if(is_c == 1):
                        is_c = self.xx_is_object()                                                
                
                if(is_c == 1):                
                        if(self.m_devices.get_items_count() == 0):
                                is_c = 0
                        
                self.xx_dbg("DBG_TransportPath::is_valid_object::out::" + str(is_c))
                
                return is_c
                                
        def get_class_str(self):
                self.xx_dbg("DBG_TransportPath::get_class_str::")
                
                ccstr = """
"""
                self.xx_dbg("DBG_TransportPath::get_class_str::")
