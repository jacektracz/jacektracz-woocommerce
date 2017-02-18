import sys
import os
from .. DBG_AdapterBase import *
        
        
class DBG_RemapPortConnectionType:
        def __init__(self,spar):                
                self.m_items = {}
                self.create_map()
                
        def create_map(self):
            
                self.m_items[0] = 'REMAPPORT_CONNECTION_TYPE_NONE'
                self.m_items[1] = 'REMAPPORT_CONNECTION_TYPE_UNSUPPORTED'
                self.m_items[2] = 'REMAPPORT_CONNECTION_TYPE_SATA'
                self.m_items[3] = 'REMAPPORT_CONNECTION_TYPE_PCIE'
            
        def get_str(self, smb):
                try:
                        if(smb >=0 and smb < len(self.m_items)):
                                return self.m_items[smb]
                        else:
                                return "Unkonown DBG_RemapPortConnectionType:" + str(smb)
                except:
                        return "UNKNOWN DBG_RemapPortConnectionType:"
        