import sys
import os

from .. DBG_AdapterBase import *       
from ..devices.DBG_DeviceFeatureN import *
from ..devices.DBG_AtaIdentifyDevice import *

class DBG_AtaDeviceN(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "AtaDevice" )
                self.xx_set_full_class_name ( "iastora!AtaDevice" )               
                self.mUdmaFeature = DBG_DeviceFeatureN("Par::DBG_AtaDeviceN")
                self.mDeviceSleepFeature = DBG_DeviceFeatureN("Par::DBG_AtaDeviceN")
                self.mIdentifyData = DBG_AtaIdentifyDevice("Parent::DBG_AtaDeviceN")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_AtaIdentifyDevice::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_AtaDeviceN::prepare_object::")
                self.mUdmaFeature.xx_inc_tabs(self)
                self.mUdmaFeature.xx_compute_arr_phy_by_parent(self,"mUdmaFeature")
                
                self.mDeviceSleepFeature.xx_inc_tabs(self)
                self.mDeviceSleepFeature.xx_compute_arr_phy_by_parent(self,"mDeviceSleepFeature")
                
                self.mIdentifyData.xx_inc_tabs(self)
                self.mIdentifyData.xx_compute_arr_phy_by_parent(self,"mIdentifyData")
                
                self.xx_dbg("DBG_AtaDeviceN::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_AtaDeviceN::print_object::")
                self.prepare_object()
                self.xx_print_ptr("")
                self.mUdmaFeature.print_object()
                self.mDeviceSleepFeature.print_object()
                self.mIdentifyData.print_object()
                self.xx_dbg("DBG_AtaDeviceN::print_object::out::")