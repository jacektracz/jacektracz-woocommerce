#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

import sys
import traceback




from JT_LoggerSettings import JT_LoggerSettings
from JT_StaticLogger import JT_StaticLogger
#==================================================================
#
#JT_LoggerSettings:
#
#==================================================================
    
#==================================================================
#    
#==================================================================

class JT_Logger:

#==================================================================
#
#==================================================================
        
    @staticmethod    
    def trace_hard_level_20( tt ):
        """trace_hard_level_20"""
        tt = JT_Logger.format_line_to_prnt ( tt )
        if JT_LoggerSettings().STDOUT_HARD() == 1:            
            print tt
            
        JT_StaticLogger.exetute_logging( tt )
            
#==================================================================
#
#==================================================================
            
    @staticmethod    
    def log_ps_line( tt ):
        """print_exception"""
        #JT_Logger.trace_hard_level_18(tt)

#==================================================================
#
#==================================================================

    @staticmethod    
    def log_ps_line_hard( tt ):
        """print_exception"""
        tt = JT_Logger.format_line_to_prnt ( tt )
        if JT_LoggerSettings().STDOUT_HARD() == 1:            
            print tt        
        JT_Logger.trace_hard_level_18(tt)
        
#==================================================================
#
#==================================================================
        
    @staticmethod    
    def print_exception( tt ):
        """print_exception"""
        
        tt = JT_Logger.format_line_to_prnt ( tt )
        
        print tt
          
        try:
            s_ex =   sys.exc_info()[0]
            print s_ex
        except:
            JT_StaticLogger.print_exception("\nexception")
            print "ex"

        try:
            print 'print_exc():'
            traceback.print_exc(file=sys.stdout)
            print
            print 'print_exc(1):'
            traceback.print_exc(limit=1, file=sys.stdout)
        except:
            JT_StaticLogger.print_exception("\nexception")
            print "exception "
            
        try:        
            JT_StaticLogger.exetute_logging( tt )
        except:
            print " exception JT_StaticLogger.exetute_logging( tt )"
        
#==================================================================
#
#==================================================================
    @staticmethod            
    def trace_method_inside(p_method_name,p_message):
        """trace_method"""
        p_message = JT_Logger.format_line_to_prnt ( p_message )
        JT_Logger.trace_method("[METHOD_INSIDE][" + p_method_name + "][" + p_message + "]")
            
    @staticmethod            
    def trace_method(tt):
        """trace_method"""
        tt = JT_Logger.format_line_to_prnt ( tt )
        if JT_LoggerSettings().STDOUT_HARD() == 1:
            print tt

        JT_StaticLogger.exetute_logging( tt )
#==================================================================
#
#==================================================================
        
    @staticmethod    
    def trace_hard_level_19( tt):
        """trace_hard_level_19"""
        tt = JT_Logger.format_line_to_prnt ( tt )
        if JT_LoggerSettings().STDOUT_HARD() == 1:
            print tt
        JT_StaticLogger.exetute_logging( tt )
        
#==================================================================
#
#==================================================================

    @staticmethod    
    def trace_hard_level_18( tt):
        """trace_hard_level_18"""
        tt = JT_Logger.format_line_to_prnt ( tt )
        if JT_LoggerSettings().STDOUT_HARD() == 1:
            print tt
        JT_StaticLogger.exetute_logging( tt )
        
#==================================================================
#
#==================================================================
        
    @staticmethod    
    def trace_hard_level_17( tt):
        """trace_hard_level_17"""
        tt = JT_Logger.format_line_to_prnt ( tt )
        if JT_LoggerSettings().STDOUT_HARD() == 1:
            print tt
        JT_StaticLogger.exetute_logging( tt )
        
        
#==================================================================
#
#==================================================================
        
    @staticmethod    
    def trace_hard_level_16( tt):
        """trace_hard_level_16"""
        tt = JT_Logger.format_line_to_prnt ( tt )
        if JT_LoggerSettings().STDOUT_HARD() == 1:
            print tt
        JT_StaticLogger.exetute_logging( tt )

#==================================================================
#
#==================================================================

    @staticmethod    
    def print_to_log_only( tt):
        """print_to_log_only"""     
        tt = JT_Logger.format_line_to_prnt ( tt )   
        JT_StaticLogger.exetute_logging(tt)
        
#==================================================================
#
#==================================================================
    @staticmethod    
    def print_output_raw( tt):
        """print_output"""
        print tt

    @staticmethod    
    def print_output( tt):
        """print_output"""
        tt = JT_Logger.format_line_to_prnt ( tt )
        print tt
        JT_StaticLogger.exetute_logging(tt)
     
#==================================================================
#
#==================================================================

    @staticmethod    
    def print_stdout( tt ):
        """print_stdout"""
        tt = JT_Logger.format_line_to_prnt ( tt )
        JT_StaticLogger.print_stdout(tt)        
        
#==================================================================
#
#==================================================================
        
    @staticmethod    
    def print_output_no_log( tt):
        """print_output"""
        tt = JT_Logger.format_line_to_prnt ( tt )        
        print tt        

#==================================================================
#
#==================================================================
    
    @staticmethod
    def format_line_to_prnt(p_ll):
        try:
            ll_out = ""
            if(p_ll == None):
                p_ll = ""
                
            if(len(p_ll) > 10048):
                ll_out = "TOO_LONG_LINE_TO_PRINT" 
            else:
                ll_out = p_ll
                
            return ll_out            
        except :
            return "ERROR_IN_LINE"
        
#==================================================================
#
#JT_StaticLogger
#
#==================================================================


