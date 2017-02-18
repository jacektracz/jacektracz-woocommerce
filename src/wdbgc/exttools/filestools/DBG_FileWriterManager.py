#==================================================================
#
#    
#    
#==================================================================

import sys
import traceback
from DBG_FileWriterData import DBG_FileWriterData
from ... DBG_AdapterBase import *

#==================================================================
#
#==================================================================

class DBG_FileWriterManager:
    m_file = []

    @staticmethod
    def trace_method(tt):
        print tt
        
#==================================================================
#
#==================================================================
        
    @staticmethod    
    def print_exception( tt ):
        """print_exception"""
            
        print tt,
          
        try:
            s_ex =   sys.exc_info()[0]
            print s_ex
            
        except:            
            print "ex"

        try:
            print 'print_exc():'
            traceback.print_exc(file=sys.stdout)
            print
            print 'print_exc(1):'
            traceback.print_exc(limit=1, file=sys.stdout)
        except:
            
            print "ex"
        
        
#==================================================================
#
#==================================================================
    
    def init_log_file(self):
        
        if(len(self.m_file) == 0):
            dd = DBG_FileWriterData()
            self.m_file.append(dd)

#==================================================================
#
#==================================================================
        
    def set_to_loging_self_log(self):
        print "[METHOD_IN][set_to_loging_self_log]"
        self.init_log_file()
        self.m_file[0].m_use_logger = 1
        print "[METHOD_OUT][set_to_loging_self_log]"
#==================================================================
#
#==================================================================
        
    def uset_to_loging_self_log(self):
        print "[METHOD_IN][uset_to_loging_self_log]"
        self.init_log_file()
        self.m_file[0].m_use_logger = 0
        print "[METHOD_OUT][uset_to_loging_self_log]"        
#==================================================================
#
#==================================================================

    def get_log_file(self):
        self.init_log_file()
        return self.m_file[0]

#==================================================================
#
#==================================================================

    @staticmethod
    def get_line(tt):
        return tt
    
#==================================================================
#

#==================================================================

    @staticmethod
    def setup_logging_spec():
        dt = datetime.now()
        s_log_header = "/rksup/config/kgr35jut/jut/python/finder_log/finder_static_logY"  
        s_log_file = DBG_FileWriterManager.get_line( 
            s_log_header
            + "_Y_" + str(dt.year)    
            + "_MN_" +  str( dt.month )
            + "_D_" + str(dt.day) 
            + "_H_" + str(dt.hour) 
            + "_M_" + str(dt.minute) 
            + "_S_" + str(dt.second) 
            + ".txt"    )
        
        return s_log_file

#==================================================================
#
#==================================================================


    def setup_logging_create_log_file(self):
        try:
            DBG_FileWriterManager.trace_method("[INFO_METHOD_IN][setup_logging_create_log_file]") 
            self.init_log_file()
            #dd = self.get_log_file()
            s_file = DBG_FileWriterManager.setup_logging_spec()    
            
            self.m_file[0].m_log_file = open(s_file,"w")
            self.m_file[0].m_log_file_opened = 1 
            print "[setup_logging_create_log_file][Log opened]" , s_file
            DBG_FileWriterManager.trace_method("[INFO_METHOD_OUT][setup_logging_create_log_file]")
        except:
            DBG_FileWriterManager.print_exception("\nexception")
            print "exception_in_create_log_file"
            
#==================================================================
#
#==================================================================
        
    def close_log_file(self):
        try:
            
            DBG_FileWriterManager.trace_method("[INFO_METHOD_IN][close_log_file]")
            
            self.init_log_file()            
            
            if(self.m_file[0].m_log_file_opened):
                self.m_file[0].m_log_file.close()
                self.m_file[0].m_log_file_opened = 0
                
            DBG_FileWriterManager.trace_method("[INFO_METHOD_OUT][close_log_file]")
            
        except:
            DBG_FileWriterManager.print_exception("\nexception")
            print "exception_in_create_log_file"
        
#==================================================================
#
#==================================================================

    def write_to_log(self,p_str):
        try:
            self.init_log_file()
            
            #file = self.get_log_file()
            #file.write(str)
            dd = DBG_FileWriterData()        
            dd = self.m_file[0]
            
            if(dd.m_use_logger == 1):
                if(dd.m_log_file_opened == 1):
                    if isinstance(p_str,str):
                        dd.m_log_file.write(str(p_str))
                        dd.m_log_file.write("\n")                
            return 1 
        except:
            #
            DBG_FileWriterManager.print_exception("\nexception_in_write_to_log")
            return 0

