import sys
from JT_Os import JT_Os
from JT_Logger import JT_Logger
from JT_FIND_KgrEnvironmentFinder import JT_FIND_KgrEnvironmentFinder
from JT_FIND_Argv import JT_FIND_ARGV
#==================================================================
#
#==================================================================

class JT_S:
    @staticmethod
    def get_str(s_str):
        return s_str
#==================================================================
#
#==================================================================
    

#==================================================================
#
#==================================================================

class JT_FIND_KgrInstallHelper:

#==================================================================
#
#==================================================================
    
    def __init__(self):
        """inint"""
        self.m_kgr = "kgr36JT"
        self.m_version = "36"
        self.m_level = "36.01.010"      
        self.m_jboss_install_source = "/srv/dist/kgr/36/36.01.010/3rdparty/J2EE/jboss"
        self.m_jboss_install_dest_localfs = "/localfs/jboss_kgr36JT/36.01.010"
        self.m_jboss_in_config = "/rksup/config/kgr36JT/jboss"
        self.m_kgr_install_source = "/srv/dist/kgr/36/36.01.010/install"
        self.m_kgr_install_dest = "/rksup/config/kgr36JT/install"
        self.m_kgr_install_etc_source = "/srv/dist/kgr/36/36.01.010/etc"
        self.m_kgr_install_etc_dest = "/rksup/config/kgr36JT/etc"        
        self.m_execute = 0  
        
#==================================================================
#
#==================================================================
    def create_variables(self):
        try:
            JT_Logger.trace_method("[METHOD_IN][create_variables]")
            
            self.m_jboss_install_source = JT_S.get_str(
                                                       "/srv/dist/kgr/" 
                                                       + self.m_version 
                                                       + "/" 
                                                       + self.m_level 
                                                       + "/3rdparty/J2EE/jboss")
            
            self.m_jboss_install_dest_localfs = JT_S.get_str(
                                                             "/localfs/jboss_" 
                                                            + self.m_kgr 
                                                            + 
                                                            "/" 
                                                            + self.m_level)
            
            self.m_jboss_in_config = JT_S.get_str("/rksup/config/" 
                                                  + self.m_kgr 
                                                  + "/jboss")
            
            self.m_kgr_install_dest = JT_S.get_str(
                                                   "/rksup/config/" 
                                                   + self.m_kgr 
                                                   + "/install")
            
            self.m_kgr_install_source = JT_S.get_str("/srv/dist/kgr/" 
                                                     + self.m_version 
                                                     + "/" 
                                                     + self.m_level 
                                                     + "/" 
                                                     + "install")
            

            self.m_kgr_install_etc_dest = JT_S.get_str("/rksup/config/" 
                                   + self.m_kgr 
                                   + "/etc")
            
            self.m_kgr_install_etc_source = JT_S.get_str("/srv/dist/kgr/" 
                                                     + self.m_version + "/" 
                                                     + self.m_level + "/etc")
                                             
        except :
            JT_Logger.print_exception("[METHOD_EXC][create_variables]")
            JT_Logger.trace_method("[METHOD_OUT_EXC][create_variables]")
            
#==================================================================
#
#==================================================================

    def print_variables(self):
        try:
            JT_Logger.trace_method("[METHOD_IN][print_variables]")
            
            
            JT_Logger.print_output("")                     
            JT_Logger.print_output("[JBOSS_SOURCE]" + self.m_jboss_install_source)
            JT_Logger.print_output("[JBOSS_DEST]" + self.m_jboss_install_dest_localfs)
            JT_Logger.print_output("[JBOSS_IN_CONFIG]" + self.m_jboss_in_config)
            
            JT_Logger.print_output("")
            JT_Logger.print_output("[KGR_INSTALL_SOURCE]" + self.m_kgr_install_source)
            JT_Logger.print_output("[KGR_INSTALL_DEST]" + self.m_kgr_install_dest)
            JT_Logger.print_output("")
            JT_Logger.print_output("[KGR_INSTALL_ETC_SOURCE]" + self.m_kgr_install_etc_source)
            JT_Logger.print_output("[KGR_INSTALL_ETC_DEST]" + self.m_kgr_install_etc_dest)
            JT_Logger.print_output("")
        except :
            JT_Logger.print_exception("[METHOD_EXC][print_variables]")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_variables]")
            
            
#==================================================================
#
#==================================================================
        
    def copy_kgr_install(self):
        try:
            JT_Logger.trace_method("[METHOD_IN][copy_kgr_install]")
            
            s_cmd = JT_S.get_str("mkdir" 
                                 + " " 
                                 + self.m_kgr_install_dest )
                                   
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
            
            s_cmd = JT_S.get_str("cp -r" 
                                 + " " 
                                 + self.m_kgr_install_source 
                                 + "/* " 
                                 + self.m_kgr_install_dest )
            
            if(self.m_execute == 1):                
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
            
        except :
            JT_Logger.print_exception("[METHOD_EXC][copy_kgr_install]")
            JT_Logger.trace_method("[METHOD_OUT_EXC][copy_kgr_install]")

#==================================================================
#
#==================================================================
        
    def copy_kgr_etc(self):
        try:
            JT_Logger.trace_method("[METHOD_IN][copy_kgr_etc]")
            
            s_cmd = JT_S.get_str("mkdir" + " " + self.m_kgr_install_etc_dest )
                                   
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
            
            s_cmd = JT_S.get_str("cp -r" 
                                 + " " 
                                 + self.m_kgr_install_etc_source 
                                 + "/* " 
                                 + self.m_kgr_install_etc_dest )
            
            if(self.m_execute == 1):                
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
            
        except :
            JT_Logger.print_exception("[METHOD_EXC][copy_kgr_etc]")
            JT_Logger.trace_method("[METHOD_OUT_EXC][copy_kgr_etc]")

#==================================================================
#
#==================================================================
                        
    def copy_env_jboss(self):
        try:
            
            JT_Logger.trace_method("[METHOD_IN]" 
                                   + "[copy_env_jboss]")

            
            self.m_jboss_install_dest_localfs = JT_S.get_str( 
                                                            "/localfs/jboss_" 
                                                            + self.m_kgr 
                                                            + 
                                                            "/" 
                                                            + self.m_level)
            
            s_cmd = JT_S.get_str("mkdir" 
                                  + " "           
                                  + "/localfs/jboss_" 
                                  + self.m_kgr 
                                  + "/" 
                                  + self.m_level)                                                        
                                   
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
            
            s_cmd = JT_S.get_str("cp -r " 
                                 + self.m_jboss_install_source 
                                 + "/* " 
                                 + self.m_jboss_install_dest_localfs)
            
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
                
            
            s_cmd = JT_S.get_str("mkdir" 
                                 + " " 
                                 + "/rksup/config/" 
                                 + self.m_kgr 
                                 + "/jboss" )
            
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )

            s_cmd = JT_S.get_str("cp -r "  
                                 + " " 
                                 + "/localfs/jboss_" 
                                 + self.m_kgr 
                                 + "/"
                                 + self.m_level
                                 + "/jboss/*"
                                 + " " 
                                 + "/rksup/config/" 
                                 + self.m_kgr 
                                 + "/jboss" )
            
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
            
            
            s_cmd = JT_S.get_str("cp -r "  
                                 + " " 
                                 + "/rksup/config/" 
                                 + self.m_kgr 
                                 + "/jboss/server/default/*"
                                 + " "
                                 + "/rksup/config/" 
                                 + self.m_kgr 
                                 + "/jboss/server/kgr"                                 
                                   )
            
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
            

            s_cmd = JT_S.get_str("mkdir"  
                                 + " " 
                                 + "/rksup/config/" 
                                 + self.m_kgr 
                                 + "/local_navigation"                                 
                                   )
            
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )

            s_cmd = JT_S.get_str("cp -r "  
                                 + " " 
                                 + " /srv/dist/kgr/" 
                                 + self.m_version 
                                 + "/" 
                                 + self.m_level                                  
                                 + "gui/xml/*"                                  
                                 + " "                                 
                                 + "/rksup/config/" 
                                 + self.m_kgr 
                                 + "/local_navigation"                                 
                                   )
            
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )


            s_cmd = JT_S.get_str("mkdir "  
                                 + " "                                 
                                 + "/rksup/config/" 
                                 + self.m_kgr
                                 + "/jt_etc_jboss"                                                                   
                                   )
            
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
                                    

            s_cmd = JT_S.get_str("cp -r "  
                                 + " " 
                                 + " /srv/dist/kgr/" 
                                 + self.m_version 
                                 + "/" 
                                 + self.m_level                                  
                                 + "etc/*"                                  
                                 + " "                                 
                                 + "/rksup/config/" 
                                 + self.m_kgr
                                 + "/jt_etc_jboss"                                                                   
                                   )
            
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
                
            
        except :
            JT_Logger.print_exception("[METHOD_EXC][copy_env_jboss]")
            JT_Logger.trace_method("[METHOD_OUT_EXC][copy_env_jboss]")

#==================================================================
#
#==================================================================
                        
    def copy_files_jms(self):
        try:
            
            JT_Logger.trace_method("[METHOD_IN]" 
                                   + "[copy_files_jms]")
            
            s_cmd = JT_S.get_str( "mkdir /rksup/config/" + self.m_kgr + "/jms" )
                                   
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
            
            s_cmd = JT_S.get_str("cp -r "
                                 + " /srv/dist/kgr/" 
                                 + self.m_version 
                                 + "/" 
                                 + self.m_level + "/3rdparty/jms"
                                 + "/* "
                                 + "/rksup/config/" + self.m_kgr + "/jms"
                                 )
            
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
                
            
            
        except :
            JT_Logger.print_exception("[METHOD_EXC][copy_files_jms]")
            JT_Logger.trace_method("[METHOD_OUT_EXC][copy_files_jms]")

#==================================================================
#
#==================================================================

    def make_ln_jboss(self):
        try:
            
            JT_Logger.trace_method("[METHOD_IN][make_ln_jboss]")
            
            
            s_cmd = JT_S.get_str("ln -s " 
                                 + self.m_jboss_install_dest_localfs 
                                 + " " 
                                 + self.m_jboss_in_config)
            
            if(self.m_execute == 1):
                JT_Os.run_pexpect_no_print( s_cmd )
            else:
                JT_Logger.print_output( s_cmd )
            
        except :
            JT_Logger.print_exception("[METHOD_EXC][make_ln_jboss]")
            JT_Logger.trace_method("[METHOD_OUT_EXC][make_ln_jboss]")
#==================================================================
#
#==================================================================

    def install_kgr(self
                    ,s_execute
                    ,s_kgr
                    ,s_version
                    ,s_level):
        try:            
            JT_Logger.trace_method("[METHOD_IN][install_kgr]")
            if(s_execute == "execute_copy_mode"):
                self.m_execute = 1
            else:
                self.m_execute = 0     
            self.m_kgr = s_kgr
            self.m_version = s_version
            self.m_level = s_level
            self.create_variables()
            self.print_variables()
            self.copy_kgr_install()
            self.copy_kgr_etc()
            self.copy_files_jms()
            self.copy_env_jboss()
            self.make_ln_jboss()
            JT_Logger.trace_method("[METHOD_OUT][install_kgr]")
        except :
            JT_Logger.print_exception("[METHOD_EXC][install_kgr")
            JT_Logger.trace_method("[METHOD_OUT_EXC][install_kgr]")
#==================================================================
#
#==================================================================
            
            
class JT_FIND_KgrInstallerExecute:
    
    @staticmethod
    def prepare_directories():
        cc = JT_FIND_KgrInstallHelper()        
        s_execute_mode = JT_FIND_ARGV.get_argv_pos_def(1,"not_execute_copy_mode")
        
        JT_Logger.print_output("[s_execute_mode:" + s_execute_mode + "]")
        
        cc.install_kgr(s_execute_mode
                       ,"kgr36JT"
                       ,"36"
                       ,"36.01.010")

        
#==================================================================
#
#==================================================================

    @staticmethod
    def check_arguments():
        JT_Logger.print_output( "")
        JT_FIND_ARGV.print_argv_pos(1,["not_execute_copy_mode","execute_copy_mode"])
        JT_FIND_ARGV.print_argv_pos(2,["not_debug_mode","debug_mode"])
        JT_FIND_ARGV.print_argv_pos(3,["not_replace_mode","replace_mode"])
        JT_FIND_ARGV.print_argv_pos(4,["not_cp_temp_to_def","cp_temp_to_def"])
        JT_FIND_ARGV.print_argv_pos(5,["not_cp_def_to_robo","cp_def_to_robo"])
        
        JT_Logger.print_output( "")
        JT_Logger.print_output( "")
        JT_FIND_ARGV.check_argv_pos(1,["not_execute_copy_mode","execute_copy_mode"])
        JT_FIND_ARGV.check_argv_pos(2,["not_debug_mode","debug_mode"])
        JT_FIND_ARGV.check_argv_pos(3,["not_replace_mode","replace_mode"])
        JT_FIND_ARGV.check_argv_pos(4,["not_cp_temp_to_def","cp_temp_to_def"])
        JT_FIND_ARGV.check_argv_pos(5,["not_cp_def_to_robo","cp_def_to_robo"])
        
#==================================================================
#
#==================================================================
        
    @staticmethod
    def prepare_config_files():
        
        
        s_debug_mode = JT_FIND_ARGV.get_argv_pos_def(2,"not_debug_mode")
        s_replace_mode = JT_FIND_ARGV.get_argv_pos_def(3,"not_replace_mode")
        s_cp_temp_to_def = JT_FIND_ARGV.get_argv_pos_def(4,"not_cp_temp_to_def")
        s_cp_def_to_robo = JT_FIND_ARGV.get_argv_pos_def(5,"not_cp_def_to_robo")
        
        JT_Logger.print_output("[prepare_config_files][s_debug_mode:" + s_debug_mode + "]")
        JT_Logger.print_output("[prepare_config_files][s_replace_mode:" + s_replace_mode + "]")
        JT_Logger.print_output("[prepare_config_files][s_cp_temp_to_def:" + s_cp_temp_to_def + "]")        
        JT_Logger.print_output("[prepare_config_files][s_cp_def_to_robo:" + s_cp_def_to_robo + "]")
        
        dd = JT_FIND_KgrEnvironmentFinder()
        #s_cp_temp_to_def = "cp_temp_to_def"
        #s_cp_def_to_robo = "cp_def_to_robo"
        #s_replace_mode = "replace_mode"
        dd.internal_build_kgr("kgr36JT"
                              ,"36"
                              ,"36.01.010"
                              ,s_debug_mode
                              , s_replace_mode
                              , s_cp_temp_to_def
                              , s_cp_def_to_robo)

#==================================================================
#
#==================================================================
               
if __name__ == '__main__':
    JT_FIND_ARGV.print_argv(0)
    JT_FIND_KgrInstallerExecute.check_arguments()
    JT_FIND_KgrInstallerExecute.prepare_directories()
    JT_FIND_KgrInstallerExecute.prepare_config_files()

#==================================================================
#
#==================================================================

#cp -r /srv/dist/kgr/36/36.01.010/3rdparty/J2EE/jboss /localfs/jboss_kgr36JT/36.01.010        
                      