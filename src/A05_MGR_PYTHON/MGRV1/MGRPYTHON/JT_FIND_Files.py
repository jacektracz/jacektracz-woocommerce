import pexpect 

from JT_Logger import JT_Logger
from JT_FIND_Headers import JT_FIND_Headers
#==================================================================
#
#==================================================================

class JT_FIND_File:
    
#==================================================================
#
#==================================================================
    
    def __init__(self):
        self.m_file_template = ""
        self.m_file_config = ""
        self.m_file_def = ""
        self.m_file_robo = ""
        self.m_file_install = ""
        self.is_backup_created = 0
        self.not_replace_in_file = 0
                
#==================================================================
#
#==================================================================
        
class JT_FIND_Files:
    
#==================================================================
#
#==================================================================
    
    def __init__(self):
        self.m_find_files = []
    #==================================================================
    #
    #==================================================================
        
    def add_kgr_file_to_list(self,p_kgr,p_file):
        """build_list_of_files"""
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[add_kgr_file_to_list]" 
                                       + "[p_file:"  + p_file + "]")
        
        s_file ="/rksup/config/" + p_kgr + "/" + p_file
        dd = JT_FIND_File()
        dd.m_file_config = s_file        
        self.m_find_files.append( dd )        
        JT_Logger.trace_hard_level_16( "[METHOD_OUT][add_kgr_file_to_list]" )
    #==================================================================
    #
    #==================================================================
        
    def init_list_of_files_to_empty(self):
        self.m_find_files = []
    #==================================================================
    #
    #==================================================================

    def add_raw_file_to_list(self, s_file):
        """add_raw_file_to_list"""
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[add_raw_file_to_list]" 
                                       + "[p_file:"  + s_file + "]")
        dd = JT_FIND_File()
        dd.m_file_config = s_file
        dd.m_file_template = s_file
        self.m_find_files.append( dd )        
        JT_Logger.trace_hard_level_16( "[METHOD_IN][add_raw_file_to_list]" )
    #==================================================================
    #
    #==================================================================

    def add_file_install_jboss_raw(self
                               , s_def_folder
                               , s_robo_folder
                               , s_kgr_name
                               , s_ver_name
                               , s_full_default_file_path
                               , s_file_name):
        """build_list_of_files"""
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[add_file_install_jboss_raw]" 
                                       + "[p_file:"  + s_full_default_file_path + "]")
        dd = JT_FIND_File()
        dd.m_file_template = s_full_default_file_path        
        dd.m_file_config = "/rksup/config/" + s_kgr_name + "/" +  s_file_name            
        dd.m_file_robo = "/rksup/config/" + s_kgr_name + "/" + s_robo_folder + "/" +  s_file_name
        dd.m_file_def = "/rksup/config/" + s_kgr_name + "/" + s_def_folder + "/" +  s_file_name
        
        dd.m_file_install = "/rksup/config/" + s_kgr_name + "/" + s_file_name
        
        self.m_find_files.append( dd )        
        JT_Logger.trace_hard_level_16( "[METHOD_IN][add_file_install_jboss_raw]" )
        
#==================================================================
#
#==================================================================
    def add_file_install_kgr_raw(self
                               , s_def_folder
                               , s_robo_folder
                               , s_kgr_name
                               , s_ver_name
                               , s_file_default
                               , s_file_name):
        """build_list_of_files"""
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[add_file_install_kgr_raw]" 
                                       + "[p_file:"  + s_file_default + "]")
        dd = JT_FIND_File()
        dd.m_file_template = "/rksup/config/" + s_kgr_name + "/etc/config/" + s_file_default        
        dd.m_file_config = "/rksup/config/" + s_kgr_name + "/" +  s_file_name            
        dd.m_file_robo = "/rksup/config/" + s_kgr_name + "/" + s_robo_folder + "/" +  s_file_name
        dd.m_file_def = "/rksup/config/" + s_kgr_name + "/" + s_def_folder + "/" +  s_file_name        
        dd.m_file_install = "/rksup/config/" + s_kgr_name + "/" +    s_file_name
        
        self.m_find_files.append( dd )        
        JT_Logger.trace_hard_level_16( "[METHOD_IN][add_file_install_kgr_raw]" )
        
#==================================================================
#
#==================================================================

    def add_file_install_jms_raw(self
                               , s_def_folder
                               , s_robo_folder
                               , s_kgr_name
                               , s_ver_name
                               , s_level
                               , s_file_default
                               , s_file_name):
        
        """add_file_install_jms_raw"""
        
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[add_file_install_jms_raw]" 
                                       + "[p_file:"  + s_file_default + "]")
        dd = JT_FIND_File()
        dd.m_file_template = "/rksup/config/" + s_kgr_name + "/jms/" + s_file_default        
        dd.m_file_config = "/rksup/config/" + s_kgr_name + "/" +  s_file_name            
        dd.m_file_robo = "/rksup/config/" + s_kgr_name + "/" + s_robo_folder + "/" +  s_file_name
        dd.m_file_def = "/rksup/config/" + s_kgr_name + "/" + s_def_folder + "/" +  s_file_name        
        dd.m_file_install = "/rksup/config/" + s_kgr_name + "/" +    s_file_name
        
        self.m_find_files.append( dd )        
        JT_Logger.trace_hard_level_16( "[METHOD_IN][add_file_install_jms_raw]" )
        
#==================================================================
#
#==================================================================
        

    def add_files_pair(self,p_old,p_new):
        dd = JT_FIND_File()
        dd.m_file_config = p_new
        dd.m_file_template = p_old
        self.m_find_files.append(dd)
        
#==================================================================
#
#==================================================================

    def build_list_of_config_files(self,p_kgr):
        """build_list_of_files"""
        JT_Logger.trace_hard_level_16( "[METHOD_IN][build_list_of_files]" )        
        self.add_kgr_file_to_list(p_kgr,"bindings-jboss-beans.xml")
        self.add_kgr_file_to_list(p_kgr,"ejb3-connectors-jboss-beans.xml")
        self.add_kgr_file_to_list(p_kgr,"hajndi-jms-ds.xml")
        self.add_kgr_file_to_list(p_kgr,"jboss-log4j.xml")
        self.add_kgr_file_to_list(p_kgr,"kas.pfe.config.xml")
        self.add_kgr_file_to_list(p_kgr,"kgr-ds.xml")
        self.add_kgr_file_to_list(p_kgr,"krms.mc.config.xml")
        self.add_kgr_file_to_list(p_kgr,"pricer_config.xml")
        self.add_kgr_file_to_list(p_kgr,"server.xml")
        self.add_kgr_file_to_list(p_kgr,"standardjboss.xml")        
        self.add_kgr_file_to_list(p_kgr,"KgrRun.conf")
        self.add_kgr_file_to_list(p_kgr,"acl.conf")
        self.add_kgr_file_to_list(p_kgr,"bridges.conf")
        self.add_kgr_file_to_list(p_kgr,"factories.conf")
        self.add_kgr_file_to_list(p_kgr,"groups.conf")
        self.add_kgr_file_to_list(p_kgr,"queues.conf")
        self.add_kgr_file_to_list(p_kgr,"routes.conf")
        self.add_kgr_file_to_list(p_kgr,"tibjmsd.conf")
        self.add_kgr_file_to_list(p_kgr,"tibrvcm.conf")
        self.add_kgr_file_to_list(p_kgr,"topics.conf")
        self.add_kgr_file_to_list(p_kgr,"transports.conf")
        self.add_kgr_file_to_list(p_kgr,"users.conf")
        self.add_kgr_file_to_list(p_kgr,"log4cxx.propertie")
        self.add_kgr_file_to_list(p_kgr,"log4j.properties")
        self.add_kgr_file_to_list(p_kgr,"rknetdbinit.log4cxx.properties")
        self.add_kgr_file_to_list(p_kgr,"install.params")
        self.add_kgr_file_to_list(p_kgr,"rknetdbcopy26.params")
        self.add_kgr_file_to_list(p_kgr,"rknetdbcopy30.params")        
        self.add_kgr_file_to_list(p_kgr,"DealManager.cfm")
        self.add_kgr_file_to_list(p_kgr,"KGRAggregationServer.cfm")
        self.add_kgr_file_to_list(p_kgr,"KGRKondorGatewayServer.cfm")
        self.add_kgr_file_to_list(p_kgr,"KGRRateManagerServer.cfm")
        self.add_kgr_file_to_list(p_kgr,"KGRServer.cfm")
        self.add_kgr_file_to_list(p_kgr,"KGRTaskServer.cfm")
        self.add_kgr_file_to_list(p_kgr,"RKNetDBInit.cfm")
        self.add_kgr_file_to_list(p_kgr,"basic.cfm")
        self.add_kgr_file_to_list(p_kgr,"expert.cfm")
        self.add_kgr_file_to_list(p_kgr,"kglagent.cfm")
        self.add_kgr_file_to_list(p_kgr,"rknetdbcopy30.cfm")
        self.add_kgr_file_to_list(p_kgr,"rknetdbcopy30U99.2.cfm")
        self.add_kgr_file_to_list(p_kgr,"source.cfm")
        self.add_kgr_file_to_list(p_kgr,"jboss5-installKGRServices.ksh")
        self.add_kgr_file_to_list(p_kgr,"startKGRWebApp_jboss.sh")
        self.add_kgr_file_to_list(p_kgr,"starttibems.sh")
        self.add_kgr_file_to_list(p_kgr,"stopKGRWebApp_jboss.sh")
        self.add_kgr_file_to_list(p_kgr,"KreditNetRepo.dat")        
        JT_Logger.trace_hard_level_16( "[METHOD_OUT][build_list_of_files]" )

    #==================================================================
    #
    #==================================================================

    def build_list_of_config_files_kgr36c_pattern(self,p_kgr):
        """build_list_of_files"""
        JT_Logger.trace_hard_level_16( "[METHOD_IN][build_list_of_files]" )        

        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/jboss5-installKGRServices.ksh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startKGRWebApp_jboss.bat")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startKGRWebApp_jboss.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/stopKGRWebApp_jboss.bat")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/stopKGRWebApp_jboss.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/log4j.properties")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/bindings-jboss-beans.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/standardjboss.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/KgrRun.conf")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/jboss-log4j.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/server.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/hajndi-jms-ds.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/ejb3-connectors-jboss-beans.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/kgr-ds.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/RTM.env")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/kgr-jetty.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/root.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/rtm-log4j.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startRTM.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/stopRTM.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/weblogic10-installKGRServices.ksh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startKGRWebApp_weblogic10.cmd")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startKGRWebApp_weblogic10.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/stopKGRWebApp_weblogic10.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startKGRWebApp.cmd")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startKGRWebApp.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/factories.conf")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/tibjmsd.conf")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/starttibems.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/starttibjms.cmd")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/KGRAggregationServer.cfm")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/DealManager.cfm")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/KGRImportServer.lcf")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/KGRKondorGatewayServer.cfm")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/KGRRateManagerServer.cfm")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/KreditNetRepo.dat")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/RMDS.cnf")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/RMDSConf.params")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/basic.cfm")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/expert.cfm")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/install.params")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/kas.pfe.config.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/kglagent.cfm")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/krms.mc.config.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/log4cxx.properties")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/rknetdbcopy26.params")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startValuationEngine")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/proxy.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/adapter.log4j.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/gui.log4j.xml")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/gui.properties")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/kgr.properties")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/reporting.properties")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/spring-config.properties")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/createCommonPaths.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/runCli.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/setActiveParams.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startFrontOfficeAdapter.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startKGRKondorAdapter.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startKocktail.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startReportBatch.sh")
        self.add_kgr_file_to_list(p_kgr,"/rksup/config/kgr36c/startSampleAdapter.sh")

    #==================================================================
    #
    #==================================================================
        
    def build_list_of_installed_jboss_files(self
                                            , s_def
                                            , s_robo
                                            , p_kgr
                                            , p_ver):
                
        """build_list_of_installed_jboss_files"""
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[build_list_of_installed_jboss_files]"
                                       + "[s_def:" + str(s_robo) + "]" 
                                       + "[s_robo:" + str(s_robo) + "]" 
                                       + "[p_kgr:" + str(p_kgr) + "]"
                                       + "[p_ver:" + str(p_ver) + "]" 
                                       + "" )        
        #cd /localfs/jboss_kgr36JT/36.01.010/jboss/
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/bin/jboss5-installKGRServices.ksh.default","jboss5-installKGRServices.ksh")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/bin/startKGRWebApp_jboss.bat.default","startKGRWebApp_jboss.bat")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/bin/startKGRWebApp_jboss.sh.default","startKGRWebApp_jboss.sh")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/bin/stopKGRWebApp_jboss.bat.default","stopKGRWebApp_jboss.bat")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/bin/stopKGRWebApp_jboss.sh.default","stopKGRWebApp_jboss.sh")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/server/template/boot/log4j.properties.default","log4j.properties")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/server/template/conf/bindingservice.beans/META-INF/bindings-jboss-beans.xml.default","bindings-jboss-beans.xml")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/server/template/conf/standardjboss.xml.default", "standardjboss.xml")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/server/template/conf/KgrRun.conf.default", "KgrRun.conf")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/server/template/conf/jboss-log4j.xml.default", "jboss-log4j.xml")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/server/template/deploy/jbossweb.sar/server.xml.default", "server.xml")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/server/template/deploy/messaging/hajndi-jms-ds.xml.default", "hajndi-jms-ds.xml")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver,"/localfs/jboss_kgr36JT/36.01.010/jboss/kgr/server/template/deploy/ejb3-connectors-jboss-beans.xml.default", "ejb3-connectors-jboss-beans.xml")
        self.add_file_install_jboss_raw(s_def, s_robo, p_kgr,p_ver," /localfs/jboss_kgr36JT/36.01.010/jboss/kgr/server/template/deploy/kgr-ds.xml.default", "kgr-ds.xml")
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN][build_list_of_installed_jboss_files]" )

    #==================================================================
    #
    #==================================================================
        
    def build_list_of_installed_kgr_files(self
                                            , s_def
                                            , s_robo
                                            , p_kgr
                                            , p_ver):
                
        """build_list_of_installed_jboss_files"""
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[build_list_of_installed_kgr_files]"
                                       + "[s_def:" + str(s_robo) + "]" 
                                       + "[s_robo:" + str(s_robo) + "]" 
                                       + "[p_kgr:" + str(p_kgr) + "]"
                                       + "[p_ver:" + str(p_ver) + "]" 
                                       + "" )        
        p_lev = ""
        #self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "ConfigUpgrade", "ConfigUpgrade")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "CorrelationConfigData.xml", "CorrelationConfigData.xml")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "DealManager.cfm.default", "DealManager.cfm")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "DevCorrHierarchy.xml", "DevCorrHierarchy.xml")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "KGRAdapter.tra.default", "KGRAdapter.tra")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "KGRAggregationServer.cfm.default", "KGRAggregationServer.cfm")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "KGRImportServer.lcf.default", "KGRImportServer.lcf")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "KGRImportServer.tra.default", "KGRImportServer.tra")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "KGRKondorGatewayServer.cfm.default", "KGRKondorGatewayServer.cfm")
        #self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "KGRParams.csv", "KGRParams.csv")
        #self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "KGRParams.help", "KGRParams.help")
        #self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "KGRParams.xls", "KGRParams.xls")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "KGRRateManagerServer.cfm.default", "KGRRateManagerServer.cfm")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "KGRTaskServer.cfm.default", "KGRTaskServer.cfm")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "KreditNetRepo.dat.default", "KreditNetRepo.dat")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "basic.cfm.default", "basic.cfm")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "expert.cfm.default", "expert.cfm")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "install.params.default", "install.params")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "kas.pfe.config.xml.default", "kas.pfe.config.xml")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "kglagent.cfm.default", "kglagent.cfm")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "krms.mc.config.xml.default", "krms.mc.config.xml")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "log4cxx.properties.default", "log4cxx.properties")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "pricer_config.xml.default", "pricer_config.xml")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "rknetdbcopy26.params.default", "rknetdbcopy26.params")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "rknetdbcopy30.params.default", "rknetdbcopy30.params")
        self.add_file_install_kgr_raw(s_def, s_robo, p_kgr,p_ver, "source.cfm.default",  "source.cfm")
        
        
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"conf/acl.conf.default","acl.conf")
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"conf/channels.conf.default","channels.conf")
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"conf/durables.conf.default","durables.conf")
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"conf/factories.conf.default","factories.conf") 
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"conf/queues.conf.default","queues.conf") 
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"conf/stores.conf.default","stores.conf")
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"conf/tibjmsd.conf.default","tibjmsd.conf")
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"conf/topics.conf.default","topics.conf") 
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"conf/transports.conf.default","transports.conf") 
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"conf/users.conf","users.conf") 

        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"starttibems.sh.default","starttibems.sh") 
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"starttibjms.cmd.default","starttibjms.cmd") 
        self.add_file_install_jms_raw(s_def, s_robo, p_kgr,p_ver,p_lev,"stoptibems.sh","stoptibems.sh") 
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN][build_list_of_installed_kgr_files]" )
        
    #==================================================================
    #
    #==================================================================
    
    def copy_files_from_new_to_old(self):
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[copy_files_from_new_to_old]")

        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[copy_files_from_new_to_old]")

    #==================================================================
    #
    #==================================================================
    def show_dir(self,s_dir):
        try:
            JT_FIND_Headers().print_finding_header( s_dir )
            print pexpect.run("ls " + s_dir)
        except:
            JT_Logger.print_exception("exception_in_show_dir")
            
    #==================================================================
    #
    #==================================================================
        
    def show_jboss_files(self):
        """shov_jboss_files"""
        try:
            JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                           + "[show_jboss_files]")
    
            
            JBOSS_ORIG_CONFIGS_DIR="/rksup/config/kgr36JT/jboss/server"
            self.show_dir(JBOSS_ORIG_CONFIGS_DIR)
            #JBOSS_MODEL_CONFIG="$JBOSS_ORIG_CONFIGS_DIR/default"
            
            JBOSS_MODEL_CONFIG = "/rksup/config/kgr36JT/jboss/server/default"
            self.show_dir(JBOSS_MODEL_CONFIG)
            
            KREDITNETHOME = "/srv/dist/kgr/36/36.01.010"
            self.show_dir(KREDITNETHOME)
            
            KGR_CONFIG_TEMPLATE="/srv/dist/kgr/36/36.01.010/3rdparty/J2EE/jboss/kgr/server/template"
            self.show_dir(KGR_CONFIG_TEMPLATE)
            
            KGR_TARGET_CONFIG="/rksup/config/kgr36JT/jboss/server/kgr"
            self.show_dir(KGR_TARGET_CONFIG)
            JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                           + "[show_jboss_files]")
        except:
            JT_Logger.print_exception("exception_in_show_jboss_files")

    #==================================================================
    #
    #==================================================================
        
