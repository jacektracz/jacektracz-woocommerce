import sys
import os
import logging

from ... appcore.globinfo.DBG_InformationData import *
        
        
class DBG_InformationsData:
    def __init__(self):
        self.m_strings = []
        
    def add_information(self,tt):
        try:
            dd = DBG_InformationData()
            dd.m_ex_str = tt        
            self.m_strings.append( dd )
        except:
            self.xx_exception("DBG_InformationsData::add_exception::excp::")
            
    def get_strings(self):
        try:
            outa = []
            for dd_ii in self.m_strings:
                    outa.append(dd_ii.m_ex_str)
            return outa
        except:
            self.xx_exception("DBG_InformationsData::get_strings::excp::")
            
    def get_len(self):
        try:
            ddo = len(self.m_strings)            
            return ddo
        except:
            self.xx_exception("DBG_InformationsData::get_strings::excp::")
            
    def xx_exception(self,tt):
        print "DBG_InformationsData::exception" + tt
        logging.exception("")
            
