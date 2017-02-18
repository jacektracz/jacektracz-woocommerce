#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

#!/opt/csw/bin/python2.6
#!/usr/bin/python
#import pexpect
#lw


import sys


from JT_Logger import JT_Logger
from JT_ExecKgrUtils import JT_ExecKgrUtils
from JT_LoggerSettings import JT_LoggerSettings
from JT_Logger import JT_StaticLogger



from JT_MonitorKgr import JT_MonitorKgr
from JT_KgrStarters import JT_KgrStarters
import pexpect
from JT_LogWritingAnaliser import JT_LogWritingAnaliser
from JT_LogReadingAnaliser import JT_LogReadingAnaliser
#==================================================================
#
#==================================================================


class JT_ExecuteMain:
    
        
#==================================================================
#
#==================================================================

    def exec_main(self):
            
        try:
            JT_StaticLogger.setup_logging_main()
            if ( len(sys.argv) > 1 ):
                arg_1 = sys.argv[1]
                l_exec = 0 
                if( arg_1 == "env"):
                    l_exec = 1    
                    JT_LoggerSettings().set_to_output()                
                    JT_LogWritingAnaliser().exec_main_env()
                    
    
                if( arg_1 == "etail"):
                    l_exec = 1    
                    JT_LogWritingAnaliser().exec_main_logs_print_number_of_lines()
    
                if( arg_1 == "tmark"):
                    l_exec = 1    
                    JT_LogWritingAnaliser().exec_main_test_1()                
    
                if( arg_1 == "imarks"):
                    l_exec = 1
                    JT_LogWritingAnaliser().exec_main_imarks()
                    
                if( arg_1 == "iemarks"):
                    l_exec = 1
                    JT_LogWritingAnaliser().exec_main_iemarks()

                if( arg_1 == "cplogs"):
                    l_exec = 1
                    JT_LogWritingAnaliser().exec_main_create_copy_of_logs()
                    
                if( arg_1 == "pmarks"):
                    l_exec = 1
                    JT_LogWritingAnaliser().exec_main_pmarks_all_files_marks_from_args()

                if( arg_1 == "pmarks_def"):
                    l_exec = 1
                    JT_LogWritingAnaliser().exec_main_pmarks_def_print_files_within_last_two()
                    
                if( arg_1 == "pmarks_find"):
                    l_exec = 1
                    JT_LogWritingAnaliser().exec_main_pmarks_find_in_first_file()

                if( arg_1 == "plogs"):
                    l_exec = 1
                    kgr_2 = sys.argv[2]                    
                    JT_LogWritingAnaliser().print_log_files(kgr_2)
                    
                if( arg_1 == "pmarks_comp"):
                    l_exec = 1
                    JT_LogWritingAnaliser().exec_main_pmarks_comp_print_files_within_computed_two()

                if( arg_1 == "ls_la"):
                    l_exec = 1                    
                    print pexpect.run('ls -la')
                    
                if( arg_1 == "start_kgr35s"):
                    l_exec = 1                    
                    dd_starter = JT_KgrStarters()
                    dd_starter.start_main_kgr35s()

                if( arg_1 == "iemarks_2"):
                    l_exec = 1
                    JT_LogReadingAnaliser().exec_main_iemarks()
                    
                if( arg_1 == "pmarks_def_2"):
                    l_exec = 1                    
                    JT_LogReadingAnaliser().exec_main_pmarks_def_print_files_within_last_two()

                if( arg_1 == "utils"):
                    l_exec = 1                    
                    JT_ExecKgrUtils().exec_utils()

                if( arg_1 == "ffile"):
                    l_exec = 1                                    
                    JT_LogWritingAnaliser().exec_main_print_whole_line_formatted()
                    
                if( arg_1 == "ffile_sel"):
                    l_exec = 1                                    
                    JT_LogWritingAnaliser().exec_main_print_whole_line_formatted_sel()
                    
                if (l_exec == 0 ) :
                    l_exec = 1                       
                    JT_MonitorKgr().exec_main_monitor_kgr()

                    
            JT_StaticLogger.close_logging()
            
        except:        
            JT_StaticLogger.close_logging()
            JT_Logger.print_exception("\nError: exception in main \n")
                
#==================================================================
#
#==================================================================

