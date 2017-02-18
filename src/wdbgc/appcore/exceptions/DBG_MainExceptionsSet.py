import sys
import os
import logging
import traceback
from ... appcore.exceptions.DBG_ExceptionsData import *
from ... appcore.config.DBG_PrintConfig import *
           
class DBG_MainExceptionsSet:
    
    m_data = None
    
    def __init__(self,pparent,sdbg):
        self.m_parent = pparent        

    def get_exceptions(self):
        try:
            if(self.__class__.m_data == None):
                self.__class__.m_data = DBG_ExceptionsData()				
            return self.__class__.m_data
        except:
                self.xx_exception("DBG_MainExceptionsSet::getItem::excp::")
                return None
            
    def add_exception(self,tt):
        try:
            #sex1 = repr(traceback.extract_stack())
            s_exc = repr(traceback.format_stack())
            maxdef = DBG_PrintConfig().getItem().get_max_g_stored_errors()
            is_stored = self.get_exceptions().get_len()            
            if(is_stored < maxdef):                
                self.get_exceptions().add_exception(tt + ":" + str(s_exc))
        except:
            self.xx_exception("DBG_MainExceptionsSet::getItem::excp::")
        
    def get_exc_as_strings(self):
        try:
            return self.get_exceptions().get_strings()
        except:
            self.xx_exception("DBG_MainExceptionsSet::getItem::excp::")        
            
    def xx_exception(self,tt):
        print "DBG_MainExceptionsSet::exception" + tt
        logging.exception("")
            
            