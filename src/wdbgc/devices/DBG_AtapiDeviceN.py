import sys
import os
import logging
from .. DBG_AdapterBase import *       
from .. devices.DBG_AtapiIdentifyDevice import *
from ..devices.DBG_DeviceFeatureN import *
                
class DBG_AtapiDeviceN(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "AtapiDevice" )
                self.xx_set_full_class_name ( "iastora!AtapiDevice" )
                self.mUdmaFeature = DBG_DeviceFeatureN("Par::DBG_AtapiDeviceN")
                self.mDeviceSleepFeature = DBG_DeviceFeatureN("Par::DBG_AtapiDeviceN")
                self.mIdentifyData = DBG_AtapiIdentifyDevice("Parent::DBG_AtapiDeviceN")
              
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_AtapiIdentifyDevice::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_AtapiDeviceN::prepare_object::")
                if(self.xx_is_object() ==1):
                        self.mUdmaFeature.set_addr_arr(self,"mUdmaFeature")                
                        self.mDeviceSleepFeature.set_addr_arr(self,"mDeviceSleepFeature")                
                        self.mIdentifyData.set_addr_arr(self,"mIdentifyData")
                self.xx_dbg("DBG_AtapiDeviceN::prepare_object::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_AtapiDeviceN::print_object::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() ==1):
                        self.mUdmaFeature.print_object()                
                        self.mDeviceSleepFeature.print_object()                
                        self.mIdentifyData.print_object()
                self.xx_dbg("DBG_AtapiDeviceN::print_object::")        
                

