import sys
import os
import logging

from ... appcore.config.DBG_PrintConfig import *
from ... appcore.logging.DBG_ExceptionPrinter import *
from ... appcore.logging.DBG_LoggingData import *

        
class DBG_LoggingFactory:
    m_data = None
    def __init__(self):
            self.m_name = ""
            
    def get_data(self):
        try:
            if(self.__class__.m_data == None):
                log_file = DBG_PrintConfig().getItem().get_path_logging("c:/iastora.log")
                self.__class__.m_data = DBG_LoggingData("DBG_Log::get_data",log_file)	
            return self.__class__.m_data
        except:
                tt = "[DBG_LogFactory::get_data::]"
                DBG_ExceptionPrinter.print_exception(tt)
                quit()          
        
    def log_info(self,tt):
        self.get_data().log_info(tt)
        
    def exc_info(self,tt):
        self.get_data().exc_info(tt)
