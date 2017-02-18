import sys
import os
from .. DBG_AdapterBase import *
        
        
class DBG_RaidTargetMap:
        def __init__(self,spar):                
                self.m_items = {}
                self.create_map()
                
        def create_map(self):
            
                self.m_items[0] = 'RaidportTargetType_PassthroughTarget'
                self.m_items[1] = 'RaidportTargetType_EmptyTarget'
                self.m_items[2] = 'RaidportTargetType_RaidTarget'
                self.m_items[3] = 'RaidportTargetType_ReadOnlyPassthroughTarget'
                self.m_items[4] = 'RaidportTargetType_PassthroughFromRaidTarget'
                self.m_items[5] = 'NN'
                self.m_items[6] = 'NN'
                self.m_items[7] = 'NN'
            
        def get_str(self, smb):
                try:
                        if(smb >=0 and smb <= 4):
                                return self.m_items[smb]
                        else:
                                return "Unknown RaidTargetType:" + str(smb)
                except:
                        return "Unknown:" + str(smb)
        
        def is_valid(self, smb):
                is_valid = 1
                try:
                        if(smb >=0 and smb <= 4):
                                is_valid = 1
                        else:
                                is_valid = 0
                                
                        return is_valid
                
                except:
                        return 0
        