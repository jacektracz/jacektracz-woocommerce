import sys
import traceback
import logging
from ... appcore.config.DBG_PrintConfig import *
from ... appcore.logging.DBG_ExceptionPrinter import *

class DBG_FileWriterData:
    
#==================================================================
#
#==================================================================
    
    def __init__(self):
        self.m_log_file = None
        self.m_log_file_opened = 0;
        self.m_use_logger = 1;
        self.m_full_path = ""        
        self.m_prefix = "iastora2"
        
    def set_path_out(self):
        try:
            self.xx_dbg("DBG_FileWriterData::set_path_out::in")
            self.m_full_path = DBG_PrintConfig().getItem().get_path_out("")
            self.xx_dbg("DBG_FileWriterData::set_path_out::out::" + self.m_full_path)
        except:
            self.xx_exception("DBG_FileWriterData::clear_file")
        
        
    def set_path_err(self):
        try:
            self.xx_dbg("DBG_FileWriterData::set_path_err::in::")        
            self.m_full_path = DBG_PrintConfig().getItem().get_path_err("")
            self.xx_dbg("DBG_FileWriterData::set_path_err::out::" + self.m_full_path)
        except:
            self.xx_exception("DBG_FileWriterData::clear_file")

    def set_path_trace(self):
        try:
            self.xx_dbg("DBG_FileWriterData::set_path_err::in::")        
            self.m_full_path = DBG_PrintConfig().getItem().get_path_trace("")
            self.xx_dbg("DBG_FileWriterData::set_path_err::out::" + self.m_full_path)
        except:
            self.xx_exception("DBG_FileWriterData::clear_file")
        
    def get_root_dir(self):
        tt = DBG_PrintConfig().getItem().get_root_dir()
        return tt
    
    def get_prefix(self):        
        return self.m_prefix
    
    def create_log_file(self,mode = "a"):
        try:
            self.xx_dbg("DBG_FileWriterData::create_log_file::in")
            self.clear_file()
            if(self.m_log_file == None):
                self.m_log_file = open(self.m_full_path,"a")
            self.xx_dbg("DBG_FileWriterData::create_log_file::out")    
        except:
            self.xx_exception("DBG_FileWriterData::clear_file")
           
    def close_file(self):
        try:
            self.xx_dbg("DBG_FileWriterData::close_file::in")
            if(self.m_log_file != None):
                if(not self.m_log_file.closed):
                    self.m_log_file.close()
            #self.xx_dbg("DBG_FileWriterData::close_file::out")
        except:
            self.xx_exception("DBG_FileWriterData::clear_file")
        
    def clear_file(self,p_str = ""):
        try:
            self.xx_dbg("DBG_FileWriterData::clear_file::in")
            if(self.m_log_file == None):
                self.m_log_file = open(self.m_full_path,"wb")
            else:
                if(self.m_log_file.closed):
                    self.m_log_file = open(self.m_full_path,"wb")
                else:
                    self.m_log_file.close()
                    self.m_log_file = open(self.m_full_path,"wb")
                    
            self.m_log_file.write("")
            self.m_log_file.close()
            self.m_log_file = None
            self.xx_dbg("DBG_FileWriterData::clear_file::out")
        except:
            self.xx_exception("DBG_FileWriterData::clear_file")
            
    def xx_dbg(self,tt):
        """ DBG_FileWriterData::xx_dbg """
        #sinfo = "[file:" + self.m_full_path + "]"
        #DBG_ExceptionPrinter.xx_dbg(sinfo + tt)
    
    def xx_exception(self,tt):
        DBG_ExceptionPrinter.print_exception(tt)
    