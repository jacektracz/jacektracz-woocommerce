import sys
from JT_Logger import JT_Logger
from JT_MonitorKgr import JT_MonitorKgr
from JT_LoggerSettings import JT_LoggerSettings
class JT_MonitorKgrPol:
    
#==================================================================
#
#==================================================================
    def exec_main_monitor_kgr_with_no_sysargs_params_def(self):
        """exec_main_monitor_kgr_with_no_sysargs_params_def"""
        #self.commarg_environment_1 = "env_france_ptx"                    
        #self.commarg_environment_1 = "env_test"
        #self.commarg_environment_1 = "kgrSet"
        #self.commarg_environment_1 = "kgr35s"
        #self.commarg_environment_1 = "kgr35b"
        #self.commarg_environment_1 = "kgr32c"
        #self.commarg_environment_1 = "kgr32a"
        #self.commarg_environment_1 = "kgr32b"
        #self.commarg_environment_1 = "fatih"
        #self.commarg_servers_2 = "srv_all"                                
        #self.commarg_servers_2 = "guiadapter"                
        #self.commarg_servers_2 = "srv_test"                            
        #self.commarg_servers_2 = "srv_jboss"
        #self.commarg_use_regex_4 = "use_regex"

#==================================================================
#
#==================================================================
    
    def exec_pol_all(self):
        dd = JT_MonitorKgr()
        dd.commarg_environment_1 = "env_pol_gdy"
        dd.commarg_servers_2 = "srv_all"                                
        dd.commarg_show_ps_line_3 = "print_ps_line"                                                                
        dd.commarg_use_regex_4 = "use_find"        
        dd.commarg_use_su_5 = "not_use_su"
        dd.commarg_print_all_6= "not_print_debug"        
        dd.commarg_use_log_7= "not_use_log"
        dd.commarg_ps_filter_8 = "no_ps_filter"            
        dd.print_parameters()        
        dd.exec_main_monitor_kgr_do_work()
        
#==================================================================
#
#==================================================================

    def exec_pol_rksup_kgr36c_jboss(self):
        dd = JT_MonitorKgr()
        dd.commarg_environment_1 = "kgr36c"
        dd.commarg_servers_2 = "srv_jboss"                                
        dd.commarg_show_ps_line_3 = "print_ps_line"                                                                
        dd.commarg_use_regex_4 = "use_find"        
        dd.commarg_use_su_5 = "not_use_su"
        dd.commarg_print_all_6 = "print_debug"        
        dd.commarg_use_log_7 = "not_use_log"
        #dd.commarg_ps_filter_8 = "rksup36"
        dd.commarg_ps_filter_8 = "rksup36"            
        dd.print_parameters()        
        dd.exec_main_monitor_kgr_do_work()
        
#==================================================================
#
#==================================================================
                
    def exec_pol_rksup36(self):
        dd = JT_MonitorKgr()
        dd.commarg_environment_1 = "env_pol_gdy_36"
        dd.commarg_servers_2 = "srv_all"                                
        dd.commarg_show_ps_line_3 = "print_ps_line"                                                                
        dd.commarg_use_regex_4 = "use_find"        
        dd.commarg_use_su_5 = "not_use_su"
        #dd.commarg_print_all_6= "not_print_debug"
        dd.commarg_print_all_6= "not_print_debug"        
        dd.commarg_use_log_7= "not_use_log"
        dd.commarg_ps_filter_8 = "rksup36"
        #JT_LoggerSettings().set_to_output()            
        dd.print_parameters()        
        dd.exec_main_monitor_kgr_do_work()
        
    def exec_pol_rksup36d(self):
        dd = JT_MonitorKgr()
        dd.commarg_environment_1 = "env_pol_gdy_36"
        dd.commarg_servers_2 = "srv_all"                                
        dd.commarg_show_ps_line_3 = "print_ps_line"                                                                
        dd.commarg_use_regex_4 = "use_find"        
        dd.commarg_use_su_5 = "not_use_su"
        #dd.commarg_print_all_6= "not_print_debug"
        dd.commarg_print_all_6= "print_debug"        
        dd.commarg_use_log_7= "not_use_log"
        dd.commarg_ps_filter_8 = "rksup36"
        #JT_LoggerSettings().set_to_output()            
        dd.print_parameters()        
        dd.exec_main_monitor_kgr_do_work()
        
#==================================================================
#
#==================================================================
                
    def exec_pol_rksup35(self):
        dd = JT_MonitorKgr()
        dd.commarg_environment_1 = "env_pol_gdy"
        dd.commarg_servers_2 = "srv_all"                                
        dd.commarg_show_ps_line_3 = "print_ps_line"                                                                
        dd.commarg_use_regex_4 = "use_find"        
        dd.commarg_use_su_5 = "not_use_su"
        dd.commarg_print_all_6= "not_print_debug"        
        dd.commarg_use_log_7= "not_use_log"
        dd.commarg_ps_filter_8 = "rksup35"            
        dd.print_parameters()        
        dd.exec_main_monitor_kgr_do_work()
        
    def exec_pol_rksup35d(self):
        dd = JT_MonitorKgr()
        dd.commarg_environment_1 = "env_pol_gdy"
        dd.commarg_servers_2 = "srv_all"                                
        dd.commarg_show_ps_line_3 = "print_ps_line"                                                                
        dd.commarg_use_regex_4 = "use_find"        
        dd.commarg_use_su_5 = "not_use_su"
        dd.commarg_print_all_6= "print_debug"        
        dd.commarg_use_log_7= "not_use_log"
        dd.commarg_ps_filter_8 = "rksup35"            
        dd.print_parameters()        
        dd.exec_main_monitor_kgr_do_work()
                
#==================================================================
#
#==================================================================
        
if __name__ == '__main__':
    try:    
        
        dd = JT_MonitorKgrPol()
        if(len(sys.argv) == 1):        
            dd.exec_pol_rksup36()
        else:            
            if(sys.argv[1] == "36"):
                dd.exec_pol_rksup36()
            if(sys.argv[1] == "35"):
                dd.exec_pol_rksup35()
            if(sys.argv[1] == "36d"):
                dd.exec_pol_rksup36d()
            if(sys.argv[1] == "35d"):
                dd.exec_pol_rksup35d()
            

        #dd.exec_pol_rksup_kgr36c_jboss()
    except:                    
        JT_Logger.print_exception("\nError: exception in main \n")

#==================================================================
#
#==================================================================
