import sys
import os
import logging
from .. DBG_AdapterBase import *

from .. nvme.DBG_NvmeController import *
from .. nvme.DBG_ApstTable import *
from .. nvme.DBG_PciHeaderReader import *
from .. nvme.DBG_AdminIdentifyNamespaceData import *
from .. nvme.DBG_AdminIdentifyControllerData import *
from .. fields.DBG_FieldsMapper import *
from .. nvme.DBG_QueueManager import *
from .. defs.DBG_NvmePortState import *
from .. appsrc.raiddpc.DBG_DeferredProcedureCall import *
class DBG_NvmePort(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_NvmePort::__init__::in::")
                self.xx_set_class_name ( "NvmePort" )
                self.xx_set_full_class_name ( "iastora!NvmePort" )
                self.m_controller = DBG_NvmeController("Parent::DBG_NvmePort")
                self.mApstTable = DBG_ApstTable("Parent::DBG_NvmePort")
                self.mIdentifyControllerData = DBG_AdminIdentifyControllerData("Parent::DBG_NvmePort")
                self.mIdentifyNamespaceData = DBG_AdminIdentifyNamespaceData("Parent::DBG_NvmePort")
                self.mPciHeaderReader = DBG_PciHeaderReader("Parent::DBG_NvmePort")
                self.m_fields = DBG_FieldsMapper("DBG_NvmePort"
                                         , self)
                
                self.mQueueManager = DBG_QueueManager("Parent::DBG_NvmePort")
                self.m_port_state = DBG_NvmePortState("Parent::DBG_NvmePort")
                
                self.m_fields.add_fields_asstr_ints([
                        "mControllerNumber"
                        ,"mTemperatureThreshold"
                        ,"mAerInternalQueueSize"
                        ,"mState"
                        ,"mMaxIoQueueEntriesCount"
                        ])
                self.mDpc = DBG_DeferredProcedureCall("Parent::DBG_Raidport")
                self.xx_dbg("DBG_NvmePort::__init__::out::")
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_NvmePort::print_object")
                                        
        def prepare_object_internal(self,pparent):
                self.xx_dbg("DBG_NvmePort::prepare_object_internal::")
                
                if(self.xx_is_object() == 1):
                
                        self.m_controller.xx_inc_tabs(self); 
                        self.m_controller.xx_compute_arr_phy_by_parent(self,"mController")
                        
                        self.mApstTable.xx_inc_tabs(self);                
                        self.mApstTable.xx_compute_arr_phy_by_parent(self,"mApstTable")
                        
                        self.mPciHeaderReader.xx_inc_tabs(self);                
                        self.mPciHeaderReader.xx_compute_arr_phy_by_parent(self,"mPciHeaderReader")
        
                        self.mIdentifyControllerData.xx_inc_tabs(self);                
                        self.mIdentifyControllerData.xx_compute_arr_phy_by_parent(self,"mIdentifyControllerData")
        
                        self.mIdentifyNamespaceData.xx_inc_tabs(self);                
                        self.mIdentifyNamespaceData.xx_compute_arr_phy_by_parent(self," mIdentifyNamespaceData")
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.m_port_state.prepare_object(self.m_fields,"mState")
                        self.m_fields.add_raw_str(self.m_port_state.get_description())
                        
                        self.mDpc.set_addr_arr(self,"mDpc")
                        self.mDpc.prepare_object()

                        self.mQueueManager.set_addr_arr(self,"mQueueManager")
                        
                self.xx_dbg("DBG_NvmePort::prepare_object_internal::out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")                        
                        self.print_object_internal(self)
                        self.xx_print_end("")
                        
                except:
                        self.xx_exception("DBG_NvmePort::print_object")
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_NvmePort::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")                
                if(self.xx_is_object() == 1):                        
                        self.m_fields.xx_print_fields("")
                        self.m_controller.print_object()
                        self.mApstTable.print_object()
                        self.mPciHeaderReader.print_object()                
                        self.mIdentifyControllerData.print_object()                        
                        self.mIdentifyNamespaceData.print_object()
                        self.mQueueManager.print_object()
                        self.mDpc.print_object()
                self.xx_dbg("DBG_NvmePort::print_object_internal::out::")                                                                
