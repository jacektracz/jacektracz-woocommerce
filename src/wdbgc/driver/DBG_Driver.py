import sys
import os
import logging
from .. DBG_AdapterBase import *       
#from .. remapport.DBG_RemapPort import *
from .. fields.DBG_FieldsMapper import *
from .. driver.DBG_DriverFeatures import *
from .. driver.DBG_Chipset import *
from .. driver.DBG_ACPI import *
from .. driver.DBG_PciCommonConfig import *
from .. appcore.config.DBG_PrintConfig import *
from .. appsrc.wcdl.DBG_TimerList import *
from .. appsrc.driverext.DBG_AenMgr import *
from .. driver.DBG_CrashHiberMemoryDescriptor import *
from .. driver.DBG_DeviceExtension_PyArray import *

class DBG_Driver(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "Driver" )
                self.xx_set_full_class_name ( "iastora!Wcdl::Driver" )
                
                #self.m_remapport = DBG_RemapPort("FROM::Driver")
                self.m_features = DBG_DriverFeatures("FROM::Driver")
                self.m_chipset = DBG_Chipset("FROM::Driver")
                self.m_acpi = DBG_ACPI("FROM::Driver")
                self.mPciCommonConfig = DBG_PciCommonConfig("FROM::Driver")
                self.major_version = "";
                self.m_fields = DBG_FieldsMapper("Driver",self)
                self.mCrashHiberMemoryDescriptor = DBG_CrashHiberMemoryDescriptor("",self)
                
                self.m_fields.add_fields_int_array([
                        "mBusNumber"
                        ,"mSlotNumber"
                        ,"mPciConfigLength"
                        ,"mListIndex"
                        ,"mExtensionCount"
                        ,"mDumpMode"
                        ])
                
                self.m_device_ext_list = DBG_DeviceExtension_PyArray("Driver",self)
                
                self.mTimerList = DBG_TimerList("FROM::Driver",self)
                self.mAenMgr = DBG_AenMgr("FROM::Driver",self)
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_Driver::prepare_object::out")
                        if(self.prepare_check() == 1):
                                return

                        if(self.xx_is_object() == 1):
                                
                                self.m_fields.initialize_by_parent(self)
                                #self.m_remapport.xx_inc_tabs( self,"DBG_Driver")                
                                #self.m_remapport.xx_compute_phy_by_parent(self,"mDeviceExtensionList[2]")
                                
                                self.m_features.xx_inc_tabs( self,"DBG_Driver") 
                                self.m_features.xx_compute_arr_phy_by_parent(self,"mFeatures")
                                
                                if(DBG_PrintConfig().getItem().self_is_above_or_equal( 15 ) == 1):
                                        self.m_chipset.xx_inc_tabs( self,"DBG_Driver") 
                                        self.m_chipset.xx_compute_arr_phy_by_parent(self,"mChipset")
                                        
                                self.m_acpi.set_addr_arr(self,"mAcpi")
                                
                                self.mPciCommonConfig.set_addr_arr(self,"mPciCommonConfig")
                                
                                self.mTimerList.set_addr_arr(self,"mTimerList")
                                self.mTimerList.prepare_object()

                                self.mAenMgr.set_addr_arr(self,"mAenMgr")
                                self.mAenMgr.prepare_object()
                                
                                self.mCrashHiberMemoryDescriptor.set_addr_arr(self,"mCrashHiberMemoryDescriptor")
                                self.mCrashHiberMemoryDescriptor.prepare_object()
                                
                                self.prepare_array_dev_ext_list()
                                
                        self.xx_dbg("DBG_Driver::prepare_object::out")
                except:
                        self.xx_exception("DBG_Driver::prepare_object::excp")
                        
        def prepare_array_dev_ext_list(self):
                try:
                        self.xx_dbg("DBG_Driver::prepare_array_dev_ext_list::in_method::")
                        rg = self.m_fields.get_fields_int("mExtensionCount")                                
                        self.m_device_ext_list.set_addr(self,"SELF")
                        self.m_device_ext_list.set_range( rg )
                        self.m_device_ext_list.set_parent(self)
                        self.m_device_ext_list.prepare_object()
                        self.xx_dbg("DBG_Driver::prepare_array_dev_ext_list::out_method::")
                except:
                        self.xx_exception("DBG_Driver::prepare_array_dev_ext_list::excp")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        
                        self.xx_dbg("DBG_Driver::print_object::out")
                        
                        self.prepare_object()
                        self.xx_print_ptr("") 
                        
                        if(self.xx_is_object() == 1):
                                
                                self.m_fields.print_object()
                                
                                if(DBG_PrintConfig().getItem().self_is_above_or_equal( 15 ) == 1):
                                        self.m_chipset.print_object()
                                        
                                self.m_features.print_object()
                                self.m_acpi.print_object()
                                self.mPciCommonConfig.print_object()
                                self.mTimerList.print_object()
                                self.mCrashHiberMemoryDescriptor.print_object()
                                self.m_device_ext_list.print_object()
                                self.mAenMgr.print_object()
                                
                                #self.m_remapport.print_object()
                        
                        self.xx_dbg("DBG_Driver::print_object::out")
                except:
                        self.xx_exception("DBG_Driver::print_object::exc")
                