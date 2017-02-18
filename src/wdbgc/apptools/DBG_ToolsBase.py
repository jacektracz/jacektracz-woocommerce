import sys
import os

from .. apptools.DBG_ToolsUtils import *

class DBG_ToolsBase:
        def __init__(self,sdbg): 
                self.m_class_name = "DBG_Base"
                self.m_full_class_name ="DBG_Base"                
                
        def xx_set_class_name(self,p_class_name):			
                self.m_class_name = p_class_name
        
        def xx_set_full_class_name(self,p_class_name):			
                self.m_full_class_name = p_class_name
            
        def xx_dbg(self, ss):
                print ss
                
        def xx_exception(self,symbol,method=""):				
                logging.exception("")

        def xx_safe_exe(self, scommand, sinfo = "no-info"):
                DBG_ToolsUtils().xx_safe_exe(scommand, sinfo)

        def xx_gett(self, stabs):
            return ""
        
