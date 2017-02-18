import sys
import os
from .. DBG_AdapterBase import *
        
        
class DBG_ChipsetIdMap:
        def __init__(self,spar):                
                self.m_items = {}
                self.create_map()
                
        def create_map(self):
            
                self.m_items[0] = 'Unknown'
                self.m_items[1] = 'ICH8'
                self.m_items[2] = 'ICH9'
                self.m_items[3] = 'ICH10'
                self.m_items[4] = 'IbexPeak'
                self.m_items[5] = 'CougarPoint'
                self.m_items[6] = 'Patsburg'
                self.m_items[7] = 'PantherPoint'
                self.m_items[8] = 'LynxPoint'
                self.m_items[9] = 'LynxPointRefresh'
                self.m_items[10] = 'LynxPointLP'
                self.m_items[11] = 'Wellsburg'
                self.m_items[12] = 'SunrisePointLP'
                self.m_items[13] = 'SunrisePointH'
                self.m_items[14] = 'CannonLake'
                self.m_items[15] = 'IceLake'
            
        def get_str(self, smb):
                try:
                        if(smb >=0 and smb < len(self.m_items)):
                                return self.m_items[smb]
                        else:
                                return "Unkonown DBG_ChipsetIdMap:" + str(smb)
                except:
                        return "UNKNOWN DBG_ChipsetIdMap:"
        