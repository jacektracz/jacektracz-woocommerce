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

from datetime import datetime

from JT_Environments import JT_Environments
from JT_Logger import JT_Logger
from JT_LoggerSettings import JT_LoggerSettings
from JT_Logger import JT_StaticLogger

from JT_Os import JT_Os
from JT_ManagerConfig import JT_ManagerConfig

from JT_Marks import JT_Marks
from JT_Files import JT_Files
from JT_Files import JT_File

from JT_Strings import JT_Strings_find_options
from JT_MonitorKgr import JT_MonitorKgr
#==================================================================
#
#==================================================================


class JT_LogWritingAnaliser:

#==================================================================
#
#==================================================================

    def __init__(self):
        self.m_logs = JT_Files()

#==================================================================
#
#==================================================================
        
    def create_log_files(self,p_kgr):
        JT_Logger.trace_hard_level_20("[METHOD_IN][create_log_files]")
        if (len(self.m_logs.m_files) == 0) :
            self.m_logs =  self.create_log_files_list(p_kgr)
        JT_Logger.trace_hard_level_20("[METHOD_OUT][create_log_files]")
        
#==================================================================
#
#==================================================================

    def show_header_0(self):
        #JT_Logger.print_output("KGR process monitor (c) 2011 REUTERS, Jacek Tracz\n")
        JT_Logger.print_output_no_log ("/-------------------------------------------------------/")
        JT_Logger.print_output_no_log ("")
        JT_Logger.print_output_no_log ("KGR Serv Monitor(c) Thomson Reuters 2011 by Jacek Tracz")
        JT_Logger.print_output_no_log ("")           
        JT_Logger.print_output_no_log ("/-------------------------------------------------------/")

#==================================================================
#
#==================================================================
        
    def show_header_1(self):
        #JT_Logger.print_output("KGR process monitor (c) 2011 REUTERS, Jacek Tracz\n")
        JT_Logger.print_output_no_log( "" )        
        JT_Logger.print_output_no_log( "[METHOD_IN][print_parameters]" )        
        JT_Logger.print_output_no_log( " python mon_ok.py " )
        JT_Logger.print_output_no_log( " [1][env_france_ptx,env_pol_gdy,kgr35s,kgr32c,kgr32a,kgr32b,fatih,kgrSet,env_test] " )
        JT_Logger.print_output_no_log( " [2][srv_all,srv_test,guiadapter] " )
        JT_Logger.print_output_no_log( " [3][print_ps_line,not_print_ps_line] " )
        JT_Logger.print_output_no_log( " [4][use_find,use_regex] " )
        JT_Logger.print_output_no_log( " [5][not_use_su,use_su]")
        JT_Logger.print_output_no_log( " [6][not_print_debug,print_debug]")
        JT_Logger.print_output_no_log( " [7][not_use_log,use_log]")        
        JT_Logger.print_output_no_log( " [8][no_ps_filter][jboss][fds]")
        JT_Logger.print_output_no_log( "" )
        JT_Logger.print_output_no_log( "" )

#==================================================================
#
#==================================================================

    def show_header(self):
        #JT_Logger.print_output("KGR process monitor (c) 2011 REUTERS, Jacek Tracz\n")
        JT_Logger.print_output( "[METHOD_IN][print_parameters]" )        
        JT_Logger.print_output( " python mon_ok.py " )
        JT_Logger.print_output( " [1][env_france_ptx,env_pol_gdy,kgr35s,kgr32c,kgr32a,kgr32b,fatih,kgrSet,env_test] " )
        JT_Logger.print_output( " [2][srv_all,srv_test,guiadapter] " )
        JT_Logger.print_output( " [3][print_ps_line,not_print_ps_line] " )
        JT_Logger.print_output( " [4][use_find,use_regex] " )
        JT_Logger.print_output( " [5][not_use_su,use_su]")
        JT_Logger.print_output( " [6][not_print_debug,print_debug]")
        JT_Logger.print_output( " [7][not_use_log,use_log]")
        JT_Logger.print_output( " [8][no_ps_filter][jboss][fds]")                
        JT_Logger.print_output( "" )
        JT_Logger.print_output( "" )

            
#==================================================================
#
#==================================================================
    
    def exec_main_env(self):
    
        dd_p_env = JT_Environments()
        dd_p_env.add_envs()
        dd_p_env.print_all_env()

#==================================================================
#
#==================================================================


    def get_params_srvs_from_args(self,dd_monitor):
        dd_srv = ["all"]
            
        if(dd_monitor.commarg_servers_2 == "all"):
            dd_srv = ["all"]
            
        if(dd_monitor.commarg_servers_2 == "test"):
            dd_srv = ["test"]
            
        if(dd_monitor.commarg_servers_2 == "guiadapter"):
            dd_srv = ["guiadapter"]
        return dd_srv    
        

            
#==================================================================
#
#==================================================================
    

    def print_head_for_file(self,p_file):
        JT_Logger.print_stdout("\n\n/*=================================================================*/")
        JT_Logger.print_stdout("*\n")
        JT_Logger.print_stdout("*\n")
        JT_Logger.print_stdout("\ntail -f " + p_file + "\n")
        JT_Logger.print_stdout("*\n")
        JT_Logger.print_stdout("*\n")
        JT_Logger.print_stdout("/*=====================================================================*/\n\n")

#==================================================================
#
#==================================================================

    def create_log_files_list(self,p_kgr):
        try:
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_log_files_list]")
            #JT_Os.run_subprocess_popen_strip("tail -f /rksup/log/kgr35s/KGRServer_master__stdout.log")
            #JT_Os.run_os_command("tail -f /rksup/log/kgrSet/KGRServer_master__stdout.log"
            
            dd_log_files = JT_Files()
            
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "kgr_log_watch","log")
            
            #dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "kgrLogger","log")
            
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "kglagent_k33__stdout","log")    
    
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "kglagent_ds40__stdout","log")
            
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "kglagent_ds50__stdout","log")

            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRAggregationServer_stdout","log")
            
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRAggregationServer_DBTraceFile","log")
            
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRImportServer_meta_stdout","log")

            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRReportBatch_stdout","log")

            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRTaskServer_1_stdout","log")
            
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRTaskServer_task_1_DBTraceFile","log")

            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRAdapter_stdout","log")
            
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "kglagent__stdout","log")
            
            dd_log_files.add_log_file_ex("/rksup/log", p_kgr, "KGRServer_master__stdout","log")
                                
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRServer_master__DBTraceFile","log")
            
            
            JT_Logger.trace_hard_level_20("[METHOD_OUT][create_log_files_list]")
            return dd_log_files
        except :
            JT_Logger.print_exception("exception_in_create_copy_of_log")
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][create_log_files_list]")
            dd_log_files_exc = JT_Files()
            return dd_log_files_exc
#==================================================================
#
#==================================================================
    def logs_print_number_of_lines(self,p_kgr,p_lines):
        JT_Logger.trace_hard_level_20("[METHOD_IN][logs_print_number_of_lines]")
        
        self.create_log_files(p_kgr)
        for dd_file in self.m_logs.m_files:
            self.logs_print_file(dd_file,p_lines)
            
        JT_Logger.trace_hard_level_20("[METHOD_OUT][logs_print_number_of_lines]")
#==================================================================
#
#==================================================================

    def create_copy_of_logs(self,p_kgr):
        try:
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_copy_of_logs]")
            self.create_log_files(p_kgr)
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_copy_of_logs][files_created]")    
            for dd_file in self.m_logs.m_files:
                JT_Logger.trace_hard_level_20("file_execution")
                
                JT_Logger.trace_hard_level_20("[create_copy_of_logs][file_execution]" 
                                              + "[m_full_path:"+ dd_file.m_full_path + "]")
    
                JT_Logger.trace_hard_level_20("[create_copy_of_logs][file_execution]" 
                                              + "[m_full_bck_path:"+ dd_file.m_full_bck_path + "]")
                
                self.create_copy_of_log(dd_file)
                
            JT_Logger.trace_hard_level_20("[METHOD_OUT][create_copy_of_logs]")
            
        except :
            JT_Logger.print_exception("exception_in_create_copy_of_log")
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][create_copy_of_logs]")
        
#==================================================================
#
#==================================================================
            
    def create_copy_of_log(self,p_dd_1):
        try:
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_copy_of_log]")
            p_dd = JT_File()
            p_dd = p_dd_1
            
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_copy_of_log]" 
                                          + "[m_full_path:" + p_dd.m_full_bck_path + "]")
            
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_copy_of_log]" 
                                          + "[m_full_bck_path:" + p_dd.m_full_bck_path + "]")
            
            s_cmd = "cp " + p_dd.m_full_path + " " +  p_dd.m_full_bck_path
            
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_copy_of_log]"  
                                          + "[s_cmd:" + s_cmd + "]")
            
            JT_Os.run_subprocess_popen_strip(s_cmd) 
            #JT_Os.run_os_command(s_cmd)
            JT_Logger.trace_hard_level_20("[METHOD_OUT][create_copy_of_log]")
        except :
            JT_Logger.print_exception("exception_in_create_copy_of_log")
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][create_copy_of_log]")
            
#==================================================================
#
#==================================================================
            
    def logs_print_file(self,dd_file,p_lines):
        try:
            JT_Logger.trace_hard_level_20("[METHOD_IN][logs_print_file]")
            self.print_head_for_file(dd_file.m_full_path)
            tt = JT_Os.tail_lines(dd_file.m_full_path,int(p_lines))            
            JT_Logger.print_stdout(tt)
            JT_Logger.trace_hard_level_20("[METHOD_OUT][logs_print_file]")
        except :
            JT_Logger.print_exception("\nError: can\'t add string to filen")
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][logs_print_file]")      

#==================================================================
#
#==================================================================
    def logs_insert_mark_test(self,p_mark,p_open_file_mode):
        JT_Logger.trace_hard_level_20("[METHOD_IN][logs_insert_mark_test]") 
        JT_Logger.trace_hard_level_20("[METHOD_IN][p_mark:" + p_mark + "]")
        JT_Logger.trace_hard_level_20("[METHOD_IN][p_open_file_mode:" + p_open_file_mode + "]")
        
        dd_file = JT_File ()
        dd_file.m_full_path = "/rksup/log/kgr35s/kgrLogger.log"
        self.logs_insert_mark_into_file(dd_file,p_mark,p_open_file_mode)
        JT_Logger.trace_hard_level_20("[METHOD_OUT][logs_insert_mark_test]")
#==================================================================
#
#==================================================================
    def print_log_files(self,p_kgr):
        try:
            JT_Logger.trace_method("[METHOD_IN][print_log_files]")
            
            self.create_log_files(p_kgr)
            
            for dd_file in self.m_logs.m_files:
                JT_Logger.print_output("LOG_FILE:" + dd_file.m_full_path)
            
            JT_Logger.trace_method("[METHOD_OUT][print_log_files]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_log_files]")
#==================================================================
#
#==================================================================

    def logs_print_files_within_marks(self,p_kgr,p_mark_start,p_mark_stop):
        try:
            JT_Logger.trace_hard_level_20("[METHOD_IN][logs_print_files_within_marks]")
            JT_Logger.trace_hard_level_20( "[p_kgr:" +  p_kgr + "]")
            JT_Logger.trace_hard_level_20( "[p_mark_start:" + p_mark_start + "]")                                                                          
            JT_Logger.trace_hard_level_20( "[p_mark_stop:" + p_mark_stop + "]")
    
            
            self.create_log_files(p_kgr)
            
            self.print_log_files(p_kgr)
            
            JT_Logger.print_output("\n/*====================================================/")
            JT_Logger.print_output("/*")
            JT_Logger.print_output("[METHOD_IN][START_LOOP_FIN_FILES]")                        
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*====================================================/")
            
            for dd_file in self.m_logs.m_files:
                dd_ff = JT_File()
                dd_ff = dd_file
                JT_LogWritingAnaliser.print_lines_within(dd_ff.m_full_path, p_mark_start,p_mark_stop)
    
            JT_Logger.print_output("\n/*====================================================/")
            JT_Logger.print_output("/*")
            JT_Logger.print_output("[METHOD_INSIDE][END_LOOP_FILES]")                        
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*====================================================/")
            
            JT_Logger.trace_hard_level_20("[METHOD_OUT][logs_print_files_within_marks]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][logs_print_files_within_marks]")

#==================================================================
#
#==================================================================

    @staticmethod
    def print_lines_within(p_filename,p_mark_start,p_mark_end):
        """print_lines_within"""

        
        try:
            JT_Logger.trace_method("[METHOD_IN][print_lines_within]")
            JT_Logger.trace_method("[p_filename:" + p_filename + "]")
            JT_Logger.trace_method("[p_mark_start:" + p_mark_start + "]")
            JT_Logger.trace_method("[p_mark_end:" + p_mark_end + "]")
        
            JT_Logger.print_output("\n/*====================================================/")
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*FILE:" + p_filename)
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*====================================================/")
            
            l_file = open(p_filename,'r')
            lines = l_file.read().split("\n")
            
            l_file.close()
            inside = 0
            not_print_line = 0        
            for ll in lines:
                if ll.find(p_mark_start) >= 0:
                    inside = 1
                    JT_Logger.print_output("INSIDE_MARK_START:" + p_mark_start +"\n")
                    not_print_line = 1
                    
                if ll.find(p_mark_end) >= 0:
                    inside = 0
                    JT_Logger.print_output("INSIDE_MARK_STOP_:" + p_mark_end +"\n")
                    not_print_line = 1
                    
                if(not_print_line == 0):
                    if( inside == 1 ):
                        JT_Logger.print_output(ll)
    
                not_print_line = 0
            
                
            JT_Logger.trace_method("[METHOD_OUT][print_lines_within]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_lines_within]")
            


#==================================================================
#
#==================================================================

    def find_marks_for_env_predef_in_first_file(self,p_kgr):
        JT_Logger.trace_method("[METHOD_IN][find_marks_for_env_predef_in_first_file]")
        dd_out =  self.find_marks_for_env_in_first_file(  p_kgr
                                                         , "JT_MARK_INPUT_JT_YEAR_2011_MONTH")
        JT_Logger.trace_method("[METHOD_OUT][find_marks_for_env_predef_in_first_file]")
        return dd_out
    
#==================================================================
#
#==================================================================
     
    def find_marks_for_env_in_first_file(self,p_kgr,p_mark_template):
        """find_marks_for_env"""
        try:
            JT_Logger.trace_method("[METHOD_IN][find_marks_for_env_in_first_file]")
            self.create_log_files(p_kgr)
            
            for dd_log_ii in self.m_logs.m_files :
                dd_log = JT_File()
                dd_log = dd_log_ii            
                dd_out = self.find_all_marks_within_file(
                                                         dd_log.m_full_path
                                                         ,p_mark_template)                            
                break
            JT_Logger.trace_method("[METHOD_OUT][find_marks_for_env_in_first_file]")
            return dd_out
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_marks_for_env_in_first_file]")
            dd_out_exc = JT_Marks()
            return dd_out_exc
        
#==================================================================
#
#==================================================================
    
    def find_all_marks_within_file(self,p_filename,p_mark_template):
        """find_all_marks_within_file"""
        try:
            JT_Logger.trace_method("[METHOD_IN][find_all_marks_within_file]") 
            JT_Logger.trace_method("[p_filename:" + p_filename + "]")
            JT_Logger.trace_method( "[p_mark_template:" + p_mark_template + "]")
            
            JT_Logger.print_output("\n/*====================================================/")
            JT_Logger.print_output("/*FINDED_MARKS")
            JT_Logger.print_output("/*FILE:" + p_filename)
            JT_Logger.print_output("/*MARK:" + p_mark_template)
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*====================================================/")
            
            l_file = open(p_filename,'r')
            lines = l_file.read().split("\n")
            
            l_file.close()
            dd_out = JT_Marks()
            
            for ll in lines:
                if ll.find(p_mark_template) >= 0:
                    JT_Logger.print_output("INSIDE_MARK:" + ll +"\n")
                    dd_out.add_Mark(str(ll).strip())
                    
                
            
            JT_Logger.trace_method("[METHOD_OUT][find_all_marks_within_file]")
            return dd_out
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_all_marks_within_file]")
            dd_exc = JT_Marks()
            return dd_exc

#==================================================================
#
#==================================================================

    def logs_insert_mark(self,p_kgr,p_mark,p_open_file_mode):
        try:
            JT_Logger.trace_hard_level_20("[METHOD_IN][logs_insert_mark]")
            JT_Logger.trace_hard_level_20( "[p_kgr:" +  p_kgr + "]")
            JT_Logger.trace_hard_level_20( "[p_mark:" + p_mark + "]")                                     
            JT_Logger.trace_hard_level_20( "[p_open_file_mode:" + p_open_file_mode + "]")
        
            self.create_log_files(p_kgr)
            
            for dd_file in self.m_logs.m_files:
                self.logs_insert_mark_into_file(dd_file,p_mark,p_open_file_mode)
                
            JT_Logger.trace_hard_level_20("[METHOD_OUT][logs_insert_mark]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][logs_insert_mark]")
        
        
#==================================================================
#
#==================================================================

    def logs_insert_mark_into_file(self,p_dd,p_mark,p_open_file_mode):
        
        try:
            JT_Logger.trace_hard_level_20("[METHOD_IN][logs_insert_mark_into_file]")
            JT_Logger.trace_hard_level_20( "[m_full_path:" +  p_dd.m_full_path + "]")                                     
            JT_Logger.trace_hard_level_20("[p_open_file_mode:" + p_open_file_mode + "]")
            
            JT_Logger.trace_hard_level_20("[OPEN_FILE:" +  p_dd.m_full_path + "]")
            l_file = open(p_dd.m_full_path,p_open_file_mode)
            #l_file.write("\n\nJT_MARK_START\n")
            l_file.write("JT_MARK_INPUT" + "_" + p_mark + "\n")
            #l_file.write("JT_MARK_END\n\n")
            JT_Logger.trace_hard_level_20("[WRITE_TO_FILE:" +  p_dd.m_full_path + "]")
            l_file.close()
            JT_Logger.trace_hard_level_20("[FILE_CLOSE:" +  p_dd.m_full_path + "]")
            JT_Logger.trace_hard_level_20("[METHOD_OUT][logs_insert_mark_into_file]")
        except :
            JT_Logger.print_exception("\nError: can\'t add string to filen")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][logs_insert_mark_into_file]")
                
#==================================================================
#
#==================================================================

    def exec_main_tail_kgrmaster(self,p_kgr,p_lines):
        JT_Logger.trace_hard_level_20("[METHOD_IN][exec_main_tail_kgrmaster]")
        self.create_log_files(p_kgr)
        #JT_Os.run_subprocess_popen_strip("tail -f /rksup/log/kgr35s/KGRServer_master__stdout.log")
        #JT_Os.run_os_command("tail -f /rksup/log/kgrSet/KGRServer_master__stdout.log"

                
        self.print_head_for_file("/rksup/log/" + p_kgr + "/KGRServer_master__stdout.log")
        tt = JT_Os.tail_lines("/rksup/log/" + p_kgr + "/KGRServer_master__stdout.log",int(p_lines))            
        JT_Logger.print_stdout(tt)
        
        self.print_head_for_file("/rksup/log/" + p_kgr + "/KGRAdapter_stdout.log")
        tt = JT_Os.tail_lines("/rksup/log/" + p_kgr + "/KGRAdapter_stdout.log",int(p_lines))
        JT_Logger.print_stdout(tt)
        
        self.print_head_for_file("/rksup/log/" + p_kgr + "/KGRServer_master__DBTraceFile.log")
        tt = JT_Os.tail_lines("/rksup/log/" + p_kgr + "/KGRServer_master__DBTraceFile.log",int(p_lines))
        JT_Logger.print_stdout(tt)
        
        self.print_head_for_file("/rksup/log/" + p_kgr + "/KGRTaskServer_1_stdout.log")
        tt = JT_Os.tail_lines("/rksup/log/" + p_kgr + "/KGRTaskServer_1_stdout.log",int(p_lines))
        JT_Logger.print_stdout(tt)
        
        self.print_head_for_file("/rksup/log/" + p_kgr + "/KGRTaskServer_task_1_DBTraceFile.log")
        tt = JT_Os.tail_lines("/rksup/log/" + p_kgr + "/KGRTaskServer_task_1_DBTraceFile.log",int(p_lines))
        JT_Logger.print_stdout(tt)
        
        self.print_head_for_file("/rksup/log/" + p_kgr + "/kgrLogger.log")
        tt = JT_Os.tail_lines("/rksup/log/" + p_kgr + "/kgrLogger.log",int(p_lines))
        JT_Logger.print_stdout(tt)
        
        self.print_head_for_file("/rksup/log/" + p_kgr + "/kglagent_k33__stdout.log")
        tt = JT_Os.tail_lines("/rksup/log/" + p_kgr + "/kglagent_k33__stdout.log",int(p_lines))
        JT_Logger.print_stdout(tt)


        self.print_head_for_file("/rksup/log/" + p_kgr + "/kglagent_ds40__stdout.log")
        tt = JT_Os.tail_lines("/rksup/log/" + p_kgr + "/kglagent_ds40__stdout.log",int(p_lines))
        JT_Logger.print_stdout(tt)
        
        self.print_head_for_file("/rksup/log/" + p_kgr + "/kglagent_ds50__stdout.log")
        tt = JT_Os.tail_lines("/rksup/log/" + p_kgr + "/kglagent_ds50__stdout.log",int(p_lines))
        JT_Logger.print_stdout(tt)
           
        #JT_Os.tail_f_loop("/rksup/log/" + p_kgr + "/KGRServer_master__stdout.log")
        
#==================================================================
#
#==================================================================
    
    def exec_main_mon(self):
        JT_Logger.trace_method("[METHOD_IN][exec_main_mon]")
        self.show_header_0()
        self.show_header_1()
                                                        
        JT_Strings_find_options().init_reg_ex_option()        
        JT_ManagerConfig().init_manager_config()        
        dd_monitor = JT_MonitorKgr()
        
        dd_monitor.exec_main_monitor_kgr()
        
        JT_Logger.trace_method("[METHOD_OUT][exec_main_mon]")
#==================================================================
#
#==================================================================
        
    @staticmethod            
    def get_mark_for_file():
        
        dt = datetime.now()
        s_log_file = JT_StaticLogger.get_line(
             "_YEAR_" +  str(dt.year)    
            + "_MONTH_" +  str( dt.month )                                        
            + "_DAY_" + str(dt.day)                                               
            + "_HOUR_" + str(dt.hour) 
            + "_MIN_" + str(dt.minute)
            + "_SEC_" + str(dt.second) )
                            
        return s_log_file

#==================================================================
#
#==================================================================

    def exec_main_pmarks_find_in_first_file(self):
        JT_LoggerSettings().set_to_output()
        #JT_LoggerSettings().uset_to_output()      
        JT_Logger.trace_method("[METHOD_IN][exec_main_pmarks_find_in_first_file]")
                                   
        kgr_2 = sys.argv[2]        
        self.find_marks_for_env_predef_in_first_file(kgr_2)
        JT_Logger.trace_method("[METHOD_OUT][exec_main_pmarks_find_in_first_file]")
        
#==================================================================
#
#==================================================================
    
    def exec_main_pmarks_def_print_files_within_last_two(self):
        JT_LoggerSettings().set_to_output()
        JT_Logger.trace_method("[METHOD_IN][exec_main_pmarks_def_print_files_within_last_two]")
        #JT_LoggerSettings().uset_to_output()                                 
        
        set_to_output_2 = sys.argv[2]
        if set_to_output_2 == "output":
            JT_LoggerSettings().set_to_output()
        else:
            JT_LoggerSettings().uset_to_output()
            
        JT_Logger.trace_method("[METHOD_IN][2][exec_main_pmarks_def_print_files_within_last_two]")
            
        kgr_2 = sys.argv[3]        
        dd_marks = self.find_marks_for_env_predef_in_first_file(kgr_2)
        len_marks = len(dd_marks.m_marks)
        if(len_marks >=2):
            mark_start = dd_marks.m_marks[len_marks-2]
            mark_end = dd_marks.m_marks[len_marks-1]
            JT_Logger.trace_method("[METHOD_ISIDE]" + "[mark_start:" + mark_start.m_mark + "]")
            JT_Logger.trace_method("[METHOD_ISIDE]" + "[mark_end:" + mark_end.m_mark + "]")
            self.logs_print_files_within_marks(kgr_2
                                           ,mark_start.m_mark
                                           ,mark_end.m_mark)
            
        JT_Logger.trace_method("[METHOD_OUT][exec_main_pmarks_def_print_files_within_last_two]")

#==================================================================
#
#==================================================================
    
    def exec_main_pmarks_comp_print_files_within_computed_two(self):
        JT_LoggerSettings().set_to_output()
        JT_Logger.trace_method("[METHOD_IN][exec_main_pmarks_comp_print_files_within_computed_two]")
        #JT_LoggerSettings().uset_to_output()                                 
        
        set_to_output_2 = sys.argv[2]
        if set_to_output_2 == "output":
            JT_LoggerSettings().set_to_output()
        else:
            JT_LoggerSettings().uset_to_output()
            
        JT_Logger.trace_method("[METHOD_IN][2][exec_main_pmarks_comp_print_files_within_computed_two]")
            
        kgr_3 = sys.argv[3]
        shift_start_4 = 0
        try:
            shift_start_4 = int(sys.argv[4])
        except:
            JT_Logger.print_exception("\nexception")
            shift_start_4 = 0
            
        shift_end_5 = 0
        try:
                shift_end_5 = int(sys.argv[5])
        except:
            JT_Logger.print_exception("\nexception")
            shift_start_4 = 0
            
        
                
        dd_marks = self.find_marks_for_env_predef_in_first_file(kgr_3)
        len_marks = len(dd_marks.m_marks)
        
        ii_start = len_marks-shift_start_4-2
        if(ii_start <0):
            ii_start = 0
            
        ii_end = len_marks-shift_end_5-1
        if(ii_end <0):
            ii_end = 1

            
        if(len_marks >=2):
            mark_start = dd_marks.m_marks[ii_start]
            mark_end = dd_marks.m_marks[ii_end]
            JT_Logger.trace_method("[METHOD_ISIDE]" + "[mark_start:" + mark_start.m_mark + "]")
            JT_Logger.trace_method("[METHOD_ISIDE]" + "[mark_end:" + mark_end.m_mark + "]")
            self.logs_print_files_within_marks(kgr_3
                                           ,mark_start.m_mark
                                           ,mark_end.m_mark)
            
        JT_Logger.trace_method("[METHOD_OUT][exec_main_pmarks_comp_print_files_within_computed_two]")

#==================================================================
#
#==================================================================

    def exec_main_iemarks(self):
        JT_LoggerSettings().set_to_output()
        #JT_LoggerSettings().uset_to_output()              
        JT_Logger.trace_method("[METHOD_IN][exec_main_iemarks]")                            
        kgr_2 = sys.argv[2]
        mark_3 = sys.argv[3]
        
        s_mm = JT_LogWritingAnaliser.get_mark_for_file()
        mark = "JT" + s_mm + "_" + mark_3
        JT_Logger.print_output("[INSERTED_MARK:" + mark + "]")
        open_file_mode_4 = sys.argv[4]
        self.create_copy_of_logs(kgr_2)                                    
        self.logs_insert_mark(kgr_2,mark,open_file_mode_4)                
        JT_Logger.trace_method("[METHOD_OUT][exec_main_iemarks]")

#==================================================================
#
#==================================================================
        
    def exec_main_imarks(self):
        JT_LoggerSettings().set_to_output()
        #JT_LoggerSettings().uset_to_output()                      
        JT_Logger.trace_method("[METHOD_IN][exec_main_imarks]")                    
        kgr_2 = sys.argv[2]
        mark_3 = sys.argv[3]
        
        s_mm = JT_LogWritingAnaliser.get_mark_for_file()
        mark = "JT" + s_mm + "_" + mark_3
        JT_Logger.print_output("[INSERTED_MARK:" + mark + "]")
        open_file_mode_4 = sys.argv[4]
        self.create_copy_of_logs(kgr_2)                                    
        self.logs_insert_mark(kgr_2,mark,open_file_mode_4)                
        JT_Logger.trace_method("[METHOD_OUT][exec_main_imarks]")

#==================================================================
#
#==================================================================

    def exec_main_pmarks_all_files_marks_from_args(self):
        JT_LoggerSettings().set_to_output()
        #JT_LoggerSettings().uset_to_output()                              
        JT_Logger.trace_method("[METHOD_IN]" 
                               + "[exec_main_pmarks_all_files_marks_from_args]")                
        kgr_2 = sys.argv[2]
        mark_start_3 = sys.argv[3]
        mark_stop_4 = sys.argv[4]
                            
        self.logs_print_files_within_marks(kgr_2
                                           ,mark_start_3
                                           ,mark_stop_4)
        
        JT_Logger.trace_method("[METHOD_OUT]" 
                               + "[exec_main_pmarks_all_files_marks_from_args]")
#==================================================================
#
#==================================================================

