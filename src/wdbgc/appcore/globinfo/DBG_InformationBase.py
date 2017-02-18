import sys
import os
from ... appcore.logging.DBG_Log import *

class DBG_InformationBase:
        def __init__(self): 
                self.m_class_name = "DBG_Base"
                self.m_full_class_name ="DBG_Base"                
                
        def xx_set_class_name(self,p_class_name):			
                self.m_class_name = p_class_name
        
        def xx_set_full_class_name(self,p_class_name):			
                self.m_full_class_name = p_class_name
            
        def xx_dbg(self,ss):
                DBG_Log().xx_dbg("[" + self.m_class_name + "]"+ ss)
        
        def xx_exception(self,symbol,method=""):				
                DBG_Log().xx_exc("[" + method + "][" +"[excp:" + symbol + "]")
                
        def xx_gett(self, stabs):
            return ""
                