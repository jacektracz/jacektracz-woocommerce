import sys
import os
from .. DBG_AdapterBase import *
from .. appcore.config.DBG_PrintConfig import *        
from .. appcore.logging.DBG_Log import *                
class DBG_HwInterfaceType:
        def __init__(self,spar):                
                self.m_items = {}
                self.create_map()
                
        def create_map(self):
                self.m_items[-1] = 'InterfaceTypeUndefined'
                self.m_items[0] = 'Internal'
                self.m_items[1] = 'Isa'
                self.m_items[2] = 'Eisa'
                self.m_items[3] = 'MicroChannel'
                self.m_items[4] = 'TurboChannel'
                self.m_items[5] = 'PCIBus'
                self.m_items[6] = 'VMEBus'
                self.m_items[7] = 'NuBus'
                self.m_items[8] = 'PCMCIABus'
                self.m_items[9] = 'CBus'
                self.m_items[10] = 'MPIBus'
                self.m_items[11] = 'MPSABus'
                self.m_items[12] = 'ProcessorInternal'
                self.m_items[13] = 'InternalPowerBus'
                self.m_items[14] = 'PNPISABus'
                self.m_items[15] = 'PNPBus'
                self.m_items[16] = 'Vmcs'
                self.m_items[17] = 'ACPIBus'
                self.m_items[18] = 'MaximumInterfaceType'
            
        def get_str(self, smb):
                try:
                        if(smb >=0 and smb < len(self.m_items)):
                                return self.m_items[smb]
                        else:
                                return "Unkonown DBG_HwInterfaceType:" + str(smb)
                except:
                        if(DBG_PrintConfig().getItem().m_print_all_errors == 1):
                                 DBG_Log().xx_exc(";DBG_HwInterfaceType][exception]")         
                        else:
                                return "UNKNOWN DBG_HwInterfaceType:"
        