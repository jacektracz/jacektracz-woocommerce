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
import re
from JT_Logger import JT_Logger
from JT_Logger import JT_LoggerSettings
from JT_Logger import JT_StaticLogger
from JT_Os import JT_Os
from JT_Printer import JT_Printer
from JT_ProcessDef import JT_ProcessDef
from JT_ProcessessDef import JT_ProcessesDef
from JT_PsLine import JT_PsLine
from JT_PsLines import JT_PsLines
from JT_ServerDef import JT_ServerDef
from JT_ServersDef import JT_ServersDef   
from JT_Strings import JT_Strings
from JT_Strings import JT_Strings_find_options
from JT_KgrInstanceDef import JT_KgrInstanceDef
from JT_KgrInstancesDef import JT_KgrInstancesDef
from JT_StaticLoggerFile import JT_StaticLoggerFile
from JT_ManagerConfig import JT_ManagerConfig
from JT_FIND_Argv import JT_FIND_ARGV
#==================================================================
#                JT_MonitorOs
#==================================================================
class JT_ExceutionLineInfo:
    def __init__(self):
        self.m_status = 0
        self.m_info = ""
        self.m_condition = ""
        self.m_line_pid = ""
        self.m_line_ps = ""
        self.m_params = ""
        self.m_current_log_line = 0
        self.m_current_fulfilled_log_line = 0
#==================================================================
#
#==================================================================
                
class JT_MonitorKgr:
    
#==================================================================
#
#==================================================================

    def print_end(self):
        """print_end"""
        print '====================================='
        
#==================================================================
#
#==================================================================


    def __init__(self):
        self.m_servers = JT_ServersDef()
        self.m_kgr_def_instances = JT_KgrInstancesDef()
        self.m_ps_lines = JT_PsLines()
        self.m_founded_processes = JT_ProcessesDef()                        
        self.output = [] 
        self.output_lines = []
        self.kgr_regex = []
        self.pid_ps_regex = []
        self.raw_instances = []
        self.euser = ""
        self.instances = []        
        self.m_su_mode = "not_set"        
        self.commarg_environment_1 = "env_france_ptx"
        self.commarg_servers_2 = "srv_all"
        self.commarg_show_ps_line_3 = "not_print_ps_line"
        self.commarg_use_regex_4 = "not_print_ps_line"
        self.commarg_use_su_5 = "nsu"
        self.commarg_print_all_6 = "not_print_debug"
        self.commarg_use_log_7 = "use_log"
        self.commarg_ps_filter_8 = "no_ps_filter"
        self.m_param_servers = []
        self.m_prind_debug_kgr_and_server = 0
        self.m_current_log_line = 0

#==================================================================
#
#==================================================================
    
    def copy_object(self,dd):
        self = dd
        
#==================================================================
#
#==================================================================

    def get_str_array(self,p_arr):
        s_out = ""
        ii=0
        for dd in p_arr:
            s_out = ("[LINE:" 
                     + "[" + str(ii) + "]" 
                     + "[" + s_out + dd + "]")
            ii = ii+1
        return s_out
        
#==================================================================
#
#==================================================================

    def create_env_from_args(self) :
        """create_env_from_args"""
        try:
            JT_Logger.trace_method("[METHOD_IN]" )
            JT_Logger.trace_method( "[create_env_from_args]") 
    
            self.load_kgr_instances_from_arg_environment_1()
            
            self.create_env_from_arg_set_servers_2()
            
            self.create_env_from_arg_print_line_3()
                        
            self.create_env_from_arg_use_regex_4()
            
            self.create_env_from_arg_use_su_5()
            
            self.create_env_from_arg_print_all_6()
            
            self.create_env_from_arg_use_log_7()
            
            JT_Logger.trace_method("[METHOD_OUT]" )
            JT_Logger.trace_method( "[create_env_from_args]") 
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][create_env_from_args]")

#==================================================================
#
#==================================================================

    def load_kgr_instances_from_arg_environment_1(self) :
        """load_kgr_instances_from_arg_environment_1"""
        
        JT_Logger.trace_method("[METHOD_IN]" )
        JT_Logger.trace_method( "[load_kgr_instances_from_arg_environment_1]") 
        JT_Logger.trace_method( "[p_kgrs:" + self.commarg_environment_1 + "]")
        JT_Logger.trace_method( "[p_srvs:" + self.get_str_array(self.m_param_servers) + "]")
            
        #self.m_kgr_def_instances.fill_default()
        i_loaded = 0
        if self.commarg_environment_1 == "env_france_ptx":
            self.m_kgr_def_instances.init_kgr_instances_ptx()
            i_loaded = 1
            
        if self.commarg_environment_1 == "env_pol_gdy":
            self.m_kgr_def_instances.init_kgr_instances_gdy()
            i_loaded = 1
            
        if self.commarg_environment_1 == "env_pol_gdy_36":
            self.m_kgr_def_instances.init_kgr_instances_gdy_36()
            i_loaded = 1
            
        if self.commarg_environment_1 == "env_test":
            self.m_kgr_def_instances.init_kgr_instances_test()
            i_loaded = 1
            
        if self.commarg_environment_1 == "kgrSet":
            self.m_kgr_def_instances.init_kgr_instances_kgrSet()
            i_loaded = 1
            
        if self.commarg_environment_1 == "fatih":
            self.m_kgr_def_instances.init_kgr_instances_fatih()
            i_loaded = 1
            
        if self.commarg_environment_1 == "kgr35s":
            self.m_kgr_def_instances.init_kgr_instances_kgr35s()
            i_loaded = 1
            
        if self.commarg_environment_1 == "kgr35b":
            self.m_kgr_def_instances.init_kgr_instances_kgr35b()
            i_loaded = 1
            
        if self.commarg_environment_1 == "kgr32c":
            self.m_kgr_def_instances.init_kgr_instances_kgr32c()
            i_loaded = 1
            
        if self.commarg_environment_1 == "kgr32a":
            self.m_kgr_def_instances.init_kgr_instances_kgr32a()
            i_loaded = 1
            
        if self.commarg_environment_1 == "kgr32b":
            self.m_kgr_def_instances.init_kgr_instances_kgr32b()
            i_loaded = 1
            
        if(i_loaded == 0):
            self.m_kgr_def_instances.add_kgr_instance_by_key(
                                                             self.commarg_environment_1)
            
        JT_Logger.trace_method("[METHOD_OUT]" )
        JT_Logger.trace_method( "[load_kgr_instances_from_arg_environment_1]") 
        
#==================================================================
#
#==================================================================

    def create_env_from_arg_print_line_3(self) :
        """create_env_from_arg_3"""
        
        JT_Logger.trace_method("[INFO_METHOD_IN][create_env_from_arg_3]" )                    
        if(self.commarg_show_ps_line_3== "print_ps_line" ):
            JT_Logger.trace_hard_level_20("[PRINT_LINE_SET_TO_1]" )
            JT_Printer().set_to_print_line()
        else:
            JT_Printer().uset_to_print_line()

#==================================================================
#
#==================================================================

    def create_env_from_arg_use_regex_4(self) :
        """create_env_from_arg_use_regex_4"""
        JT_Logger.trace_method("[METHOD_IN][create_env_from_arg_use_regex_4]" )
        
        if(self.commarg_use_regex_4 == "use_regex" ):
            JT_Strings_find_options().set_reg_ex_option()
        else:
            JT_Strings_find_options().uset_reg_ex_option()
        JT_Logger.trace_method("[METHOD_OUT][create_env_from_arg_use_regex_4]" )

#==================================================================
#
#==================================================================

    def create_env_from_arg_use_su_5(self) :
        """create_env_from_arg_use_su_5"""
        JT_Logger.trace_method("[INFO_METHOD_IN]" + "[create_env_from_arg_use_su_5]")
        JT_Logger.trace_method("[commarg_use_su_5:" +self.commarg_use_su_5 + "]")
            
        if(self.commarg_use_su_5 == "use_su" ):
            self.m_su_mode = "use_su"
        else:
            self.m_su_mode = "not_use_su"
        
        JT_Logger.trace_method("[m_su_mode:" + self.m_su_mode + "]" )    
        JT_Logger.trace_method("[METHOD_OUT]" + "[create_env_from_arg_use_su_5]")
        
            
#==================================================================
#
#==================================================================

    def create_env_from_arg_print_all_6(self) :
        """create_env_from_arg_print_all_6"""
        JT_Logger.trace_method("[METHOD_IN]" 
                               + "[create_env_from_arg_print_all_6]" )         
           
        JT_LoggerSettings().uset_to_output()
                   
        if(self.commarg_print_all_6 == "print_debug"):
            JT_LoggerSettings().set_to_output()
            
        if(self.commarg_print_all_6 == "not_print_debug"):
            JT_LoggerSettings().uset_to_output()
            
        try:
            JT_Logger.trace_hard_level_20("[METHOD_INSIDE]]"  
                + "[" + str(JT_Strings_find_options().get_reg_ex_option()) + "]")    

        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][create_env_from_arg_print_all_6]")
        
        JT_Logger.trace_method("[METHOD_OUT]" 
                               + "[create_env_from_arg_print_all_6]" )         

#==================================================================
#
#==================================================================

    def create_env_from_arg_use_log_7(self) :
        
        JT_Logger.trace_method("[METHOD_IN]" + "[create_env_from_arg_use_log_7]" )
        if(self.commarg_use_log_7  == "use_log"):
            JT_StaticLoggerFile().set_to_loging_self_log()
        else:
            JT_StaticLoggerFile().uset_to_loging_self_log()

        
        JT_Logger.trace_method("[METHOD_OUT]" + "[create_env_from_arg_use_log_7]" )         
            
#==================================================================
#
#==================================================================
    
    
    def create_env_from_arg_set_servers_2(self) :
        """create_env_from_arg_set_servers_2"""
        
        try:
            JT_Logger.trace_method("[METHOD_IN]" )
            JT_Logger.trace_method("[create_env_from_arg_set_servers_2]") 
            JT_Logger.trace_method( "[p_srvs:" + self.get_str_array(self.m_param_servers) + "]")
                
            self.m_param_servers = ["srv_all"]
            
            i_is_param_in_list = 0
            if(self.commarg_servers_2 == "srv_all"):
                self.m_param_servers = ["srv_all"]
                i_is_param_in_list = 1
                
            if(self.commarg_servers_2 == "srv_test"):
                self.m_param_servers = ["srv_test"]
                i_is_param_in_list = 1
                
            if(self.commarg_servers_2 == "guiadapter"):
                self.m_param_servers = ["guiadapter"]
                i_is_param_in_list = 1
                    
            if(self.commarg_servers_2 == "srv_jboss"):
                self.m_param_servers = ["srv_jboss"]    
                i_is_param_in_list = 1
                
            if (i_is_param_in_list == 0):
                self.m_param_servers = []
                self.m_param_servers.append(str(self.commarg_servers_2))
                
            JT_Logger.trace_method( "[METHOD_INSIDE_CREATE_SRV][p_srvs:" + self.get_str_array(self.m_param_servers) + "]")
            
            for ii_srv in self.m_param_servers :
                try:
                    i_filled = 0
                    if ii_srv == "srv_test":
                        JT_Logger.trace_method("[ADDING_SRV_TEST]") 
                        self.m_servers.internal_init_servers_definition_test()
                        i_filled = 1
            
                    if ii_srv == "gui":
                        JT_Logger.trace_method("[ADDING_SRV_GUI]") 
                        self.m_servers.internal_init_servers_definition_gui()
                        i_filled = 1
                        
                    if ii_srv == "kns":
                        JT_Logger.trace_method("[ADDING_SRV_KNS]") 
                        self.m_servers.internal_init_servers_definition_kns()
                        i_filled = 1
                        
                    if ii_srv == "ems":
                        JT_Logger.trace_method("[ADDING_SRV_EMS]") 
                        self.m_servers.internal_init_servers_definition_ems()
                        i_filled = 1
                        
                    if ii_srv == "kts":
                        JT_Logger.trace_method("[ADDING_SRV_KTS]") 
                        self.m_servers.internal_init_servers_definition_kts()
                        i_filled = 1
                        
                    if ii_srv == "guiadapter":
                        JT_Logger.trace_method("[ADDING_SRV_GUIADAPTER]") 
                        self.m_servers.internal_init_servers_definition_gui_adapter()
                        i_filled = 1
                        
                    if ii_srv == "srv_all":
                        JT_Logger.trace_method("[ADDING_SRV_ALL]") 
                        self.m_servers.internal_init_servers_definition_all()
                        i_filled = 1
                        
                    if ii_srv == "srv_jboss":
                        JT_Logger.trace_method("[internal_init_servers_definition_jboss]") 
                        self.m_servers.internal_init_servers_definition_jboss()
                        i_filled = 1
                        
                    if i_filled == 0:
                        try:
                            JT_Logger.trace_method("[ADDING_SRV_BY_KEY]" + "[" + ii_srv + "]")
                            self.m_servers.get_srv_by_key(ii_srv)
                        except:
                            JT_Logger.print_exception("\nException_3")
                            
                except :
                    JT_Logger.print_exception("\nException")
                    JT_Logger.trace_method("[METHOD_OUT_EXC][create_env_from_arg_set_servers_2]")
                    
            JT_Logger.trace_method("[METHOD_OUT]" )
            JT_Logger.trace_method("[create_env_from_arg_set_servers_2]") 
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][create_env_from_arg_set_servers_2]")
            

#==================================================================
#
#==================================================================

    
    def fill_environments_data(self) :
        """fill_environments_data"""
        try:
            JT_Logger.trace_method("[INFO_METHOD_IN]") 
            JT_Logger.trace_method("[fill_environments_data]")
            try: 
                JT_Logger.trace_method("[p_kgrs:" + self.commarg_environment_1 + "]")
                JT_Logger.trace_method("[p_srvs:" + self.get_str_array(self.m_param_servers) + "]")
            except :
                JT_Logger.print_exception("\nException_l1")
                    
            self.pid_ps_regex = re.compile("^\s+(\w+)\s+(\d+)")        
            
            self.euser = JT_Os.get_euser()
            
            JT_Logger.trace_method("[METHOD_OUT][fill_environments_data]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_environments_data]")
            
#==================================================================
#
#==================================================================

    def fill_all_ps_lines(self) :
        """fill_all_ps_lines"""
        try:
            l_m = "fill_all_ps_lines"
            JT_Logger.trace_method("[INFO_METHOD_IN]") 
            JT_Logger.trace_method("[fill_all_ps_lines]")
             
            try:
                JT_Logger.trace_method("[p_kgrs:" + self.commarg_environment_1 + "]")
                JT_Logger.trace_method("[p_srvs:" + self.get_str_array(self.m_param_servers) + "]")
            except :
                JT_Logger.print_exception("\nException_log_info_only")
                                                            
            if (self.euser == "rms_syb"):
                JT_Logger.trace_hard_level_20("[M_I][" + l_m + "][PS_FOR_RMS_SYB]" )
                self.output = JT_Os.get_ps_list_rms_syb()
            else:
                JT_Logger.trace_hard_level_20("[M_I][" + l_m + "][PS_FOR_RMS_SYB]" )
                self.output = JT_Os.get_ps_list()        
            
            JT_Logger.trace_hard_level_20("[M_I][" + l_m + "][INFO_OUTPUT_FROM_PS_1]" )
            
            self.output_lines = self.output.splitlines()
            
            JT_Logger.trace_hard_level_20("[M_I][" + l_m + "][INFO_OUTPUT_FROM_PS_2]" )
            #JT_Logger.trace_hard_level_20("[" + self.get_str_array(self.output_lines) + "]")
            
                    
            for line in self.output_lines :
                if (self.line_is_excluded(line) == 0):
                    if (self.commarg_ps_filter_8 != "no_ps_filter" ):
                        if(line.find(self.commarg_ps_filter_8) >= 0) :
                            JT_Logger.trace_hard_level_20("[M_I][" + l_m + "][PS_LINE_INCLUDED_WITH_FILTER]")                                                 
                            self.m_ps_lines.add_ps_line(line)
                        else:
                            JT_Logger.trace_hard_level_20("[M_I][" + l_m + "][LINE_EXCLUDED_WITH_FILTER][" + line + "]")
                    else:
                        JT_Logger.trace_hard_level_20("[M_I][" + l_m + "][PS_LINE_INCLUDED_WITHOUT_FILTER]")
                        self.m_ps_lines.add_ps_line(line)
                else:                    
                    JT_Logger.trace_hard_level_20("[M_I][" + l_m + "][PS_LINE_EXCLUDED_BY_DESIGN]")
            
            JT_Logger.trace_method("[METHOD_OUT]" + l_m + "[NUMBER_OF_LINES_INCLUDED]")
            JT_Logger.trace_method("[" +str(len(self.m_ps_lines.m_ps_lines)) + "]")        
            JT_Logger.trace_method("[METHOD_OUT][fill_all_ps_lines]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_all_ps_lines]")
                        
        
#==================================================================
#
#==================================================================
        
    def fill_servers_in_env(self):
        
        try:        
            JT_Logger.trace_method("[INFO_METHOD_IN]" + "[fill_servers_in_env]")                                    
            
            for dd_kgr_instance in self.m_kgr_def_instances.m_kgr_instances:
                dd_ki = JT_KgrInstanceDef()
                dd_ki = dd_kgr_instance                        
                self.print_debug_kgr_instance(dd_ki.m_KgrInstanceName)
                
                self.fill_kgr_instances_with_servers( dd_kgr_instance )
                
            JT_Logger.trace_method("[METHOD_OUT][fill_servers_in_env]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_servers_in_env]")

#==================================================================
#
#==================================================================

    def fill_kgr_instances_with_servers(self,dd_kgr_instance):
        
        try:                 
                 
            JT_Logger.trace_method("[METHOD_IN][fill_kgr_instances_with_servers]")
            dd_ki = JT_KgrInstanceDef()
            dd_ki = dd_kgr_instance                        
            JT_Logger.trace_hard_level_20("[m_KgrInstanceName:" + dd_ki.m_KgrInstanceName + "]")
                
            
            for dd_server_ii in self.m_servers.m_srvs:
                dd_srv_def = JT_ServerDef ()
                dd_srv_def = dd_server_ii
                
                self.print_debug_server_instance(
                                                 dd_ki.m_KgrInstanceName
                                                 , dd_srv_def.m_server_name)
                
                self.fill_server_with_all_ps_lines(
                                                   dd_ki
                                                   , dd_srv_def)
                                         
            JT_Logger.trace_method("[METHOD_OUT][fill_kgr_instances_with_servers]")
        except :
            JT_Logger.print_exception("\nException_in_2")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_kgr_instances_with_servers]")

#==================================================================
#
#==================================================================

    def fill_ps_lines_with_data(self):
        try:
            JT_Logger.trace_method("[METHOD_IN][fill_ps_lines_with_data]")
            
                                                   
            for dd_ps_line_ii in self.m_ps_lines.m_ps_lines:
                dd_js_line = JT_PsLine()
                dd_js_line = dd_ps_line_ii        
                str_ps_line = dd_js_line.m_Line
                user_from_ps,pid_from_ps = JT_Os.get_procinfo_from_ps_line(
                                                                       str_ps_line
                                                                       ,self.pid_ps_regex)
                                
                dd_ps_line_ii.m_user_id = user_from_ps
                dd_ps_line_ii.m_pid_id = pid_from_ps                
            JT_Logger.trace_method("[METHOD_OUT][fill_ps_lines_with_data]")                    
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_ps_lines_with_data]")

#==================================================================
#
#==================================================================

    def fill_server_with_all_ps_lines_servers_first(self,dd_kgr_instance,dd_server):
        try:
            JT_Logger.trace_method("[METHOD_IN][fill_server_with_all_ps_lines_servers_first]")
            
            JT_Logger.trace_hard_level_20("[m_server_name:" + dd_server.m_server_name + "]") 
                                                   
            for dd_ps_line_ii in self.m_ps_lines.m_ps_lines:
                dd_js_line = JT_PsLine()
                dd_js_line = dd_ps_line_ii        
                str_ps_line = dd_js_line.m_Line
                JT_Logger.log_ps_line_hard("[METHOD_IN][fill_server_with_all_ps_lines_servers_first]")
                JT_Logger.log_ps_line_hard("[PS_LINE_HARD]" + "[" + str_ps_line + "]")
                dd_li = JT_ExceutionLineInfo()
                self.find_processes_for_server_ex(dd_ps_line_ii
                                                  , str_ps_line
                                                  , dd_server
                                                  , dd_kgr_instance
                                                  , "all"
                                                  , dd_li)
                
                
            JT_Logger.trace_method("[METHOD_OUT][fill_server_with_all_ps_lines_servers_first]")                    
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_server_with_all_ps_lines_servers_first]")


#==================================================================
#
#==================================================================

    def print_servers_in_env(self):
        try:        
            JT_Logger.trace_method("[INFO_METHOD_IN]" + "[print_servers_in_env]")
            self.print_servers_in_en_with_and_without_ref_2()            
            JT_Logger.trace_method("[METHOD_OUT][print_servers_in_env]")            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_servers_in_env]")
            
#==================================================================
#
#==================================================================
    def print_servers_in_en_with_and_without_ref_2(self):
        try:        
            JT_Logger.trace_method("[INFO_METHOD_IN]" + "[print_servers_in_en_with_and_without_ref_2]")
            for dd_kgr_instance in self.m_kgr_def_instances.m_kgr_instances:
                
                count_ii = len(dd_kgr_instance.m_procs_for_kgrinstance.m_processess)                    
    
                JT_Logger.print_output("************************************************************************")                
                JT_Logger.print_output("*")        
                JT_Logger.print_output("*                 KGR:" 
                    +"[" + dd_kgr_instance.m_KgrInstanceName + "]" 
                    + "[srvs:" + str(count_ii) + "]")
                JT_Logger.print_output("*")                
                JT_Logger.print_output("************************************************************************")
                        
                JT_Logger.print_output("************************************************************************")                
                JT_Logger.print_output("*" 
                    +"[" + dd_kgr_instance.m_KgrInstanceName + "]" 
                    + " WITHOUT_REFERENCED_PROCESSESS")
                JT_Logger.print_output("************************************************************************")        
    
                for dd_process_ii in dd_kgr_instance.m_procs_for_kgrinstance.m_processess:
                    dd_process = JT_ProcessDef()
                    dd_process = dd_process_ii
                    if(len(dd_process.m_referenced_processess) == 0 ):
                        dd_process.print_process()                        

                JT_Logger.print_output("************************************************************************")                
                JT_Logger.print_output("*" 
                    +"[" + dd_kgr_instance.m_KgrInstanceName + "]" 
                    + " WITH_REFERENCED_PROCESSESS")
                JT_Logger.print_output("************************************************************************")        

                for dd_process_ii in dd_kgr_instance.m_procs_for_kgrinstance.m_processess:
                    dd_process = JT_ProcessDef()
                    dd_process = dd_process_ii
                    if(len(dd_process.m_referenced_processess) > 0 ):
                        dd_process.print_process()                        
                
            JT_Logger.trace_method("[METHOD_OUT][print_servers_in_en_with_and_without_ref_2]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_servers_in_env]")

#==================================================================
#
#==================================================================

    def print_servers_in_en_with_and_without_ref(self):
        try:        
            JT_Logger.trace_method("[INFO_METHOD_IN]" + "[print_servers_in_env]")
            for dd_kgr_instance in self.m_kgr_def_instances.m_kgr_instances:
                
                count_ii = len(dd_kgr_instance.m_procs_for_kgrinstance.m_processess)                    
    
                JT_Logger.print_output("************************************************************************")                
                JT_Logger.print_output("*")        
                JT_Logger.print_output("*                 KGR:" 
                    +"[" + dd_kgr_instance.m_KgrInstanceName + "]" 
                    + "[srvs:" + str(count_ii) + "]")
                JT_Logger.print_output("*")                
                JT_Logger.print_output("************************************************************************")        
    
                for dd_process_ii in dd_kgr_instance.m_procs_for_kgrinstance.m_processess:
                    dd_process = JT_ProcessDef()
                    dd_process = dd_process_ii
                    dd_process.print_process()                        
                
            JT_Logger.trace_method("[METHOD_OUT][print_servers_in_env]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_servers_in_env]")

#==================================================================
#
#==================================================================

    def print_servers_in_en_without_ref(self):
        try:        
            JT_Logger.trace_method("[INFO_METHOD_IN]" + "[print_servers_in_env]")
            for dd_kgr_instance in self.m_kgr_def_instances.m_kgr_instances:
                
                count_ii = len(dd_kgr_instance.m_procs_for_kgrinstance.m_processess)                    
    
                JT_Logger.print_output("************************************************************************")                
                JT_Logger.print_output("*")        
                JT_Logger.print_output("*                 KGR:" 
                    +"[" + dd_kgr_instance.m_KgrInstanceName + "]" 
                    + "[srvs:" + str(count_ii) + "]")
                JT_Logger.print_output("*")                
                JT_Logger.print_output("************************************************************************")        
    
                for dd_process_ii in dd_kgr_instance.m_procs_for_kgrinstance.m_processess:
                    dd_process = JT_ProcessDef()
                    dd_process = dd_process_ii
                    if(len(dd_process.m_referenced_processess) == 0 ):
                        dd_process.print_process()                        
                
            JT_Logger.trace_method("[METHOD_OUT][print_servers_in_env]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_servers_in_env]")
            
#==================================================================
#
#==================================================================
                    
    def print_servers_in_en_with_ref(self):
        try:        
            JT_Logger.trace_method("[INFO_METHOD_IN]" + "[print_servers_in_env]")
            for dd_kgr_instance in self.m_kgr_def_instances.m_kgr_instances:
                
                count_ii = len(dd_kgr_instance.m_procs_for_kgrinstance.m_processess)                    
    
                JT_Logger.print_output("************************************************************************")                
                JT_Logger.print_output("*")        
                JT_Logger.print_output("*                 KGR:" 
                    +"[" + dd_kgr_instance.m_KgrInstanceName + "]" 
                    + "[srvs:" + str(count_ii) + "]")
                JT_Logger.print_output("*")                
                JT_Logger.print_output("************************************************************************")        
    
                for dd_process_ii in dd_kgr_instance.m_procs_for_kgrinstance.m_processess:
                    dd_process = JT_ProcessDef()
                    dd_process = dd_process_ii
                    if(len(dd_process.m_referenced_processess) > 0 ):                    
                        dd_process.print_process()                        
                
            JT_Logger.trace_method("[METHOD_OUT][print_servers_in_env]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_servers_in_env]")

#==================================================================
#
#==================================================================
                    
    def print_servers_in_env_to_log(self):        
        try:
            JT_Logger.print_to_log_only("[INFO_METHOD_IN]" + "[print_servers_in_env")
            for dd_kgr_instance in self.m_kgr_def_instances.m_kgr_instances:
                
                                    
                JT_Logger.print_to_log_only("KGR_INSTANCE_START_PRINT_DATA:") 
                JT_Logger.print_to_log_only( "[m_KgrInstanceName:" +  dd_kgr_instance.m_KgrInstanceName + "]") 
                
                
                for dd_process in dd_kgr_instance.m_procs_for_kgrinstance.m_processess:
                    dd_process.print_process_to_log()
                    
                JT_Logger.print_to_log_only("KGR_INSTANCE_END:" 
                    + dd_kgr_instance.m_KgrInstanceName + "]")

            JT_Logger.trace_method("[METHOD_OUT][print_servers_in_env_to_log]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_servers_in_env_to_log]")
                    
#==================================================================
#
#==================================================================
                
    def print_state(self):        
        try:
            JT_Logger.trace_method("[METHOD_IN]" + "[print_state]")
            len_ps_lines = len(self.m_ps_lines.m_ps_lines)
            JT_Logger.trace_method("[LEN_PS_LINES:" + str(len_ps_lines) + "]")            
            len_kgrs = len(self.m_kgr_def_instances.m_kgr_instances)              
            JT_Logger.trace_method("[LEN_KGRS][find_kgr_instances][" + str(len_kgrs) + "]")
            len_srvs = len(self.m_servers.m_srvs)
            JT_Logger.trace_method("[LEN_SRVS][" + str(len_srvs) + "]")            
            JT_Logger.trace_method("[METHOD_OUT]" + "[print_state]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_state]")
#==================================================================
#
#==================================================================

    def print_state_header(self,p_header):        
        try:
            JT_Logger.trace_method("[METHOD_IN]" + "[print_state_header]")
            
            JT_Logger.print_output("*******************************************************")
            JT_Logger.print_output("*")
            JT_Logger.print_output("*          " + p_header + " *")
            JT_Logger.print_output("*")
            JT_Logger.print_output("*******************************************************")
            
            JT_Logger.trace_method("[METHOD_OUT]" + "[print_state_header]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_state_header]")

#==================================================================
#
#==================================================================
    def print_state_servers(self):        
        try:
            JT_Logger.trace_method("[METHOD_IN]" + "[print_state_servers]")
            
            self.print_state_header("[STATE_SRVS]")
            
            try:
                for dd_srv in self.m_servers.m_srvs:
                    dd_s = JT_ServerDef()
                    dd_s = dd_srv
                    JT_Logger.print_output("[SRV][" + dd_s.m_server_name + "]"
                                           + "[" + dd_s.m_ProcessName  + "]")
                                                
                    ll_sd = dd_s.get_srv_info("kgrExample")
                    JT_Logger.print_output("[SRV][ll_sd:" + ll_sd + "]")
                    JT_Logger.print_output("")
                    
            except :
                JT_Logger.print_exception("\nException_2")


            JT_Logger.print_output("[METHOD_OUT]" + "[print_state]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_state_servers]")
#==================================================================
#
#==================================================================

    def print_state_kgrs(self):        
        try:
            JT_Logger.trace_method("[METHOD_IN]" + "[print_state_kgrs]")
            
            self.print_state_header("[STATE_KGRS]")
            
            try:
                for dd_kgr_instance in self.m_kgr_def_instances.m_kgr_instances:
                    dd_k = JT_KgrInstanceDef()
                    dd_k = dd_kgr_instance                
                    JT_Logger.print_output("[KGR][" + dd_k.m_KgrInstanceName + "]")
            except :
                JT_Logger.print_exception("\nException_1")


            JT_Logger.print_output("[METHOD_OUT]" + "[print_state_kgrs]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_state_kgrs]")
#==================================================================
#
#==================================================================

    def print_state_ps_lines(self):        
        try:
            JT_Logger.trace_method("[METHOD_IN]" + "[print_state_ps_lines]")
            
            self.print_state_header("STATE_PS_LINES")
            
            try:
                for dd_line_ii in self.m_ps_lines.m_ps_lines :
                    dd_line = JT_PsLine()
                    dd_line = dd_line_ii
                    JT_Logger.print_output("[PS_LINE_IN_EXECUTION]" 
                                           + "[USER:" + dd_line.m_user_id + "]"
                                           + "[PID:" + dd_line.m_pid_id + "]"
                                           + "[PS_LINE:" + dd_line.m_Line + "]"
                                           )                                       
            except :
                JT_Logger.print_exception("\nException_3")


            JT_Logger.print_output("[METHOD_OUT]" + "[print_state_ps_lines]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_state_ps_lines]")
            
#==================================================================
#
#==================================================================

    
    def print_state_ex(self):        
        try:
            JT_Logger.trace_method("[METHOD_IN]" + "[print_state_ex]")
            
            self.print_state_kgrs()
            self.print_state_servers()
            self.print_state_ps_lines()
                
            JT_Logger.print_output("[METHOD_OUT]" + "[print_state]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_state_ex]")
            
#==================================================================
#
#==================================================================
            
    def find_refereced_processs(self):
        try:        
            JT_Logger.trace_method("[INFO_METHOD_IN]" + "[find_refereced_processs]")
            for dd_kgr_instance in self.m_kgr_def_instances.m_kgr_instances:            
                for dd_process_ii in dd_kgr_instance.m_procs_for_kgrinstance.m_processess:                    
                     
                    JT_Logger.trace_method("[IN_LOOP]find_refereced_processs]")                     
                    dd_process = JT_ProcessDef()
                    dd_process = dd_process_ii
                    self.find_refereced_process_by_id( dd_process )

            JT_Logger.trace_method("[METHOD_OUT][find_refereced_processs]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_refereced_processs]")


#==================================================================
#
#==================================================================

    def get_processess_by_id(self,p_process_id,p_KgrInstancesDef):
        try:        
            JT_Logger.trace_method("[INFO_METHOD_IN]" + "[get_processess_by_id")
            dd_kgrs = JT_KgrInstancesDef()
            dd_kgrs = p_KgrInstancesDef
            ll_out = []
            for dd_kgr_instance_ii in dd_kgrs.m_kgr_instances:
                      
                dd_kgr_instance = JT_KgrInstanceDef()     
                dd_kgr_instance = dd_kgr_instance_ii
                 
                for dd_process_ii in dd_kgr_instance.m_procs_for_kgrinstance.m_processess:
                    
                    JT_Logger.trace_method("[METHOD_INSIDE]" + "[dd_process]")
                    
                    dd_ref_process = JT_ProcessDef()
                    dd_ref_process = dd_process_ii                    
                    
                    if (dd_ref_process.m_pid == p_process_id ):
                        ll_out.append(dd_ref_process)
                                        
            JT_Logger.trace_method("[METHOD_OUT]" + "[get_processess_by_id]")
            return ll_out
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][get_processess_by_id]")
            ll_out_e = []
            return ll_out_e    
                    
#==================================================================
#
#==================================================================
                

    def find_refereced_process_by_id(self,p_ProcessDef):
        try:        
            JT_Logger.trace_method("[INFO_METHOD_IN]" + "[find_refereced_process_by_id")
            ll_m = "find_refereced_process_by_id"
            dd_proc = JT_ProcessDef()
            dd_proc = p_ProcessDef
            
            ll_procs_with_equal_id = self.get_processess_by_id(
                                                               dd_proc.m_pid
                                                               ,self.m_kgr_def_instances)

            JT_Logger.trace_method("[METHOD_INSIDE][" + ll_m + "]" 
                                   + "[PID_ID:" + str(dd_proc.m_pid) + "]"
                                   + "[LEN_PROC_WITH_EQUAL_ID:" + str(len(ll_procs_with_equal_id)) + "]"
                                   )
            for dd_ref_process_ii in ll_procs_with_equal_id:            
                dd_ref_process = JT_ProcessDef()
                dd_ref_process = dd_ref_process_ii                    
                if ( p_ProcessDef.m_kgr_instance != dd_ref_process.m_kgr_instance) :
                    JT_Logger.trace_method("[METHOD_INSIDE][" + ll_m + "][ADD_WITH_ANOTHER_INSTANCE]")
                    dd_proc.m_referenced_process_name = p_ProcessDef.m_kgr_instance
                    dd_proc.m_referenced_processess.append(dd_ref_process)
                else:
                    JT_Logger.trace_method("[METHOD_INSIDE][" + ll_m + "][SAME_INSTANCE]") 
                                   
                    
                                        
            JT_Logger.trace_method("[METHOD_OUT]" + "[find_refereced_process_by_id]")
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_refereced_process_by_id]")
                
    
                    
#==================================================================
#
#==================================================================
                
    def print_server_info(self,str_ps_line,dd_server,dd_kgr_instance):            
        """print_server_info"""
        
#==================================================================
#
#==================================================================
        
    def is_kgr_in_ps(self,str_ps_line,kgr_instance_name):
        """is_kgr_in_ps"""
        try:        
            dd_out= JT_Strings.find_word(str_ps_line,kgr_instance_name)            
            return dd_out
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][is_kgr_in_ps]")
            return -1        

#==================================================================
#
#==================================================================
            
    @staticmethod
    def is_instance_for_pid(user_from_ps,pid_from_ps,instance,executed_user) :
    
        JT_Logger.trace_method("[INFO_METHOD_IN]") 
        JT_Logger.trace_method("[is_instance_for_pid:" + user_from_ps + "]") 
        JT_Logger.trace_method("[pid_from_ps:" + str(pid_from_ps) + "]")
            
        if user_from_ps == executed_user :
            cmd = ["pargs",str(pid_from_ps)]
        else :            
            cmd = ["pargs",str(pid_from_ps)]

        JT_Logger.trace_hard_level_16("[CMD]")            
        JT_Logger.trace_hard_level_16(cmd)
        
        output = JT_Os.run_os_command(cmd)
        
        if JT_Strings.find_word(output, instance) > -1:
            return 1
         
        cmd.insert(len(cmd)-1,"-e")
        output = JT_Os.run_os_command(cmd)
        
        if JT_Strings.find_word(output, instance) > -1:
            return 1
             
        return -1
    
            
#==================================================================
#
#==================================================================
    def is_kgr_in_pargs(self, user_from_ps,pid_from_ps,kgr_instance_name,euser):
        """is_kgr_in_pargs"""
        try:
            JT_Logger.trace_method("[METHOD_IN][is_kgr_in_pargs]")
            dd_out = JT_MonitorKgr.is_instance_for_pid(
                                                       user_from_ps
                                                       ,pid_from_ps
                                                       ,kgr_instance_name
                                                       ,euser)
            JT_Logger.trace_method("[METHOD_OUT][is_kgr_in_pargs]")
            return dd_out
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][is_kgr_in_pargs]")
            return -1        
#==================================================================
#
#==================================================================
    def check_all_in_line(self,ps_line,pargs,pserverdef):
        """check_all_in_line"""
#==================================================================
#
#==================================================================

    def check_all_args_in_line(self,ps_line,pargs):
        """check_all_args_in_line"""
        
        try:
            JT_Logger.trace_hard_level_18("[METHOD_IN][check_all_args_in_line]")     
            JT_Logger.log_ps_line("[METHOD_IN][check_all_args_in_line][" + ps_line + "]")
            dd_out = 1
            for pp_par in pargs.m_Params:
                JT_Logger.trace_hard_level_18("WORD:[" + pp_par.m_ParamName + "]")
                dd_out =  JT_Strings.find_word(ps_line, pp_par.m_ParamName )
                JT_Logger.trace_hard_level_18("WORD:[" + pp_par.m_ParamName + "]")                
                JT_Logger.trace_hard_level_18("[" + str(dd_out) + "]")
                if dd_out < 0:
                    JT_Logger.trace_hard_level_18("[INSIDE][break_with_no_word[" + pp_par.m_ParamName + "]") 
                    break
    
            JT_Logger.trace_hard_level_18("[METHOD_OUT][check_all_args_in_line]")                                                                     
            JT_Logger.trace_hard_level_18( "[dd_out:" + str(dd_out) + "]")
                            
            return dd_out

        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][check_all_args_in_line]")
            return -1

#==================================================================
#
#==================================================================
        
    def is_word_in_line(self, ps_line,server_name):
        """is_word_in_line"""
        try:
            dd_out =  JT_Strings.find_word(ps_line,server_name)
            return dd_out
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][check_all_args_in_line]")
            return -1
        
            
#==================================================================
#
#==================================================================
        
    def get_generic_one_word(self, server_name):
        try:
            l_words = []
            l_words.append("" + server_name + "")            
            return l_words
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][get_generic_one_word]")
            raise

        
#==================================================================
#
#==================================================================

    def check_one_word_from_list(self, ps_line,l_words):
        try:
            JT_Logger.trace_method("[METHOD_IN][check_one_word_from_list]")
            dd_out = -1            
            for l_word in l_words:
                JT_Logger.trace_method("[word:" + l_word + "]")
                dd_out_tmp = JT_Strings.find_word(ps_line, l_word )
                JT_Logger.trace_hard_level_18("[" + str(dd_out) + "]")
                if dd_out_tmp >= 0 :
                    dd_out = dd_out_tmp
                    break
            JT_Logger.trace_method("[METHOD_OUT][check_one_word_from_list]")
            JT_Logger.trace_method("[" + str(dd_out) + "]")    
            return dd_out
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][check_one_word_from_list]")
            return -1

#==================================================================
#
#==================================================================
    def check_server_for_ps_line(self, ps_line,server_name):
        """check_server_for_parg_line"""            
        try:
            JT_Logger.trace_method("[METHOD_IN][check_server_for_ps_line]")
            l_words = self.get_generic_one_word(server_name)
            dd_out = self.check_one_word_from_list(ps_line,l_words)
                                            
            JT_Logger.trace_hard_level_18("[METHOD_OUT][check_server_for_ps_line]")                                                                     
            JT_Logger.trace_hard_level_18( "[dd_out:" + str(dd_out) + "]")                            
            return dd_out            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][check_server_for_ps_line]")
            return -1

#==================================================================
#
#==================================================================
    def check_server_for_parge_line(self, ps_line,server_name):
        """check_server_for_parg_line"""
        try:
            JT_Logger.trace_method("[METHOD_IN][check_server_for_parge_line]")
            l_words = self.get_generic_one_word(server_name)
            dd_out = self.check_one_word_from_list(ps_line,l_words)
            
                
            JT_Logger.trace_hard_level_18("[METHOD_OUT][check_server_for_parge_line]")                                                                     
            JT_Logger.trace_hard_level_18( "[dd_out:" + str(dd_out) + "]")
                            
            return dd_out            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][check_server_for_parge_line]")
            return -1
#==================================================================
#
#==================================================================
                
    def check_server_for_parg_line(self, ps_line,server_name):
        """check_server_for_parg_line"""
        try:
            JT_Logger.trace_method("[METHOD_IN][check_server_for_parg_line]")
            l_words = self.get_generic_one_word(server_name)                        
            dd_out = self.check_one_word_from_list(ps_line, l_words)    
                
            JT_Logger.trace_hard_level_18("[METHOD_OUT][check_server_for_parg_line]")                                                                     
            JT_Logger.trace_hard_level_18( "[dd_out:" + str(dd_out) + "]")
                            
            return dd_out            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][check_server_for_parg_line]")
            return -1
                
                                                
            
#==================================================================
#
#==================================================================

    def trace_computation_info(self
                               , tt
                               ,dd_server
                               ,dd_kgr_instance
                               ,user_from_ps
                               ,pid_from_ps
                               ,str_ps_line
                               ,show_line):

        try:
            JT_Logger.trace_hard_level_18("[INFO]" )
            JT_Logger.trace_hard_level_18("[ADD_PROCESS]") 
            JT_Logger.trace_hard_level_18( "[dd_server.m_ProcessName:" + dd_server.m_ProcessName + "]") 
            JT_Logger.trace_hard_level_18(" [m_KgrInstanceName:" + dd_kgr_instance.m_KgrInstanceName + "]") 
            JT_Logger.trace_hard_level_18( "[user_from_ps:" + user_from_ps + "]") 
            JT_Logger.trace_hard_level_18( "[pid_from_ps:" + pid_from_ps + "]") 
            JT_Logger.log_ps_line( "[str_ps_line:" + str_ps_line + "]")
        except:
            JT_Logger.print_exception("\nException")

#==================================================================
#
#==================================================================

    def get_kgr_instance_for_pargs(self,p_kgr):
        dd_out = p_kgr
        return dd_out

#==================================================================
#
#==================================================================
    
    def get_kgr_instance_for_ps_line(self,p_kgr):
        dd_out = p_kgr
        return dd_out

#==================================================================
#
#==================================================================
    
    def get_kgr_instance_for_pargse(self,p_kgr):
        dd_out = p_kgr
        return dd_out
    
#==================================================================
#
#==================================================================
    
    def find_kgr_in_pargse_line(self
                                ,p_PsLine
                                ,str_ps_line
                                ,p_ServerDef
                                ,p_KgrInstanceDef
                               ,user_from_ps
                               ,pid_from_ps
                               ,pargseline):
        try:
            JT_Logger.trace_method("[METHOD_IN][find_kgr_in_pargse_line]")
            ll_m = "find_kgr_in_pargse_line"
            out_status = 1
            
            dd_PsLine = JT_PsLine()
            dd_PsLine = p_PsLine
                        
            dd_server = JT_ServerDef()
            dd_server = p_ServerDef
            
            dd_kgr_instance = JT_KgrInstanceDef()
            dd_kgr_instance = p_KgrInstanceDef
            
            if ( dd_server.m_KgrInstanceNameInPargse == 1 ):
                JT_Logger.trace_hard_level_17("[METHOD_ISIDE][" 
                                              + ll_m + "][m_KgrInstanceNameInPargse]")
                
                if pargseline == "":
                    out_status,pargseline = self.get_pargs_line(
                            dd_PsLine.m_user_id
                            ,pid_from_ps
                            ,self.euser
                            ,str_ps_line
                            ,self.m_su_mode
                            ,1)                    
                    
                            
                JT_Logger.trace_method("[METHOD_INSIDE][" + ll_m + "][SU_MODE:" + self.m_su_mode + "]")                  
                len_line = len(pargseline) 
                if( len_line > 0 ):   
                    JT_Logger.trace_hard_level_17("[METHOD_ISIDE]" 
                                              + ll_m + "[LEN_KGR_IN_PARGSE:" 
                                              + str(len_line) + "]")       
                    
                    l_kgr_pa = self.get_kgr_instance_for_pargse(dd_kgr_instance.m_KgrInstanceName)
                    dd_1 = self.check_server_for_parge_line(
                                                            pargseline
                                                            ,l_kgr_pa)
                    if( dd_1 < 0 ) :
                        JT_Logger.trace_method("[METHOD_OUT_FAIL][" + ll_m + "][PATTERN_NOT_FULLFILLED]")
                        out_status = 0        
                    else:
                        JT_Logger.trace_method("[METHOD_OUT_SUCCESS][" + ll_m + "][PATTERN_FULLFILLED")
                        out_status = 1
                                    
                else:
                    JT_Logger.trace_method("[METHOD_OUT_FAIL][" + ll_m + "][LINELEN0]")
                    out_status = 0
                    
            else:
                JT_Logger.trace_hard_level_17("[METHOD_OUT_SUCCESS][" + ll_m + "][NO_KGR_IN_PARGE]")
                out_status = 1
            
            JT_Logger.trace_method("[METHOD_OUT][find_kgr_in_pargse_line]")
            JT_Logger.trace_method("[out_status:" + str(out_status) +"]")    
            return out_status,pargseline
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_kgr_in_pargse_line]")
            return 0,""
        
#==================================================================
#
#==================================================================

    def find_params_in_pargse_line(self
                                        ,p_PsLine
                                        ,str_ps_line
                                        ,p_ServerDef
                                        ,p_KgrInstanceDef
                                        ,user_from_ps
                                        ,pid_from_ps
                                        ,pargseline):            
        try:
            JT_Logger.trace_method("[METHOD_IN][find_params_in_pargse_line]")
            ll_m = "find_params_in_pargse_line"
            out_status = 1
            dd_PsLine = JT_PsLine()
            dd_PsLine = p_PsLine            
            
            dd_server = JT_ServerDef()
            dd_server = p_ServerDef
            #dd_kgr_instance =JT_KgrInstanceDef()
            #dd_kgr_instance = p_KgrInstanceDef
            
            len_words = len(dd_server.m_ParamsPargseLine.m_Params)
            
            if( len_words) > 0 :
                JT_Logger.trace_hard_level_17("[METHOD_ISIDE]" 
                                              + ll_m + "[LEN_PARAMS_IN_PARGSE:" 
                                              + str(len_words) + "]")       
                
                if pargseline == "":
                    out_status,pargseline = self.get_pargs_line(
                            dd_PsLine.m_user_id
                            ,pid_from_ps
                            ,self.euser
                            ,str_ps_line
                            ,self.m_su_mode
                            ,1)                    
                                                                 
                JT_Logger.trace_method("[METHOD_INSIDE][" + ll_m + "][SU_MODE:" + self.m_su_mode + "]")
                if(len(pargseline) > 0 ):   
                    JT_Logger.trace_hard_level_17(" PARGSE_FOR_ID") 
                    JT_Logger.trace_hard_level_17( "[pid_from_ps:" + pid_from_ps + "]" )
                    JT_Logger.log_ps_line( "[pargseline:" + pargseline + "]" )
        
                    dd_1 = self.check_all_args_in_line(pargseline, dd_server.m_ParamsPargseLine)
                    if( dd_1 < 0 ) :
                        JT_Logger.trace_method("[METHOD_OUT_FAIL][" + ll_m + "][PATTERN_NOT_FULLFILLED]")
                        out_status = 0
                    else:
                        JT_Logger.trace_method("[METHOD_OUT_SUCCESS][" + ll_m + "][PATTERN_FULLFILLED")
                        out_status = 1
                else:
                    JT_Logger.trace_method("[METHOD_OUT_SUCCESS][" + ll_m + "][LINELEN0")
                    out_status = 0
                    
            else:
                JT_Logger.trace_hard_level_17("[METHOD_OUT_FAIL][" + ll_m + "][NO_PARAMS_IN_PARG]")
                out_status = 1
            
            JT_Logger.trace_method("[METHOD_OUT][find_params_in_pargse_line]")
            JT_Logger.trace_method("[out_status:" + str(out_status) + "]")    
            return out_status,pargseline
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_params_in_pargse_line]")
            return 0,""

        
#==================================================================
#
#==================================================================


    def get_pargs_line(self                          
                          ,user_from_ps
                          ,pid_from_ps
                          ,executed_user
                          ,str_ps_line
                          ,su_mode
                          ,pargs_e) :
        try:
            JT_Logger.trace_method("[METHOD_IN][get_pargs_line]")
            try:
                JT_Logger.trace_method("[METHOD_IN][get_pargs_line]")
                JT_Logger.trace_method("[user_from_ps:" + user_from_ps + "]")
                JT_Logger.trace_method("[pid_from_ps:" + pid_from_ps + "]")
                JT_Logger.trace_method("[executed_user:" + executed_user + "]")
                JT_Logger.trace_method("[su_mode:" + su_mode + "]")
            except :
                JT_Logger.print_exception("\nException_info_method")
                
            ll_m = "get_pargs_line"      
            out_status = 0
            pargsline = ""
            JT_Logger.trace_method("[METHOD_IN][get_pargs_line]")
            if(user_from_ps != executed_user):
                out_status = 0
                pargsline = ""
                JT_Logger.trace_method("[METHOD_OUT_FAIL][" + ll_m + "][INPROPER_PROCESS_USER]")                        
            else:
                out_status = 1
                if(pargs_e == 0):
                    JT_Logger.trace_method("[METHOD_INSIDE][" + ll_m + "][pargs]")
                    pargsline = self.run_pargs_command(
                        user_from_ps
                        ,pid_from_ps
                        ,self.euser
                        ,str_ps_line
                        ,self.m_su_mode)
                else:
                    JT_Logger.trace_method("[METHOD_INSIDE][" + ll_m + "][pargse]")
                    pargsline = self.run_pargs_e_command(
                        user_from_ps
                        ,pid_from_ps
                        ,self.euser
                        ,str_ps_line
                        ,self.m_su_mode)
                    
            if(len(pargsline)== 0):
                out_status = 0
                        
            JT_Logger.trace_method("[METHOD_OUT][get_pargs_line][" + str(out_status) + "]")
            return out_status,pargsline
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][get_pargs_line]")
            return 0,""

#==================================================================
#
#==================================================================


    def run_pargs_e_command(self                          
                          ,user_from_ps
                          ,pid_from_ps
                          ,executed_user
                          ,str_ps_line
                          ,su_mode) :
        try:      
            JT_Logger.trace_method("[METHOD_IN][run_pargs_e_command]")
            #ll_m = "run_pargs_command"
            pargsline,dd_nsu = JT_Os.get_pargs_e_line(
                user_from_ps
                ,pid_from_ps
                ,executed_user
                ,str_ps_line
                ,su_mode)
            
            if self.m_su_mode != "not_su":
                self.m_su_mode = dd_nsu                
            
            JT_Logger.trace_method("[METHOD_OUT][run_pargs_e_command]")    
            return pargsline        
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][run_pargs_e_command]")
            return ""

#==================================================================
#
#==================================================================

    def run_pargs_command(self                          
                          ,user_from_ps
                          ,pid_from_ps
                          ,executed_user
                          ,str_ps_line
                          ,su_mode) :
        try:      
            JT_Logger.trace_method("[METHOD_IN][run_pargs_command]")
            #ll_m = "run_pargs_command"
            pargsline,dd_nsu = JT_Os.get_pargs_line(
                user_from_ps
                ,pid_from_ps
                ,executed_user
                ,str_ps_line
                ,su_mode)
            
            if self.m_su_mode != "not_su":
                self.m_su_mode = dd_nsu                
            
            JT_Logger.trace_method("[METHOD_OUT][run_pargs_command]")    
            return pargsline        
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][run_pargs_command]")
            return ""
        
#==================================================================
#
#==================================================================

    def find_params_in_pargs_line(self
                                  ,jt_PsLine
                                   ,str_ps_line
                                   ,p_ServerDef
                                   ,p_KgrInstanceDef
                                   ,user_from_ps
                                   ,pid_from_ps
                                   ,pargsline):
        try:      
            JT_Logger.trace_method("[METHOD_IN][find_params_in_pargs_line]")
            ll_m = "find_params_in_pargs_line"
            out_status = 1
            dd_PsLine = JT_PsLine()
            dd_PsLine = jt_PsLine
            dd_server = JT_ServerDef()
            dd_server = p_ServerDef
            #dd_kgr_instance =JT_KgrInstanceDef()
            #dd_kgr_instance = p_KgrInstanceDef
            len_pargs = len(dd_server.m_ParamsPargsLine.m_Params)            
            if( len_pargs) > 0 :
                
                if pargsline ==     "":
                    out_status,pargsline = self.get_pargs_line(
                            dd_PsLine.m_user_id
                            ,pid_from_ps
                            ,self.euser
                            ,str_ps_line
                            ,self.m_su_mode
                            ,0)
                                                                                             
                JT_Logger.trace_method("[METHOD_INSIDE][" + ll_m + "][SU_MODE:" + self.m_su_mode + "]")
                len_line = len(pargsline) 
                if(len_line > 0 ):        
                    JT_Logger.trace_hard_level_17("[METHOD_ISIDE]" + ll_m + "[LEN_PARGSE:" + str(len_line) + "]")       
                    JT_Logger.trace_method_inside(ll_m,"[PARGS_FOR_ID][" + pid_from_ps + "]" )
                    
                    dd_1 = self.check_all_args_in_line(pargsline, dd_server.m_ParamsPargsLine)
                    if( dd_1 < 0 ) :
                        JT_Logger.trace_method("[METHOD_OUT_FAIL][" + ll_m + "][PATTERN_NOT_FULLFILLED]")
                        out_status = 0
                    else:
                        JT_Logger.trace_method("[METHOD_OUT_SUCCESS][" +ll_m + "][PATTERN_FULLFILLED")
                        out_status = 1                        
                else:
                    JT_Logger.trace_hard_level_17("[METHOD_OUT_FAIL][" +ll_m + "][LINELEN0]")
                    out_status = 0
            else:
                JT_Logger.trace_hard_level_17("[METHOD_OUT_SUCCESS][" +ll_m + "][NO_PARAMS_IN_PARGS]")
                out_status = 1
                
            JT_Logger.trace_method("[METHOD_OUT][find_params_in_pargs_line]")
            JT_Logger.trace_method("[out_status:" + str(out_status) +"]")    
            return out_status,pargsline
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_params_in_pargs_line]")
            out_status = 0
            pargsline = ""
            return out_status,pargsline

#==================================================================
#
#==================================================================

    def find_kgr_in_pargs_line(self
                               ,jt_PsLine
                               ,str_ps_line
                               ,dd_server
                               ,dd_kgr_instance
                               ,user_from_ps
                               ,pid_from_ps
                               ,pargsline):
        try:
            JT_Logger.trace_method("[METHOD_IN][find_kgr_in_pargs_line]")
            ll_m="find_kgr_in_pargs_line"
            dd_PsLine = JT_PsLine()
            dd_PsLine = jt_PsLine
            
            out_status = 1
            if ( dd_server.m_KgrInstanceNameInPargs == 1 ):
                
                JT_Logger.trace_hard_level_17("( dd_server.m_KgrInstanceNameInPargs == 1 )")
                
                if pargsline ==     "":
                    out_status,pargsline = self.get_pargs_line(
                            dd_PsLine.m_user_id
                            ,pid_from_ps
                            ,self.euser
                            ,str_ps_line
                            ,self.m_su_mode
                            ,0)
                    
                JT_Logger.trace_method("[METHOD_INSIDE][" + ll_m + "][SU_MODE:" + self.m_su_mode + "]")            
                len_line = len(pargsline)
                if(len_line > 0 ):
                    JT_Logger.trace_hard_level_17("[METHOD_ISIDE]" + ll_m + "[LEN_PARAMS_IN_PS:" + str(len_line) + "]")       
                    l_kgr_pa = self.get_kgr_instance_for_pargs(dd_kgr_instance.m_KgrInstanceName)
                    dd_1 = self.check_server_for_parg_line(pargsline,l_kgr_pa)
                    if( dd_1 < 0 ) :
                        JT_Logger.trace_method("[METHOD_OUT_FAIL[" +ll_m + "][PATTERN_NOT_FULLFILLED]")
                        out_status = 0
                    else:
                        JT_Logger.trace_method("[METHOD_OUT_SUCCESS][" +ll_m + "][PATTERN_FULLFILLED")
                        out_status = 1
                else:
                    JT_Logger.trace_method("[METHOD_OUT_FAIL][" +ll_m + "][LINELEN0]")                    
                    out_status = 0
            else:
                JT_Logger.trace_hard_level_17("[METHOD_OUT_FAIL][" +ll_m + "][NO_KGR_NAME_IN_PARGS]")
                out_status = 1

            JT_Logger.trace_method("[METHOD_OUT][find_kgr_in_pargs_line]")
            JT_Logger.trace_method("[out_status:" + str(out_status) +"]")
            return out_status,pargsline
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_kgr_in_pargs_line]")
            return 0,""
    
#==================================================================
#
#==================================================================

    def find_params_in_ps_line(self
                               ,str_ps_line
                               ,dd_server
                               ,dd_kgr_instance
                               ,user_from_ps
                               ,pid_from_ps):
        try:        
            JT_Logger.trace_method("[METHOD_IN][find_params_in_ps_line]")
            ll_m = "find_params_in_ps_line"
            out_status = 1
            len_params_ps = len(dd_server.m_ParamsPsLine.m_Params)
            if( len_params_ps ) > 0 :
                JT_Logger.trace_hard_level_17("[METHOD_ISIDE]" + ll_m + "[LEN_PARAMS_IN_PS:" + str(len_params_ps) + "]")
                dd_1 = self.check_all_args_in_line(str_ps_line, dd_server.m_ParamsPsLine)
                if( dd_1 < 0 ) :
                    out_status = 0
                    JT_Logger.trace_method("[METHOD_OUT_SUCCESS[" +ll_m + "][PATTERN_NOT_FULLFILLED]")                    
                else:
                    out_status = 1
                    JT_Logger.trace_hard_level_17("[METHOD_OUT_SUCCESS][" +ll_m + "][PATTERN_FULLFILLED]")
            else:
                out_status = 1
                JT_Logger.trace_hard_level_17("[METHOD_OUT_FAIL][" +ll_m + "][NO_PARAMS_FOR_PS]")
                
            JT_Logger.trace_method("[METHOD_IN][find_params_in_ps_line]")
            JT_Logger.trace_method("[out_status:" + str(out_status) +"]")    
            return out_status
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_params_in_ps_line]")
            return 0
    
#==================================================================
#
#==================================================================

    def find_kgr_in_ps_line(self
                               ,str_ps_line
                               ,dd_server
                               ,dd_kgr_instance
                               ,user_from_ps
                               ,pid_from_ps):

        try:
                    
            JT_Logger.trace_method("[METHOD_IN][find_kgr_in_ps_line]")
            ll_m = "find_kgr_in_ps_line"
            out_status = 1
            if ( dd_server.m_KgrInstanceNameInPs == 1 ):
                
                JT_Logger.trace_hard_level_17("[METHOD_ISIDE][KgrInstanceNameInPs]")
                l_kgr_pa = self.get_kgr_instance_for_ps_line(dd_kgr_instance.m_KgrInstanceName)
                dd_1 = self.check_server_for_ps_line(str_ps_line,l_kgr_pa)
                                
                if( dd_1 < 0 ) :
                    out_status = 0
                    JT_Logger.trace_method("[METHOD_OUT_FAIL][" +ll_m + "][PATTERN_NOT_FULLFILLED]")                    
                else:
                    out_status = 1
                    JT_Logger.trace_hard_level_17("[METHOD_OUT_SUCCESS][" +ll_m + "][PATTERN_FULLFILLED]")                    
            else:
                out_status = 1
                JT_Logger.trace_hard_level_17("[METHOD_OUT_SUCCESS][" +ll_m + "][NO_KGR_IN_PS_LINE]")
            
            JT_Logger.trace_method("[METHOD_OUT][find_kgr_in_ps_line]")
            JT_Logger.trace_method("[out_status:" + str(out_status) +"]")
                
            return out_status
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_kgr_in_ps_line]")
            return 0



#==================================================================
#
#==================================================================
            
    
    def print_debug_kgr_instance(self,s_kgr_instance_name):
        try:        
            if(self.m_prind_debug_kgr_and_server == 1):
                JT_Logger.trace_method("[INFO_METHOD_IN]" + "[print_debug_kgr_instance]")                                    
                JT_Logger.print_output("")                                    
                JT_Logger.print_output("")
                JT_Logger.print_output("###################################################################")
                JT_Logger.print_output("#")
                JT_Logger.print_output("#")
                JT_Logger.print_output("#KGR:                              " + s_kgr_instance_name +"")
                JT_Logger.print_output("#")
                JT_Logger.print_output("#")
                JT_Logger.print_output("###################################################################")
                
                JT_Logger.print_output("")
                JT_Logger.print_output("")
                    
                JT_Logger.trace_method("[METHOD_OUT][print_debug_kgr_instance]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_servers_in_env]")

#==================================================================
#
#==================================================================

    def print_debug_server_instance(self,s_kgr_instance_name,s_server_name):
        try:        
            if(self.m_prind_debug_kgr_and_server == 1):

                JT_Logger.trace_method("[INFO_METHOD_IN]" + "[print_debug_kgr_instance]")                                    
                JT_Logger.print_output("")                                    
                JT_Logger.print_output("")
                JT_Logger.print_output("\t###################################################################")
                JT_Logger.print_output("\t#")
                JT_Logger.print_output("\t#KGR:                              " + s_kgr_instance_name + "")
                JT_Logger.print_output("\t#SERVER:                              " + s_server_name + "")
                JT_Logger.print_output("\t#")
                JT_Logger.print_output("\t#")
                JT_Logger.print_output("\t###################################################################")
                
                JT_Logger.print_output("")
                JT_Logger.print_output("")
                    
                JT_Logger.trace_method("[METHOD_OUT][print_debug_kgr_instance]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_servers_in_env]")
    
#==================================================================
#
#==================================================================

    def print_fullfilled_condition_u(self
                                   ,s_kgr_instance_name
                                   ,s_server_name
                                   ,s_condition_name
                                   ,s_res
                                   ,i_line):
        s_res_str = ""
        if(s_res == 0):
            s_res_str = "SERVER_IS_NOT_FOUND"
        else:
            s_res_str = "SERVER_IS_FOUND"        

        JT_Logger.print_output("\t\t####################################################" 
                               +"#######################################################")
        JT_Logger.print_output("\t\t#")
        JT_Logger.print_output("\t\t#KGR:" + s_kgr_instance_name + ""
                               + " SERVER:" + s_server_name + ""        
                               + " OUT:" + s_res_str
                               + " LINE:" + str(i_line))
        JT_Logger.print_output("\t\t#")
        JT_Logger.print_output("\t\t####################################################" 
                               + "####################################################")

#==================================================================
#
#==================================================================
    
    def print_fullfilled_condition_nu(self
                                   ,s_kgr_instance_name
                                   ,s_server_name
                                   ,s_condition_name
                                   ,s_res):
        s_res_str = ""
        if(s_res == 0):
            s_res_str = "SERVER_IS_NOT_FOUND"
        else:
            s_res_str = "SERVER_IS_FOUND"        

        JT_Logger.print_output("\t\t####################################################" 
                               +"#######################################################")
        JT_Logger.print_output("\t\t#")
        JT_Logger.print_output("\t\t#KGR:" + s_kgr_instance_name + ""
                               + " SERVER:" + s_server_name + ""        
                               + " OUT:" + s_res_str)
        JT_Logger.print_output("\t\t#")
        JT_Logger.print_output("\t\t####################################################" 
                               + "####################################################")
        
#==================================================================
#
#==================================================================
        
    def print_fullfilled_condition_v2(self
                                   , s_kgr_instance_name
                                   , s_server_name
                                   , s_condition_name
                                   , s_res
                                   , p_dd_li):
        
        JT_Logger.print_output("\t\t###################################################################")               
        JT_Logger.print_output("\t\t#KGR:                                 " + s_kgr_instance_name + "")
        JT_Logger.print_output("\t\t#SERVER:                                  " + s_server_name + "")         
        JT_Logger.print_output("\t\t#CONDITIONS_FULLFILLED:                       " + s_condition_name + "       " + str(s_res))
        JT_Logger.print_output("\t\t#CONDITION:                                    " + p_dd_li.m_condition  + "")
        JT_Logger.print_output("\t\t#PARAMS:                                           " + p_dd_li.m_params  + "")
        JT_Logger.print_output("\t\t#PS_LINE:                                          " + p_dd_li.m_line_ps  + "")        
        JT_Logger.print_output("\t\t###################################################################")
        
#==================================================================
#
#==================================================================

    def print_fullfilled_condition_one_line(self
                                   , s_kgr_instance_name
                                   , s_server_name
                                   , s_condition_name
                                   , s_res
                                   , p_dd_li):

        s_res_str = ""
        if(s_res == 0):
            s_res_str = "LINE_NOT_OK"
        else:
            s_res_str = "LINE_OK"
            
        JT_Logger.print_output("------------------------------------------"
                               +"----------------------------------------"
                               +"----------------------------------------")
                        
        
        JT_Logger.print_output("-"                               
                        +"[" + str(p_dd_li.m_current_log_line) + "]"
                        "[LINE_EXEC]"                                                    
                        + "[" + s_kgr_instance_name + "]" 
                        + "[" + s_server_name + "]"
                        + "[" + s_res_str + "]"                                 
                        + "[" + p_dd_li.m_condition  + "]"                        
                        + "[" + p_dd_li.m_params  + "]"
                        + "[" + p_dd_li.m_line_ps  + "]")        

        
        JT_Logger.print_output("------------------------------------------"
                               +"----------------------------------------"
                               +"----------------------------------------")
        
        
#==================================================================
#
#==================================================================
    def fill_server_with_all_ps_lines(self,dd_kgr_instance,dd_server):
        try:
            JT_Logger.trace_method("[METHOD_IN][fill_server_with_all_ps_lines]")
            
            JT_Logger.trace_hard_level_20("[m_server_name:" + dd_server.m_server_name + "]")
            
            dd_ki = JT_KgrInstanceDef()
            dd_ki = dd_kgr_instance
            i_fulfilled_cond = 0 
            dd_si = JT_ServerDef()
            dd_si = dd_server
            #1 find_kgr_in_ps_line
            i_fullfilled_line = 0
            for dd_ps_line_ii in self.m_ps_lines.m_ps_lines:
                dd_js_line = JT_PsLine()
                dd_js_line = dd_ps_line_ii        
                str_ps_line = dd_js_line.m_Line
                JT_Logger.log_ps_line_hard("[METHOD_IN][fill_server_with_all_ps_lines]")
                JT_Logger.log_ps_line_hard("[PS_LINE_HARD]" + "[" + str_ps_line + "]")
                dd_li = JT_ExceutionLineInfo()
                i_fulfilled_tmp = self.find_processes_for_server_ex(
                                                    dd_ps_line_ii
                                                  , str_ps_line
                                                  , dd_server
                                                  , dd_kgr_instance
                                                  ,"all"
                                                  , dd_li)
                
                self.print_fullfilled_condition_one_line(
                                                dd_ki.m_KgrInstanceName
                                                , dd_si.m_server_name
                                                , dd_li.m_condition
                                                , i_fulfilled_tmp
                                                , dd_li)
                
                if(i_fulfilled_tmp == 1):
                    i_fullfilled_line = dd_li.m_current_fulfilled_log_line
                    i_fulfilled_cond = 1
                
            self.print_fullfilled_condition_u(
                                            dd_ki.m_KgrInstanceName
                                            , dd_si.m_server_name
                                            , "all"
                                            , i_fulfilled_cond
                                            , i_fullfilled_line)
                
            JT_Logger.trace_method("[METHOD_OUT][fill_server_with_all_ps_lines][" + str(i_fulfilled_cond) + "]")                    
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_server_with_all_ps_lines]")
    
#==================================================================
#
#==================================================================
        
    def fill_server_with_all_ps_lines_condition_first(self,dd_kgr_instance,dd_server):
        try:
            JT_Logger.trace_method("[METHOD_IN][fill_server_with_all_ps_lines_condition_first]")
            
            JT_Logger.trace_hard_level_20("[m_server_name:" + dd_server.m_server_name + "]")
            
            i_fulfilled_cond = 0 
            
            #1 find_kgr_in_ps_line
            for dd_ps_line_ii in self.m_ps_lines.m_ps_lines:
                dd_js_line = JT_PsLine()
                dd_js_line = dd_ps_line_ii        
                str_ps_line = dd_js_line.m_Line
                JT_Logger.log_ps_line_hard("[METHOD_IN][fill_server_with_all_ps_lines]")
                JT_Logger.log_ps_line_hard("[PS_LINE_HARD]" + "[" + str_ps_line + "]")
                dd_li = JT_ExceutionLineInfo()
                i_fulfilled_tmp = self.find_processes_for_server_ex(
                                                    dd_ps_line_ii
                                                  , str_ps_line
                                                  , dd_server
                                                  , dd_kgr_instance
                                                  ,"find_kgr_in_ps_line"
                                                  ,dd_li)
                
                if(i_fulfilled_tmp == 1):
                    i_fulfilled_cond = 1
                
            self.print_fullfilled_condition_nu("","","find_kgr_in_ps_line",i_fulfilled_cond)
            
            #2 find_kgr_in_ps_line
            i_fulfilled_cond = 0 
            for dd_ps_line_ii in self.m_ps_lines.m_ps_lines:
                dd_js_line = JT_PsLine()
                dd_js_line = dd_ps_line_ii        
                str_ps_line = dd_js_line.m_Line
                JT_Logger.log_ps_line_hard("[METHOD_IN][fill_server_with_all_ps_lines]")
                JT_Logger.log_ps_line_hard("[PS_LINE_HARD]" + "[" + str_ps_line + "]")
                dd_li = JT_ExceutionLineInfo()
                i_fulfilled_tmp = self.find_processes_for_server_ex(
                                                    dd_ps_line_ii
                                                  , str_ps_line
                                                  , dd_server
                                                  , dd_kgr_instance
                                                  ,"find_params_in_ps_line"
                                                  ,dd_li)
                if(i_fulfilled_tmp == 1):
                    i_fulfilled_cond = 1
                
            self.print_fullfilled_condition_nu("","","find_params_in_ps_line",i_fulfilled_cond)
                
            #3
            i_fulfilled_cond = 0 
            for dd_ps_line_ii in self.m_ps_lines.m_ps_lines:
                dd_js_line = JT_PsLine()
                dd_js_line = dd_ps_line_ii        
                str_ps_line = dd_js_line.m_Line
                JT_Logger.log_ps_line_hard("[METHOD_IN][fill_server_with_all_ps_lines]")
                JT_Logger.log_ps_line_hard("[PS_LINE_HARD]" + "[" + str_ps_line + "]")
                dd_li = JT_ExceutionLineInfo()
                i_fulfilled_tmp = self.find_processes_for_server_ex(
                                                    dd_ps_line_ii
                                                  , str_ps_line
                                                  , dd_server
                                                  , dd_kgr_instance
                                                  ,"find_kgr_in_pargs_line"
                                                  ,dd_li)
                
                if(i_fulfilled_tmp == 1):
                    i_fulfilled_cond = 1
                
            self.print_fullfilled_condition_nu("","","find_kgr_in_pargs_line",i_fulfilled_cond)

            #4
            i_fulfilled_cond = 0 
            for dd_ps_line_ii in self.m_ps_lines.m_ps_lines:
                dd_js_line = JT_PsLine()
                dd_js_line = dd_ps_line_ii        
                str_ps_line = dd_js_line.m_Line
                JT_Logger.log_ps_line_hard("[METHOD_IN][fill_server_with_all_ps_lines]")
                JT_Logger.log_ps_line_hard("[PS_LINE_HARD]" + "[" + str_ps_line + "]")
                dd_li = JT_ExceutionLineInfo()
                i_fulfilled_tmp = self.find_processes_for_server_ex(
                                                    dd_ps_line_ii
                                                  , str_ps_line
                                                  , dd_server
                                                  , dd_kgr_instance
                                                  ,"find_params_in_pargs_line"
                                                  ,dd_li)
                if(i_fulfilled_tmp == 1):
                    i_fulfilled_cond = 1
                
            self.print_fullfilled_condition_nu("","","find_params_in_pargs_line",i_fulfilled_cond)

            #5
            i_fulfilled_cond = 0 
            for dd_ps_line_ii in self.m_ps_lines.m_ps_lines:
                dd_js_line = JT_PsLine()
                dd_js_line = dd_ps_line_ii        
                str_ps_line = dd_js_line.m_Line
                JT_Logger.log_ps_line_hard("[METHOD_IN][fill_server_with_all_ps_lines]")
                JT_Logger.log_ps_line_hard("[PS_LINE_HARD]" + "[" + str_ps_line + "]")
                dd_li = JT_ExceutionLineInfo()
                i_fulfilled_tmp = self.find_processes_for_server_ex(
                                                    dd_ps_line_ii
                                                  , str_ps_line
                                                  , dd_server
                                                  , dd_kgr_instance
                                                  ,"find_params_in_pargse_line"
                                                  ,dd_li)
                if(i_fulfilled_tmp == 1):
                    i_fulfilled_cond = 1
                
            self.print_fullfilled_condition_nu("","","find_params_in_pargse_line",i_fulfilled_cond)
                
            #6
            i_fulfilled_cond = 0 
            for dd_ps_line_ii in self.m_ps_lines.m_ps_lines:
                dd_js_line = JT_PsLine()
                dd_js_line = dd_ps_line_ii        
                str_ps_line = dd_js_line.m_Line
                JT_Logger.log_ps_line_hard("[METHOD_IN][fill_server_with_all_ps_lines]")
                JT_Logger.log_ps_line_hard("[PS_LINE_HARD]" + "[" + str_ps_line + "]")
                dd_li = JT_ExceutionLineInfo()
                i_fulfilled_tmp = self.find_processes_for_server_ex(
                                                    dd_ps_line_ii
                                                  , str_ps_line
                                                  , dd_server
                                                  , dd_kgr_instance
                                                  ,"find_kgr_in_pargse_line"
                                                  ,dd_li)
                if(i_fulfilled_tmp == 1):
                    i_fulfilled_cond = 1
                
            self.print_fullfilled_condition_nu("","","find_kgr_in_pargse_line",i_fulfilled_cond)
                
            JT_Logger.trace_method("[METHOD_OUT][fill_server_with_all_ps_lines_condition_first]")                    
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][fill_server_with_all_ps_lines_condition_first]")
    
#==================================================================
#
#==================================================================
    #dd_li = JT_ExceutionLineInfo()
    def find_processes_for_server_ex(self
                                     ,p_JT_PsLine
                                     ,str_ps_line
                                     ,p_ServerDef
                                     ,p_KgrInstanceDef
                                     ,p_alg_number
                                     ,p_dd_li):            
        """find_processes_for_server_ex"""        
        try:
            
            
            JT_Logger.trace_method("[INFO_METHOD_IN]" + "[find_processes_for_server]")
            self.m_current_log_line = self.m_current_log_line + 1
            p_dd_li.m_current_log_line = self.m_current_log_line
            dd_kgr_instance = JT_KgrInstanceDef()
            dd_kgr_instance = p_KgrInstanceDef
            dd_server = JT_ServerDef()
            dd_server = p_ServerDef
            JT_Logger.trace_method( "[m_ProcessName:"  + dd_server.m_ProcessName + "]") 
            JT_Logger.trace_method("[m_KgrInstanceName:" + dd_kgr_instance.m_KgrInstanceName + "]") 
            JT_Logger.log_ps_line( str_ps_line )
            jt_PsLine = JT_PsLine()
            jt_PsLine = p_JT_PsLine
            user_from_ps = jt_PsLine.m_user_id
            pid_from_ps = jt_PsLine.m_pid_id
            p_dd_li.m_line_ps = jt_PsLine.m_Line
            
            if( pid_from_ps == "") :
                JT_Logger.trace_hard_level_17("NO_PID_IN_PS_THIS_IS_NOT_PROCESS")
                return 0
    
            #count_in = len(dd_kgr_instance.m_procs_for_kgrinstance.m_processess)        
            
            if self.line_is_excluded(str_ps_line) == 1:
                p_dd_li.m_condition = "line_is_exluded"
                JT_Logger.trace_hard_level_18( "[FOUND_PROCESS_IN_LINE_LINE_AND_EXCLUDED]") 
                JT_Logger.trace_hard_level_18( "[m_ProcessName:"+ dd_server.m_ProcessName + "]")
                return 0
    
            #1    
            if(p_alg_number == "find_kgr_in_ps_line" or p_alg_number == "all"):
                continue_code = self.find_kgr_in_ps_line(
                                           str_ps_line                                       
                                           ,dd_server
                                           ,dd_kgr_instance
                                           ,user_from_ps
                                           ,pid_from_ps)
                
                if continue_code == 0:
                    p_dd_li.m_condition = "find_kgr_in_ps_line"
                    p_dd_li.m_params = dd_kgr_instance.m_KgrInstanceName
                    JT_Logger.trace_method("[INFO_METHOD_OUT][NOT_FULLFILLED]" 
                                           + "[find_processes_for_server]"
                                           + "[find_kgr_in_ps_line]")
                    return 0 

            #2
            if(p_alg_number == "find_params_in_ps_line" or p_alg_number == "all"):
                continue_code = self.find_params_in_ps_line(
                                           str_ps_line                                       
                                           ,dd_server
                                           ,dd_kgr_instance
                                           ,user_from_ps
                                           ,pid_from_ps)
                
                if continue_code == 0:
                    p_dd_li.m_condition = "find_params_in_ps_line"
                    p_dd_li.m_params = dd_server.get_params_ps_line_info()
                    JT_Logger.trace_method("[INFO_METHOD_OUT][NOT_FULLFILLED]" 
                                           + "[find_processes_for_server]"
                                           + "[find_params_in_ps_line]")
                    return 0 
                
                
                self.trace_computation_info("[INFO]" + "[ADD_PROCESS_HAD_PROCESS"
                    ,dd_server,dd_kgr_instance,user_from_ps ,pid_from_ps,str_ps_line,1)
            
            #3    
            pargsline = "" 
            if(p_alg_number == "find_kgr_in_pargs_line" or p_alg_number == "all"):                                             
                continue_code,pargsline = self.find_kgr_in_pargs_line(
                                                                      jt_PsLine
                                                                       ,str_ps_line                                       
                                                                       ,dd_server
                                                                       ,dd_kgr_instance
                                                                       ,user_from_ps
                                                                       ,pid_from_ps
                                                                       ,pargsline)
                
                if continue_code == 0:
                    p_dd_li.m_condition = "find_kgr_in_pargs_line"
                    p_dd_li.m_params = dd_kgr_instance.m_KgrInstanceName
                    JT_Logger.trace_method("[INFO_METHOD_OUT][NOT_FULLFILLED]" 
                                           + "[find_processes_for_server]"
                                           + "[find_kgr_in_pargs_line]")
                    return 0 
            #4   
            if(p_alg_number == "find_params_in_pargs_line" or p_alg_number == "all"):
                
                continue_code,pargsline = self.find_params_in_pargs_line(
                                                                        jt_PsLine
                                                                        ,str_ps_line                                       
                                                                        ,dd_server
                                                                        ,dd_kgr_instance
                                                                        ,user_from_ps
                                                                        ,pid_from_ps
                                                                        ,pargsline)
                
                if continue_code == 0:
                    p_dd_li.m_condition = "find_params_in_pargs_line"
                    p_dd_li.m_params = dd_server.get_params_pargs_line_info()
                    JT_Logger.trace_method("[INFO_METHOD_OUT][NOT_FULLFILLED]" 
                                           + "[find_processes_for_server]" 
                                           + "[find_params_in_pargs_line]")
                    return 0 

            #5
            pargseline = ""
            if(p_alg_number == "find_params_in_pargse_line" or p_alg_number == "all"):            
                continue_code,pargseline = self.find_params_in_pargse_line(  
                                                                            jt_PsLine
                                                                            ,str_ps_line                                       
                                                                           ,dd_server
                                                                           ,dd_kgr_instance
                                                                           ,user_from_ps
                                                                           ,pid_from_ps
                                                                           ,pargseline)
                if continue_code == 0:
                    p_dd_li.m_condition = "find_params_in_pargse_line"
                    p_dd_li.m_params = dd_server.get_params_pargse_line_info()
                    JT_Logger.trace_method("[INFO_METHOD_OUT][NOT_FULLFILLED]" 
                                           + "[find_processes_for_server]" 
                                           + "[find_params_in_pargse_line]")
                    return 0 
            
            #6
            #pargseline = ""
            if(p_alg_number == "find_kgr_in_pargse_line" or p_alg_number == "all"):                        
                continue_code,pargseline = self.find_kgr_in_pargse_line(
                                                                        jt_PsLine
                                                                        ,str_ps_line                                       
                                                                       ,dd_server
                                                                       ,dd_kgr_instance
                                                                       ,user_from_ps
                                                                       ,pid_from_ps
                                                                       ,pargseline) 
    
                if continue_code == 0:
                    p_dd_li.m_condition = "find_kgr_in_pargse_line"
                    p_dd_li.m_params = dd_kgr_instance.m_KgrInstanceName
                    JT_Logger.trace_method("[INFO_METHOD_OUT][NOT_FULLFILLED]" 
                                           + "[find_processes_for_server]" 
                                           + "[find_kgr_in_pargse_line]")
                    return 0 
                                
            p_dd_li.m_current_fulfilled_log_line = self.m_current_log_line
                                         
            dd_pta = self.get_process_to_add(
                 str_ps_line
                , pid_from_ps
                , user_from_ps
                , dd_kgr_instance
                , dd_server)                        
            
            dd_pta.m_process_log_line_fullfilled = p_dd_li.m_current_fulfilled_log_line
            dd_kgr_instance.m_procs_for_kgrinstance.add_process_to_processes(dd_pta)                        
            self.m_founded_processes.add_process_to_processes( dd_pta )
            
            JT_Logger.trace_method("[METHOD_OUT][find_processes_for_server_ex][1]")                                                                    
            return 1
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][find_processes_for_server_ex]")
            return 0
            
#==================================================================
#
#==================================================================


    def get_process_to_add(self
                           ,line
                           ,pid_from_ps
                           ,user_from_ps
                           ,dd_kgr_instance
                           ,dd_server):
        JT_Logger.trace_method("[METHOD_IN]" + "[get_process_to_add")
        JT_Logger.trace_hard_level_18("[INFO_METHOD_IN]" + "[get_process_to_add")
        dd_pd = JT_ProcessDef()
        dd_pd.m_pid = pid_from_ps
        dd_pd.m_kgr_instance = dd_kgr_instance.m_KgrInstanceName
        dd_pd.m_server_name = dd_server.m_server_name                        
        dd_pd.m_User = user_from_ps
        dd_pd.m_Counters = 1
        dd_pd.m_LineOfProcess = line
        dd_pd.m_server = dd_server
        JT_Logger.trace_method("[METHOD_OUT]" + "[get_process_to_add")
        return dd_pd
        
#==================================================================
#
#==================================================================
        
    def process_command_args_inner(self):
        try:
            
            JT_Logger.print_output("[METHOD_IN].[process_command_args_inner]")
            try:
                ii=0
                for ll_ss in sys.argv :
                    JT_Logger.print_output( "[PAR][" + str (ii) + "][" + ll_ss + "]")
                    ii = ii+1
            except:
                JT_Logger.print_exception("\nException_in_par")
            
            try:
                p_1 = sys.argv[1]
            except:
                JT_Logger.print_exception("\nException")
                p_1 = "env_pol_gdy"             
            try:
                p_2 = sys.argv[2]
            except:
                JT_Logger.print_exception("\nException")
                p_2 = "srv_all"
                             
            try:
                p_3 = sys.argv[3]
            except:
                JT_Logger.print_exception("\nException")
                p_3 = "not_print_ps_line"
                             
            try:    
                p_4 = sys.argv[4]
            except:
                JT_Logger.print_exception("\nException")
                p_4 = "use_find"             

            try:
                p_5 = sys.argv[5]
            except:
                JT_Logger.print_exception("\nException")
                p_5 = "not_use_su"
                             
            try:
                p_6 = sys.argv[6]
            except:
                JT_Logger.print_exception("\nException")
                p_6 = "not_print_debug"
                             
            try:
                p_7 = sys.argv[7]
            except:
                JT_Logger.print_exception("\nException")
                p_7 = "not_use_log"             
            try:
                p_8 = sys.argv[8]
            except:
                JT_Logger.print_exception("\nException")
                p_8 = "no_ps_filter"
                             
                
            JT_Logger.print_output( "[p_1:commarg_environment_1:" + p_1 + "]" )
            JT_Logger.print_output( "[p_2:commarg_servers_2:" + p_2 + "]" )
            JT_Logger.print_output( "[p_3:commarg_show_ps_line_3:" + p_3 + "]" )
            JT_Logger.print_output( "[p_4:commarg_use_regex_4:" + p_4 + "]" )
            JT_Logger.print_output( "[p_5:commarg_use_su_5:" + p_5 + "]" )
            JT_Logger.print_output( "[p_6:commarg_print_all_6:" + p_6 + "]" )
            JT_Logger.print_output( "[p_7:commarg_use_log_7:" + p_7 + "]" )
            JT_Logger.print_output( "[p_8:commarg_ps_filter_8:" + p_8 + "]" )
            if(p_1 =="h"):
                self.print_parameters()
                exit    
                
            self.commarg_environment_1 = p_1
            
            if(p_1 =="env_france_ptx"):
                self.commarg_environment_1 = "env_france_ptx"
                
            if(p_1 == "env_pol_gdy"):
                self.commarg_environment_1 = "env_pol_gdy"
                
            if(p_1 == "def_1"):
                self.commarg_environment_1 = "env_pol_gdy"
                
            if(p_1 == "env_test"):
                self.commarg_environment_1 = "env_test"
                
            if(p_1 == "kgrSet"):
                self.commarg_environment_1 = "kgrSet"
    
            if(p_1 == "kgr35s"):
                self.commarg_environment_1 = "kgr35s"
                
            if(p_1 == "kgr35b"):
                self.commarg_environment_1 = "kgr35b"
                
            if(p_1 == "kgr32c"):
                self.commarg_environment_1 = "kgr32c"
                
            if(p_1 == "kgr32a"):
                self.commarg_environment_1 = "kgr32a"

            if(p_1 == "kgr32b"):
                self.commarg_environment_1 = "kgr32b"
                
            if(p_1 == "fatih"):
                self.commarg_environment_1 = "fatih"
    
            self.commarg_servers_2 = p_2

            if(p_2 =="def_2"):
                self.commarg_servers_2 = "srv_all"
            
            if(p_2 =="srv_all"):
                self.commarg_servers_2 = "srv_all"                
                
            if(p_2 =="guiadapter"):
                self.commarg_servers_2 = "guiadapter"
                
            if(p_2 =="srv_test"):
                self.commarg_servers_2 = "srv_test"
                            
            if(p_2 =="srv_jboss"):
                self.commarg_servers_2 = "srv_jboss"            
            
            self.commarg_show_ps_line_3 = "print_ps_line"
            
            if(p_3 == "print_ps_line"):            
                self.commarg_show_ps_line_3 = "print_ps_line"

            if(p_3 == "def_3"):            
                self.commarg_show_ps_line_3 = "no_print_ps_line"
                
            if(p_3 == "not_print_ps_line"):            
                self.commarg_show_ps_line_3 = "not_print_ps_line"
                
            self.commarg_use_regex_4 = "use_find"
            
            if(p_4 == "def_4"):            
                self.commarg_use_regex_4 = "use_find"

            if(p_4 == "use_find"):            
                self.commarg_use_regex_4 = "use_find"
                
            if(p_4 == "use_regex"):            
                self.commarg_use_regex_4 = "use_regex"
    
            self.commarg_use_su_5 = "not_use_su"
            
            if(p_5 == "def_5"):            
                self.commarg_use_su_5 = "not_use_su"
            
            if(p_5 == "not_use_su"):                        
                self.commarg_use_su_5 = "not_use_su"
                
            if(p_5 == "use_su"):            
                self.commarg_use_su_5 = "use_su"
                
            self.commarg_print_all_6= "not_print_debug"
            
            if(p_6 == "print_debug"):                        
                self.commarg_print_all_6= "print_debug"
            else:
                self.commarg_print_all_6= "not_print_debug"

            if(p_6 == "def_6"):                        
                self.commarg_print_all_6= "not_print_debug"
                
            if(p_7 == "use_log"):                        
                self.commarg_use_log_7= "use_log"
            else:
                self.commarg_use_log_7= "not_use_log"
                                
            self.commarg_ps_filter_8 = p_8            
            if(p_8 == "no_ps_filter"):                        
                self.commarg_ps_filter_8 = "no_ps_filter"
            
            self.print_parameters()
            
            JT_Logger.trace_method("[METHOD_OUT][process_command_args_inner]")
        except :
            self.set_standard_parameters()
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][process_command_args_inner]")
            return 0
                              
    
#==================================================================
#
#==================================================================

    def set_standard_parameters(self):
        try:
            JT_Logger.trace_method("[METHOD_IN][set_standard_parameters]")
            self.commarg_environment_1 = "env_france_ptx"
            self.commarg_servers_2 = "srv_all"
            self.commarg_show_ps_line_3 = "print_ps_line"
            self.commarg_use_regex_4 = "use_find"
            self.commarg_use_su_5 = "not_use_su"
            self.commarg_print_all_6 = "not_print_debug"
            self.commarg_use_log_7 = "not_use_log"
            self.commarg_ps_filter_8 = "no_ps_filter"
            self.print_parameters()
            JT_Logger.trace_method("[METHOD_OUT][set_standard_parameters]")
        except:
            JT_Logger.print_exception("\nException")
        
#==================================================================
#
#==================================================================
    
    def print_parameters(self):
        try:
            JT_Logger.print_output( "[METHOD_IN][print_parameters]" )        
            JT_Logger.print_output( " python mon_ok.py " )
            JT_Logger.print_output( " [1][env_france_ptx,env_pol_gdy,env_pol_gdy_36,kgr35s,kgr35b,kgr32c,kgr32a,kgr32b,fatih,kgrSet,env_test] " )
            JT_Logger.print_output( " [2][srv_all,srv_test,guiadapter,srv_jboss] " )
            JT_Logger.print_output( " [3][print_ps_line,not_print_ps_line] " )
            JT_Logger.print_output( " [4][use_find,use_regex] " )
            JT_Logger.print_output( " [5][not_use_su,use_su]")
            JT_Logger.print_output( " [6][not_print_debug,print_debug]")
            JT_Logger.print_output( " [7][not_use_log,use_log]")
            JT_Logger.print_output( " [8][no_ps_filter][jboss][fds]")
            JT_Logger.print_output( "[commarg_environment_1:" + self.commarg_environment_1 + "]" )
            JT_Logger.print_output( "[commarg_servers_2:" + self.commarg_servers_2 + "]")
            JT_Logger.print_output( "[commarg_show_ps_line_3:" + self.commarg_show_ps_line_3 + "]")
            JT_Logger.print_output( "[commarg_use_regex_4:" + self.commarg_use_regex_4 + "]")
            JT_Logger.print_output( "[commarg_use_su_5:" + self.commarg_use_su_5 + "]" )
            JT_Logger.print_output( "[commarg_print_all_6:" + self.commarg_print_all_6 + "]" )
            JT_Logger.print_output( "[commarg_use_log_7:" + self.commarg_use_log_7 + "]" )
            JT_Logger.print_output( "[commarg_ps_filter_8:" + self.commarg_ps_filter_8 + "]" )
            JT_Logger.print_output( "[METHOD_OUT][print_parameters]" )
        except:
            JT_Logger.print_exception("\nException")
        
#==================================================================
#
#==================================================================

    def line_is_excluded(self, line):

        #if (line.find(" tail -f ") != -1 or line.find(" tee ") != -1 or line.find("/java/") != -1 ):
        if (line.find(" tail -f ") != -1 ):
            return 1
        
        if (line.find(" tee ") != -1 ):
            return 1
        
        if (line.find(" root ") != -1 ):
            return 1
        
        return 0
        
#==================================================================
#
#==================================================================
    
    def process_command_args(self):    
        
        try:
            JT_Logger.trace_method("[METHOD_IN][process_command_args]")
            self.process_command_args_inner()
            JT_Logger.trace_method("[METHOD_OUT][process_command_args]")
        except:
            self.set_standard_parameters()
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][process_command_args]")
            return 0
            

#==================================================================
#
#==================================================================
        
    def print_servers_to_output(self):                
        try:
            self.print_servers_to_output_with_lines()
            self.print_servers_to_output_without_lines()
        except:
            JT_Logger.print_exception("\nException")

#==================================================================
#
#==================================================================

    def print_servers_to_output_with_lines(self):                
        try:
            JT_Logger.trace_method("[INFO_METHOD_IN][print_servers_to_log]") 
            JT_Logger.print_output("************************************************************************")
            JT_Logger.print_output("*")
            JT_Logger.print_output("*")        
            JT_Logger.print_output("*                               PRINT_WITH_LINES")
            JT_Logger.print_output("*")
            JT_Logger.print_output("*")
            JT_Logger.print_output("************************************************************************")        
            
            JT_Printer().set_exec_to_print_line()
            self.print_servers_in_env()        
            JT_Logger.trace_method("[INFO_METHOD_OUT][print_servers_to_log]")
        except:
            JT_Logger.print_exception("\nException")
#==================================================================
#
#==================================================================

    def print_servers_to_output_without_lines(self):                
        try:
            JT_Logger.trace_method("[INFO_METHOD_IN][print_servers_to_log]") 
            JT_Logger.print_output("************************************************************************")
            JT_Logger.print_output("*")
            JT_Logger.print_output("*")
            JT_Logger.print_output("*                               PRINT_WITHOUT_LINES")
            JT_Logger.print_output("*")
            JT_Logger.print_output("*")
            JT_Logger.print_output("************************************************************************")        
            JT_Printer().uset_exec_to_print_line()
            self.print_servers_in_env()
            JT_Logger.trace_method("[INFO_METHOD_OUT][print_servers_to_log]")
        except:
            JT_Logger.print_exception("\nException")
        
#==================================================================
#
#==================================================================

    def print_servers_to_log(self):
        try:
            JT_Logger.trace_method("[INFO_METHOD_IN][print_servers_to_log]")        
            JT_Printer().set_exec_to_print_line()
            self.print_servers_in_env_to_log()
            JT_Printer().uset_exec_to_print_line()
            self.print_servers_in_env_to_log()
            JT_Logger.trace_method("[INFO_METHOD_OUT][print_servers_to_log]")  
        except:
            JT_Logger.print_exception("\nException")

#==================================================================
#
#==================================================================

    def get_list_of_kgr(self):
        ll_out = []
        ll_out.append("srv_all")
        ll_out.append("kgr35")
        ll_out.append("kgr35b")
        ll_out.append("kgr32")
        ll_out.append("kgr32b")
        ll_out.append("kgr32c")
        ll_out.append("thor")
        ll_out.append("pegase")
        ll_out.append("fatih")
        ll_out.append("kgr36JT")
        return ll_out
    
#==================================================================
#
#==================================================================
    
    def check_arguments(self):
        JT_Logger.print_output( "")                
        JT_Logger.print_output( "========== CHECKING ARGUMENTS===========")
        JT_FIND_ARGV.print_argv_pos(1,["env_pol_gdy","env_france_ptx"])
        JT_FIND_ARGV.print_argv_pos(2,self.get_list_of_kgr())        
        JT_FIND_ARGV.print_argv_pos(3,["not_print_ps_line","print_ps_line"])
        JT_FIND_ARGV.print_argv_pos(4,["use_find","use_regex"])
        JT_FIND_ARGV.print_argv_pos(5,["not_use_su","use_su"])
        JT_FIND_ARGV.print_argv_pos(6,["not_print_debug","print_debug"])
        JT_FIND_ARGV.print_argv_pos(7,["not_use_log","use_log"])
        JT_FIND_ARGV.print_argv_pos(8,["rksup32","rksup35","rksup36"])
        
        JT_Logger.print_output( "")
        JT_Logger.print_output( "")        
        JT_Logger.print_output( "")
        JT_FIND_ARGV.check_argv_pos(1,["env_pol_gdy","env_france_ptx"])
        JT_FIND_ARGV.check_argv_pos(2,self.get_list_of_kgr())
        
        JT_FIND_ARGV.check_argv_pos(3,["not_print_ps_line","print_ps_line"])
        JT_FIND_ARGV.check_argv_pos(4,["use_find","use_regex"])
        JT_FIND_ARGV.check_argv_pos(5,["not_use_su","use_su"])
        JT_FIND_ARGV.check_argv_pos(6,["not_print_debug","print_debug"])
        JT_FIND_ARGV.check_argv_pos(7,["not_use_log","use_log"])
        JT_FIND_ARGV.check_argv_pos(8,["rksup32","rksup35","rksup36"])

#==================================================================
#
#==================================================================
    def exec_main_monitor_kgr_do_work(self):
        
        try:
            JT_Logger.trace_method("[METHOD_IN][exec_main_monitor_kgr_do_work]")
            
            JT_ManagerConfig().init_manager_config()
            
                    
            JT_Strings_find_options().init_reg_ex_option()        

            self.exec_mv_logging()
            
            self.create_env_from_args()            
            
            self.fill_environments_data()
            
            self.print_state_servers()
            
            self.fill_all_ps_lines()
                    
            self.fill_ps_lines_with_data()
            
            self.fill_servers_in_env()
            
            self.find_refereced_processs()
            
            self.print_state()
            
            self.print_state_ps_lines()
            
            self.print_servers_to_output_with_lines()
            
            self.print_state_kgrs()
            
            self.print_state_servers()            
            
            self.print_servers_to_output_without_lines()
                                    
            
            self.print_servers_to_log()
            #self.print_state_servers()
            self.print_end()
            
            JT_Logger.trace_method("[METHOD_OUT][exec_main_monitor_kgr_do_work]")
            return 1
        except:
            self.set_standard_parameters()
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][exec_main_monitor_kgr_do_work]")
            return 0
        
#==================================================================
#
#==================================================================

    def exec_mv_logging(self):
        
        try:
            JT_Os.setup_mv_logging()
        except:
            JT_Logger.print_exception("\nError: exception in main \n")
            print "exec_main_monitor_kgr"
#==================================================================
#
#==================================================================

    def exec_main_monitor_kgr(self):
                
        try:
            JT_Logger.trace_method("[METHOD_IN][exec_main_monitor_kgr]")
            self.exec_mv_logging()
            self.check_arguments()
            
            self.process_command_args()

            self.exec_main_monitor_kgr_do_work();
                        
            JT_Logger.trace_method("[METHOD_OUT][exec_main_monitor_kgr]")
            return 1
        except:
            self.set_standard_parameters()
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][exec_main_monitor_kgr]")
            return 0
        

        
#==================================================================
#
#==================================================================
    def set_parameters_pol(self):
                
        try:
            self.commarg_environment_1 = "env_pol_gdy"
            self.commarg_servers_2 = "srv_all"                                
            self.commarg_show_ps_line_3 = "print_ps_line"                                        
                            
            self.commarg_use_regex_4 = "use_find"
            
            self.commarg_use_su_5 = "not_use_su"
            self.commarg_print_all_6= "not_print_debug"
            
            self.commarg_use_log_7= "not_use_log"
            self.commarg_ps_filter_8 = "no_ps_filter"            
            self.print_parameters()
            return 1
        except:
            self.set_standard_parameters()
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][exec_main_monitor_kgr_with_no_sysargs]")
            return 0
#==================================================================
#
#==================================================================
        
    def exec_main_monitor_kgr_with_no_sysargs_pol(self):            
        try:
            JT_Logger.trace_method("[METHOD_IN][exec_main_monitor_kgr_with_no_sysargs_pol]")
                        
            self.set_parameters_pol()
            
            self.exec_main_monitor_kgr_do_work();            
                        
            JT_Logger.trace_method("[METHOD_OUT][exec_main_monitor_kgr_with_no_sysargs_pol]")
            return 1
        
        except:
            self.set_standard_parameters()
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][exec_main_monitor_kgr_with_no_sysargs_pol]")
            return 0
        
#==================================================================
#
#==================================================================
        
    def exec_main_safe(self):
        try:    
            
            JT_StaticLogger.setup_logging_main()
            dd = JT_MonitorKgr()
            dd.exec_main_monitor_kgr()
            JT_StaticLogger.close_logging()
                            
        except:        
            JT_StaticLogger.close_logging()
            JT_Logger.print_exception("\nError: exception_exec_main_safe \n")
                
#==================================================================
#
#==================================================================

if __name__ == '__main__':
    try:    
        dd = JT_MonitorKgr()
        dd.exec_main_safe()        
    except:                    
        JT_Logger.print_exception("\nError: exception in main \n")
    
    
