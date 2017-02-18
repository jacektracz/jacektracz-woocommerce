import sys
import pexpect
from JT_Logger import JT_Logger
from JT_LoggerSettings import JT_LoggerSettings
from JT_Logger import JT_StaticLogger


from JT_Files import JT_Files
#==================================================================
#
#==================================================================


class JT_ExecKgrUtils:

#==================================================================
#
#==================================================================

    def __init__(self):
        self.m_logs = JT_Files()
        self.m_test = 1

#==================================================================
#
#==================================================================

    def exec_utils(self):
        try:
            JT_StaticLogger.setup_logging_main()
            JT_LoggerSettings().set_to_output()
                                    
            JT_Logger.trace_method("[METHOD_IN][exec_utils]")
            arg_2 = sys.argv[2]            
            if(arg_2 == "ls_loginfo"):
                kgr_3 = sys.argv[3]
                self.ls_logging(kgr_3)
                
            if(arg_2 == "ls_log"):
                kgr_3 = sys.argv[3]
                self.ls_log( kgr_3 )
                
            JT_Logger.trace_method("[METHOD_OUT][exec_utils]")
                        
        except:
            JT_Logger.print_exception("\nexception")
            print "error_in_setup_logging"

#==================================================================
#
#==================================================================
        
    def ls_logging(self,p_kgr):
        try:
            JT_Logger.trace_method("[METHOD_IN][ls_logging]")
            cmd = "ls -la /rksup/log/" + p_kgr + "/logs_info"
            
            JT_Logger.print_output( cmd )
            
            print pexpect.run(cmd)
            JT_Logger.trace_method("[METHOD_OUT][ls_logging]")            
        except:
            JT_Logger.print_exception("\nexception")
            print "error_in_setup_logging"
            
#==================================================================
#
#==================================================================
        
    def ls_log(self,p_kgr):
        try:
            JT_Logger.trace_method("[METHOD_IN][ls_logging]")
            cmd = "ls -lt /rksup/log/" + p_kgr 
            
            JT_Logger.print_output( cmd )
            
            print pexpect.run(cmd)
            
            JT_Logger.trace_method("[METHOD_OUT][ls_logging]")            
        except:
            JT_Logger.print_exception("\nexception")
            print "error_in_setup_logging"
