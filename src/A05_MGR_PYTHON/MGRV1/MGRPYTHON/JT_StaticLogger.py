#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

import sys
#import logging
import traceback
from datetime import datetime
from JT_LoggerSettings import JT_LoggerSettings
from JT_StaticLoggerFile import JT_StaticLoggerFile

#==================================================================
#
#==================================================================
        
class JT_StaticLogger:

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
            
            #JT_StaticLogger.exetute_logging( tt + s_ex)
            
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
    @staticmethod
    def get_line(pp):
        return pp
        
#==================================================================
#
#==================================================================
    
    @staticmethod
    def setup_logging_main():
        JT_LoggerSettings().set_to_output()
        JT_StaticLogger.trace_method("[INFO_METHOD_IN][setup_logging_main]")        
        try:                        
            JT_StaticLoggerFile().setup_logging_create_log_file()
        except:
            JT_StaticLogger.print_exception("\nexception")
            print "error_in_setup_logging"
            
        try:
            JT_StaticLogger.setup_logging_lib()            
            
        except:
            JT_StaticLogger.print_exception("\nexception")
            print "error_in_setup_logging"
        
        JT_StaticLogger.trace_method("[INFO_METHOD_OUT][setup_logging_main]")
            
#==================================================================
#
#==================================================================

#==================================================================
#
#==================================================================
            
    @staticmethod    
    def setup_logging_lib():
        try:
            dt = datetime.now()
            s_log_header = "/rksup/config/kgr35jut/jut/python/finder_log/finder_logY"  
            s_log_file = JT_StaticLogger.get_line( 
                s_log_header
                + "_Y_" + str(dt.year)    
                + "_MTH_" +  str( dt.month )
                + "_D_" + str(dt.day) 
                + "_H_" + str(dt.hour) 
                + "_M_" + str(dt.minute) 
                + "_S_" + str(dt.second) 
                + ".txt"    )
            
            #l = logging.INFO
            #print "LOG_FILENAME:",s_log_file
            #logging.basicConfig(level=logging.INFO, filename=s_log_file)
            #logging.info("START_LOGGING")
                
            #JT_Os.run_subprocess_popen_strip("mkdir /rksup/config/kgr35jut/jut/python/finder_log/bck/")
            #JT_Os.run_subprocess_popen_strip("mv /rksup/config/kgr35jut/jut/python/finder_log/*.txt /rksup/config/kgr35jut/jut/python/finder_log/bck/")
            
            return s_log_file
        except:
            JT_StaticLogger.print_exception("\nexception")
            print "error_in_setup_logging"

#==================================================================
#
#==================================================================
        
    @staticmethod
    def exetute_logging(tt):
        try:        
            #logging.info(tt)
            JT_StaticLoggerFile().write_to_log(tt)
        except:
            print "error_in_exetute_logging"
#==================================================================
#
#==================================================================
    
    @staticmethod
    def close_logging():
        try:                    
            JT_StaticLoggerFile().close_log_file()
        except:
            print "error_in_close_logging"

#==================================================================
#
#==================================================================
            
    @staticmethod    
    def print_stdout( tt ):
        """print_stdout"""     
        sys.stdout.write( tt )   
            
