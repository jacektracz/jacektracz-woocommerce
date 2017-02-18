
from JT_FIND_Headers import JT_FIND_Headers
from JT_Logger import JT_Logger
from JT_FIND_Replacement import JT_FIND_Replacement
#==================================================================
#
#==================================================================
class JT_FIND_Words:
    def __init__(self):
        self.m_words = []

#==================================================================
#p_dd: JT_FIND_Replacement
#==================================================================
        
    def add_word(self, p_dd):
        self.m_words.append( p_dd )
        
#==================================================================
#
#==================================================================
        
    def add_word_s(self, p_ss):
        dd_ll = JT_FIND_Replacement()
        dd_ll.m_word_new = p_ss
        dd_ll.m_word_old = p_ss
        self.m_words.append( dd_ll )
#==================================================================
#
#==================================================================
        
    def add_words_from_strins(self
                  ,p_ll):
                
        for ii_ss in p_ll :
            self.add_word_s(ii_ss)
#==================================================================
#
#==================================================================
            
    @staticmethod
    def get_words_from_strins(p_ll):
        dd_out = JT_FIND_Words()        
        for ii_ss in p_ll :
            dd_out.add_word_s(ii_ss)
        return dd_out
#==================================================================
#
#==================================================================

class JT_FIND_WordsList:
    
    def __init__(self):
        self.m_words_lists = []

        
#==================================================================
#
#==================================================================
        
    #p_dd: JT_FIND_Words
    def add_words(self
                  ,p_dd):
        self.m_words_lists.append( p_dd )

        
#==================================================================
#
#==================================================================
            
class JT_FIND_Replacements:
    
#==================================================================
#
#==================================================================
    
    def __init__(self):
        self.m_repl_words = []
        self.m_kgr = "kgr36JT"
        self.m_kgr_version = "36"
        self.m_kgr_level = "36.01.010"
#==================================================================
#
#==================================================================
        
    def init_replacement_words_from_active_config_kgr(self
                                                      ,s_kgr
                                                      ,s_version
                                                      ,s_level):
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                        + "[init_replacement_words_from_active_config_kgr]" )

        self.m_kgr = s_kgr
        self.m_kgr_version = s_version
        self.m_kgr_level = s_level
        self.add_repl_sentences_kgr_config("RMDS_NETWORK_SERVICE_PORT","NOT_SET_RMDS_NETWORK_SERVICE_PORT")
        self.add_repl_sentences_kgr_config("RMDS_NETWORK_NETWORK","NOT_SET_RMDS_NETWORK_NETWORK")
        self.add_repl_sentences_kgr_config("RMDS_NETWORK_ENABLEENTITLEMENTS","NOT_SET_RMDS_NETWORK_ENABLEENTITLEMENTS")
        self.add_repl_sentences_kgr_config("RMDS_DEFAULT_BEGINDATE","NOT_SET_RMDS_DEFAULT_BEGINDATE")
        self.add_repl_sentences_kgr_config("RMDS_SOURCENAME","NOT_SET_RMDS_SOURCENAME")
        self.add_repl_sentences_kgr_config("RMDS_WORKDIRECTORY","NOT_SET_RMDS_WORKDIRECTORY")
        self.add_repl_sentences_kgr_config("RMDS_DEFAULT_ENDDATE","NOT_SET_RMDS_DEFAULT_ENDDATE")
        self.add_repl_sentences_kgr_config("RMDS_OUTPUTDIRECTORY","NOT_SET_RMDS_OUTPUTDIRECTORY")        
        self.add_repl_sentences_kgr_config("RMDS_NETWORK_SERVICENAME","NOT_SET_RMDS_NETWORK_SERVICENAME")
        self.add_repl_sentences_kgr_config("RMDS_NETWORK_TRANSLATIONFILE","NOT_SET_RMDS_NETWORK_TRANSLATIONFILE")
        self.add_repl_sentences_kgr_config("RMDS_NETWORK_INFRA","NOT_SET_RMDS_NETWORK_INFRA")
        self.add_repl_sentences_kgr_config("RMDS_NETWORK_DAEMON","NOT_SET_RMDS_NETWORK_DAEMON")
        
        #self.add_repl_sentences_kgr_config("KGS_GUI_WS_URL", "http://gdnssun23:18190/KGRWebServices/")
        self.add_repl_sentences_kgr_config("KNET_LICENSE_TIMEOUT","25")
        self.add_repl_sentences_kgr_config("KIS_WRITEBUFFERSIZE","0")
        self.add_repl_sentences_kgr_config("KIS_MAXMESSAGEWAIT","5")
        self.add_repl_sentences_kgr_config("KIS_MAXMESSAGESENT","0")
        self.add_repl_sentences_kgr_config("KIS_CACHETIMEOUT","0")
        self.add_repl_sentences_kgr_config("ADAPTER_SSL_TRUST_STORE_PATH","/rksup/log/" + self.m_kgr + "/kreditnetdata/gui/app_config/server.truststore")        
        self.add_repl_sentences_kgr_config("ADAPTER_SSL_KEY_STORE_PASSWD","rksup36")
        self.add_repl_sentences_kgr_config("ADAPTER_SSL_KEY_STORE_PATH","/rksup/log/" + self.m_kgr + "/kreditnetdata/gui/app_config/server.keystore")
        self.add_repl_sentences_kgr_config("APPSERVER_PREPORT","319")
        self.add_repl_sentences_kgr_config("RTM_TMP_DIR","/rksup/log/" + self.m_kgr + "/kreditnetdata/tmp/jettytmp")
        self.add_repl_sentences_kgr_config("TMP_ROOT_DIR","/rksup/log/" + self.m_kgr + "/kreditnetdata/tmp") 
        self.add_repl_sentences_kgr_config("KREDITNETDATA","/rksup/log/" + self.m_kgr + "/kreditnetdata/")
        self.add_repl_sentences_kgr_config("TIBEMS_DIR", "/qakplus/qa_obj/ems/4.4.2/sun4sol/ems/")
        self.add_repl_sentences_kgr_config("JBOSS_SERVER_BASE_DIR", "/rksup/config/" + self.m_kgr + "/jboss/server")
        self.add_repl_sentences_kgr_config("WEBAPP_CONFIG_DIR", "/rksup/config/" + self.m_kgr + "/")
        self.add_repl_sentences_kgr_config("WEBAPP_DICTIONARIES_DIR", "/srv/dist/kgr/" + self.m_kgr_version + "/" + self.m_kgr_level + "/gui/dictionaries/")
        self.add_repl_sentences_kgr_config("WEBAPP_CONFIG_DIR", "/rksup/config/" + self.m_kgr + "/")
        self.add_repl_sentences_kgr_config("WEBAPP_EAR_DIR", "/srv/dist/kgr/" + self.m_kgr_version + "/" + self.m_kgr_level + "/gui/ear/")
        self.add_repl_sentences_kgr_config("WEBAPP_XML_DIR", "/srv/dist/kgr/" + self.m_kgr_version + "/" + self.m_kgr_level + "/gui/xml")
        self.add_repl_sentences_kgr_config("WEBAPP_LIBS_DIR", "/srv/dist/kgr/" + self.m_kgr_version + "/" + self.m_kgr_level + "/gui/libs/")
        self.add_repl_sentences_kgr_config("APPSERVER_NAME", "kgr")
        self.add_repl_sentences_kgr_config("SRV_LOG_DIR", "/rksup/log/" + self.m_kgr + "/")
        self.add_repl_sentences_kgr_config("TIBRV_DIR", "/qakplus/qa_alpha/rms/rv/7.x/sun4sol/")                
        #END KgrRun.conf        
        self.add_repl_sentences_kgr_config("JMS_PORT", "18192")
        self.add_repl_sentences_kgr_config("EMPTY", "@Unset")
        self.add_repl_sentences_kgr_config("J2EE_SERVER_TYPE", "jboss")
        self.add_repl_sentences_kgr_config("APPSERVER_HOSTNAME", "gdnssun23")
        self.add_repl_sentences_kgr_config("APPSERVER_PORT", "18190")
        self.add_repl_sentences_kgr_config("APPSERVER_HTTPSPORT", "18194")
        self.add_repl_sentences_kgr_config("WEBAPP_CUSTOM_ENABLE", "true")
        self.add_repl_sentences_kgr_config("WEBAPP_SOURCE_LIST", "MASTER_KREDITNET,KONDOR30")
        self.add_repl_sentences_kgr_config("WEB_LOG_DIR", "/rksup/log/" + self.m_kgr + "/")
        self.add_repl_sentences_kgr_config("LOG4J_LEVEL", "DEBUG")
        self.add_repl_sentences_kgr_config("LOG4J_PORT", "18191")
        self.add_repl_sentences_kgr_config("KETAT_FOLDER", "/rksup/config/" + self.m_kgr + "/jboss/server/kgr/tmp/ketat")        
        self.add_repl_sentences_kgr_config("BUILDER_FOLDER", "/rksup/config/" + self.m_kgr + "/jboss/server/kgr/tmp/builder")
        self.add_repl_sentences_kgr_config("COMMON_GUI_SERVER_WORK_DIR", "/rksup/log/" + self.m_kgr + "/gui_work/")
        self.add_repl_sentences_kgr_config("BEA_HOME_DIR", "/opt/bea")
        self.add_repl_sentences_kgr_config("WL_HOME_DIR", "/opt/bea/wlserver8.1")
        self.add_repl_sentences_kgr_config("DOMAIN_NAME", "kgr")
        
        self.add_repl_sentences_kgr_config("WL_DOMAIN_DIR", "/rksup/config/" + self.m_kgr + "/weblogic10/")
        #self.add_repl_sentences_kgr_config("WL_DOMAIN_DIR", "/srv/dist/kgr/" + self.m_kgr_version + "/" + self.m_kgr_level + "/3rdparty/J2EE/weblogic")
        self.add_repl_sentences_kgr_config("WL_TEMP_DIR", "/rksup/config/" + self.m_kgr + "/tmp")
        self.add_repl_sentences_kgr_config("APPSERVER_ADMIN_USER", "weblogic")
        self.add_repl_sentences_kgr_config("APPSERVER_ADMIN_PASSWD", "weblogic")
        self.add_repl_sentences_kgr_config("WAS_INSTALL_ROOT", "/opt/websphere/AppServer")
        self.add_repl_sentences_kgr_config("WAS_NODE_NAME", "localhostNode01")
        self.add_repl_sentences_kgr_config("WAS_ADMIN_USER", "admin")
        self.add_repl_sentences_kgr_config("WAS_ADMIN_PASSWD", "admin")
        self.add_repl_sentences_kgr_config("WAS_SERVER_NAME", "server1")
        self.add_repl_sentences_kgr_config("WAS_PROFILE_NAME", "AppSrv01")
        self.add_repl_sentences_kgr_config("KGR_DS_NAME", "GDN_KGR36JT")
        self.add_repl_sentences_kgr_config("KGRIQ_SERVER_NAME", "@Unset")
        self.add_repl_sentences_kgr_config("KGR_DB_HOST", "gdnssun23")
        self.add_repl_sentences_kgr_config("KGR_DB_PORT", "17190")
        self.add_repl_sentences_kgr_config("KGR_DB_NAME", "kgr36")
        self.add_repl_sentences_kgr_config("KGRIQ_DB_NAME", "kgriq")
        self.add_repl_sentences_kgr_config("KGR_DB_USER_NAME", "kgr_owner")
        self.add_repl_sentences_kgr_config("KGRIQ_DB_USER_NAME", "rknet35")
        self.add_repl_sentences_kgr_config("KGR_DB_USER_PWD", "nofuture")
        self.add_repl_sentences_kgr_config("KGRIQ_DB_USER_PWD", "rknet35")        
        self.add_repl_sentences_kgr_config("PFE_CACHE_DIRECTORY", "/rksup/config/" + self.m_kgr + "/pfecache/")
        self.add_repl_sentences_kgr_config("VAR_DS_NAME", "GDN_KGR36JT")
        self.add_repl_sentences_kgr_config("VAR_DB_HOST", "gdnssun23")
        self.add_repl_sentences_kgr_config("VAR_DB_PORT", "17190")
        self.add_repl_sentences_kgr_config("VAR_DB_NAME", "kgr36_var")
        self.add_repl_sentences_kgr_config("VAR_DB_USER_NAME", "kgr_owner")
        self.add_repl_sentences_kgr_config("VAR_DB_USER_PWD", "nofuture")
        self.add_repl_sentences_kgr_config("CUSTOM_DB_HOST", "gdnssun23")
        self.add_repl_sentences_kgr_config("CUSTOM_DB_PORT", "17190")
        self.add_repl_sentences_kgr_config("CUSTOM_DB_NAME", "kgr36_custom")
        self.add_repl_sentences_kgr_config("CUSTOM_DB_USER_NAME", "kgr_owner")
        self.add_repl_sentences_kgr_config("CUSTOM_DB_USER_PWD", "nofuture")
        self.add_repl_sentences_kgr_config("KPLUSHOME3", "/ksup/2.6/latest")
        self.add_repl_sentences_kgr_config("EXTERNAL_SOURCE", "KONDOR30")
        self.add_repl_sentences_kgr_config("KONDOR_CONFIG_FOLDER", "/ksup/2.6/latest/entities/Standalone/config")
        self.add_repl_sentences_kgr_config("KONDOR_LOGIN", "kplus")
        self.add_repl_sentences_kgr_config("KONDOR_PASSWORD", "kplus")
        self.add_repl_sentences_kgr_config("DSDRIVER_DIR", "DSDRIVER_DIR")
        self.add_repl_sentences_kgr_config("RDV_REPORT_PORT", "19192")
        self.add_repl_sentences_kgr_config("RDV_TRADE_PORT", "19191")
        self.add_repl_sentences_kgr_config("BASEL2_ENABLE", "True")
        self.add_repl_sentences_kgr_config("MAX_THREADS_NB", "20")
        self.add_repl_sentences_kgr_config("MEMCACHED_ENABLE", "False")
        self.add_repl_sentences_kgr_config("MEMCACHED_CONNECTION_INFO", "localhost:11211")
        self.add_repl_sentences_kgr_config("RDV_COMM_PORT", "19193")
        self.add_repl_sentences_kgr_config("TASK_THREADS_NB", "4")
        self.add_repl_sentences_kgr_config("IQ_DATABASE_ENABLE", "false")
        self.add_repl_sentences_kgr_config("PNL_DS_NAME", "GDN_KGR36JT")
        self.add_repl_sentences_kgr_config("PNL_DB_NAME", "kgr36_var")        
        self.add_repl_sentences_kgr_config("TIBEMS_CONFIG_DIR", "/rksup/config/" + self.m_kgr + "/")
        self.add_repl_sentences_kgr_config("JAVA_HOME", "/nfs/vol5/support/programs/sun4sol/java/")
        self.add_repl_sentences_kgr_config("RDV_DAEMON", "tcp:19190")
        self.add_repl_sentences_kgr_config("RDV_NETWORK", ";230.255.123.219")
        self.add_repl_sentences_kgr_config("JMS_HOSTNAME", "gdnssun23")        
        self.add_repl_sentences_kgr_config("SCENARIO_DIRECTORY", "/rksup/log/" + self.m_kgr + "/scenarios/")
        self.add_repl_sentences_kgr_config("RATE_IMPORT_DIR", "/rksup/log/" + self.m_kgr + "/rate/")
        self.add_repl_sentences_kgr_config("PV_IMPORT_DIR", "/rksup/log/" + self.m_kgr + "/var/")
        self.add_repl_sentences_kgr_config("PFE_DS_NAME", "GDN_KGR36JT")
        self.add_repl_sentences_kgr_config("PFE_DB_NAME", "kgr36_pfe")
        self.add_repl_sentences_kgr_config("RATE_DS_NAME", "GDN_KGR36JT")
        self.add_repl_sentences_kgr_config("RATE_DB_NAME", "kgr36_rate")
        self.add_repl_sentences_kgr_config("JBOSS_TEMP_DIR", "/rksup/config/" + self.m_kgr + "/jboss/server/kgr/tmp")
        self.add_repl_sentences_kgr_config("JBOSS_HOME", "/rksup/config/" + self.m_kgr + "/jboss")
        self.add_repl_sentences_kgr_config("JBOSS_SERVER_BASE_DIR", "/rksup/config/" + self.m_kgr + "/jboss/server")
        self.add_repl_sentences_kgr_config("CSV_LOCATION", "@Unset",)
        self.add_repl_sentences_kgr_config("PNL_AUTO_REPLICATION", "False")
        self.add_repl_sentences_kgr_config("CSV_NB_MAX_ROW", "1000000")
        self.add_repl_sentences_kgr_config("SQL_TRANSACTION_SPLIT_NB_ELEMENTS", "0")
        self.add_repl_sentences_kgr_config("PROXY_SERVER_NAME", "gdnssun23")
        self.add_repl_sentences_kgr_config("WS_SERVER_PORT", "18190")
        self.add_repl_sentences_kgr_config("WS_PATH", "/KGRWebServices")
        self.add_repl_sentences_kgr_config("WS_SERVER_HOSTNAME", "gdnssun23")
        self.add_repl_sentences_kgr_config("WEBAPP_CLIENT_LIB_DIR", "/srv/dist/kgr/" + self.m_kgr_version + "/" + self.m_kgr_level + "/gui/client_libs")
        self.add_repl_sentences_kgr_config("IMPORTSERVER_PATH", "/rksup/log/" + self.m_kgr + "/var/")
        self.add_repl_sentences_kgr_config("FS_RISKENGINE_SCRIPT", "/srv/dist/kgr/" + self.m_kgr_version + "/" + self.m_kgr_level + "/etc/startValuationEngine")
        self.add_repl_sentences_kgr_config("FS_FILES_PATH", "/rksup/log/" + self.m_kgr + "/fs/")
        self.add_repl_sentences_kgr_config("FS_ARCHIVE_PATH", "/rksup/log/" + self.m_kgr + "/archive/")
        self.add_repl_sentences_kgr_config("FS_SERVICE_HOSTNAME", "gdnssun23")
        self.add_repl_sentences_kgr_config("FS_SERVICE_PORT", "16198")
        self.add_repl_sentences_kgr_config("IQ_MODE_FOR_KVS", "ASE_ONLY")
        self.add_repl_sentences_kgr_config("KGS_LOG_LEVEL", "Info")
        self.add_repl_sentences_kgr_config("KGS_LOG_FILE", "/rksup/log/" + self.m_kgr + "//(PROGRAM).log")
        self.add_repl_sentences_kgr_config("KGS_KNS_WS_URL", "http://gdnssun23:16199")
        self.add_repl_sentences_kgr_config("KGS_GUI_WS_URL", "http://gdnssun23:18190/KGRWebServices/")
        self.add_repl_sentences_kgr_config("KGS_KGR_LOGIN", "kgr_owner")
        self.add_repl_sentences_kgr_config("KGS_KGR_PASSWORD", "nofuture")
        
        self.add_repl_sentences_kgr_config("KGS_KONDOR_WS_URL", "http://gdnssun23:18190/KGRWebServices/")
        self.add_repl_sentences_kgr_config("KGS_KONDOR_LOCATOR_WSDL", "/ksup/2.6/latest/common/wsdl/locator.wsdl")
        self.add_repl_sentences_kgr_config("KGS_EXTERNAL_SOURCE", "EXTERNAL_SOURCE")
        self.add_repl_sentences_kgr_config("KGS_KONDOR_LOGIN", "kplus")
        self.add_repl_sentences_kgr_config("KGS_KONDOR_PASSWORD", "kplus")
        self.add_repl_sentences_kgr_config("KGS_TRADEKAST_SERVER_HOSTNAME", "gdnssun23")
        self.add_repl_sentences_kgr_config("KGS_TRADEKAST_RDV_SERVICE", "@Unset")
        self.add_repl_sentences_kgr_config("KGS_TRADEKAST_RDV_NETWORK", "@Unset")
        self.add_repl_sentences_kgr_config("KGS_TRADEKAST_RDV_DAEMON", "@Unset")
        self.add_repl_sentences_kgr_config("KGS_TRADEKAST_CODIFIER", "KGR_KGS")
        self.add_repl_sentences_kgr_config("KGS_TRADEKAST_CONN_MODE", "m_jboss_install_dest_localfs")
        self.add_repl_sentences_kgr_config("KGS_TRADEKAST_TCP_PORT", "tradekast")
        self.add_repl_sentences_kgr_config("KGS_DATA_HANDLED", "NeverCheckUserCode;Folders;Portfolios;Branches;OTAssignConfig;RisKatcherConfig;ConfigCurvesAssign;")
        self.add_repl_sentences_kgr_config("INTERFACES_DIR", "/rksup/log/" + self.m_kgr + "/")
        self.add_repl_sentences_kgr_config("LOCAL_HOSTNAME", "gdnssun23")
        self.add_repl_sentences_kgr_config("MASTER_KREDITNET_OFFICE", "AMERICAN")
        self.add_repl_sentences_kgr_config("USE_DEFAULT_PROFILE", "YES")
        self.add_repl_sentences_kgr_config("DEFAULT_PROFILE", "PROFI-ADMIN")
        self.add_repl_sentences_kgr_config("USE_DEFAULT_OFFICE", "YES")
        self.add_repl_sentences_kgr_config("DEFAULT_OFFICE", "OFFIC-ADMIN")
        self.add_repl_sentences_kgr_config("FS_ADAPTER_HOSTNAME", "gdnssun23")
        self.add_repl_sentences_kgr_config("FS_ADAPTER_PORT", "16199")
        self.add_repl_sentences_kgr_config("KRMS_TIMESERIES_XSD", "/srv/dist/kgr/" + self.m_kgr_version + "/" + self.m_kgr_level + "/interface/rate/dataSchemas/TimeSeriesImport.xsd")
        self.add_repl_sentences_kgr_config("SOAP_SERVER_ENABLE", "True")
        self.add_repl_sentences_kgr_config("KGR_SOAP_PORT", "16199")
        self.add_repl_sentences_kgr_config("KGS_KONDOR_DM_SOAP_PORT", "16762:16762|16764")
        self.add_repl_sentences_kgr_config("KGS_KONDOR_DM_SERVER_HOSTNAME", "@Unset")
        self.add_repl_sentences_kgr_config("POWERSYNC_SERVICE", "16190")
        self.add_repl_sentences_kgr_config("DB_MAX_CONNECTION", "50")
        self.add_repl_sentences_kgr_config("DB_MIN_CONNECTION", "1")
        self.add_repl_sentences_kgr_config("MAX_USER_NB", "10")
        self.add_repl_sentences_kgr_config("MAX_PROCS_NB", "18")
        self.add_repl_sentences_kgr_config("RKNET_DBGROUP_NAME", "public")
        self.add_repl_sentences_kgr_config("KGRIQ_PROXY_DBGROUP_NAME", "@Unset")
        self.add_repl_sentences_kgr_config("KGRIQ_DBGROUP_NAME", "@Unset")
        self.add_repl_sentences_kgr_config("KGRIQ_PROXY_PASSWD", "@Unset")
        self.add_repl_sentences_kgr_config("KGRIQ_REMOTE_PASSWD", "@Unset")
        self.add_repl_sentences_kgr_config("PFE_DB_USER_PWD", "nofuture")
        self.add_repl_sentences_kgr_config("PFE_DB_USER_NAME", "kgr_owner")
        self.add_repl_sentences_kgr_config("SCRIPT_AFTER_SKIP", "Y")
        self.add_repl_sentences_kgr_config("SCRIPT_BEFORE_SKIP", "Y")
        self.add_repl_sentences_kgr_config("SCRIPT_AFTER", "@Unset")
        self.add_repl_sentences_kgr_config("SCRIPT_BEFORE", "@Unset")
        self.add_repl_sentences_kgr_config("KGRIQ_PROXY_USER_NAME", "KGRIQ_PROXY_USER_NAME")
        self.add_repl_sentences_kgr_config("KGRIQ_REMOTE_USER_NAME", "KGRIQ_REMOTE_USER_NAME")
        self.add_repl_sentences_kgr_config("VAR_SOURCE", "KONDOR30")
        self.add_repl_sentences_kgr_config("BASE_CURRENCY", "EUR")
        self.add_repl_sentences_kgr_config("RDV_ADAPTER_PUBLISH_SERVICE_PORT", "20193")
        self.add_repl_sentences_kgr_config("RDV_ADAPTER_SUBSCRIBE_SERVICE_PORT", "20193")
        self.add_repl_sentences_kgr_config("RDV_ADAPTER_LOGIN", "rknet")
        self.add_repl_sentences_kgr_config("RDV_IMPORT_SUBSCRIBE_SERVICE_PORT", "20192")
        
        
        
        #dod
        self.add_repl_sentences_kgr_config("RDV_BIN_PATH", "/qakplus/qa_alpha/rms/rv/7.x/sun4sol/bin")
        self.add_repl_sentences_kgr_config("RDV_LIB_PATH", "/qakplus/qa_alpha/rms/rv/7.x/sun4sol/bin")
        self.add_repl_sentences_kgr_config("", "")
        self.add_repl_sentences_kgr_config("", "")
        self.add_repl_sentences_kgr_config("", "")
        
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                        + "[init_replacement_words_from_active_config_kgr]" )
                
    #==================================================================
    #
    #==================================================================

    def add_repl_sentences_kgr_config(self,p_old,p_new):
        
        dd = JT_FIND_Replacement()
        if(p_old != p_new):
            dd.m_word_new = p_new
            dd.m_word_old = "$V(" + p_old + ")"
            if(dd.m_word_new == "@Unset"):
                dd.m_word_new = ""
            if(dd.m_word_new == "EMPTY"):
                dd.m_word_new = ""                
        else:
            JT_Logger.print_output("[add_repl_sentences_kgr_config][VARIABLE_NOT_SET:" + "$V(" + p_old + ")")
            dd.m_word_new = "$V(" + p_old + ")"
            dd.m_word_old = "$V(" + p_old + ")"
                            
        self.m_repl_words.append(dd)

    #==================================================================
    #
    #==================================================================

    def add_repl_sentences(self,p_old,p_new):
        dd = JT_FIND_Replacement()
        dd.m_word_new = p_new
        dd.m_word_old = p_old
        self.m_repl_words.append(dd)
        
    #==================================================================
    #
    #==================================================================
        
    def build_words_by_mask_xx_3xx(self
                                   ,p_mask_port_xx_old
                                   ,p_mask_port_xx_new
                                   ,p_mask_port_kgr_old
                                   ,p_mask_port_kgr_new):
        
        JT_Logger.trace_hard_level_16 ( '[METHOD_IN][build_words_by_mask_xx_3xx]')

        self.add_repl_sentences("KREDITNETDB","KREDITNETDB")
                        
        self.add_repl_sentences("L7_patchall","L7_patchall")    
        #if(self.m_fast_return==1 ):
        #    return
        
        for ii in self.m_for:
            JT_FIND_Headers().print_finding_header("FINDING [16" + p_mask_port_xx_old + ii + "]")
            self.add_repl_sentences("16" + p_mask_port_xx_old + ii,"16" + p_mask_port_xx_new + ii)                
        
        for ii in self.m_for:
            JT_FIND_Headers().print_finding_header("FINDING [17" + p_mask_port_xx_old + ii + "]")        
            self.add_repl_sentences("17" + p_mask_port_xx_old + ii,"17" + p_mask_port_xx_new + ii)
                
        
        for ii in self.m_for:
            JT_FIND_Headers().print_finding_header("FINDING [18" + p_mask_port_xx_old + ii + "]")                    
            self.add_repl_sentences("18" + p_mask_port_xx_old + ii,"18" + p_mask_port_xx_new + ii)                        
        
        for ii in self.m_for:
            JT_FIND_Headers().print_finding_header("FINDING [19" + p_mask_port_xx_old + ii + "]")                
            self.add_repl_sentences("19" + p_mask_port_xx_old + ii,"19" + p_mask_port_xx_new + ii)        

        JT_FIND_Headers().print_finding_header("FINDING [5583]")
        
        self.add_repl_sentences("5583","5583")
        
        
        JT_FIND_Headers().print_finding_header("FINDING [5582]")
        
        self.add_repl_sentences("5582","5582")
        
        JT_FIND_Headers().print_finding_header("FINDING [42073]")
                
        
        self.add_repl_sentences("42073","18" + p_mask_port_xx_new + "9")
        
        JT_FIND_Headers().print_finding_header("FINDING [kgr3" + p_mask_port_kgr_old + "]")
        
        self.add_repl_sentences("kgr3" + p_mask_port_kgr_old,"kgr3" + p_mask_port_kgr_new)        
        
        JT_FIND_Headers().print_finding_header("FINDING [230.255.123.11" + p_mask_port_xx_old + "]")
        
        self.add_repl_sentences("230.255.123.11" + p_mask_port_xx_old,"230.255.123.11" + p_mask_port_xx_new)
        
        JT_FIND_Headers().print_finding_header("FINDING [GDN_KGR3"+ str.upper(p_mask_port_kgr_old) + "]")
        
        self.add_repl_sentences("GDN_KGR3"+ str.upper(p_mask_port_kgr_old),"GDN_KGR3" + str.upper(p_mask_port_kgr_new))
        
        JT_FIND_Headers().print_finding_header("FINDING [GDN_kgr3" + str.upper(p_mask_port_kgr_new) + "]")
        
        self.add_repl_sentences("GDN_kgr3"+ str.upper(p_mask_port_kgr_old),"GDN_KGR3" + str.upper(p_mask_port_kgr_new))        
        
        JT_Logger.trace_hard_level_16 ( "[METHOD_OUT]" 
                                        + "[replace_generic_from_to_port_by_mask_xx_35x_2]")

#==================================================================
#
#==================================================================


    def build_words_db_port(self
                                   ,p_mask_port_xx_old
                                   ,p_mask_port_xx_new
                                   ,p_mask_port_kgr_old
                                   ,p_mask_port_kgr_new):
        
        JT_Logger.trace_hard_level_16 ( '[METHOD_IN][build_words_by_mask_xx_3xx]')

        self.add_repl_sentences("KREDITNETDB","KREDITNETDB")
                        
        self.add_repl_sentences("L7_patchall","L7_patchall")    

#==================================================================
#
#==================================================================


#$KREDITNETHOME=/srv/dist/kgr/" + self.m_kgr_version + "/" + self.m_kgr_level + "/
#$KPLUSHOME3=/ksup/2.6/latest
#JBOSS_SERVER_BASE_DIR
#BEA_HOME_DIR
#JBOSS_SERVER_BASE_DIR
#JBOSS_SERVER_BASE_DIR=/rksup/config/kgr35/jboss/server

#KgrRun.conf
        
