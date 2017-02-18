import sys
import defines
import logging
from pykd import *
from defines import *
from proc_utils import *
from dbg_classess_utils import *
from DBG_ATA_IDENTIFY_DEVICE_DATA import *
from DBG_DeviceFeature import *                
from DBG_SCSI_REQUEST_BLOCK import *
from DBG_SENSE_DATA import *
                
class DBG_AtaDevice:
        def __init__(self,sptr):
                self.m_ptr = sptr
                self.m_obj_expr = ""
                
        def printObj(self):
                try:
                        d = DBG_ATA_IDENTIFY_DEVICE_DATA()
                        d.setPointer(self.m_ptr)
                        d.printObj()
                        
                        df = DBG_DeviceFeature(self.m_ptr,"mPuisFeature")
                        df.printObj()
                        
                        df = DBG_DeviceFeature(self.m_ptr,"mHybridHintFeature")
                        df.printObj()
                        
                        df = DBG_DeviceFeature(self.m_ptr,"mWriteCacheFeature")
                        df.printObj()
                        
                        df = DBG_DeviceFeature(self.m_ptr,"mDeviceSleepFeature")
                        df.printObj()

                        df = DBG_DeviceFeature(self.m_ptr,"mUdmaFeature")
                        df.printObj()
                        
                        df = DBG_DeviceFeature(self.m_ptr,"mDeviceAutoPartialSlumberFeature")
                        df.printObj()
                        
                        df = DBG_DeviceFeature(self.m_ptr,"mDeviceInitiatedPowerManagementFeature")
                        df.printObj()

                        df = DBG_DeviceFeature(self.m_ptr,"mDmaSetupAutoActivateFeature")
                        df.printObj()
                        
                        df = DBG_SCSI_REQUEST_BLOCK(self.m_ptr,"mPrivateSrb")
                        df.printObj()
                        
                        df = DBG_SENSE_DATA(self.m_ptr,"mPrivateSenseData")
                        df.printObj()
                        
                        
                except:
                        print '=========================exception occured================='
                        logging.exception('')
                        print '==========================================================='
                        return
                





