import sys
import os
from .. DBG_AdapterBase import *
        
        
class DBG_DiskStateMap(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_Defines::__init__::in::")
                self.xx_set_class_name ( "Chipset" )
                self.xx_set_full_class_name ( "iastora!Wcdl::Chipset" )
                self.xx_dbg("DBG_Chipset::__init__::out")
                self.disk_state_map = {}
                
        def create_map(self):

            self.disk_state_map['SPARE_DISK'] = 0x01  
            self.disk_state_map['CONFIGURED_DISK'] = 0x02  
            self.disk_state_map['FAILED_DISK'] = 0x04
            self.disk_state_map['USABLE_DISK'] = 0x08
            self.disk_state_map['DETECTED_DISK'] = 0x10
            self.disk_state_map['CLAIMED_DISK'] = 0x20 
            self.disk_state_map['PASSTHRU_DISK'] = 0x40
            self.disk_state_map['OFFLINE_DISK'] = 0x80 
            self.disk_state_map['CONFIG_ON_DISK'] = 0x100
            self.disk_state_map['DISK_SMART_EVENT_TRIGGERED'] = 0x200 
            self.disk_state_map['DISK_SMART_EVENT_SUPPORTED'] = 0x400 
            self.disk_state_map['FORMATTING_DISK'] = 0x800
            self.disk_state_map['FORMAT_SUCCEEDED'] = 0x1000
            self.disk_state_map['FORMAT_FAILED'] = 0x2000
            self.disk_state_map['ELIGIBLE_FOR_SPARE'] = 0x4000
            self.disk_state_map['OFFLINE_ARRAY_MEMBER'] = 0x8000
            self.disk_state_map['CONFIG_IS_UPREV'] = 0x10000
            self.disk_state_map['DISK_WRITE_CACHE_DISABLED'] = 0x20000
            self.disk_state_map['UNKNOWN_DISK_FAILURE'] = 0x40000
            self.disk_state_map['DO_READ_CONFIG'] = 0x80000 
            self.disk_state_map['POWERED_OFF_DISK'] = 0x100000
            self.disk_state_map['BOOTABLE_DISK'] = 0x200000
            self.disk_state_map['CLONE_DISK_MODIFIED'] = 0x400000
            self.disk_state_map['PASSTHRU_DISK_WMPB'] = 0x800000
            self.disk_state_map['LOCKED_DISK'] = 0x1000000
            self.disk_state_map['NVM_DEVICE'] = 0x2000000 
            self.disk_state_map['NVMHCI_HEALTH_FAILED'] = 0x4000000 
            self.disk_state_map['NVMHCI_HEALTH_READONLY'] = 0x8000000
            self.disk_state_map['PORT_IN_D3'] = 0x10000000
            self.disk_state_map['SDR0_IS_HIDDEN'] = 0x20000000      
            self.disk_state_map['CVFD_ELIGIBLE_DISK'] = 0x40000000  
            self.disk_state_map['NEWLY_ADDED_DISK'] = 0x80000000 
