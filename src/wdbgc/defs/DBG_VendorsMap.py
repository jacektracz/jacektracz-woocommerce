import sys
import os        
        
class DBG_VendorsMap:
        def __init__(self,spar):                
                self.m_items = []
                self.create_map()

                
        def create_map(self):            
                self.m_items = [
                        "StateUnknown"
                        ]

            
        def get_str(self, smb):
                try:
                        if(smb >=0 and smb < len(self.m_items)):
                                return self.m_items[smb]
                        else:
                                return "Unknown_DBG_VendorsMap:" + str(smb)
                except:
                        return "Unknown_DBG_VendorsMap:"
        