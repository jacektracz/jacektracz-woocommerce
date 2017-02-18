import sys
import os
import logging
from .. DBG_AdapterBase import *
from .. appsrc.ahciintl.DBG_AhciHbaCapabilities import *
from .. ahci.DBG_AhciPortsGeneric import *
from .. ahci.DBG_MiniportParameters import *
from .. ahci.DBG_AhciMemoryRegisters import *
from .. fields.DBG_FieldsMapper import *
from .. appcore.config.DBG_PrintConfig import *
from .. defs.DBG_AhciControllerMap import *

class DBG_AhciController(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_AhciController::__init__::in::")
                self.xx_set_class_name ( "AhciController" )
                self.xx_set_full_class_name ( "iastora!AhciController" )
                self.m_cap = DBG_AhciHbaCapabilities("FROM::DBG_AhciController")
                self.m_ahci_ports =  DBG_AhciPortsGeneric("FROM::DBG_AhciController",self)
                self.mMiniportParameters = DBG_MiniportParameters("FROM::DBG_AhciController")
                self.m_fields = DBG_FieldsMapper("DBG_AhciController"
                                         ,self)
                self.aBar = DBG_AhciMemoryRegisters("FROM::DBG_AhciController")
                self.mPlatformDeviceId = 0
                self.xx_dbg("DBG_AhciController::__init__::out::")
               
        
        def prepare_object(self):
                self.xx_dbg("DBG_AhciController::prepare_object::in::")
                if(self.xx_is_object() == 1):
                        
                        self.aBar.set_addr_arr(self,"aBar")
                        self.aBar.prepare_object()
                                                
                        self.m_cap.xx_inc_tabs(self);                
                        self.m_cap.xx_compute_arr_phy_by_parent(self,"Capabilities")
                        
                        self.mMiniportParameters.xx_inc_tabs(self);                
                        self.mMiniportParameters.xx_compute_arr_phy_by_parent(self,"mMiniportParameters")
                        
                        self.m_ahci_ports.set_addr(self,"SELF")
                        
                        self.m_fields.set_fields_parent(self)
                        
                        if(DBG_PrintConfig().getItem().self_is_above_or_equal( 15 ) == 1):
                                self.m_fields.add_fields_int_array([
                                        "mPortsImplemented"
                                        ,"mVendorId"
                                        ,"mRevisionId"])
                        
                        self.m_fields.add_fields_hex_array([
                                "mInCsMode"                                
                                ,"mDeviceId"
                                ,"mPlatformDeviceId"                                
                                ])
                        self.m_fields.prepare_object()
                        
                        self.mPlatformDeviceId = self.m_fields.get_fields_hex("mPlatformDeviceId")
                        
                self.xx_dbg("DBG_AhciController::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_AhciController::print_object::in::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):
                        self.print_internals()
                        self.m_fields.xx_print_fields("")
                        self.aBar.print_object()
                        self.m_cap.print_object()
                        self.mMiniportParameters.print_object()
                        self.m_ahci_ports.print_object()
                        
                self.xx_dbg("DBG_AhciController::print_object::out::")

        def print_internals(self):
                try:
                        
                        hh = "0x" + str(self.mPlatformDeviceId).upper();
                        hx = self.get_hex(hh)
                        self.m_fields.add_raw_str( "mPlatformDeviceId:" + str(hx),2)                                                
                        smap1 = DBG_AhciControllerMap("").get_str(hx)
                        
                        self.m_fields.add_raw_str( "RaidId_Name:" + smap1,2)
                except:
                        self.xx_exception("DBG_AhciController::print_internals")

        def get_hex(self,hh):
                try:
                        h1 = int(hh, 16)
                        h = hex(h1)
                        return h
                except:
                        self.xx_exception("DBG_AhciController::get_hex[" + hh + "]")
                
        def get_str(self):
                
                ccs = """
                
                """