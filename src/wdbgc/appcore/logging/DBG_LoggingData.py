import sys
import os
import logging

from ... appcore.config.DBG_PrintConfig import *
from ... appcore.logging.DBG_ExceptionPrinter import *
from ... appcore.logging.DBG_LoggerItem import *


class DBG_LoggingData:
    def __init__(self,sdbg,sfile_dbg):
            self.m_dbg_logger =  DBG_LoggerItem(sfile_dbg)
            self.m_err_logger =  DBG_LoggerItem(sfile_dbg + "_err.txt")
            self.m_out_logger =  DBG_LoggerItem(sfile_dbg + "_out.html")
            
    def log_info(self,tt):
        self.m_dbg_logger.logger.info(tt)
        
    def exc_info(self,tt):
        self.m_dbg_logger.logger.info(tt)
        self.m_err_logger.logger.info(tt)