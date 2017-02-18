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
import pexpect
from datetime import datetime

from JT_Logger import JT_Logger
from JT_LoggerSettings import JT_LoggerSettings
from JT_Logger import JT_StaticLogger

from JT_Os import JT_Os
from JT_ManagerConfig import JT_ManagerConfig

from JT_Marks import JT_Marks
from JT_Files import JT_Files
from JT_FilePair import JT_FilePair
from JT_FilesPairs import JT_FilesPairs
from JT_File import JT_File
from JT_Mark import JT_Mark
from JT_Strings import JT_Strings_find_options
from JT_MonitorKgr import JT_MonitorKgr
#==================================================================
#
#==================================================================


class JT_LogReadingAnaliser:

#==================================================================
#
#==================================================================

    def __init__(self):
        self.m_logs = JT_Files()
        self.m_test = 0

#==================================================================
#
#==================================================================

    def exec_utils(self,p_kgr):
        try:
            JT_StaticLogger.setup_logging_main()
            JT_LoggerSettings().set_to_output()            
            JT_Logger.trace_method("[METHOD_IN][exec_utils]")
            arg_2 = sys.argv[2]            
            if(arg_2 == "ls_loginfo"):
                kgr_3 = sys.argv[3]
                self.ls_logging(kgr_3)
                
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
            print pexpect.run(cmd)
            JT_Logger.trace_method("[METHOD_OUT][ls_logging]")            
        except:
            JT_Logger.print_exception("\nexception")
            print "error_in_setup_logging"
            

#==================================================================
#
#==================================================================

    @staticmethod    
    def setup_mv_logging(p_kgr):
        try:
            JT_Logger.trace_method("[METHOD_IN][setup_mv_logging]")
            JT_Os.run_subprocess_popen_strip_without_logging("mkdir /rksup/log/" + p_kgr + "/logs_info")
            JT_Logger.trace_method("[METHOD_OUT][setup_mv_logging]")            
        except:
            JT_Logger.print_exception("\nexception")
            print "error_in_setup_logging"
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
        JT_Logger.print_output_no_log( "" )
        JT_Logger.print_output_no_log( "" )

#==================================================================
#
#==================================================================

    def show_header(self):
        #JT_Logger.print_output("KGR process monitor (c) 2011 REUTERS, Jacek Tracz\n")
        JT_Logger.print_output( "[METHOD_IN][print_parameters]" )        
        JT_Logger.print_output( " python mon_ok.py " )
        JT_Logger.print_output( "" )
        JT_Logger.print_output( "" )

                
            
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
            
            dd_log_files = JT_FilesPairs()
            
            #dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "kgr_log_watch","log")
            
            #dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "kgrLogger","log")
            
            
            #START_FILES
            if(self.m_test == 0):
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
            else:
                dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRImportServer_meta_stdout","log")
                #dd_log_files.add_log_file_ex("/rksup/log", p_kgr, "KGRServer_master__stdout","log")
                #dd_log_files.add_log_file_ex("/rksup/log" , p_kgr , "KGRServer_master__DBTraceFile","log")
            
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
            
    def create_copy_of_log(self,p_File):
        try:
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_copy_of_log]")
            p_dd = JT_File()
            p_dd = p_File
            
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_copy_of_log]" 
                                          + "[m_full_path:" + p_dd.m_full_bck_path + "]")
            
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_copy_of_log]" 
                                          + "[m_full_bck_path:" + p_dd.m_full_bck_path + "]")
            
            s_cmd = "cp " + p_dd.m_full_path + " " +  p_dd.m_full_bck_path
            
            JT_Logger.trace_hard_level_20("[METHOD_IN][create_copy_of_log]"  
                                          + "[s_cmd:" + s_cmd + "]")
            
            JT_Os.run_subprocess_popen_strip(s_cmd)             
            JT_Logger.trace_hard_level_20("[METHOD_OUT][create_copy_of_log]")
        except :
            JT_Logger.print_exception("exception_in_create_copy_of_log")
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][create_copy_of_log]")
            
#==================================================================
#
#==================================================================

    def logs_get_last_line_for_file(self,p_File):
        try:
            dd_file = JT_File()
            dd_file = p_File
            JT_Logger.trace_hard_level_20("[METHOD_IN][logs_print_file]")
            self.print_head_for_file(dd_file.m_full_path)
            tt = JT_Os.tail_lines(dd_file.m_full_path,int(1))            
            JT_Logger.print_stdout(tt)
            JT_Logger.trace_hard_level_20("[METHOD_OUT][logs_print_file]")
        except :
            JT_Logger.print_exception("\nError: can\'t add string to filen")
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][logs_print_file]")      
            
#==================================================================
#
#==================================================================
            
    def logs_print_file(self,p_File,p_lines):
        try:
            dd_file = JT_File()
            dd_file = p_File
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
            
            for dd_file_pair_ii in self.m_logs.m_files:
                dd_fp = JT_FilePair()
                dd_fp = dd_file_pair_ii
                dd_ff = dd_fp.m_log_file
                
                JT_Logger.print_output("LOG_FILE:" + dd_ff.m_full_path)
            
            JT_Logger.trace_method("[METHOD_OUT][print_log_files]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_log_files]")
#==================================================================
#
#==================================================================

    def logs_print_files_within_marks(self
                                      ,p_kgr
                                      ,p_mark_start
                                      ,p_mark_stop):
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
            
            for dd_file_pair_ii in self.m_logs.m_files:
                
                dd_fp = JT_FilePair()
                dd_fp = dd_file_pair_ii
                dd_ff = dd_fp.m_log_file
                JT_LogReadingAnaliser.print_lines_within_for_one_file(
                                                         dd_ff.m_full_path
                                                         , p_mark_start
                                                         , p_mark_stop)
    
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
    def print_lines_within_for_one_file(p_filename,p_mark_start,p_mark_end):
        """print_lines_within_for_one_file"""

        
        try:
            JT_Logger.trace_method("[METHOD_IN][print_lines_within_for_one_file]")
            JT_Logger.trace_method("[p_filename:" + p_filename + "]")
            JT_Logger.trace_method("[p_mark_start:" + p_mark_start + "]")
            JT_Logger.trace_method("[p_mark_end:" + p_mark_end + "]")
        
            JT_Logger.print_output("\n/*====================================================/")
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*FILE:" + p_filename)
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*====================================================/")
            
            if (len(p_mark_start) < 8):
                JT_Logger.trace_method("[METHOD_OUT_1][print_lines_within_for_one_file]")
                return

            if (len(p_mark_end) < 8):
                JT_Logger.trace_method("[METHOD_OUT_2][print_lines_within_for_one_file]")
                return
            
            if(p_mark_start == "NULL_LINE_MARK"):
                JT_Logger.trace_method("[METHOD_OUT_3][print_lines_within_for_one_file]")
                return
            
            if(p_mark_end == "NULL_LINE_MARK"):
                JT_Logger.trace_method("[METHOD_OUT_4][print_lines_within_for_one_file]")
                return
                
            l_file = open(p_filename,'r')
            lines = l_file.read().split("\n")
            
            l_file.close()
            inside = 0
            not_print_line = 0    
            number_of_printed_lines = 0    
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
                        JT_Logger.print_output( ll )
                        number_of_printed_lines = number_of_printed_lines + 1
    
                not_print_line = 0
            
            JT_Logger.print_output("PRINTED_LINES:" + str(number_of_printed_lines) +"\n")
                
            JT_Logger.trace_method("[METHOD_OUT][print_lines_within_for_one_file]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_lines_within_for_one_file]")
            


#==================================================================
#
#==================================================================

    def find_marks_for_env_predef_in_first_file_deprecated(self,p_kgr):
        try:
            JT_Logger.trace_method("[METHOD_IN][find_marks_for_env_predef_in_first_file]")
            dd_out = JT_Marks()
            dd_out =  self.fill_marks_for_all_logs( p_kgr )
            
            JT_Logger.trace_method("[METHOD_OUT][find_marks_for_env_predef_in_first_file]")
            return dd_out
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_marks_for_env_predef_in_first_file]")
            dd_out_exc = JT_Marks()
            return dd_out_exc

#==================================================================
#
#==================================================================

    def print_selected_start_end_for_all_logs(self):
        """print_selected_start_end_for_all_logs"""
        try:
            
            JT_Logger.trace_method("[METHOD_IN][print_selected_start_end_for_all_logs]")
            
            for dd_log_ii in self.m_logs.m_files:
                dd_log_pair = JT_FilePair()
                dd_log_pair = dd_log_ii
                    
                dd_log_file = JT_File()
                dd_log_file = dd_log_pair.m_log_file
                        
                dd_marks = JT_Marks()
                dd_marks = dd_log_file.get_marks()
                    
                dd_mark_start = JT_Mark()
                dd_mark_start = dd_marks.m_mark_start

                dd_mark_end = JT_Mark()
                dd_mark_end = dd_marks.m_mark_start 

                JT_LogReadingAnaliser.print_lines_within_for_one_file(
                                                         dd_log_file.m_full_path
                                                         ,dd_mark_start.m_line_from_file
                                                         , dd_mark_end.m_line_from_file)
                             
                            
            JT_Logger.trace_method("[METHOD_OUT][print_selected_start_end_for_all_logs]")
            return 1
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_selected_start_end_for_all_logs]")
            return 0


#==================================================================
#
#==================================================================

    def fill_marks_start_end_for_all_logs(self,p_ii_start,p_ii_end):
        """fill_marks_start_end_for_all_logs"""
        
        try:
            
            JT_Logger.trace_method("[METHOD_IN][fill_marks_start_end_for_all_logs]")
            l_mm = "fill_marks_start_end_for_all_logs"
            
            for dd_log_ii in self.m_logs.m_files:
                dd_log_pair = JT_FilePair()
                dd_log_pair = dd_log_ii            
                
                dd_log_file = JT_File()
                dd_log_file = dd_log_pair.m_log_file
                
                dd_marks = JT_Marks()
                dd_marks = dd_log_file.get_marks()
                                                
                len_marks = len(dd_marks.m_marks_list)
                
                if(len_marks >= p_ii_start):
                    mark_start = dd_marks.m_marks_list[len_marks - p_ii_start]
                    mark_end = dd_marks.m_marks_list[len_marks - p_ii_end]
                    
                    JT_Logger.trace_method("[METHOD_ISIDE][" + l_mm + "][mark_start:" + mark_start.m_mark + "]")
                    JT_Logger.trace_method("[METHOD_ISIDE][" + l_mm + "][mark_end:" + mark_end.m_mark + "]")
                                        
                    dd_log_ii.set_marks( mark_start, mark_end)
                else:
                    mark_start = JT_Mark()
                    mark_end = JT_Mark()
                    dd_log_ii.set_marks( mark_start, mark_end)
                            
            JT_Logger.trace_method("[METHOD_OUT][fill_marks_start_end_for_all_logs]")
            return 1
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_marks_start_end_for_all_logs]")
            return 0
    
#==================================================================
#
#==================================================================

     
    def fill_marks_for_all_logs(
                                self
                                ,p_kgr
                                ,p_mark_template = "JT_MARK_INPUT_JT_YEAR_2011_MONTH"):
        """fill_marks_for_all_logs"""
        try:
            
            JT_Logger.trace_method("[METHOD_IN][fill_marks_for_all_logs]")
            
            self.create_log_files(p_kgr)
            
            for dd_log_ii in self.m_logs.m_files:
                dd_log = JT_FilePair()
                dd_log = dd_log_ii            
                self.fill_marks_for_one_log_file(dd_log,p_mark_template)
                
            JT_Logger.trace_method("[METHOD_OUT][fill_marks_for_all_logs]")
            return 1
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_marks_for_all_logs]")
            return 0
        
#==================================================================
#
#==================================================================

    def fill_marks_for_one_log_file(self,dd_log_ii,p_mark_template):
        """fill_marks_for_one_log_file"""
        try:
            JT_Logger.trace_method("[METHOD_IN][fill_marks_for_one_log_file]")                        
            
            dd_log = JT_FilePair()
            dd_log = dd_log_ii            
            dd_file_info = JT_File()
            dd_file_info = dd_log.m_log_file_info 
            dd_out = self.get_all_marks_for_one_file(
                                                     dd_file_info.m_full_path
                                                     ,p_mark_template)
                                        
            dd_log_ii.m_log_file_info.set_marks( dd_out )
            dd_log_ii.m_log_file.set_marks( dd_out )
            
            JT_Logger.trace_method("[METHOD_OUT][fill_marks_for_one_log_file]")
            return dd_out
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_marks_for_one_log_file]")
            dd_out_exc = JT_Marks()
            return dd_out_exc
        
#==================================================================
#
#==================================================================
    
    def get_all_marks_for_one_file(self, p_filename, p_mark_template):
        """get_all_marks_for_one_file"""
        try:
            JT_Logger.trace_method("[METHOD_IN][get_all_marks_for_one_file]") 
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
            dd_marks = JT_Marks()
            
            for ll in lines:
                if ll.find(p_mark_template) >= 0:
                    JT_Logger.print_output("INSIDE_MARK:" + ll +"\n")
                    l_mark_line = ll
                    
                    line_from_mark = self.get_line_from_mark(l_mark_line)
                    JT_Logger.print_output("[FILE:" + p_filename + "][line_from_mark:" + line_from_mark + "]")
                    dd_mark = JT_Mark()
                    dd_mark.m_mark = l_mark_line
                    dd_mark.m_line_from_file = line_from_mark
                    dd_marks.m_marks_list.append( dd_mark )                                    
            
            JT_Logger.trace_method("[METHOD_OUT][get_all_marks_for_one_file]")
            return dd_marks
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][get_all_marks_for_one_file]")
            dd_exc = JT_Marks()
            return dd_exc

#==================================================================
#
#==================================================================

    def logs_insert_mark(self,p_kgr,p_mark,p_open_file_mode):
        try:
            JT_Logger.trace_hard_level_20("[METHOD_IN][logs_insert_mark]")
            ll_m = "logs_insert_mark"
            JT_Logger.trace_hard_level_20( "[p_kgr:" +  p_kgr + "]")
            JT_Logger.trace_hard_level_20( "[p_mark:" + p_mark + "]")                                     
            JT_Logger.trace_hard_level_20( "[p_open_file_mode:" + p_open_file_mode + "]")
        
            self.create_log_files(p_kgr)
            
            for dd_file_pair_ii in self.m_logs.m_files:
                dd_log_pair = JT_FilePair()
                dd_log_pair = dd_file_pair_ii         
                last_file_lane = JT_Os.get_last_not_empty_file_line(
                                                                    dd_log_pair.m_log_file.m_full_path)
                
                
                    
                JT_Logger.trace_hard_level_20("[M_INSIDE][" + ll_m + "][last_file_lane:" + last_file_lane + "]")    
                l_mark = p_mark + "<LINE>" + last_file_lane + "</LINE>"
                JT_Logger.trace_hard_level_20("[M_INSIDE][" + ll_m + "][l_mark:" + l_mark + "]")
                self.logs_insert_mark_into_file(
                                                dd_log_pair.m_log_file_info
                                                ,l_mark
                                                ,"a")
                
            JT_Logger.trace_hard_level_20("[METHOD_OUT][logs_insert_mark]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][logs_insert_mark]")
        
        
#==================================================================
#
#==================================================================
    def close_file(self,dd):
        try:
            if(dd != None):
                dd.close()
        except:
            JT_Logger.print_exception("\nException")
#==================================================================
#
#==================================================================
            
    def append_mark_to_file(self,p_file_path,p_mark,p_mode):
        try:
            l_file = None
            try:
                l_file = open(p_file_path,p_mode)
                
                l_file.write("JT_MARK_INPUT" + "_" + p_mark + "\n")
                                
                self.close_file(l_file)
            
            except:
                self.close_file(l_file)
            
        except:
            JT_Logger.print_exception("\nException")
            
#==================================================================
#
#==================================================================
        
    def logs_insert_mark_into_file(self, p_File, p_mark, p_open_file_mode):
        
        try:
            p_dd = JT_File()
            p_dd = p_File
            JT_Logger.trace_hard_level_20("[METHOD_IN][logs_insert_mark_into_file]")
            JT_Logger.trace_hard_level_20("[METHOD_INSIDE][m_full_path:" +  p_dd.m_full_path + "]")                                     
            JT_Logger.trace_hard_level_20("[METHOD_INSIDE][p_open_file_mode:" + p_open_file_mode + "]")            
            JT_Logger.trace_hard_level_20("[METHOD_INSIDE][MARK:" +  p_mark + "]")
            
            try:
                self.append_mark_to_file(p_dd.m_full_path,p_mark,"a")            
            except:
                self.append_mark_to_file(p_dd.m_full_path,p_mark,"w")
                
            JT_Logger.trace_hard_level_20("[FILE_CLOSE:" +  p_dd.m_full_path + "]")
            JT_Logger.trace_hard_level_20("[METHOD_OUT][logs_insert_mark_into_file]")
        except :
            JT_Logger.print_exception("\nError: can\'t add string to filen")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][logs_insert_mark_into_file]")

                
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
        try:
            dt = datetime.now()
            s_log_file = JT_StaticLogger.get_line(
                 "_YEAR_" +  str(dt.year)    
                + "_MONTH_" +  str( dt.month )                                        
                + "_DAY_" + str(dt.day)                                               
                + "_HOUR_" + str(dt.hour) 
                + "_MIN_" + str(dt.minute)
                + "_SEC_" + str(dt.second) )
                                
            return s_log_file
        except :
            JT_Logger.print_exception("\nError: can\'t add string to filen")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][get_mark_for_file]")
            return "file_logger"


#==================================================================
#
#==================================================================

    def exec_main_iemarks(self):
        try:
            JT_LoggerSettings().set_to_output()
            #JT_LoggerSettings().uset_to_output()              
            JT_Logger.trace_method("[METHOD_IN][exec_main_iemarks]")                            
            kgr_2 = sys.argv[2]
            mark_3 = sys.argv[3]
            
            s_mm = JT_LogReadingAnaliser.get_mark_for_file()
            mark = "JT" + s_mm + "_" + mark_3
            JT_Logger.print_output("[INSERTED_MARK:" + mark + "]")
            open_file_mode_4 = "a"
            #self.create_copy_of_logs(kgr_2)
            
            JT_LogReadingAnaliser.setup_mv_logging( kgr_2 )
                                                
            self.logs_insert_mark(kgr_2,mark,open_file_mode_4)
                            
            JT_Logger.trace_method("[METHOD_OUT][exec_main_iemarks]")
        except :
            JT_Logger.print_exception("\[Exception_in][exec_main_iemarks]")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][exec_main_iemarks]")

#==================================================================
#
#==================================================================
        
    def exec_main_imarks(self):
        try:
            JT_LoggerSettings().set_to_output()
            #JT_LoggerSettings().uset_to_output()                      
            JT_Logger.trace_method("[METHOD_IN][exec_main_imarks]")                    
            kgr_2 = sys.argv[2]
            mark_3 = sys.argv[3]
            
            s_mm = JT_LogReadingAnaliser.get_mark_for_file()
            mark = "JT" + s_mm + "_" + mark_3
            JT_Logger.print_output("[INSERTED_MARK:" + mark + "]")
            open_file_mode_4 = sys.argv[4]
            #self.create_copy_of_logs(kgr_2)                                    
            self.logs_insert_mark(kgr_2,mark,open_file_mode_4)                
            JT_Logger.trace_method("[METHOD_OUT][exec_main_imarks]")
        except :
            JT_Logger.print_exception("\[Exception_in][exec_main_imarks]")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][exec_main_imarks]")

#==================================================================
#
#==================================================================

    def exec_main_pmarks_all_files_marks_from_args(self):
        try:
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

        except :
            JT_Logger.print_exception("\[Exception_in][exec_main_pmarks_all_files_marks_from_args]")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][exec_main_pmarks_all_files_marks_from_args]")
        
#==================================================================
#
#==================================================================


    def get_line_from_mark(self,p_str_line):
        try:
            JT_Logger.trace_method("[METHOD_IN]" + "[get_line_from_mark]")                
            
            i_start = p_str_line.find("<LINE>")
            i_s_1 = i_start + 6
            i_end = p_str_line.find("</LINE>") -2            
            ll_out = p_str_line[i_s_1:i_end]
            
            JT_Logger.trace_method("[METHOD_OUT]" + "[get_line_from_mark][" + ll_out + "]")
            
            return ll_out
        except :
            JT_Logger.print_exception("\[Exception_in][exec_main_pmarks_all_files_marks_from_args]")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][exec_main_pmarks_all_files_marks_from_args]")

#==================================================================
#
#==================================================================

    
    def exec_main_pmarks_def_print_files_within_last_two(self):
        try:
            JT_LoggerSettings().set_to_output()
            JT_Logger.trace_method("[METHOD_IN][exec_main_pmarks_def_print_files_within_last_two]")
            
            set_to_output_2 = sys.argv[2]
            if set_to_output_2 == "output":
                JT_LoggerSettings().set_to_output()
            else:
                JT_LoggerSettings().uset_to_output()
                
            JT_Logger.trace_method("[METHOD_IN][2][exec_main_pmarks_def_print_files_within_last_two]")
                
            kgr_2 = sys.argv[3]        
            
            self.fill_marks_for_all_logs( kgr_2 )
            
            self.fill_marks_start_end_for_all_logs( 2, 1 )
                   
            self.print_selected_start_end_for_all_logs()

                
            JT_Logger.trace_method("[METHOD_OUT][exec_main_pmarks_def_print_files_within_last_two]")
        except :
            JT_Logger.print_exception("\Exception_in_exec_main_pmarks_def_print_files_within_last_two")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][exec_main_pmarks_def_print_files_within_last_two]")

#==================================================================
#
#==================================================================
    
    def exec_main_pmarks_comp_print_files_within_computed_two(self):
        try:
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
                
            
                    
            dd_marks = self.fill_marks_for_all_logs(kgr_3)
            len_marks = len(dd_marks.m_marks_list)
            
            ii_start = len_marks-shift_start_4-2
            if(ii_start <0):
                ii_start = 0
                
            ii_end = len_marks-shift_end_5-1
            if(ii_end <0):
                ii_end = 1
    
            self.fill_marks_for_all_logs( kgr_3  )
            
            self.fill_marks_start_end_for_all_logs( ii_start, ii_end )
                   
            self.print_selected_start_end_for_all_logs()

                                
            JT_Logger.trace_method("[METHOD_OUT][exec_main_pmarks_comp_print_files_within_computed_two]")
        except :
            JT_Logger.print_exception("\[Exception_in][exec_main_pmarks_comp_print_files_within_computed_two]")                          
            JT_Logger.trace_hard_level_20("[METHOD_OUT_EXC][exec_main_pmarks_comp_print_files_within_computed_two]")


#==================================================================
#
#==================================================================
