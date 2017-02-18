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

from JT_Os import JT_Os
from JT_Environments import JT_Environments
from JT_Logger import JT_Logger
from JT_LoggerSettings import JT_LoggerSettings
from JT_Logger import JT_StaticLogger


from JT_Marks import JT_Marks
from JT_Files import JT_Files
from JT_Files import JT_File

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

    def create_and_fill_log_files_list_task_server(self,p_kgr):
        try:
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_and_fill_log_files_list_task_server]")
            #JT_Os.run_subprocess_popen_strip("tail -f /rksup/log/kgr35s/KGRServer_master__stdout.log")
            #JT_Os.run_os_command("tail -f /rksup/log/kgrSet/KGRServer_master__stdout.log"
            
            dd_log_files = JT_Files()
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "kgr_log_watch","log")
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRTaskServer_1_stdout","log")
            
            dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRTaskServer_task_1_DBTraceFile","log")
            self.m_logs = dd_log_files
            JT_Logger.trace_hard_level_20("[METHOD_OUT][create_and_fill_log_files_list_task_server]")
            
            return dd_log_files
        except :
            JT_Logger.print_exception("create_and_fill_log_files_list_task_server")
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][create_and_fill_log_files_list_task_server]")
            dd_log_files_exc = JT_Files()
            return dd_log_files_exc
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
                JT_LogWritingAnaliser.print_lines_within(
                                                         dd_ff.m_full_path
                                                         , p_mark_start
                                                         ,p_mark_stop)
    
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
            
            
            lines = JT_LogWritingAnaliser.get_lines_for_opened_file(p_filename)
            
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
                        ll = JT_Logger.format_line_to_prnt( ll )
                        JT_Logger.print_output(ll)
    
                not_print_line = 0
            
                
            JT_Logger.trace_method("[METHOD_OUT][print_lines_within]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_lines_within]")

#==================================================================
#
#==================================================================
            
    @staticmethod
    def format_line_to_prnt(p_ll):
        try:
            ll_out = ""
            if(p_ll == None):
                p_ll = ""
                
            if(len(p_ll) > 2048):
                ll_out = "TOO_LONG_LINE_TO_PRINT" 
            else:
                ll_out = p_ll
                
            return ll_out            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_lines_within]")
            return "ERROR_IN_LINE"

#==================================================================
#
#==================================================================

    @staticmethod
    def get_line_started_from(p_ll, p_tt):
        try:
            i_exec = 0
            s_line = ""
            s_line = p_ll
            s_tt = ""
            s_tt = p_tt
            
            i_s = s_line.find( s_tt )
            
            if(i_s <0):
                i_s = s_line.find(s_tt.upper())
            
            if(i_s > 0):
                i_len = len(s_line)
                s_line = s_line[i_s:i_len]
                i_exec = 1
                                
            return i_exec,s_line
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][get_line_started_from]")
            i_exec = 1
            return i_exec, "ERROR_IN_LINE_get_line_started_from"
        
#==================================================================
#
#==================================================================

    @staticmethod
    def get_line_beetwen(ll_out, p_start,p_end):
        try:
            i_exec = 0
            i_s = ll_out.find(p_start)
            
            if(i_s <0):
                i_s = ll_out.find(p_start.upper())
                
            i_e = ll_out.find(p_end)
            if(i_e <0):
                i_e = ll_out.find(p_end.upper())
                    
            if( i_s > 0 and i_e > 0):                
                i_len = len(ll_out)
                ll_tail = ll_out[i_e : i_len]
                ll_out = p_start + " * " + ll_tail
                i_exec = 1
                
            return i_exec,ll_out
        
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][get_line_beetwen]")
            return 1,"ERROR_IN_LINE_get_line_beetwen"
        
#==================================================================
#
#==================================================================
    @staticmethod
    def is_not_valid_sentence(p_line_for_sentence,p_sentence):
        try:
            
            JT_Logger.trace_method("[METHOD_IN][is_not_valid_sentence]")
            JT_Logger.trace_method("[p_line_for_sentence:" + p_line_for_sentence + "]")
            JT_Logger.trace_method("[p_sentence:" + p_sentence + "]")
            
            i_exec = 0    
            i_not_valid = 0
            s_ll = p_line_for_sentence.upper()
            
            ii_finded = s_ll.find(p_sentence) >=0
            if ( ii_finded > 0):
                i_not_valid = 1
                i_exec = 1
                
            JT_Logger.trace_method("[METHOD_OUT][is_not_valid_sentence]" 
                                   + "[i_exec:" + str(i_exec) + "]" 
                                   + "[i_not_valid:" + str(i_not_valid)  + "]"
                                   + "[ii_finded:" + str (ii_finded) + "]")
            
            return i_exec,i_not_valid
        
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][is_not_valid_sentence]")
            i_exec =0
            i_not_valid = 0 
            return i_exec,i_not_valid
#==================================================================
#
#==================================================================

    @staticmethod
    def line_is_excluded_db_layer(p_ll):
        try:
            i_not_valid = 0
            i_exec = 0
            s_ll = ""
            s_ll = p_ll.upper()
            
            if( i_exec == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"* FROM CPTY")
            if(i_not_valid == 1):
                i_exec =1
                
            if( i_exec == 0):
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"* FROM INSTRUMENT")
            if(i_not_valid == 1):
                i_exec =1
                
            if( i_exec == 0):
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"* FROM FOLDER")
            if(i_not_valid == 1):
                i_exec =1
                
            if( i_exec == 0):
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"* FROM CURRENCY")
            if(i_not_valid == 1):
                i_exec =1

            if( i_exec == 0):
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"* FROM KNTABLE")
            if(i_not_valid == 1):
                i_exec =1

            if( i_exec == 0):
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"* FROM KNUSER KNUSER")
            if(i_not_valid == 1):
                i_exec =1
                
            if( i_exec == 0):    
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"* FROM KNUSERCONFIG")
            if(i_not_valid == 1):
                i_exec =1
                
            if( i_exec == 0):    
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"* FROM SETUP")
            if(i_not_valid == 1):
                i_exec =1

            if( i_exec == 0):    
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"* FROM KMODULE")
            if(i_not_valid == 1):
                i_exec =1
                
            if( i_exec == 0):    
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"* FROM AUDITSETUP")
            if(i_not_valid == 1):
                i_exec =1
                 
            if( i_exec == 0):    
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"* FROM KMODULETABLE")
            if(i_not_valid == 1):
                i_exec =1


            if( i_exec == 0):    
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"INSERT INTO AUDITMSG")
            if(i_not_valid == 1):
                i_exec =1
                
            if( i_exec == 0):    
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"INSERT INTO AUDITMSG")
            if(i_not_valid == 1):
                i_exec =1


            if( i_exec == 0):    
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"UPDATE AUDITMSG SET MESSAGELONG")
                
            if(i_not_valid == 1):
                i_exec =1
                
                
            return i_exec,i_not_valid            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][line_is_excluded_db_layer]")
            return 0
        
#==================================================================
#
#==================================================================

    @staticmethod
    def line_is_excluded_in_prnt_kgr_layer(p_ll):
        try:
            JT_Logger.trace_method("[METHOD_IN][line_is_excluded_in_prnt_kgr_layer]")
            i_not_valid = 0
            i_exec = 0
            s_ll = ""
            s_ll = p_ll.upper()
            
            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"LIBC")
            
                
            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"LIBSOCKET")


            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"LWP_")
                
                
            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"LIBSYBCS_")
                                

            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"LIBSYB")

            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"_POSIX")

            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"ITH_CRITICALSECTION")

            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"TIBRVMSG")

            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"KRO_RESULT")

            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"KNEL_STRINGVALUE")
                                
            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"KNEL_ULONGVALUE")

            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"OPERATOR")
                
            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"UNSIGNED")

            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"LIBTIBRV")
                
            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"KGR_IDENTIFIER")
                
            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"KNEL_OPAQUEVALUE")
                
            if( i_not_valid == 0):            
                i_exec,i_not_valid = JT_LogWritingAnaliser.is_not_valid_sentence(s_ll,"INSTANCE()")
                                
                
            JT_Logger.trace_method("[METHOD_OUT][line_is_excluded_in_prnt_kgr_layer]" 
                                   + "[i_exec:" + str(i_exec) + "]"
                                   + "[i_not_valid:" + str(i_not_valid) + "]")    
            return i_exec,i_not_valid            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][line_is_excluded_in_prnt_kgr_layer]")
            return 0
        
#==================================================================
#
#==================================================================

    @staticmethod
    def line_is_valid_to_prnt_db_layer(p_ll, p_remove_sentences):
        try:
            i_exec = 0
            ll_out = ""
            ll_out = JT_Logger.format_line_to_prnt( p_ll )
            
            i_exec,ll_out = JT_LogWritingAnaliser.get_line_beetwen(ll_out, "select" , "from")
                            
            if(i_exec == 0):                
                i_exec,ll_out = JT_LogWritingAnaliser.get_line_started_from(ll_out,"insert")
                    
                
            if(i_exec == 0):
                i_exec,ll_out = JT_LogWritingAnaliser.get_line_started_from(ll_out,"update")

            if(i_exec == 0):
                i_exec,ll_out = JT_LogWritingAnaliser.get_line_started_from(ll_out,"Query")
                
            if(i_exec == 0):
                i_exec,ll_out = JT_LogWritingAnaliser.get_line_started_from(ll_out,"Read")
                
            if( p_remove_sentences == 1):
                i_exec_valid_line = 0
                if(i_exec == 1):                
                    i_exec_valid_line,i_not_valid = JT_LogWritingAnaliser.line_is_excluded_db_layer( ll_out )
    
                if(i_exec_valid_line == 1 and i_not_valid == 1):
                    i_exec = 0
                                
            if(i_exec == 0):
                ll_out = "NOT_PRINT_LINE"
                
            return i_exec,ll_out            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_lines_within]")
            return 0,"ERROR_IN_LINE"

#==================================================================
#
#==================================================================

    @staticmethod
    def line_is_valid_to_prnt_kgr_layer(p_ll):
        try:
            JT_Logger.trace_method("[METHOD_IN][line_is_valid_to_prnt_kgr_layer]")
            
            ll_out = ""
            ll_out = JT_Logger.format_line_to_prnt( p_ll )
            
            JT_Logger.trace_method("[METHOD_INSIDE][" + ll_out + "]")
                
            i_exec_validing_line = 0
            i_exec_validing_line,i_line_is_excluded = JT_LogWritingAnaliser.line_is_excluded_in_prnt_kgr_layer( ll_out )
            i_valid = 1
            if(i_line_is_excluded):
                i_valid = 0
            else:
                i_valid = 1
                
            JT_Logger.trace_method("[METHOD_OUT][line_is_valid_to_prnt_kgr_layer]" 
                                   + "[i_exec_validing_line:" + str (i_exec_validing_line) + "]"
                                   + "[i_line_is_excluded:" + str (i_line_is_excluded) + "]"
                                   + "[i_valid:" + str (i_valid) + "]")
            
            return i_valid,ll_out            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][line_is_valid_to_prnt_kgr_layer]")
            return 0,"ERROR_IN_LINE"
            
#==================================================================
#
#==================================================================
            
    @staticmethod
    def print_whole_file_formatted(p_filename):
        """print_whole_file_formatted"""

        
        try:
            JT_Logger.trace_method("[METHOD_IN][print_whole_file_formatted]")
            JT_Logger.trace_method("[p_filename:" + p_filename + "]")
        
            JT_Logger.print_output("\n/*====================================================/")
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*FILE:" + p_filename)
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*====================================================/")
            
            
            lines = JT_LogWritingAnaliser.get_lines_for_opened_file(p_filename)
            
            for ll in lines:
                ll = JT_Logger.format_line_to_prnt( ll )
                JT_Logger.print_output(ll)
                
            JT_Logger.trace_method("[METHOD_OUT][print_whole_file_formatted]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_whole_file_formatted]")

#==================================================================
#
#==================================================================

    @staticmethod
    def print_whole_file_formatted_kgr_layer_lib(p_filename):
        """print_whole_file_formatted_kgr_layer_lib"""

        
        try:
            JT_Logger.trace_method("[METHOD_IN][print_whole_file_formatted_kgr_layer_lib]")
            JT_Logger.trace_method("[p_filename:" + p_filename + "]")
        
            JT_Logger.print_output("\n/*====================================================/")
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*FILE:" + p_filename)
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*====================================================/")
            
            
            lines = JT_LogWritingAnaliser.get_lines_for_opened_file(p_filename)
            
            for ll in lines:
                ll = JT_Logger.format_line_to_prnt( ll )
                JT_Logger.print_output(ll)
                
            JT_Logger.trace_method("[METHOD_OUT][print_whole_file_formatted_kgr_layer_lib]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_whole_file_formatted_kgr_layer_lib]")


            
#==================================================================
#
#==================================================================


    @staticmethod
    def get_lines_for_opened_file(p_filename):
        """get_lines_for_opened_file"""
        
        try:
            
            JT_Logger.trace_method("[METHOD_IN][get_lines_for_opened_file]")                    
            l_file = open(p_filename,'r')
            lines = l_file.read().split("\n")            
            l_file.close()
            ll_out = []
            for ll in lines:
                ll_formatted = JT_Logger.format_line_to_prnt( ll )
                ll_out.append( ll_formatted ) 
            
            JT_Logger.trace_method("[METHOD_OUT][get_lines_for_opened_file]")
            return ll_out            
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][get_lines_for_opened_file]")
            ll_out_exc = []
            ll_out_exc.append("EXCEPTION_IN_READING_FILE")
            return ll_out_exc

#==================================================================
#
#==================================================================
            
    @staticmethod
    def print_whole_file_formatted_db_layer(p_filename, p_remove_sentences):
        """print_whole_file_formatted_db_layer"""

        
        try:
            JT_Logger.trace_method("[METHOD_IN][print_whole_file_formatted_db_layer]")
            JT_Logger.trace_method("[p_filename:" + p_filename + "]")
        
            JT_Logger.print_output("\n/*====================================================/")
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*FILE:" + p_filename)
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*====================================================/")
            
            lines = JT_LogWritingAnaliser.get_lines_for_opened_file(p_filename)
            
            for ll in lines:
                ll = JT_Logger.format_line_to_prnt( ll )
                i_exec,ll_to_print = JT_LogWritingAnaliser.line_is_valid_to_prnt_db_layer( 
                                                                                          ll
                                                                                          , p_remove_sentences )
                if(i_exec):
                    JT_Logger.trace_method("[METHOD_INSIDE][print_whole_file_formatted_db_layer][LINE_IS_PRINTED]")
                    JT_Logger.print_output(ll_to_print)
                
            JT_Logger.trace_method("[METHOD_OUT][print_whole_file_formatted_db_layer]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_whole_file_formatted_db_layer]")
            
#==================================================================
#
#==================================================================

    @staticmethod
    def print_whole_file_formatted_kgr_layer(p_filename):
        """print_whole_file_formatted_kgr_layer"""

        
        try:
            JT_Logger.trace_method("[METHOD_IN][print_whole_file_formatted_kgr_layer]")
            JT_Logger.trace_method("[p_filename:" + p_filename + "]")
        
            JT_Logger.print_output("\n/*====================================================/")
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*FILE:" + p_filename )
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*====================================================/")
            
            lines = JT_LogWritingAnaliser.get_lines_for_opened_file(p_filename)
            
            for ll in lines:
                ll = JT_Logger.format_line_to_prnt( ll )
                i_exec,ll_to_print = JT_LogWritingAnaliser.line_is_valid_to_prnt_kgr_layer( ll)
                
                if(i_exec):
                    JT_Logger.print_output(ll_to_print)
                
            JT_Logger.trace_method("[METHOD_OUT][print_whole_file_formatted_kgr_layer]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_whole_file_formatted_kgr_layer]")
            
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
        self.set_file_list(3, kgr_2)
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
        self.set_file_list(4,kgr_2)
        dd_marks = self.find_marks_for_env_predef_in_first_file(kgr_2)
        len_marks = len(dd_marks.m_marks_list)
        if(len_marks >=2):
            mark_start = dd_marks.m_marks_list[len_marks-2]
            mark_end = dd_marks.m_marks_list[len_marks-1]
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
            
        self.set_file_list(6, kgr_3)        
                
        dd_marks = self.find_marks_for_env_predef_in_first_file( kgr_3 )
        len_marks = len(dd_marks.m_marks_list)
        
        ii_start = len_marks - shift_start_4 - 2
        if(ii_start <0):
            ii_start = 0
            
        ii_end = len_marks - shift_end_5-1
        if(ii_end <0):
            ii_end = 1

            
        if(len_marks >=2):
            mark_start = dd_marks.m_marks_list[ii_start]
            mark_end = dd_marks.m_marks_list[ii_end]
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
        open_file_mode_4 = sys.argv[4]
        self.set_file_list(5,kgr_2)
                
        s_mm = JT_LogWritingAnaliser.get_mark_for_file()
        mark = "JT" + s_mm + "_" + mark_3        
        JT_Logger.print_output("[INSERTED_MARK:" + mark + "]")
        self.create_copy_of_logs(kgr_2)                                    
        self.logs_insert_mark(kgr_2,mark,open_file_mode_4)                
        JT_Logger.trace_method("[METHOD_OUT][exec_main_iemarks]")

#==================================================================
#
#==================================================================
    def set_file_list(self,p_pos_for_env,p_kgr):
        try:
            JT_Logger.trace_hard_level_20("[METHOD_IN][set_file_list][p_pos_for_env:" + str(p_pos_for_env) + "]")
            files_4 = "NOT_SET"    
            i_len = len(sys.argv)
                
            if(i_len >= p_pos_for_env + 1):
                files_4 = sys.argv[p_pos_for_env]
                
            JT_Logger.trace_hard_level_20("[METHOD_INSIDE][set_file_list][pos:" + str(p_pos_for_env) + "][files_4:" + files_4 + "]")
                
            if(files_4 == "task_server"):
                self.create_and_fill_log_files_list_task_server(p_kgr)
                
            JT_Logger.trace_hard_level_20("[METHOD_OUT][set_file_list]")
        except :
            JT_Logger.print_exception("exception_in_set_file_list")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][set_file_list]")
       
#==================================================================
#
#==================================================================
        
    def exec_main_imarks(self):
        JT_LoggerSettings().set_to_output()
        JT_Logger.trace_method("[METHOD_IN][exec_main_imarks]")                    
        kgr_2 = sys.argv[2]
        mark_3 = sys.argv[3]
        
        self.set_file_list(4, kgr_2)
            
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
        self.set_file_list(5, kgr_2)
                            
        self.logs_print_files_within_marks(kgr_2
                                           ,mark_start_3
                                           ,mark_stop_4)
        
        JT_Logger.trace_method("[METHOD_OUT]" 
                               + "[exec_main_pmarks_all_files_marks_from_args]")
        
#==================================================================
#
#==================================================================

    def exec_main_logs_print_number_of_lines(self):
        JT_LoggerSettings().set_to_output()
                                            
        JT_Logger.trace_method("[METHOD_IN]" 
                               + "[exec_main_logs_print_number_of_lines]")                
        kgr_env = sys.argv[2]
        num_lines = sys.argv[3]        
                                    
        self.set_file_list(4,kgr_env)

        self.logs_print_number_of_lines(kgr_env, num_lines)                
                            
        
        JT_Logger.trace_method("[METHOD_OUT]" 
                               + "[exec_main_logs_print_number_of_lines]")

#==================================================================
#
#==================================================================

    def exec_main_create_copy_of_logs(self):
        JT_LoggerSettings().set_to_output()
                                            
        JT_Logger.trace_method("[METHOD_IN]" 
                               + "[exec_main_create_copy_of_logs]")                
        kgr_2 = sys.argv[2]
        self.set_file_list(3, kgr_2)
        
        self.create_copy_of_logs(kgr_2)                                        
        
        JT_Logger.trace_method("[METHOD_OUT]" 
                               + "[exec_main_create_copy_of_logs]")
#==================================================================
#
#==================================================================

    def exec_main_test_1(self):
        JT_LoggerSettings().set_to_output()
                                            
        JT_Logger.trace_method("[METHOD_IN]" 
                               + "[exec_main_test_1]")                
        JT_LoggerSettings().set_to_output()
        mark = sys.argv[2]
        JT_Logger.print_output("[INSERTED_MARK:" + mark + "]")
        open_file_mode = sys.argv[3]
        JT_LogWritingAnaliser().create_copy_of_logs("kgr35s")
        JT_LogWritingAnaliser().logs_insert_mark_test(mark,open_file_mode)                
        
        JT_Logger.trace_method("[METHOD_OUT]" 
                               + "[exec_main_test_1]")


#==================================================================
#
#==================================================================

    def exec_main_print_whole_line_formatted(self):
        try:
            JT_LoggerSettings().set_to_output()
                                                
            JT_Logger.trace_method("[METHOD_IN]" 
                                   + "[exec_main_print_whole_line_formatted]")                
            p_filename = sys.argv[2]
            
            JT_LogWritingAnaliser.print_whole_file_formatted(p_filename)
                                                    
            
            JT_Logger.trace_method("[METHOD_OUT]" 
                                   + "[exec_main_print_whole_line_formatted]")

        except :
            JT_Logger.print_exception("exec_main_print_whole_line_formatted")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][exec_main_print_whole_line_formatted]")

#==================================================================
#
#==================================================================

    def exec_main_print_whole_line_formatted_db_layer(self):
        try:
            JT_LoggerSettings().set_to_output()
                                                
            JT_Logger.trace_method("[METHOD_IN]" 
                                   + "[exec_main_print_whole_line_formatted_db_layer]")
            
            p_filename = sys.argv[2]
                            
            p_debug = sys.argv[3]
                        
            if(p_debug == "debug"):
                JT_LoggerSettings().set_to_output()
            else:
                JT_LoggerSettings().uset_to_output()
            
            p_remove_sentence = sys.argv[4]
            i_rs = 0        
            if(p_remove_sentence == "remove_sentences"):
                i_rs = 1
            else:
                i_rs =0
                                        
            JT_LogWritingAnaliser.print_whole_file_formatted_db_layer( 
                                                                 p_filename
                                                                 , i_rs )
                                                    
            
            JT_Logger.trace_method("[METHOD_OUT]" 
                                   + "[exec_main_print_whole_line_formatted_db_layer]")

        except :
            JT_Logger.print_exception("exec_main_print_whole_line_formatted_db_layer")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][exec_main_print_whole_line_formatted_db_layer]")

#==================================================================
#
#==================================================================

    def exec_main_print_whole_line_formatted_kgr_layer(self):
        try:
            JT_LoggerSettings().set_to_output()
                                                
            JT_Logger.trace_method("[METHOD_IN]" 
                                   + "[exec_main_print_whole_line_formatted_kgr_layer]")
            
            p_filename = sys.argv[2]
                            
            p_debug = sys.argv[3]
                        
            if(p_debug == "debug"):
                JT_LoggerSettings().set_to_output()
            else:
                JT_LoggerSettings().uset_to_output()
            
            JT_LogWritingAnaliser.print_whole_file_formatted_kgr_layer( 
                                                                 p_filename
                                                                 )
                                                    
            
            JT_Logger.trace_method("[METHOD_OUT]" 
                                   + "[exec_main_print_whole_line_formatted_kgr_layer]")

        except :
            JT_Logger.print_exception("exec_main_print_whole_line_formatted_kgr_layer")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][exec_main_print_whole_line_formatted_kgr_layer]")


#==================================================================
#
#==================================================================

    def exec_main(self):
            
        try:
            JT_StaticLogger.setup_logging_main()
            if ( len(sys.argv) > 1 ):
                arg_1 = sys.argv[1]
                                 
                if( arg_1 == "env"):                    
                    JT_LoggerSettings().set_to_output()                
                    JT_LogWritingAnaliser().exec_main_env()                    
    
                if( arg_1 == "etail"):
                        
                    JT_LogWritingAnaliser().exec_main_logs_print_number_of_lines()
    
                if( arg_1 == "tmark"):
                        
                    JT_LogWritingAnaliser().exec_main_test_1()                
    
                if( arg_1 == "imarks"):
                    
                    JT_LogWritingAnaliser().exec_main_imarks()
                    
                if( arg_1 == "iemarks"):
                    
                    JT_LogWritingAnaliser().exec_main_iemarks()

                if( arg_1 == "cplogs"):
                    
                    JT_LogWritingAnaliser().exec_main_create_copy_of_logs()
                    
                if( arg_1 == "pmarks"):
                    
                    JT_LogWritingAnaliser().exec_main_pmarks_all_files_marks_from_args()

                if( arg_1 == "pmarks_def"):
                    
                    JT_LogWritingAnaliser().exec_main_pmarks_def_print_files_within_last_two()
                    
                if( arg_1 == "pmarks_find"):
                    
                    JT_LogWritingAnaliser().exec_main_pmarks_find_in_first_file()

                if( arg_1 == "plogs"):
                    
                    kgr_2 = sys.argv[2]                    
                    JT_LogWritingAnaliser().print_log_files(kgr_2)
                    
                if( arg_1 == "pmarks_comp"):
                    
                    JT_LogWritingAnaliser().exec_main_pmarks_comp_print_files_within_computed_two()

                if( arg_1 == "ffile"):
                                                        
                    JT_LogWritingAnaliser().exec_main_print_whole_line_formatted()
                    
                if( arg_1 == "ffile_sel"):
                                                    
                    JT_LogWritingAnaliser().exec_main_print_whole_line_formatted_db_layer()
                    
                if( arg_1 == "ffile_kgr"):                                                    
                    JT_LogWritingAnaliser().exec_main_print_whole_line_formatted_kgr_layer()
                    
                    
            JT_StaticLogger.close_logging()
            
        except:        
            JT_StaticLogger.close_logging()
            JT_Logger.print_exception("\nError: exception in main \n")
                
#==================================================================
#
#==================================================================

    def exec_main_print_truss_without_c(self):
        try:
            JT_LoggerSettings().set_to_output()
                                                
            JT_Logger.trace_method("[METHOD_IN]" 
                                   + "[exec_main_print_truss_without_c]")                
            p_filename = sys.argv[2]
            
            JT_LogWritingAnaliser.print_whole_file_formatted(
                                                             p_filename)
                                                    
            
            JT_Logger.trace_method("[METHOD_OUT]" 
                                   + "[exec_main_print_truss_without_c]")

        except :
            JT_Logger.print_exception("exec_main_print_whole_line_formatted")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][exec_main_print_truss_without_c]")

#==================================================================
#
#==================================================================

if __name__ == '__main__':
    try:    
        dd = JT_LogWritingAnaliser()
        dd.exec_main()            
    except:                    
            JT_Logger.print_exception("\nError: exception in main \n")
