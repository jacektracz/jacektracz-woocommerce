import sys
import os
from ... appcore.logging.DBG_Log import *

class DBG_Base:
        def __init__(self,pparent,sdbg): 
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


        def get_parent_tabs(self, parent,ii_tabs):
                tabsp = ""                                        
                try:
                        self.xx_dbg("DBG_Base::get_parent_tabs::in::")
                        
                        if(parent != None):
                                if(hasattr(parent, 'xx_gett')):
                                        tabsp = parent.xx_gett(ii_tabs)
                        return tabsp                                                                                
                        self.xx_dbg("DBG_Base::get_parent_tabs::out::")
                        
                except:                        
                        self.xx_exception("DBG_Base::get_parent_tabs:exc::")                        
                        return tabsp
