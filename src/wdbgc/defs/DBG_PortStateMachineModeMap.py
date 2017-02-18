import sys
import os        
        
class DBG_PortStateMachineModeMap:
        def __init__(self,spar):                
                self.m_items = []
                self.create_map()
                
        def create_map(self):
            
                self.m_items = [
                "Uninitialized",
                    "NotReady",
                    "Enumerating",
                    "FatalErrorRecovery",
                    "Ready",
                    "NoDeviceFound",
                    "Failed",
                    "Paused",
                    "Stopped"
                ]
            
        def get_str(self, smb):
                try:
                        if(smb >=0 and smb < len(self.m_items)):
                                return self.m_items[smb]
                        else:
                                return "Unkonown_DBG_PortStateMachineMap:" + str(smb)
                except:
                        return "Unkonown_DBG_PortStateMachineMap:"
        