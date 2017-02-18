#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================
from JT_Logger import JT_Logger

from JT_Environment import JT_Environment

#==================================================================
#
#Class JT_Environment
#
#==================================================================


class JT_Environments:
    def __init__(self):
        self.m_environment = []
#==================================================================
#
#==================================================================
        
    def define_envs(self):
        self.add_env_kgrJut()
        self.add_env_kgrSet()

#==================================================================
#
#==================================================================
    def add_envs(self):
        
        dd = JT_Environment()
        dd.define_environment_kgrJut()
        self.m_environment.append(dd)
        
        dd = JT_Environment()
        dd.define_environment_kgrSet()
        self.m_environment.append(dd)
        
        dd = JT_Environment()
        dd.define_environment_kgr35b()
        self.m_environment.append(dd)
        
        dd = JT_Environment()
        dd.define_environment_kgr35s()
        self.m_environment.append(dd)
        
#==================================================================
#
#==================================================================
        
    def print_all_env(self):
        
        try:
            JT_Logger.trace_method("[METHOD_IN][print_all_env]")
            for dd_env in self.m_environment:
                JT_Logger.print_output("ENVIRONMENT")
                for dd_srv in dd_env.m_services:
                    try:
                        JT_Logger.print_output(dd_srv.m_value + " " + dd_srv.m_key)
                    except:
                        JT_Logger.print_exception("\nexception\n")
                        
            JT_Logger.trace_method("[METHOD_OUT][print_all_env]")
            
        except:
            JT_Logger.print_exception("\nexception\n")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_all_env]")
#==================================================================
#
#==================================================================
        
    def add_env_kgrJut(self):
        dd = JT_Environment()
        dd.define_environment_kgrJut()
        self.m_environment.append(dd)

#==================================================================
#
#==================================================================
        
    def add_env_kgrSet(self):
        dd = JT_Environment()
        dd.define_environment_kgrSet()
        self.m_environment.append(dd)
