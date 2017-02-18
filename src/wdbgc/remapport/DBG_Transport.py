import sys
import os
from .. DBG_AdapterBase import *

from .. defs.DBG_RemapPortConnectionInterface import *
from .. defs.DBG_RemapPortConnectionType import *
from .. fields.DBG_FieldsMapper import *

from .. appcore.memory.DBG_Utils import *
from .. appcore.memory.DBG_MemoryTools import *
from .. ahci.DBG_AhciController import *
from .. nvme.DBG_NvmePort import *
from .. appsrc.raidtargets.DBG_EndDeviceTarget import *
from .. ports.DBG_HwInitializationData import *
from .. ports.DBG_PortConfigurationInformation import *
from .. appcore.config.DBG_PrintConfig import *
from .. remapport.DBG_TransportIds import *
class DBG_Transport(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_Transport::__init__::method_in::")
                self.xx_set_class_name ( "TRANSPORT" )
                self.xx_set_full_class_name ( "iastora!TRANSPORT" )
                self.m_print_all_transports = 0
                self.mType = 0
                self.m_index = 0
                self.mInterface = 0
                self.m_ahci_c = DBG_AhciController("FORM::DBG_Transport")
                self.m_nvme_port = DBG_NvmePort("FORM::DBG_Transport")
                self.mInitializationData = DBG_HwInitializationData("FORM::DBG_Transport")
                self.mPortConfig = DBG_PortConfigurationInformation("FORM::DBG_Transport")
                self.mDeviceInStandby = DBG_EndDeviceTarget("FORM::DBG_Transport")
                self.mTransportIds = DBG_TransportIds("FORM::DBG_Transport",self)
                self.mTransportOn = 0
                self.mInterface = 0
                self.mBusWidth = 0
                self.mBusSpeed = 0
                self.m_fields = DBG_FieldsMapper("DBG_Transport"
                                         , self)
                
                self.m_fields.add_fields_int_array([
                        "mTransportOn"
                        ,"mInterface"                        
                        ,"mType"
                        ,"mBusWidth"
                        ,"mBusSpeed"
                        ])
                
                if(DBG_PrintConfig().getItem().self_is_above_or_equal( 15 ) == 1):
                        self.m_fields.add_fields_int_array([
                                "mCycleRouterIndex"
                                ,"mInterruptMode"
                                ,"mNumOfMSsixInterruptsVectors"
                                ,"mMiniportBar"
                                ])
                
                
                self.xx_dbg("DBG_Transport::__init__::method_out::")

        def prepare_object(self):
                try:
                        self.prepare_object_internal()                                
                except:
                        self.xx_exception("DBG_Transport::print_object")
                        
        def set_transport_idx(self,pp):
                self.m_index = pp
                
        def prepare_object_internal(self):
                self.xx_dbg("DBG_Transport::prepare_object_internal::")
                self.mType =  DBG_MemoryTools().xx_get_int(self,"mType")
                self.mTransportOn = DBG_MemoryTools().xx_get_int(self,"mTransportOn")
                self.m_print_all_transports = DBG_PrintConfig().getItem().m_print_all_remap_transports
                self.clear_messages()
                self.add_message("mTransportOn:" + str(self.mTransportOn))
                self.add_message("m_print_all_transports:" + str(self.m_print_all_transports))
                
                if(self.mTransportOn !=1):
                        self.xx_dbg("DBG_Transport::prepare_object_internal::out::0::")
                        return
                
                self.m_fields.set_fields_parent(self)
                self.m_fields.prepare_object()
                self.mInterface = self.m_fields.get_fields_int("mInterface")
                self.mBusWidth = self.m_fields.get_fields_int("mBusWidth")
                self.mBusSpeed = self.m_fields.get_fields_int("mBusWSpeed")
                
                self.mPortConfig.set_addr_arr(self,"mPortConfig")
                self.mInitializationData.set_addr_arr(self,"mInitializationData")                                
                if(self.mInterface == 2 ): 
                        self.m_ahci_c.xx_inc_tabs(self);        
                        self.m_ahci_c.xx_compute_phy_by_parent(self,"mDeviceExtension")
                
                if(self.mInterface == 3 ):        
                        self.m_nvme_port.xx_inc_tabs(self)
                        self.m_nvme_port.xx_compute_phy_by_parent(self,"mDeviceExtension")
                
                #self.mDeviceInStandby.xx_inc_tabs(self)
                #self.mDeviceInStandby.xx_compute_phy_by_parent(self,"mDeviceInStandby")
                if(DBG_PrintConfig().getItem().self_is_above_or_equal( 15 ) == 1):
                        self.mTransportIds.set_addr_arr(self,"mTransportIds")
                        self.mTransportIds.prepare_object()
                self.xx_dbg("DBG_Transport::prepare_object::out")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_Transport::print_object")
                        
        def print_object_internal(self):
                
                self.xx_dbg("DBG_Transport::print_object::")
                self.prepare_object()                
                if(self.mTransportOn != 1):
                        self.xx_dbg("DBG_Transport::print_object::out::000::")
                        if(self.m_print_all_transports == 1):
                                self.xx_print_ptr("")
                                dd_fields = DBG_FieldsMapper("DBG_Transport"
                                                 , self)
                                                
                                s_info = ""
                                s_info = s_info +  "Transport_not_used[" + str(self.m_index) + "]"
                                s_info = s_info +  "[mTransportOn:" + str(self.mTransportOn) + "]"
                                dd_fields.initialize_by_parent(self)
                                dd_fields.add_raw_str(s_info)
                                dd_fields.print_object()
                        else:
                                self.xx_dbg("DBG_Transport::print_object::out::001::")
                else:                        
                        
                        self.xx_print_ptr("")
                        self.m_fields.add_raw_str( "ConnType:" + DBG_RemapPortConnectionType("").get_str(self.mType))
                        self.m_fields.add_raw_str( "ConnInterface:" + DBG_RemapPortConnectionInterface("").get_str(self.mInterface))                        
                        self.m_fields.xx_print_fields("")
                        
                        self.mInitializationData.print_object()
                        self.mPortConfig.print_object()
                        
                        if(self.mInterface == 2 ):                                                
                                if( self.m_ahci_c.xx_is_object() == 1):
                                        self.m_ahci_c.print_object()
                                        
                        if(self.mInterface == 3 ):        
                                if( self.m_nvme_port.xx_is_object() == 1):
                                        self.m_nvme_port.print_object()
                                        
                        if(DBG_PrintConfig().getItem().self_is_above_or_equal( 15 ) == 1):                 
                                self.mTransportIds.print_object()
                        
                        #self.mDeviceInStandby.print_object()
                
                self.xx_dbg("DBG_Transport::print_object::out")
                

                
