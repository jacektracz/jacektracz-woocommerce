import sys
import os
import logging
from .. apptools.DBG_ToolsBase import *
from .. apptools.DBG_EnvItemData import *
from .. apptools.DBG_EnvManagerData import *
        
class DBG_EnvManager(DBG_ToolsBase):
        m_data = None
        def __init__(self,spar):                
                DBG_ToolsBase.__init__(self,spar)
                self.xx_set_class_name ( "DBG_EnvManager" )
                self.xx_set_full_class_name ( "iastora!::DBG_EnvManager" )                
        
        def getData(self):
            try:
                if(self.__class__.m_data == None):
                    self.__class__.m_data = DBG_EnvManagerData("")
                return self.__class__.m_data
            except:
                    self.xx_exception("DBG_PrintConfig::getItem::excp::")
                    return None

