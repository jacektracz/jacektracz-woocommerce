import sys
import os
import logging
from .. apptools.DBG_ToolsBase import *
from .. apptools.DBG_EnvItemData import *

class DBG_EnvManagerData(DBG_ToolsBase):
        def __init__(self,spar):                
                DBG_ToolsBase.__init__(self,spar)
                self.xx_set_class_name ( "DBG_EnvManager" )
                self.xx_set_full_class_name ( "iastora!::DBG_EnvManager" )
                self.m_items = []
                self.create_items()
                
        def create_items(self):
                """ ccc """
                for dd_ii in DBG_EnvItemData("").get_items():
                        self.m_items.append(dd_ii)
                
        def print_items(self):
                dd_out = None
                for dd_ii in self.m_items:
                        dd_ii.print_info()
                        
        def get_by_selector(self, pselector):
                dd_out = None
                for dd_ii in self.m_items:
                        if(dd_ii.m_selector == pselector):
                                dd_out = dd_ii
                                break
                return dd_out
                
        def get_items(self):
                return self.m_items
        