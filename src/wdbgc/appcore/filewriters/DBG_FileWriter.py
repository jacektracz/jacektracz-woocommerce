import sys
import os
import traceback
import logging
from ... appcore.filewriters.DBG_FileWriterData import *
from ... appcore.logging.DBG_ExceptionPrinter import *

class DBG_FileWriter:
    m_file = []
    m_out = None
    m_err = None
    m_trace = None
    
    @staticmethod
    def trace_method(tt):
        """trace_method"""
        #print tt
    
        
    @staticmethod    
    def clear_files():
        try:
            
            if(DBG_FileWriter.m_out == None):
                DBG_FileWriter.m_out = DBG_FileWriterData()
                DBG_FileWriter.m_out.set_path_out()
                DBG_FileWriter.m_out.clear_file()
                
            if(DBG_FileWriter.m_err == None):
                DBG_FileWriter.m_err = DBG_FileWriterData()
                DBG_FileWriter._err.set_path_err()
                DBG_FileWriter.m_err.clear_file()
            
        except:
            DBG_FileWriter.print_exception_and_quit("\nexception_in_write_to_log")
            return 0
        
    @staticmethod        
    def initialize_files():
        try:
            if(DBG_FileWriter.m_out == None):
                DBG_FileWriter.m_out = DBG_FileWriterData()
                DBG_FileWriter.m_out.set_path_out()
                DBG_FileWriter.m_out.create_log_file()
                
                
            if(DBG_FileWriter.m_err == None):
                DBG_FileWriter.m_err = DBG_FileWriterData()
                DBG_FileWriter.m_err.set_path_err()
                DBG_FileWriter.m_err.create_log_file()
                
            if(DBG_FileWriter.m_trace == None):
                DBG_FileWriter.m_trace = DBG_FileWriterData()
                DBG_FileWriter.m_trace.set_path_err()
                DBG_FileWriter.m_trace.create_log_file()
                
        except:
            DBG_FileWriter.print_exception_and_quit("\nexception_in_write_to_log")
            return 0
        
    @staticmethod                
    def close_files():
        try:
            
            if(DBG_FileWriter.m_out != None):
                DBG_FileWriter.m_out.close_file()
                DBG_FileWriter.m_out = None
                    
            if(DBG_FileWriter.m_err != None):
                DBG_FileWriter.m_err.close_file()
                DBG_FileWriter.m_err = None
                
            if(DBG_FileWriter.m_trace != None):
                DBG_FileWriter.m_trace.close_file()
                DBG_FileWriter.m_trace = None
                    
        except:
            DBG_FileWriter.print_exception_and_quit("\nexception_in_write_to_log")
            return 0
        
    def write_to_log(self,p_str):        
        DBG_FileWriter.write_to_out(p_str)
        
    @staticmethod 
    def write_to_out(p_str):
        try:
            DBG_FileWriter.initialize_files()
            DBG_FileWriter.write_to_file(p_str,DBG_FileWriter.m_out)
            return 1 
        except:
            DBG_FileWriter.print_exception_and_quit("\nexception_in_write_to_log")
            return 0
        
    @staticmethod 
    def write_to_err(p_str):
        try:
            DBG_FileWriter.initialize_files()
            DBG_FileWriter.write_to_file(p_str,DBG_FileWriter.m_err)
            return 1 
        except:
            DBG_FileWriter.print_exception_and_quit("\nexception_in_write_to_log")
            return 0

    @staticmethod 
    def write_to_trace(p_str):
        try:
            DBG_FileWriter.initialize_files()
            DBG_FileWriter.write_to_file(p_str,DBG_FileWriter.m_trace)
            return 1 
        except:
            DBG_FileWriter.print_exception_and_quit("\nexception_in_write_to_log")
            return 0
        
    @staticmethod    
    def write_to_file(p_str,dd):
        try:
            
                        
            if(dd.m_log_file == None):
                DBG_FileWriter.d_write("DBG_FileWriter::write_to_file::{dd.m_log_file == None]")
                DBG_FileWriter.quit_process()
                return 0
                       
            
            dd.m_log_file.write(str(p_str))
            dd.m_log_file.write("\n")
            dd.m_log_file.flush()
            return 1 
        except:
            DBG_FileWriter.print_exception_and_quit("\nexception_in_write_to_log")
            return 0
        
    @staticmethod 
    def d_write(p_str):
        """d_write"""
        print p_str

    @staticmethod    
    def print_exception_and_quit( tt ):
        """print_exception_and_quit"""
        #logging.exception('')
        DBG_FileWriter.print_exception_internal(tt)
        DBG_FileWriter.quit_process()
        
    @staticmethod    
    def write_to_log_exception( tt ):
        """print_exception_and_quit"""
        #logging.exception('')
        DBG_FileWriter.print_exception_internal(tt)
    
    
    @staticmethod    
    def print_exception_internal( tt ):
        """print_exception_and_quit"""                
        try:
            s_ex =   sys.exc_info()[0]            
            DBG_FileWriter.write_to_err(tt + str(s_ex))
        except:
            DBG_ExceptionPrinter.print_exception(tt)
            
    @staticmethod        
    def quit_process():
        #os._exit(1)
        quit()
