#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

from JT_Logger import JT_Logger
from JT_ServerDef import JT_ServerDef 
#==================================================================
#
#==================================================================


class JT_ServersDef:
    def __init__(self):
        self.m_srvs = []
        
#==================================================================
#
#==================================================================
    def internal_init_servers_definition_test(self):    
        JT_Logger.trace_method("[METHOD_OUT][internal_init_servers_definition_test]")
        self.m_srvs.append(self.get_srv_kglagent_peripherals())
        JT_Logger.trace_method("[METHOD_OUT][internal_init_servers_definition_test]")

#==================================================================
#
#==================================================================

    def internal_init_servers_definition_jboss(self):    
        JT_Logger.trace_method("[METHOD_OUT][internal_init_servers_definition_jboss]")
        self.m_srvs.append(self.get_srv_KGRWebApp())
        self.m_srvs.append(self.get_srv_GUI())
        self.m_srvs.append(self.get_srv_GUI_36()) 
        JT_Logger.trace_method("[METHOD_OUT][internal_init_servers_definition_jboss]")
        
#==================================================================
#
#==================================================================
    def internal_init_servers_definition_gui(self):    
        JT_Logger.trace_method("[INFO].internal_init_servers_definition.METHOD_IN")
        self.m_srvs.append(self.get_srv_GUI()) 
        
#==================================================================
#
#==================================================================
    def internal_init_servers_definition_kns(self):    
        JT_Logger.trace_method("[INFO][internal_init_servers_definition_gui][METHOD_IN]")
        self.m_srvs.append(self.get_srv_KNS()) 

#==================================================================
#
#==================================================================
    def internal_init_servers_definition_ems(self):    
        JT_Logger.trace_method("[INFO][internal_init_servers_definition_ems][METHOD_IN]")
        self.m_srvs.append(self.get_srv_EMS())        
        
    def internal_init_servers_definition_kts(self):    
        JT_Logger.trace_method("[INFO][internal_init_servers_definition_ems][METHOD_IN]")
        self.m_srvs.append(self.get_srv_KTS()) 

    def internal_init_servers_definition_gui_adapter(self):
        JT_Logger.trace_method("[INFO][internal_init_servers_definition_gui_adapter][METHOD_IN]")
        self.m_srvs.append(self.get_srv_GUI_ADAPTER()) 

#==================================================================
#
#==================================================================
    
    def internal_init_servers_definition_all(self):    
        JT_Logger.trace_method("[INFO].internal_init_servers_definition_all.METHOD_IN")
        self.m_srvs.append(self.get_srv_KNS())
        self.m_srvs.append(self.get_srv_KTS())
        self.m_srvs.append(self.get_srv_KIS())
        self.m_srvs.append(self.get_srv_KAS())
        self.m_srvs.append(self.get_srv_PS_and_Kgr("KVS","KGRVaRServer"))
        self.m_srvs.append(self.get_srv_PS_and_Kgr("KRMS","KGRRateManagerServer"))
        self.m_srvs.append(self.get_srv_KGRAdapter())
        self.m_srvs.append(self.get_srv_KGLagent())
        self.m_srvs.append(self.get_srv_kglagent_peripherals())
        self.m_srvs.append(self.get_srv_KGLagent_Start())
        self.m_srvs.append(self.get_srv_Gatevay())
        self.m_srvs.append(self.get_srv_KGRWebApp())
        self.m_srvs.append(self.get_srv_EMS()) 
        self.m_srvs.append(self.get_srv_GUI())
        self.m_srvs.append(self.get_srv_GUI_36())  
        self.m_srvs.append(self.get_srv_GUI_ADAPTER())
        self.m_srvs.append(self.get_srv_FOA())
        self.m_srvs.append(self.get_srv_database())
        
        self.m_srvs.append(self.get_srv_ds())
        self.m_srvs.append(self.get_srv_bs())
        self.m_srvs.append(self.get_srv_rdv())
        self.m_srvs.append(self.get_srv_kms())
        self.m_srvs.append(self.get_srv_krs())
        self.m_srvs.append(self.get_srv_kis())
        self.m_srvs.append(self.get_srv_kcs())
        self.m_srvs.append(self.get_srv_kbs())
        self.m_srvs.append(self.get_srv_kois())
        self.m_srvs.append(self.get_srv_startksrv())
        
        
        
#==================================================================
#
#==================================================================
                
    def get_srv(self,name,pname):
        dd = JT_ServerDef()
        dd.m_server_name= name
        dd.m_ProcessName = pname
        dd.m_ProcessNameInPsLine = 1
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 0
        return dd


#==================================================================
#
#==================================================================
    def get_srv_kis(self):
        dd = self.get_srv("kis","kis")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("kis")
        return dd
#==================================================================
#
#==================================================================

    def get_srv_rdv(self):
        dd = self.get_srv("rdv","rdv")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("rdv")
        return dd
#==================================================================
#
#==================================================================
            
    def get_srv_Gatevay(self):
        dd = self.get_srv("Gatevay","KGRKondorGatewayServer")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("KGRKondorGatewayServer")
        dd.m_ParamsPargsLine.add_param_s("KGRKondorGatewayServer")        
        return dd

#==================================================================
#
#==================================================================

            
    def get_srv_KAS(self):
        dd = self.get_srv("KAS","KGRAggregationServer")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("KGRAggregationServer")
        return dd

#==================================================================
#
#==================================================================

            
        
    def get_srv_PS_and_Kgr(self,name,pname):
        dd = JT_ServerDef()
        dd.m_server_name= name
        dd.m_ProcessName = pname
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 1
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s(pname)
        return dd


#==================================================================
#
#==================================================================

    def get_srv_KGRAdapter(self):
        dd = self.get_srv("Adapter","KGRAdapter")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 1
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("KGRAdapter")
        return dd

#==================================================================
#
#==================================================================

#==================================================================
#
#==================================================================

    def get_srv_KIS(self):
        dd = self.get_srv("KIS","KGRImportServer")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        #dd.m_ParamsPsLine.add_param_s("KGRImportServer")
        dd.m_ParamsPargsLine.add_param_s("KGRImportServer")
        return dd
        

#==================================================================
#
#==================================================================

    def get_srv_KGLagent(self):
        dd = self.get_srv("KGLAgent_bin_dist","kglagent")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 1
        dd.m_ParamsPsLine.add_param_s("kglagent")
        dd.m_ParamsPargsLine.add_param_s("kglagent")
        dd.m_ParamsPargsLine.add_param_s("dist")
        return dd

#==================================================================
#
#==================================================================

    def get_srv_kglagent_peripherals(self):
        dd = self.get_srv("KGLAgent_bin_peripherlas","kglagent")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        #dd.m_ParamsPsLine.add_param_s("kglagent")
        dd.m_ParamsPargsLine.add_param_s("kglagent")
        dd.m_ParamsPargsLine.add_param_s("peripherals")
        return dd


#==================================================================

    def get_srv_KGLagent_Start(self):
        dd = self.get_srv("KGLAgent_start","kglagent")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 1
        dd.m_ParamsPsLine.add_param_s("kglagent")
        dd.m_ParamsPargsLine.add_param_s("startkglagent")
        dd.m_ParamsPargsLine.add_param_s("ksh")
        return dd
        
#==================================================================
#
#==================================================================

    def get_srv_KNS(self):
        dd = self.get_srv("KNS","KGRServer")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        #dd.m_ParamsPsLine.add_param_s("KGRServer")
        dd.m_ParamsPargsLine.add_param_s("KGRServer")
        return dd
    
#==================================================================
#
#==================================================================

    def get_srv_GUI(self):
        dd = self.get_srv("KGR_GUI_JBOSS(java)","java")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 1
        dd.m_ParamsPsLine.add_param_s("java")
        dd.m_ParamsPargsLine.add_param_s("_jboss.sh")        
        return dd

#==================================================================
#
#==================================================================

    def get_srv_GUI_36(self):
        dd = JT_ServerDef()
        dd.m_server_name= "JAVA_KGR_GUI_JBOSS_36"
        dd.m_ProcessName = ""        
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 1
        dd.m_ParamsPsLine.add_param_s("java")
        dd.m_ParamsPsLine.add_param_s("run.sh")
        dd.m_ParamsPargseLine.add_param_s("gui.properties")
        return dd
    
#==================================================================
#
#==================================================================
    
    def get_srv_KGRWebApp(self):
        dd = self.get_srv("startKGRWebApp_jboss","startKGRWebApp_jboss.sh]")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 1
        dd.m_ParamsPsLine.add_param_s("startKGRWebApp_jboss.sh")
        return dd

#==================================================================
#
#==================================================================

    def get_srv_GUI_ADAPTER(self):
        dd = self.get_srv("KGR_GUI_ADAPTER","java")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("java")        
        dd.m_ParamsPargsLine.add_param_s("adapter")
        #dd.m_ParamsPargsLine.add_param_s("com.reuters.kgr.adapter.wsserver.Server")
        
        return dd
        
#==================================================================
#
#==================================================================

    def get_srv_EMS(self):
        dd = self.get_srv("EMS(tibems in ps,kgr in ps)","tibems")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 1
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("tibemsd")        
        return dd
        
#==================================================================
#
#==================================================================

    def get_srv_KTS(self):
        dd = self.get_srv("KTS( KGRTaskServer in ps, kgr in ps)","KGRTaskServer")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        #dd.m_ParamsPsLine.add_param_s("KGRTaskServer")
        dd.m_ParamsPargsLine.add_param_s("KGRTaskServer")        
        return dd
                
#==================================================================
#
#==================================================================


    def get_srv_FOA(self):
        dd = self.get_srv("FOA","startFrontOfficeAdapter.sh")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("startFrontOfficeAdapter.sh")
        return dd

#==================================================================
#
#==================================================================

    def get_srv_kbs(self):
        dd = self.get_srv("FOA","kbs")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("kbs")
        return dd
#==================================================================
#
#==================================================================

    def get_srv_startksrv (self):
        dd = self.get_srv("startksrv ","startksrv")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("startksrv")
        return dd
#==================================================================
#
#==================================================================

    def get_srv_krs(self):
        dd = self.get_srv("krs","krs")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 1
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("krs")
        return dd
#==================================================================
#
#==================================================================

    def get_srv_kms (self):
        dd = self.get_srv("kms ","kms")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 1
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("kms")
        return dd

#==================================================================
#
#==================================================================

    def get_srv_kois (self):
        dd = self.get_srv("kois","kois")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 1
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("kois")
        return dd
#==================================================================
#
#==================================================================
    
    def get_srv_tradecast (self):
        dd = self.get_srv("tradecast","tradecast")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 1
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("tradecast")
        return dd
#==================================================================
#
#==================================================================
    
    def get_srv_kcs (self):
        dd = self.get_srv("kcs","kcs")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 1
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("kcs")
        return dd
#==================================================================
#
#==================================================================
    
    def get_srv_bs (self):
        dd = self.get_srv("bs","bs")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 1
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("bs")
        return dd
#==================================================================
#
#==================================================================
    
    def get_srv_ds (self):
        dd = self.get_srv("ds( something kp, kgr in ps, ds in ps)","ds")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 1
        dd.m_KgrInstanceNameInPargs = 0
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("ds")
        return dd

#==================================================================
#
#==================================================================

    def get_srv_database(self):
        dd = self.get_srv("DATABASE","dataserver")
        dd.m_ProcessNameInPsLine = 0
        dd.m_ProcessNameInArgs = 0
        dd.m_KgrInstanceNameInPs = 0
        dd.m_KgrInstanceNameInPargs = 1
        dd.m_KgrInstanceNameInPargse = 0
        dd.m_ParamsPsLine.add_param_s("dataserver")
        return dd
    
    
        
#==================================================================
#
#==================================================================
    def get_srv_by_key(self,p_str_key):    
        JT_Logger.trace_method("[METHOD_IN[get_srv_by_key]")
        
        if( p_str_key == "KNS"):
            self.m_srvs.append(self.get_srv_KNS())
            
        if( p_str_key == "KTS"):
            self.m_srvs.append(self.get_srv_KTS())
            
        if( p_str_key == "KIS"):
            self.m_srvs.append(self.get_srv_KIS())
            
        if( p_str_key == "KAS"):
            self.m_srvs.append(self.get_srv_KAS())
            
        if( p_str_key == "KVS"):
            self.m_srvs.append(self.get_srv_PS_and_Kgr("KVS","KGRVaRServer"))
            
        if( p_str_key == "RATE"):
            self.m_srvs.append(self.get_srv_PS_and_Kgr("KRMS","KGRRateManagerServer"))
            
        if( p_str_key == "KGRAdapter"):
            self.m_srvs.append(self.get_srv_KGRAdapter())
            
        if( p_str_key == "KGLAgent"):
            self.m_srvs.append(self.get_srv_KGLagent())
            
        if( p_str_key == "kglagent_peripherals"):
            self.m_srvs.append(self.get_srv_kglagent_peripherals())
            
        if( p_str_key == "KGLagent_Start"):
            self.m_srvs.append(self.get_srv_KGLagent_Start())
            
        if( p_str_key == "Gatevay"):
            self.m_srvs.append(self.get_srv_Gatevay())
            
        if( p_str_key == "KGRWebApp"):
            self.m_srvs.append(self.get_srv_KGRWebApp())
            
        if( p_str_key == "EMS"):
            self.m_srvs.append(self.get_srv_EMS())
            
        if( p_str_key == "GUI"): 
            self.m_srvs.append(self.get_srv_GUI())
            
        if( p_str_key == "GUI_ADAPTER"): 
            self.m_srvs.append(self.get_srv_GUI_ADAPTER())
            
        if( p_str_key == "FOA"):
            self.m_srvs.append(self.get_srv_FOA())
            
        if( p_str_key == "database"):
            self.m_srvs.append(self.get_srv_database())
            
        if( p_str_key == "ds"):
            self.m_srvs.append(self.get_srv_ds())
            
        if( p_str_key == "bs"):
            self.m_srvs.append(self.get_srv_bs())
            
        if( p_str_key == "rdv"):
            self.m_srvs.append(self.get_srv_rdv())
            
        if( p_str_key == "kms"):
            self.m_srvs.append(self.get_srv_kms())
            
        if( p_str_key == "krs"):
            self.m_srvs.append(self.get_srv_krs())
            
        if( p_str_key == "kis"):
            self.m_srvs.append(self.get_srv_kis())
            
        if( p_str_key == "kcs"):
            self.m_srvs.append(self.get_srv_kcs())
            
        if( p_str_key == "kbs"):
            self.m_srvs.append(self.get_srv_kbs())
            
        if( p_str_key == "kois"):
            self.m_srvs.append(self.get_srv_kois())
            
        if( p_str_key == "startksrv"):
            self.m_srvs.append(self.get_srv_startksrv())
            
        JT_Logger.trace_method("[METHOD_OUT][get_srv_by_key]")
#==================================================================
#
#==================================================================
        