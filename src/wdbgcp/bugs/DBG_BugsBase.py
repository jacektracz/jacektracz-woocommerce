import sys
import os

from .. bugs.DBG_BugsUtils import *

class DBG_BugsBase:
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
                DBG_BugsUtils().xx_safe_exe(scommand, sinfo)

        def xx_gett(self, stabs):
            return ""
        
        def xx_bp(self,tt):                
                self.xx_safe_exe("bp " + tt)
             
        def bp(self,tt):                
                self.xx_safe_exe("bp " + "iaStorA!" + tt)
                
        def xx_bp_arr(self,pp):                
                for dd_ii in pp:
                        self.bp(dd_ii)
                