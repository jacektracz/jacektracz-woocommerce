import sys
import os
import logging

from ... appcore.config.DBG_PrintConfig import *
from ... appcore.logging.DBG_ExceptionPrinter import *
from ... appcore.exceptions.DBG_MainExceptionsSet import *
from ... appcore.filewriters.DBG_FileWriter import *
from ... appcore.htmlwriters.DBG_MainPrintDispatcher import *
from ... appcore.logging.DBG_LoggingFactory import *

        
class DBG_Log:
    
    def __init__(self):
            self.m_name = ""
                        
    def xx_dbg(self,ss):
        try:
            
            dd = DBG_PrintConfig().getItem().m_dbg_all                             
            if(dd == 1 ):                
                DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( ss ) 
                
            dd = DBG_PrintConfig().getItem().m_dbg_all_logger                             
            if(dd == 1 ):
                DBG_LoggingFactory().log_info(ss)
                
        except:
            tt = "[DBG_Log::xx_dbg::]"
            DBG_ExceptionPrinter.print_exception(tt)
            quit()          
            
    def xx_exc(self,ss):
        try:
            if(DBG_PrintConfig().getItem().m_exit_on_exception ==1):
                logging.exception('')
                quit()
                
            dd = DBG_PrintConfig().getItem().m_dbg_all_logger
            if(dd == 1 ):
                DBG_LoggingFactory().exc_info(ss)
            
            if(DBG_PrintConfig().getItem().m_print_all_errors ==1):
                print ss
                logging.exception('')
                DBG_ExceptionPrinter.print_exception( ss )
                
            if(DBG_PrintConfig().getItem().m_log_all_errors ==1):                            
                DBG_FileWriter.write_to_log_exception(ss)
                
            if(DBG_PrintConfig().getItem().m_store_errors == 1):            
                DBG_MainExceptionsSet(self,"xx_exc").add_exception ( ss )                
                
            return ""
        except:
            tt = "[DBG_Log::xx_exc::]"
            logging.exception('')
            quit()          
            DBG_ExceptionPrinter.print_exception(tt + ss)
            
