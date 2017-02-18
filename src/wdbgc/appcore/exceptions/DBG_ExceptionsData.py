import sys
import os
import logging

from ... appcore.exceptions.DBG_ExceptionData import *
        
        
class DBG_ExceptionsData:
    def __init__(self):
        self.m_exceptions = []
        
    def add_exception(self,tt):
        try:
            dd = DBG_ExceptionData()
            dd.m_ex_str = tt        
            self.m_exceptions.append( dd )
        except:
            self.xx_exception("DBG_ExceptionsData::add_exception::excp::")
            
    def get_strings(self):
        try:
            outa = []
            for dd_ii in self.m_exceptions:
                    outa.append(dd_ii.m_ex_str)
            return outa
        except:
            self.xx_exception("DBG_ExceptionsData::get_strings::excp::")
            
    def get_len(self):
        try:
            ddo = len(self.m_exceptions)            
            return ddo
        except:
            self.xx_exception("DBG_ExceptionsData::get_strings::excp::")
            
    def xx_exception(self,tt):
        print "DBG_ExceptionsData::exception" + tt
        logging.exception("")
            
