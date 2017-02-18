import sys
import os        
        
class DBG_TargetIdentifyState:
        def __init__(self,spar):                
                self.m_items = []
                self.create_map()

                
        def create_map(self):            
                self.m_items = [
                "IDENTIFY_NOT_STARTED",
                "IDENTIFY_INQUIRY_IN_PROGRESS",
                "IDENTIFY_INQUIRY_COMPLETED",
                "IDENTIFY_INQUIRY_DEVICE_IDENTIFICATION_IN_PROGRESS",
                "IDENTIFY_INQUIRY_DEVICE_IDENTIFICATION_COMPLETED",
                "IDENTIFY_INQUIRY_SERIAL_NUMBER_IN_PROGRESS",
                "IDENTIFY_INQUIRY_SERIAL_NUMBER_COMPLETED",
                "IDENTIFY_INQUIRY_BLOCK_DEVICE_IN_PROGRESS",
                "IDENTIFY_INQUIRY_BLOCK_DEVICE_COMPLETED",
                "IDENTIFY_INQUIRY_BLOCK_PROVISIONING_IN_PROGRESS",
                "IDENTIFY_INQUIRY_BLOCK_PROVISIONING_COMPLETED",
                "IDENTIFY_LOGSENSE_SMART_IN_PROGRESS",
                "IDENTIFY_LOGSENSE_SMART_COMPLETED",
                "IDENTIFY_TEST_UNIT_READY_IN_PROGRESS",
                "IDENTIFY_TEST_UNIT_READY_COMPLETED",
                "IDENTIFY_START_UNIT_IN_PROGRESS",
                "IDENTIFY_START_UNIT_COMPLETED",
                "IDENTIFY_READ_CAPACITY_IN_PROGRESS",
                "IDENTIFY_READ_CAPACITY_COMPLETED",
                "IDENTIFY_SECURITY_PROTOCOL_IN_PROGRESS",
                "IDENTIFY_SECURITY_PROTOCOL_COMPLETED",
                "IDENTIFY_PREBOOT_VISIBLE_IN_PROGRESS",
                "IDENTIFY_PREBOOT_VISIBLE_COMPLETED",
                "IDENTIFY_ATA_IDENTIFY_DEVICE_IN_PROGRESS",
                "IDENTIFY_ATA_IDENTIFY_DEVICE_COMPLETED",
                "IDENTIFY_ATA_SET_FEATURES_PUIS_SPINUP_IN_PROGRESS",
                "IDENTIFY_ATA_SET_FEATURES_PUIS_SPINUP_COMPLETED",
                "IDENTIFY_COMPLETED"]                        

            
        def get_str(self, smb):
                try:
                        if(smb >=0 and smb < len(self.m_items)):
                                return self.m_items[smb]
                        else:
                                return "Unknown_DBG_TargetIdentifyState:" + str(smb)
                except:
                        return "Unknown_DBG_TargetIdentifyState:"
        