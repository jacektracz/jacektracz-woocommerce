
from JT_FIND_Service import JT_FIND_Service
class JT_FIND_Services:
    def __init__(self):
        self.m_logger = []
        self.m_services = []
    
#==================================================================
#
#==================================================================

    def add_logger(self,plogger):
        self.m_logger.append(plogger)
#==================================================================
#
#==================================================================
    
    def logger_print(self,line):
        self.m_logger[0].trace_hard(line)
#==================================================================
#
#==================================================================
        
    def define_services(self):
        self.add_service_o(self.m_services,self.get_service("WebGui","18180"))
#==================================================================
#
#==================================================================

    def add_service_o(self, plist,p_dd):
        plist.append(p_dd)
#==================================================================
#
#==================================================================
        
    def add_service(self, plist, pport, pname):
        plist.append(self.get_service(pport,pname))
#==================================================================
#
#==================================================================
        
    def get_service(self,pport,pname):
        ds = JT_FIND_Service()
        ds.m_Port = pport
        ds.m_ServiceName=pname
        return ds
#==================================================================
#
#==================================================================

    def print_services(self):
        for dd_services in self.m_services:
            self.logger_print(dd_services.m_Port + " " + dd_services.m_ServiceName)
