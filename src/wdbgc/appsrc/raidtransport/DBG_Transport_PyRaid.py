import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.raidtransport.DBG_TransportPath_PyArray import *
from ... appsrc.raidtargets.DBG_TransportTarget import *
from ... appsrc.wcdl.DBG_RaidportSpinLock import *
from ... appsrc.raidtransport.DBG_FastList_TransportTarget import *
from ... appsrc.raiddpc.DBG_DeferredProcedureCall import *
from ... ports.DBG_HwInitializationData import *
class DBG_Transport_PyRaid(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_Transport_PyRaid::__init__::in::")
                self.xx_set_class_name ( "Transport" )
                self.xx_set_full_class_name ( "iastora!Transport" )
                self.mPath = DBG_TransportPath_PyArray("Parent::DBG_Transport_PyRaid")
                
                self.m_fields = DBG_FieldsMapper("DBG_Transport_PyRaid",self)
                
                self.mDispatchQueue = DBG_FastList_TransportTarget("DBG_Transport_PyRaid",self)
                
                self.create_fields()
                self.m_adapter = DBG_TransportTarget("Parent::DBG_Transport_PyRaid")
                self.mTransportSpinLock = DBG_RaidportSpinLock(self,"Parent::DBG_Transport_PyRaid")
                self.mDispatchDpc = DBG_DeferredProcedureCall("Parent::DBG_Raidport")
                self.mEnumerationDpc = DBG_DeferredProcedureCall("Parent::DBG_Raidport")
                self.sHwInitializationData  = DBG_HwInitializationData("Parent::DBG_Raidport")
                self.xx_dbg("DBG_Transport_PyRaid::__init__::in::")

        def create_fields(self):
                try:
                        sver = DBG_PrintConfig().getItem().get_version()
                        
                                
                        self.m_fields.add_fields_int_array([
                                "mNumPaths"
                                ,"mNumTargets"                        
                                ,"mIsEnumerating"
                                ,"mIsInitializing"
                                ,"mRestartEnumeration"
                                ,"mDeviceInStandbyPresent"
                                ,"mDeviceChangedDuringEnum"
                                ])
                        
                        if(DBG_PrintConfig().getItem().m_is_handled_lun == 1):
                                self.m_fields.add_fields_int_array([
                                        "mNumLuns"
                                        ])
                        
                except:
                        self.xx_exception("DBG_Transport_PyRaid::create_fields")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_Transport_PyRaid::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_Transport_PyRaid::prepare_object::")
                if(self.xx_is_object() == 1):
                        self.m_fields.set_fields_parent(self)
                        
                        self.mPath.set_addr(self,"SELF")
                        self.mPath.prepare_object(self)
                        
                        self.m_adapter.set_addr(self,"mAdapterTarget")
                        self.m_adapter.prepare_object()
                        
                        self.mTransportSpinLock.set_addr_arr(self,"mTransportSpinLock")
                        self.mTransportSpinLock.prepare_object()
                        
                        
                        self.mDispatchQueue.set_addr_arr(self,"mDispatchQueue")
                        self.mDispatchQueue.prepare_object()
                        
                        self.mDispatchDpc.set_addr_arr(self,"mDispatchDpc")
                        self.mDispatchDpc.prepare_object()
                        
                        
                        self.mEnumerationDpc.set_addr_arr(self,"mEnumerationDpc")
                        self.mEnumerationDpc.prepare_object()
                        
                        self.sHwInitializationData.set_addr_arr(self,"sHwInitializationData")
                        self.sHwInitializationData.prepare_object()
                        
                self.xx_dbg("DBG_Transport_PyRaid::prepare_object::out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_Transport_PyRaid::print_object")                                        
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_Transport_PyRaid::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):                
                        self.m_fields.xx_print_fields("")
                        self.mPath.print_object()
                        self.m_adapter.print_object()
                        self.mTransportSpinLock.print_object()
                        self.mDispatchQueue.print_object()
                        self.mDispatchDpc.print_object()
                        self.mEnumerationDpc.print_object()
                        self.sHwInitializationData.print_object()
                self.xx_dbg("DBG_Transport_PyRaid::print_object_internal::out::")                        
                        
                
        def get_class_str(self):
                self.xx_dbg("DBG_Transport_PyRaid::get_class_str::")
                
                ccstr = """
"""
                self.xx_dbg("DBG_Transport_PyRaid::get_class_str::")
