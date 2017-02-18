#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

import pexpect 
import subprocess
from datetime import time
from JT_Logger import JT_Logger
from JT_ManagerConfig import JT_ManagerConfig
from JT_SSH import JT_SSH
from JT_OS_Getguid import JT_OS_Getguid
#==================================================================
#
#JT_Os
#
#==================================================================
    
class JT_Os:

#==================================================================
#
#==================================================================
    @staticmethod    
    def setup_mv_logging():
        try:
            JT_Os.run_subprocess_popen_strip_without_logging("mv /rksup/config/kgr35jut/jut/python/finder_log/*.txt /rksup/config/kgr35jut/jut/python/finder_log/bck/")            
        except:
            JT_Logger.print_exception("\nexception")
            print "error_in_setup_logging"
#==================================================================
#
#==================================================================
    
    @staticmethod
    def tail_f(p_file):
        interval = 1.0
        
        while True:
            where = p_file.tell()
            line = p_file.readline()
            if not line:
                time.sleep(interval)
                p_file.seek(where)
            else:
                yield line

#==================================================================
#
#==================================================================
          
    @staticmethod
    def tail_f_loop(p_file):
        for line in JT_Os.tail_f(open(p_file)):
            print line,    
            

#==================================================================
#
#==================================================================
    
    @staticmethod
    def tail_lines(filename,linesback=10,returnlist=0):
        """tail_lines"""
        try:
            return JT_Os.tail_lines_inner(filename,linesback,returnlist)
        except :
            JT_Logger.print_exception("\nError: can\'t find file or read data\n")
           
#==================================================================
#
#==================================================================

    @staticmethod
    def print_lines_within(p_filename,p_mark_start,p_mark_end):
        """print_lines_within"""

        JT_Logger.trace_method("[METHOD_IN][print_lines_within]")
        try:
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
                    JT_Logger.print_output("INSIDE_MARK_STOP:" + p_mark_end +"\n")
                    not_print_line = 1
                    
                if(not_print_line == 0):
                    if( inside == 1 ):
                        JT_Logger.print_output(ll)
    
                not_print_line = 0
            JT_Logger.trace_method("[METHOD_OUT][print_lines_within]")
        except :
            JT_Logger.print_exception("\nError: can\'t find file or read data\n")            
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_lines_within]")

#==================================================================
#
#==================================================================
    
    @staticmethod
    def tail_lines_inner(filename,linesback=10,returnlist=0):
        """Does what "tail -10 filename" would have done"""
        try:
            JT_Logger.trace_method("[METHOD_IN][tail_lines_inner]")
            avgcharsperline=75
            l_file = open(filename,'r')
            while 1:
                try: 
                    l_file.seek(-1 * avgcharsperline * linesback,2)
                except IOError: 
                    l_file.seek(0)
                
                if l_file.tell() == 0: 
                    atstart=1
                else: 
                    atstart=0
        
                lines=l_file.read().split("\n")
                if (len(lines) > (linesback+1)) or atstart: 
                    break
                #The lines are bigger than we thought
                avgcharsperline = avgcharsperline * 1.3 #Inc avg for retry
                
            l_file.close()
        
            if len(lines) > linesback: 
                start=len(lines)-linesback -1
            else: 
                start=0
            if returnlist: return lines[start:len(lines)-1]
        
            out=""
            for l in lines[start:len(lines)-1]: 
                out = out + l + "\n"
            JT_Logger.trace_method("[METHOD_OUT][tail_lines_inner]")
            return out
        except :
            JT_Logger.print_exception("\nException\n")
            out=""
            return out
#==================================================================
#
#==================================================================
    @staticmethod
    def get_valid_line_from_line_list(lineList):
        """get_last_not_empty_file_line"""
        try:
            JT_Logger.trace_method("[METHOD_IN][get_valid_line_from_line_list]")
            out_line = "NULL_LINE_MARK"
            ii_valid_lines = 0
            ii_all_lines = 0
            for line_ii in reversed(lineList):
                line_ii_stripped = line_ii.strip()
                ii_all_lines = ii_all_lines +1
                if(len(line_ii_stripped) > 0 and line_ii_stripped != ""): 
                    out_line = line_ii_stripped
                    ii_valid_lines = ii_valid_lines + 1
                    if(ii_valid_lines > 2):
                        break

                if(ii_all_lines > 500):     
                    out_line = "NULL_LINE_MARK"               
                    break
            JT_Logger.trace_method("[METHOD_OUT][get_valid_line_from_line_list]")    
            return out_line
        except :
            JT_Logger.print_exception("\nException\n")
            JT_Logger.trace_method("[METHOD_OUT_EXC][get_valid_line_from_line_list]")
            out_last_exc = "NULL_LINE_MARK"
            return out_last_exc
        
#==================================================================
#
#==================================================================

    @staticmethod
    def get_valid_line_from_line(p_line):
        """get_last_not_empty_file_line"""
        try:
            l_mm = "get_valid_line_from_line"
            out_line = p_line
            len_line = len(p_line)
            JT_Logger.trace_method("[METHOD_INSIDE][" + l_mm + "][len_line_1:" + str(len_line) + "]")
            
            if ( len_line > 60 ):
                out_line = p_line[0:59]
                
            JT_Logger.trace_method("[METHOD_INSIDE][" + l_mm + "][len_line_2:" + str(len_line) + "]")

            return out_line
        except :
            JT_Logger.print_exception("\nException\n")
            out_last_exc = "NULL_LINE_MARK"
            return out_last_exc
        
#==================================================================
#
#==================================================================
        
    @staticmethod
    def get_last_not_empty_file_line(filename):
        """get_last_not_empty_file_line"""
        try:
            
            JT_Logger.trace_method("[METHOD_IN]" + "[get_last_not_empty_file_line][filename:" + filename + "]")
            l_mm = "get_last_not_empty_file_line"
                        
            fileHandle = None
            
            try:
                fileHandle = open ( filename, "r" )
            except:
                JT_Logger.trace_method("[METHOD_OUT_1][" + l_mm + "][filename:" + filename + "][NOT_EXISTS]")
                out_last_line = "NULL_LINE_MARK"
                return out_last_line

            lineList = fileHandle.readlines()
            fileHandle.close()
                    
            out_line = JT_Os.get_valid_line_from_line_list( lineList )
            
            out_line = JT_Os.get_valid_line_from_line( out_line )

            JT_Logger.trace_method("[METHOD_OUT][get_last_not_empty_file_line][last_file_lane:" + out_line + "]")
            
            return out_line
        except :
            JT_Logger.print_exception("\nException\n")
            out_last_line = "NULL_LINE_MARK"
            return out_last_line
        
#==================================================================
#
#==================================================================

    @staticmethod    
    def get_last_not_empty_file_line_fast(filename,linesback=20,avgcharsperline=75):
        """get_last_not_empty_file_line_fast"""
        try:
            
            l_file = open(filename,'r')
            while 1:
                try: 
                    l_file.seek(-1 * avgcharsperline * linesback,2)
                except IOError: 
                    l_file.seek(0)
                
                if l_file.tell() == 0: 
                    atstart=1
                else: 
                    atstart=0
        
                lines=l_file.read().split("\n")
                if (len(lines) > (linesback+1)) or atstart: 
                    break
                #The lines are bigger than we thought
                avgcharsperline = avgcharsperline * 1.3 #Inc avg for retry
                
            l_file.close()
        
            out_last_line = ""
            for line_ii in reversed(lines):
                if(len(line_ii) >0): 
                    out_last_line = line_ii
                    break       
                     
            return out_last_line
        except :
            JT_Logger.print_exception("\nException\n")
            out=""
            return out

#==================================================================
#
#==================================================================
    @staticmethod
    def run_subprocess_popen_strip_without_logging(cmd):
        JT_Logger.trace_method("[METHOD_IN]" + "[run_subprocess_popen_strip_without_logging]")
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out = p.stdout.read().strip()
        JT_Logger.trace_method("[METHOD_OUT]" + "[run_subprocess_popen_strip_without_logging]")
        return out

#==================================================================
#
#==================================================================
    
    @staticmethod
    def run_subprocess_popen_strip(cmd):
        JT_Logger.trace_method("[METHOD_IN]" + "[run_subprocess_popen_strip]")
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out = p.stdout.read().strip()
        JT_Logger.trace_method("[METHOD_OUT]" + "[run_subprocess_popen_strip]")
        return out
        
#==================================================================
#
#==================================================================
    
    @staticmethod
    def get_euser() :
        """get_euser"""
        JT_Logger.trace_method("[METHOD_IN]" + "[get_euser]")
        dd_out =  JT_OS_Getguid.get_euser() 
        JT_Logger.trace_method("[METHOD_OUT]" + "[get_euser]")
        return dd_out
    
#==================================================================
#
#==================================================================
    
    @staticmethod
    def get_ps_list() :        
        """get_ps_list"""
        JT_Logger.trace_method("[METHOD_IN]" + "[get_ps_list: ps -ef]")
        dd_out =  JT_Os.run_os_command(["ps","-ef"])
        JT_Logger.trace_method("[INFO_METHOD_OUT]" + "[get_ps_list: ps -ef]")
                               
        return dd_out

#==================================================================
#
#==================================================================

    @staticmethod
    def get_ps_list_rms_syb() :        
        """get_ps_list"""
        JT_Logger.trace_method("[METHOD_IN]" + "[get_ps_list_rms_syb: ps -e]")
        dd_out =  JT_Os.run_os_command(["ps","-e"])
        JT_Logger.trace_method("[INFO_METHOD_OUT]" + "[get_ps_list_rms_syb: ps -e]")                               
        return dd_out
        
#==================================================================
#
#==================================================================
    @staticmethod    
    def run_os_command(cmd) :
        JT_Logger.trace_method("[METHOD_IN]" + "[run_os_command]")
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        dd_out= proc.communicate()[0]
        JT_Logger.trace_method("[METHOD_OUT]" + "[run_os_command]")
        return dd_out
#==================================================================
#
#==================================================================
    @staticmethod    
    def get_procinfo_from_ps_line(ps_line,pid_ps_regex) :    
        """returns a tuple (user_from_ps,pid_from_ps)"""
        
        JT_Logger.trace_method("[INFO_METHOD_IN]" 
            + "[get_procinfo_from_ps_line]")        
            
        dd_out = pid_ps_regex.search(ps_line)
        dd_out_user = ""
        dd_out_pid = ""
        if dd_out:
            dd_out_user =dd_out.group(1)             
            dd_out_pid = dd_out.group(2)
                    
        JT_Logger.trace_method("[INFO_METHOD_OUT]" 
                               + "[dd_out_user:" + dd_out_user + "]" 
                               + "[" + dd_out_pid + "]")
        
        return  dd_out_user, dd_out_pid
#==================================================================
#
#==================================================================

    @staticmethod
    def get_pargs_line(user_from_ps,pid_from_ps,executed_user,executed_line,su_mode) :
        return JT_Os.inner_get_pargs_e_line_pexpect(
                                            user_from_ps
                                            ,pid_from_ps
                                            ,executed_user
                                            ,executed_line
                                            , su_mode
                                            ,0)

#==================================================================
#
#==================================================================

    @staticmethod
    def get_pargs_e_line(user_from_ps,pid_from_ps,executed_user,executed_line, su_mode) :
        return JT_Os.inner_get_pargs_e_line_pexpect(
                                            user_from_ps
                                            ,pid_from_ps
                                            ,executed_user
                                            ,executed_line
                                            , su_mode
                                            ,1)
#==================================================================
#
#==================================================================

    @staticmethod
    def inner_get_pargs_e_line(user_from_ps,pid_from_ps,executed_user,executed_line, su_mode,p_pargse) :
        try:
            JT_Logger.trace_method("[INFO_METHOD_IN]") 
            JT_Logger.trace_method( "[get_instance_from_piduser:" + user_from_ps + "]") 
            JT_Logger.trace_method( "[pid_from_ps:" + str(pid_from_ps) + "]")
    
            dd_nsu = su_mode
            if user_from_ps == executed_user :
                cmd = ["pargs",str(pid_from_ps)]
            else :
                if (JT_ManagerConfig.DEF_USE_SU_FOR_ANOTHER_USERS() and su_mode == "use_su") :
                    JT_Logger.print_output("[" + executed_line + "]")        
                    JT_Logger.print_output("you shoud login on user:")  
                    JT_Logger.print_output(" user_from_ps" )
                    JT_Logger.print_output("[" + executed_line + "]")        
                        
                    dd_nsu = raw_input("Accept su: [n] not use su for that ps line,[na] for not use su at all ?: ")
                    if( dd_nsu == "n" or dd_nsu == "na"):
                            cmd = ["pargs",str(pid_from_ps)]
                    else:
                            cmd = ["ssh","-l",user_from_ps,"localhost","pargs",pid_from_ps] 
                else:
                    cmd = ["pargs",str(pid_from_ps)]                            
    
            JT_Logger.trace_hard_level_16("[CMD]")            
            try:            
                JT_Logger.trace_hard_level_16(cmd)
            except:
                " exception in JT_Logger.trace_hard_level_16(cmd)"
                
            if( p_pargse ==1):
                cmd.insert(len(cmd)-1,"-e")
                
            output = JT_Os.run_os_command(cmd)
            
            JT_Logger.trace_method("[METHOD_OUT]") 
            JT_Logger.trace_method( "[get_instance_from_piduser]") 
            
            return output, dd_nsu
        except :
            JT_Logger.print_exception("\nException\n")
            JT_Logger.trace_method("[METHOD_OUT_EXC][inner_get_pargs_e_line_pexpect]")            
            return "", "not_use_su"
#==================================================================
#
#==================================================================
    @staticmethod
    def get_passwd_for_users(p_usr):
        if(p_usr == "rms_syb"):
            return "sybase"
        if(p_usr == "rksup32"):
            return "knet30"
        if(p_usr == "rksup35"):
            return "knet30"                        
        return ""
#==================================================================
#
#==================================================================

    @staticmethod
    def get_su_mode(user_from_ps,executed_user,su_mode):
        JT_Logger.trace_method("[METHOD_IN][get_su_mode]")
        dd_out_su_mode = -1
        if dd_out_su_mode == -1:
            if user_from_ps == executed_user :
                JT_Logger.trace_method("[METHOD_IN][get_su_mode][OUT][1]")
                dd_out_su_mode= 0
                
        if dd_out_su_mode == -1:                
            if su_mode != "use_su" :
                JT_Logger.trace_method("[METHOD_IN][get_su_mode][OUT][2]")
                dd_out_su_mode= 0
                
        if dd_out_su_mode == -1:                
            if JT_ManagerConfig.DEF_USE_SU_FOR_ANOTHER_USERS() == 0 :
                JT_Logger.trace_method("[METHOD_IN][get_su_mode][OUT][3]")
                dd_out_su_mode= 0
                
        if dd_out_su_mode == -1:                
            if JT_Os.get_passwd_for_users(user_from_ps) == "" :
                JT_Logger.trace_method("[METHOD_IN][get_su_mode][OUT][4]")
                dd_out_su_mode= 0
                
        if dd_out_su_mode == -1:
            JT_Logger.trace_method("[METHOD_IN][get_su_mode][OUT][5]")
            dd_out_su_mode = 1
            
        JT_Logger.trace_method("[METHOD_OUT][get_su_mode][" + str(dd_out_su_mode) + "]")    
        return dd_out_su_mode
#==================================================================
#
#==================================================================
        
    @staticmethod
    def inner_get_pargs_e_line_pexpect(
                                       user_from_ps
                                       ,pid_from_ps
                                       ,executed_user
                                       ,executed_line
                                       ,su_mode
                                       ,p_pargse) :
        try:
            
            JT_Logger.trace_method("[METHOD_IN][inner_get_pargs_e_line_pexpect]") 
            JT_Logger.trace_method( "[get_instance_from_piduser:" + user_from_ps + "]") 
            JT_Logger.trace_method( "[pid_from_ps:" + str(pid_from_ps) + "]")
            JT_Logger.trace_method( "[su_mode:" + str(su_mode) + "]")
            JT_Logger.trace_method( "[user_from_ps:" + str(user_from_ps) + "]")
            JT_Logger.trace_method( "[executed_user:" + str(executed_user) + "]")
            JT_Logger.trace_method( "[p_pargse:" + str(p_pargse) + "]")                
            
            ssh_exec = JT_Os.get_su_mode(
                                         user_from_ps
                                         ,executed_user
                                         ,su_mode)
            
            JT_Logger.trace_method( "[ssh_exec:" + str(ssh_exec) + "]")\
                            
            dd_output = None
            
            if(ssh_exec == 0):
                
                cmd = ["pargs",str(pid_from_ps)]
                
                if( p_pargse ==1):
                    cmd.insert(len(cmd)-1,"-e")
                    
                JT_Logger.trace_hard_level_16("[CMD]")            
                try:            
                    JT_Logger.trace_hard_level_16(cmd)
                except:
                    " exception in JT_Logger.trace_hard_level_16(cmd)"
                    
                dd_output = JT_Os.run_os_command(cmd)
                            
            if(ssh_exec == 1):
                l_pass = JT_Os.get_passwd_for_users(user_from_ps)                                        
                JT_Logger.trace_hard_level_16("[user_from_ps:" + user_from_ps + "]")
                JT_Logger.trace_hard_level_16("[l_pass:" + l_pass + "]")
                
                l_comm = "pargs"
                if( p_pargse ==1):
                    l_comm = "pargs -e"
                    
                dd_output = JT_SSH.do_ssh(user_from_ps,l_pass,l_comm)
                
            JT_Logger.trace_method("[METHOD_OUT][inner_get_pargs_e_line_pexpect]")
            return dd_output, su_mode
        except :
            JT_Logger.print_exception("\nException\n")
            JT_Logger.trace_method("[METHOD_OUT_EXC][inner_get_pargs_e_line_pexpect]")            
            return "",su_mode
        
#==================================================================
#
#==================================================================


         
    @staticmethod
    def run_pexpect_print(s_cmd):
        try:
            JT_Logger.trace_method("[METHOD_IN][run_expect_print][" + s_cmd + "]")
            print pexpect.run(s_cmd)
        except :
            JT_Logger.print_exception("[METHOD_EXCEPTION][run_expect_print]")
            JT_Logger.trace_method("[METHOD_OUT_EXC][run_expect_print]")            

    @staticmethod
    def run_pexpect_no_print(s_cmd):
        try:
            JT_Logger.trace_method("[METHOD_IN][run_pexpect_no_print][" + s_cmd + "]")
            pexpect.run(s_cmd)
        except :
            JT_Logger.print_exception("[METHOD_EXCEPTION][run_pexpect_no_print]")
            JT_Logger.trace_method("[METHOD_OUT_EXC][run_pexpect_no_print]")            
    