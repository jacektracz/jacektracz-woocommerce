import sys
import os
import logging
import traceback
from ... appcore.config.DBG_PrintConfig import *
from ... appcore.globinfo.DBG_InformationsData import *

class DBG_MainInformationsSet:
    
    m_data = None
    
    def __init__(self,pparent,sdbg):
        self.m_parent = pparent        

    def get_information(self):
        try:
            if(self.__class__.m_data == None):
                self.__class__.m_data = DBG_InformationsData()				
            return self.__class__.m_data
        except:
                self.xx_exception("DBG_MainInformationsSet::getItem::excp::")
                return None
            
    def add_information(self,tt):
        try:
            self.get_information().add_information( str( tt ))
        except:
            self.xx_exception("DBG_MainInformationsSet::getItem::excp::")
        
    def get_infos_as_strings(self):
        try:
            return self.get_information().get_strings()
        except:
            self.xx_exception("DBG_MainInformationsSet::getItem::excp::")
            s_exc = ["exception_in_get_infos_as_strings"]
            return s_exc
            
    def xx_exception(self,tt):
        print "DBG_MainInformationsSet::exception" + tt
        logging.exception("")
            
            