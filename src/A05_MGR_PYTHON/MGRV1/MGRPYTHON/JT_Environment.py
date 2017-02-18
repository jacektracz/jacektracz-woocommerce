#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

from JT_Service import JT_Service

class JT_Environment:

#==================================================================
#
#==================================================================

    def __init__(self):
        self.m_services = []
        self.m_env_name = ""


#==================================================================
#
#==================================================================
        
        
    def add_service(self,plist,p_key,p_value):
        plist.append(self.get_service(p_key,p_value))
        

#==================================================================
#
#==================================================================
        
    def add_service_2(self,plist,p_key,p_value,p_group):
        plist.append(self.get_service_2(p_key,p_value,p_group))

#==================================================================
#
#==================================================================

    def add_service_adapter(self,p_group,p_key,p_value):
        ds = JT_Service()
        ds.m_value = p_value
        ds.m_key=p_key
        return ds;
        


#==================================================================
#
#==================================================================
        
    def get_service(self,p_key,p_value):
        ds = JT_Service()
        ds.m_value = p_value
        ds.m_key=p_key
        return ds;
    


#==================================================================
#
#==================================================================
        
    def get_service_2(self,p_key,p_value,p_group):
            ds = JT_Service()
            ds.m_value = p_value
            ds.m_key=p_key
            ds.m_group = p_group           
            return ds;
        

#==================================================================
#
#==================================================================

    def define_environment_http(self):
        self.add_service(self.m_services,"WebGui_Http_32b","http://gdnssun23:18020/kgr")
        self.add_service(self.m_services,"WebGui_Http_32a","http://gdnssun23:18010/kgr")

#==================================================================
#
#==================================================================
    def define_environments_PORTS(self):
        self.m_env_name="PORTS"
        self.add_service(self.m_services,"POWER_SYNC","16XX0")
        self.add_service(self.m_services,"EXTERNAL_VAL_PORT","16XX1")
        
        self.add_service(self.m_services,"RKNET_DB","17XX0")
        self.add_service(self.m_services,"RKNET_DB_BACKUP","17XX1")
        
        self.add_service(self.m_services,"PFE_DB","17XX2")
        self.add_service(self.m_services,"PFE_DB_BACKUP","17XX3")

        self.add_service(self.m_services,"RATE_DB","17XX4")
        self.add_service(self.m_services,"RATE_DB_BACKUP","17XX5")

        self.add_service(self.m_services,"VAR_DB","17XX6")
        self.add_service(self.m_services,"VAR_DB_BACKUP","17XX7")

        self.add_service(self.m_services,"CUSTOM_DB","17XX8")
        self.add_service(self.m_services,"CUSTOM_DB_BACKUP","17XX9")
        
        self.add_service(self.m_services,"RKNET_DB_BACKUP","17XX1")
        
        self.add_service(self.m_services,"WEB_GUI","18XX0")
        
        self.add_service(self.m_services,"LOG_4_J","18XX1")
        self.add_service(self.m_services,"JMS","18XX2")
        self.add_service(self.m_services,"JBOSS_WS","18XX3")
        self.add_service(self.m_services,"JBOSS_NAMING","18XX4")
        self.add_service(self.m_services,"JBOSS_BOOTSTRAP","18XX5")
        self.add_service(self.m_services,"JBOSS_RMI","18XX6")        
        
#==================================================================
#
#==================================================================
    def define_environments_masks_2bit(self):
        self.m_env_name="SERVICES MASKS"
        self.add_service(self.m_services,"KGR32A_14060","01")
        self.add_service(self.m_services,"32L16_KGR32B_16030","02")                   
        self.add_service(self.m_services,"KGR36JT","19")                
        self.add_service(self.m_services,"KGR35S" ,"18")        
        self.add_service(self.m_services,"KGR35B" ,"10")
        self.add_service(self.m_services,"KGR36"  ,"12")    
        self.add_service(self.m_services,"KGR32"  ,"07")
        self.add_service(self.m_services,"KGR32C" ,"09")
        self.add_service(self.m_services,"fatih"  ,"45")
        self.add_service(self.m_services,"thor"   ,"08")
        #self.add_service(self.m_services,"KGR32A"  ,"07")
                    
#==================================================================
#
#==================================================================

    def define_environments_masks(self):
        self.m_env_name="SERVICES MASKS"
        self.add_service(self.m_services,"KGR32A","1X01X")                
        self.add_service(self.m_services,"KGR36JT","1X19X")                
        self.add_service(self.m_services,"KGR35S" ,"1X18X")        
        self.add_service(self.m_services,"KGR35B" ,"1X10X")
        self.add_service(self.m_services,"KGR36"  ,"1X12X")    
        self.add_service(self.m_services,"KGR32"  ,"1X00X")
        self.add_service(self.m_services,"KGR32"  ,"1X07X")
        self.add_service(self.m_services,"fatih"  ,"3X45X")
        self.add_service(self.m_services,"thor"   ,"1X08X")

#==================================================================
#
#==================================================================


    def define_environment_pegase(self):
    
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WebGui_Http","http://ptxsksup35:36080/kgr")
        self.add_service(self.m_services,"WEB_GUI_USER","admin")        
        self.add_service(self.m_services,"WEB_GUI_USER","reuters")
        
        self.add_service(self.m_services,"WEB_GUI_USER","iamhappy")        
        self.add_service(self.m_services,"WEB_GUI_USER","iamhappy")
        
        self.add_service(self.m_services,"DB_SERVER_NAME","DS_PEGASE")        
        self.add_service(self.m_services,"DB_SERVER_PORT","5590")        
        self.add_service(self.m_services,"DB_SERVER_HOST","ptxsksup34")
                        
        self.add_service(self.m_services,"DB_SERVER_USER","sa")        
        self.add_service(self.m_services,"DB_SERVER_PASSWORD","nocore")                
        

#==================================================================
#
#==================================================================

    def define_environment_get_passwords_sha_256(self):        
        self.add_service(self.m_services,"iamhappy",  "53b2e165b6a2bb595c6a14d4355b42c00b1a1d737f1ccb6714ff28e89863e2d4")
        self.add_service(self.m_services,"rknet",     "28554dc80e4eefaad67c428d9409dc3f2749834429fe89dc7969acf84de28cc7")
        self.add_service(self.m_services,"rknet12",   "48b1eb4612fb9cad55a2fb5780c70e03bf0b1fc319c5b05a87489d7c40b12a53")
        self.add_service(self.m_services,"kgr_owner", "3e93cfcce88f16f110d4afbfc66b7531c3afe78e7f5b1461577353e9c029b707")
        self.add_service(self.m_services,"nofuture", "4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")                    

#==================================================================
#
#==================================================================
    
    def define_environment_rembrandt(self):
    
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WEB_GUI_USER","admin")        
        self.add_service(self.m_services,"WEB_GUI_USER","rknet")
        self.add_service(self.m_services,"WebGui_Http","http://sunxsol10:29080/kgr")
        
        #DS_REMBRANDT
        #master tcp ether sunxsol10 4028
        #query tcp ether sunxsol10 4028
        #
        #DS_REMBRANDT_BACK
        #master tcp ether sunxsol10 4030
        #query tcp ether sunxsol10 4030
        


#==================================================================
#
#==================================================================

    def define_environment_ds50(self):
    
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WEB_GUI_USER","kplus")        
        self.add_service(self.m_services,"WEB_GUI_USER","kplusds50")                    
        self.add_service(self.m_services,"RUN_SEQUENCE_1","ptxsksup35 /ksup/programs/scripts $  DealManager pegase ds50")
        self.add_service(self.m_services,"RUN_SEQUENCE_2","ksup30; ksup30")                    
        self.add_service(self.m_services,"RUN_SEQUENCE_3","startkglagent30 pegase ds50")
        
#==================================================================
#
#==================================================================

    def define_environment_davinci(self):    
        self.add_service(self.m_services,"WebGui","")        
        self.add_service(self.m_services,"WebGui_Http","http://sunxsol10:59080/kgr")        
        self.add_service(self.m_services,"KNS_SERVER","rksup36@ptxsksup35 /rksup/log/davinci")


#==================================================================
#
#==================================================================


    def define_environment_thor(self):
    
        self.add_service(self.m_services,"WebGui","")
        
        self.add_service(self.m_services,"WebGui_Http","http://sunxsol10:19080/kgr")
        self.add_service(self.m_services,"WebGui_Http","http://ptxvaix06a:19080/kgr")
        
        self.add_service(self.m_services,"WS_HTTP","http://sunxsol10:19080/KGRWebServices")
        self.add_service(self.m_services,"WS_HTTP","http://ptxvaix06a:19080/KGRWebServices")
		
        
        self.add_service(self.m_services,"WEB_GUI_USER","admin")        
        self.add_service(self.m_services,"WEB_GUI_USER","rknet12")                    

        self.add_service(self.m_services,"WEB_GUI_USER_2","JT_T6_U1")        
        self.add_service(self.m_services,"WEB_GUI_USER_2","rknet14")                    
        
        self.add_service(self.m_services,"DB_PORT_COMPUTED_MASK_THOR","1X08X")
        self.add_service(self.m_services,"DB_PORT_COMPUTED_MASK_RKNET_DB","17XX0")
        self.add_service(self.m_services,"DB_PORT_COMPUTED_RKNET_DB","17080")

        self.add_service(self.m_services,"DB_SERVER_NAME","DS_THOR")        
        self.add_service(self.m_services,"DB_SERVER_PORT","4006")        
        self.add_service(self.m_services,"DB_SERVER_HOST","ptxsksup35")                
        
        self.add_service_2(self.m_services,"KNS","","") 
        self.add_service(self.m_services,"DB_SERVER_NAME","")        
        self.add_service(self.m_services,"DB_SERVER_PORT","")        
        self.add_service(self.m_services,"DB_SERVER_HOST","")                

        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network","")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network","")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network","")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","")        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","")
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network","")        
        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network","")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","")
        self.add_service(self.m_services,"ADAPTER.serverImport.network","")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","0")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        
        

#==================================================================
#
#==================================================================

    def define_environment_fritigern(self):
        self.add_service(self.m_services,"DESCRIPTION","for exercise copy of fatih")


#==================================================================
#
#==================================================================

    def define_environment_allaric(self):
        self.add_service(self.m_services,"DESCRIPTION","read only copy of fatih")
        

#==================================================================
#
#==================================================================

    def define_environment_fatih(self):
        self.add_service(self.m_services,"PORT_MASK","1X19X")    
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WebGui_Http","http://ptxsksup35:35450")
        self.add_service(self.m_services,"WebGuiKgrUser","kgr35")
        self.add_service(self.m_services,"WebGuiKgrPasswd","reuters")
        self.add_service(self.m_services,"WebGuiKgrEncryptedPasswd","234330834c41105ad5ed794fa036e085b40225c44f9228bb9e2692f427917605")
        
        self.add_service_2(self.m_services,"KNS","","") 
        self.add_service(self.m_services,"DB_SERVER_NAME","DS_FATIH")        
        self.add_service(self.m_services,"DB_SERVER_PORT","4300")        
        self.add_service(self.m_services,"DB_SERVER_HOST","ptxsksup35")                
        self.add_service(self.m_services,"KGR_DB_NAME"," rknet") 
        self.add_service(self.m_services,r"tibrvlisten -service 35454 -daemon tcp:35456 -network "";230.231.151.42"" "">"" ")
        self.add_service(self.m_services,"DB_SERVER_BACK_NAME","")        
        self.add_service(self.m_services,"DB_SERVER_BACK_PORT","")        
        self.add_service(self.m_services,"DB_SERVER_BACK_HOST","")
                        
        self.add_service(self.m_services,"DEALMANAGER_K35_USER","kplus")
        self.add_service(self.m_services,"DEALMANAGER_K35_PASSWORD","kplusk35")
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","tcp://ptxsksup35:35451")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","tcp:35456")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network",";230.231.151.42")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","tcp:35456")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network",";230.231.151.42")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","35453")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","35454")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","tcp:35456")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network",";230.231.151.42")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","MASTER_KREDITNET")        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","tcp:35456")
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network",";230.231.151.42")        
        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","35455")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","35458")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","tcp://ptxsksup35:35451")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network","")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","")
        self.add_service(self.m_services,"ADAPTER.serverImport.network","")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","0")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        
        
        self.add_service(self.m_services,"MRP_GUI_STARTING_POINT_KPLUS_K33","kgr.adapter.ws.url.K33=http://ptxsksup35:35496/KGRCanonicalService")
        self.add_service(self.m_services,"MRP_ADAPTER_WS_KPLUS_K33","kgr.adapter.ws.url=http://ptxsksup35:35496/KGRCanonicalService")

        #ADAPTERS
        self.add_service(self.m_services,"kgr.adapter.ws.url.DS50-VAR","http://ptxsksup35:35457/KGRCanonicalService")
        self.add_service(self.m_services,"kgr.adapter.ws.url.DS36","http://ptxsksup35:35470/KGRCanonicalService")
        self.add_service(self.m_services,"kgr.adapter.ws.url.K33","http://ptxsksup35:35496/KGRCanonicalService")
        
        self.add_service_adapter(self.m_services,"ADAPTER_50","kgr.logs.status.ws.url","http://ptxsksup35:35450//KGRWebServices/LogsAndStatusService")

        #WS Url of the Adapter
        self.add_service_adapter(self.m_services,"ADAPTER_50","kgr.adapter.ws.url","http://ptxsksup35:35457/KGRCanonicalService")
        
        
#==================================================================
#
#==================================================================

    def define_environment_kgr35a(self):
        self.add_service(self.m_services,"WebGui_Http","http://gdnsxsol01:18070")
        

#==================================================================
#
#==================================================================
        
    def define_environment_kgr36JT(self):
        self.add_service(self.m_services,"PORT_MASK","1X19X")    
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WebGui_Http","")
        self.add_service_2(self.m_services,"KNS","","") 
        self.add_service(self.m_services,"DB_SERVER_NAME","GDN_KGR36JT")        
        self.add_service(self.m_services,"DB_SERVER_PORT","17190")        
        self.add_service(self.m_services,"DB_SERVER_HOST","gdnssun23")                
        self.add_service(self.m_services,"DB_SERVER_USER","sa")                
        self.add_service(self.m_services,"DB_SERVER_PASSWD","nocore")                

        self.add_service(self.m_services,"DB_SERVER_BACK_NAME","GDN_KGR36JT_back")        
        self.add_service(self.m_services,"DB_SERVER_BACK_PORT","17191")        
        self.add_service(self.m_services,"DB_SERVER_BACK_HOST","")                
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network","")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network","")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network","")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","")        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","")
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network","")        
        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network","")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","")
        self.add_service(self.m_services,"ADAPTER.serverImport.network","")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","0")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        
        
        

#==================================================================
#
#==================================================================

    def define_environment_kgr36(self): 


        self.add_service(self.m_services,"PORT_MASK","1X12X")   
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WebGui_Http","")
        self.add_service_2(self.m_services,"KNS","","") 
        self.add_service(self.m_services,"DB_SERVER_NAME","GDN_KGR36")        
        self.add_service(self.m_services,"DB_SERVER_PORT","17120")        
        self.add_service(self.m_services,"DB_SERVER_HOST","gdnssun23")                
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network","")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network","")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network","")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","")        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","")
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network","")        
        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network","")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","")
        self.add_service(self.m_services,"ADAPTER.serverImport.network","")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","0")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        
        
        

#==================================================================
#
#==================================================================
    
    def define_environment_kgrJut(self):
        self.add_service(self.m_services,"WebGui","18180")
        self.add_service(self.m_services,"WebGui_Http","http://gdnssun23:18180/kgr/")

#==================================================================
#
#==================================================================

    def define_environment_kgr35MRP(self):    
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WebGui_Http","")
        self.add_service_2(self.m_services,"KNS","","") 
        self.add_service(self.m_services,"DB_SERVER_NAME","")        
        self.add_service(self.m_services,"DB_SERVER_PORT","")        
        self.add_service(self.m_services,"DB_SERVER_HOST","")                
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network","")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network","")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network","")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","")        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","")
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network","")        
        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network","")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","")
        self.add_service(self.m_services,"ADAPTER.serverImport.network","")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","0")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        
        


#==================================================================
#
#==================================================================

        
    def define_environment_kgr32c(self):
    
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WebGui_Http","http://gdnssun23:18090/kgr/")
        self.add_service_2(self.m_services,"KNS","","") 
        self.add_service(self.m_services,"DB_SERVER_NAME","")        
        self.add_service(self.m_services,"DB_SERVER_PORT","")        
        self.add_service(self.m_services,"DB_SERVER_HOST","")                

        self.add_service(self.m_services,"GUI_KGR_USER","kgr_owner")        
        self.add_service(self.m_services,"GUI_KGR_PASSWORD","nofuture")                
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network","")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network","")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network","")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","")        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","")
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network","")        
        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network","")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","")
        self.add_service(self.m_services,"ADAPTER.serverImport.network","")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","0")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        
        

#==================================================================
#
#==================================================================
                        
    def define_environment_kgr32a(self):
    
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WebGui_Http","http://gdnssun23:18010/kgr/")
        self.add_service_2(self.m_services,"KNS","","") 
        self.add_service(self.m_services,"DB_SERVER_NAME","")        
        self.add_service(self.m_services,"DB_SERVER_PORT","")        
        self.add_service(self.m_services,"DB_SERVER_HOST","")                
        self.add_service(self.m_services,"GUI_KGR_USER","kgr_owner")        
        self.add_service(self.m_services,"GUI_KGR_PASSWORD","nofuture")                
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network","")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network","")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network","")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","")        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","")
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network","")        
        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network","")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","")
        self.add_service(self.m_services,"ADAPTER.serverImport.network","")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","0")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        
        


#==================================================================
#
#==================================================================
        
    def define_environment_kgr35template(self):
    
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WebGui_Http","")
        self.add_service_2(self.m_services,"KNS","","") 
        self.add_service(self.m_services,"DB_SERVER_NAME","")        
        self.add_service(self.m_services,"DB_SERVER_PORT","")        
        self.add_service(self.m_services,"DB_SERVER_HOST","")                
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network","")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network","")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network","")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","")        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","")
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network","")        
        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network","")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","")
        self.add_service(self.m_services,"ADAPTER.serverImport.network","")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","0")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        
        
#==================================================================
#
#==================================================================

    def define_environment_kgr35(self):
    
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WebGui_Http","http://gdnssun23:18040/kgr")
        self.add_service(self.m_services,"WebGui_Http","http://sunxsol01:18040/kgr")
        self.add_service(self.m_services,"WebGui_Http","http://gdnsxsol01:18040/kgr")
        self.add_service(self.m_services,"WebGuiuser","kgr_owner")
        self.add_service(self.m_services,"WebGuipassword","nofuture")
        
        self.add_service_2(self.m_services,"KNS","","") 
        self.add_service(self.m_services,"DB_SERVER_NAME","KreditNet.Config.Server.*.WebServiceEnable: True")


        self.add_service(self.m_services,"DB_SERVER_NAME","")        
        self.add_service(self.m_services,"DB_SERVER_PORT","")        
        self.add_service(self.m_services,"DB_SERVER_HOST","")                
        
        self.add_service(self.m_services,"HTTP_ENCRYPTED_PASSWD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network","")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network","")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network","")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","")
                
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network","")
                        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","")
                
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network","")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","")
        self.add_service(self.m_services,"ADAPTER.serverImport.network","")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","0")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        

#==================================================================
#
#==================================================================

    def define_environment_kgr35s(self):
    
        self.add_service(self.m_services,"PORT_MASK","1X18X")
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WebGui_Http","http://gdnssun23:18180/kgr/")
        self.add_service_2(self.m_services,"KNS","","") 
        self.add_service(self.m_services,"DB_SERVER_NAME","GDN_KGR35S")        
        self.add_service(self.m_services,"DB_SERVER_PORT","17180")        
        self.add_service(self.m_services,"DB_SERVER_HOST","gdnssun23")                
        
        self.add_service(self.m_services,"DB_USER","sa")                
        self.add_service(self.m_services,"DB_PASSWORD","nocore")
        
        self.add_service(self.m_services,"GUI_USER","kgr_owner")                
        self.add_service(self.m_services,"GUI_PASSWORD","nofuture")                
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network",";230.255.123.118")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network","")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network","")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","")        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","")
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network","")        
        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network","")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","")
        self.add_service(self.m_services,"ADAPTER.serverImport.network","")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","0")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        

#==================================================================
#
#==================================================================


    def define_environment_davinci(self):
        """define_environment_davinci"""
        self.add_service(self.m_services,"WEB_GUI","http://sunxsol10:59080/kgr/")
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","rknet")


#==================================================================
#
#==================================================================

    def define_environment_kgr36e(self):
        """define_environment_kgr36c"""
        self.add_service(self.m_services,"WEB_GUI","http://gdnssun23:18220/kgr")
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        self.add_service(self.m_services,"DB_PORT","17200")
        
        #4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5
        #DB_KGR36C
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        self.add_service(self.m_services,"DB_PORT","17200")


        self.add_service(self.m_services,"WEB_GUI_USER","jt_2")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","reuters")

#==================================================================
#
#==================================================================
    def define_environment_kgr36g(self):
        """define_environment_kgr36g"""
        self.add_service(self.m_services,"WEB_GUI","http://gdnssun23:18220/kgr")
        self.add_service(self.m_services,"WEB_GUI","http://gdnssun23:18220/KGRWebServices")
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        self.add_service(self.m_services,"DB_PORT","17200")
        
        #4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5
        #DB_KGR36C
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        self.add_service(self.m_services,"DB_PORT","17200")


        self.add_service(self.m_services,"WEB_GUI_USER","jt_2")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","reuters")

#==================================================================
#
#==================================================================

    def define_environment_kgr36f(self):
        """define_environment_kgr36f"""
        self.add_service(self.m_services,"WEB_GUI","http://gdnssun23:18220/kgr")
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        self.add_service(self.m_services,"DB_PORT","17200")
        
        #4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5
        #DB_KGR36C
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        self.add_service(self.m_services,"DB_PORT","17200")


        self.add_service(self.m_services,"WEB_GUI_USER","jt_2")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","reuters")


#==================================================================
#
#==================================================================

    def define_environment_kgr36c(self):
        """define_environment_kgr36c"""
        self.add_service(self.m_services,"WEB_GUI","http://gdnssun23:18190/kgr")
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        self.add_service(self.m_services,"DB_PORT","17200")
        
        #4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5
        #DB_KGR36C
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        
        self.add_service(self.m_services,"WEB_GUI_USER","admin")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","4e1b74fa85f37d8ae2e93a7206af836478c5ad556c4b2c267401176ab0c7c8f5")
        self.add_service(self.m_services,"DB_PORT","17200")


        self.add_service(self.m_services,"WEB_GUI_USER","jt_2")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","reuters")
        
#==================================================================
#	kgr36
#==================================================================
    
    def define_environment_kgr36_pawel(self):
        """define_environment_kgr36_pawel"""
        self.add_service(self.m_services,"WEB_GUI","http://gdnssun23:18120/kgr")
        self.add_service(self.m_services,"WEB_GUI","http://gdnsxsol01:18120/kgr")
        self.add_service(self.m_services,"WEB_GUI_USER","kgr_owner")
        self.add_service(self.m_services,"WEB_GUI_PASSWORD","nofuture")
        
#==================================================================
#
#==================================================================


    def define_environment_versions(self):
		self.add_service(self.m_services,"KGR_VERSION_35A","35.3.04405")
		self.add_service(self.m_services,"KGR_VERSION_35B","35.3.04405")
		self.add_service(self.m_services,"KGR_VERSION_35","35.3.04111")

#==================================================================
#
#==================================================================

    def define_environment_kgr35b(self):
        self.add_service(self.m_services,"PORT_MASK","1X10X")
        self.add_service(self.m_services,"WebGui","")
        self.add_service(self.m_services,"WebGui_Http","http://gdnssun23:18100/kgr")
        self.add_service(self.m_services,"WebGui_Http","http://gdnsxsol01:18100/kgr")
        self.add_service(self.m_services,"WS_HTTP","http://gdnssun23:18100/KGRWebServices")
        self.add_service(self.m_services,"KGR_VERSION","35.3.04405")
        self.add_service_2(self.m_services,"KNS","","") 
        self.add_service(self.m_services,"DB_SERVER_NAME","")        
        self.add_service(self.m_services,"DB_SERVER_PORT","")        
        self.add_service(self.m_services,"DB_SERVER_HOST","")                
        
        self.add_service(self.m_services,"WebGui_User","kgr_owner")
        self.add_service(self.m_services,"WebGui_password","nofuture")
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network","230.255.123.110")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network","")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network","")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","")        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","")
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network","")        
        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network","")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","")
        self.add_service(self.m_services,"ADAPTER.serverImport.network","")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","0")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        
        
        
#18000
    def define_environment_kgr32(self):
    
        self.add_service(self.m_services,"WebGui","50000")
        self.add_service(self.m_services,"WebGui_Http","http://gdnssun23:18000/kgr")

#==================================================================
#
#==================================================================

    def define_environment_kgrSet(self):
    
        self.add_service(self.m_services,"WebGui","50000")
        self.add_service(self.m_services,"WebGui_Http","http://ptxslvsup01:50000/kgr")
        self.add_service_2(self.m_services,"KNS","","3.04505") 
        self.add_service(self.m_services,"DB_SERVER_NAME","LVSUP04")        
        self.add_service(self.m_services,"DB_SERVER_PORT","4000")        
        self.add_service(self.m_services,"DB_SERVER_HOST","ptxslvsup04")                
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","tcp://ptxslvsup01:50060")
        
        #CLIENT_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Daemon","tcp:50050")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Report.Transport.Network",";230.231.151.32")
        
        #CLIENT_TRADING
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Daemon","tcp:50050")        
        self.add_service(self.m_services,"KreditNet.Config.Client.*.Trading.Transport.Network",";230.231.151.32")
        
        #CLIENT_CLUSTER
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Report.Transport.Service","50020")        
        self.add_service(self.m_services,"KreditNet.Config.ClientCluster.*.Trading.Transport.Service","50030")
        
        #SERVER_REPORT
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Daemon","tcp:50050")    
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Report.Transport.Network",";230.231.151.32")
        #"TRDP","7500"
        #"PGM","7550"
        
        #SERVER_TRADING                
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.DefaultSourceShortName","MASTER_KREDITNET")        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Daemon","tcp:50050")
        self.add_service(self.m_services,"KreditNet.Config.Server.*.Trading.Transport.Network",";230.231.151.32")        
        
        self.add_service(self.m_services,"KreditNet.Config.ServerCluster.*.Transport.Service","50040")
        
        self.add_service(self.m_services,"KreditNet.Config.Server.*.SoapServerPort","50090")
        
        self.add_service(self.m_services,"KGL.JmsRvBridge.Jms.Connection.BrokerUrl","tcp://ptxslvsup01:50060")
        
        
        #ADAPTER
        
        self.add_service(self.m_services,"ADAPTER.serverDefault.service","50583")        
        self.add_service(self.m_services,"ADAPTER.serverDefault.network",";230.231.151.32")
        self.add_service(self.m_services,"ADAPTER.serverDefault.daemon","tcp:50050")        
        
        self.add_service(self.m_services,"ADAPTER.serverImport.service","50582")
        self.add_service(self.m_services,"ADAPTER.serverImport.network",";230.231.151.32")
        self.add_service(self.m_services,"ADAPTER.serverImport.daemon","tcp:50050")        
        
        #MESSAGE_GENERATOR
        
        
        self.add_service(self.m_services,"DEF_RVD_SERVICE","50583")        
        self.add_service(self.m_services,"DEF_RVD_NETWORK",";230.231.151.32")
        self.add_service(self.m_services,"DEF_RVD_DAEMON","tcp:50050")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT","KNETADAPTER.1.0.TRADING.DEALCHANGE.REQUEST")        
        self.add_service(self.m_services,"DEF_RVD_SUBJECT_REPLY ","KNETADAPTER.1.0.TRADING.DEALCHANGE.REPLY")
        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")        
        self.add_service(self.m_services,"","")
        self.add_service(self.m_services,"","")        


    def define_environment_kgr36a(self):    
        self.add_service(self.m_services,"WebGui","50000")
        self.add_service(self.m_services,"WebGui_Http","http://gdnsxsol01:18130/kgr")
      

    def define_environments(self):
		self.add_kgr_addr(self.m_services,"kgr35b","http://gdnsxsol01:18100/kgr")
		self.add_kgr_addr(self.m_services,"kgr35a","http://gdnsxsol01:18070/kgr")                    
        #self.add_service(self.m_services,"kgr36","http://gdnsxsol01:18120/kgr")        
        #self.add_kgr_addr(self.m_services,"kgr36a","http://gdnsxsol01:18130/kgr")

