import sys
import os
from .. DBG_AdapterBase import *
from .. appcore.config.DBG_PrintConfig import *        
from .. appcore.logging.DBG_Log import *                
class DBG_RemapPortConnectionInterface:
        def __init__(self,spar):                
                self.m_items = {}
                self.create_map()
                
        def create_map(self):
            
                self.m_items[0] = 'REMAPPORT_CONNECTION_INTERFACE_UNKNOWN'
                self.m_items[1] = 'REMAPPORT_CONNECTION_INTERFACE_UNSUPPORTED'
                self.m_items[2] = 'REMAPPORT_CONNECTION_INTERFACE_AHCI'
                self.m_items[3] = 'REMAPPORT_CONNECTION_INTERFACE_NVME'
            
        def get_str(self, smb):
                try:
                        if(smb >=0 and smb < len(self.m_items)):
                                return self.m_items[smb]
                        else:
                                return "Unkonown DBG_RemapPortConnectionInterface:" + str(smb)
                except:
                        if(DBG_PrintConfig().getItem().m_print_all_errors == 1):
                                 DBG_Log().xx_exc(";DBG_RemapPortConnectionInterface][exception]")         
                        else:
                                return "UNKNOWN DBG_RemapPortConnectionInterface:"
        