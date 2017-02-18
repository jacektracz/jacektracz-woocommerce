import sys
import os
from .. helpers.DBG_Utils import *
from .. helpers.DBG_PrintDispatcher import *        
class DBG_Field:
    def __init__(self):
            self.m_ptr = DBG_MemoryPtr()                
            
    def xx_print(self):
        if self.m_type == "I":
            s_addr = self.xx_get_addr_str()
            DBG_PrintDispatcher.xx_print( self.m_tabs + self.m_name + ": " + DBG_Utils().xx_getAsInt(s_addr))
                         
        
    
class DBG_Fields:
    def xx_add_field(self):
        self.m_ptr = DBG_MemoryPtr()
        
    