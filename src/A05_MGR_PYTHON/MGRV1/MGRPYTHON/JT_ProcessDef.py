#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

from JT_Logger import JT_Logger
from JT_StaticLogger import JT_StaticLogger
from JT_Printer import JT_Printer 
from JT_ServerDef import JT_ServerDef 
#==================================================================
#
#==================================================================
    
class JT_ProcessDef :
    def __init__(self):
        self.m_pid = ""
        self.m_server_name ="NN"
        self.m_State="0"
        self.m_kgr_instance = ""
        self.m_User = ""
        self.m_Counters = 0    
        self.m_LineOfProcess = ""
        self.m_referenced_process_id=""
        self.m_referenced_process_name=""
        self.m_referenced_processess = []
        self.m_server = JT_ServerDef()
        self.m_process_log_line_fullfilled = 0
#==================================================================
#
#==================================================================
        
    def __cmp__(self,other):         
        cc =  cmp(self.m_kgr_instance,other.m_kgr_instance) 
        if cc != 0:
            return cc            
        cc1 = cmp(self.m_server_name,other.m_server_name)
        return cc1
    
#==================================================================
#
#==================================================================

    def print_process_short_line(self):
        try:
    
            
            if JT_Printer.DEF_PRINT_SHORT_LINE_TXT()    == 1:
                JT_Logger.print_output("")
                try:
                    line_server_def = "\t" +  self.m_server.get_srv_info(self.m_kgr_instance )
                    JT_Logger.print_output(line_server_def)
                except:
                    JT_Logger.print_exception("exception_server_def")
                    
                try:
                    l_ref_processess = self.get_referenced_processess()
                    ll = self.get_line("\t" 
                        + "[" + self.m_kgr_instance + "]" 
                        + "[" + self.m_server_name + "]" 
                        + "[" +  " " + self.m_User + "]" 
                        + "[" + str(self.m_pid) + "]" 
                        + "[line_where_find:" + str(self.m_process_log_line_fullfilled) + "]"                        
                        #+ "[" + self.m_referenced_process_name + "]"
                        + "[" + l_ref_processess + "]")
                                        
                    JT_Logger.print_output(ll)
                except:
                    JT_Logger.print_exception("exception_server_def")

                try:                                    
                    if JT_Printer().get_exec_print_line()  == 1:    
                        JT_Logger.print_output( "[line:" + self.m_LineOfProcess + "]" )
                except:
                    JT_Logger.print_exception("exception_server_def")
                    
        except:
            JT_Logger.print_exception("exception")
            return "error_in[print_process_long_line]"
        
#==================================================================
#
#==================================================================
    def print_process_long_line(self):
        try:            
            if JT_Printer.DEF_PRINT_LONG_LINE_TXT()    == 1:         
                JT_Logger.print_output("")       
                try:
                    line_server_def = "\t" +  self.m_server.get_srv_info(self.m_kgr_instance )
                    JT_Logger.print_output(line_server_def)
                except:
                    JT_Logger.print_exception("exception_server_def")
                    
                try:
                    l_ref_processess = self.get_referenced_processess()
                    ll = self.get_line("\t" 
                        + "[KgrInstance:" + self.m_kgr_instance + "]" 
                        + "[ServerName:" + self.m_server_name + "]" 
                        + "[user_from_ps:" +  " " + self.m_User + "]" 
                        + "[pid_from_ps:" + str(self.m_pid) + "]" 
                        + "[line_where_find:" + str(self.m_process_log_line_fullfilled) + "]"

                        #+ "[m_referenced_process_name:" + self.m_referenced_process_name + "]"
                        + "[" + l_ref_processess + "]")
                        
        
                    JT_Logger.print_output( ll )
                except:
                    JT_Logger.print_exception("exception_server_def")
                
                try:
                    if JT_Printer().get_exec_print_line()  == 1:
                        JT_Logger.print_output( "[line:" + self.m_LineOfProcess + "]" )
                except:
                    JT_Logger.print_exception("exception_server_def")
                    
        except:
            JT_Logger.print_exception("exception")
            return "error_in[print_process_long_line]"
             
#==================================================================
#
#==================================================================
                
    def print_process(self):
        try:
            self.print_process_short_line()
            self.print_process_long_line()
        except:
            JT_Logger.print_exception("exception")
            return "error_in[get_referenced_process]"
                
        
#==================================================================
#
#==================================================================
    def get_line(self,pp):
        return pp
#==================================================================
#
#==================================================================
    def get_referenced_processess(self):
        try:        
            ll=""
            for dd_proc in self.m_referenced_processess:
                ll = ll + "=>[" + dd_proc.get_referenced_process() + "]"
            return ll
        except:
            JT_Logger.print_exception("exception")
            return "error_in[get_referenced_processess]"
    
#==================================================================
#
#==================================================================

    def get_referenced_process(self):
        try:
            ll = self.get_line(
                "[" + self.m_kgr_instance + "]" 
                + "[" + self.m_server_name + "]" 
                + "[" + str(self.m_pid) + "]") 
            return ll
        except:
            JT_Logger.print_exception("exception")
            return "error_in[get_referenced_process]"
#==================================================================
#
#==================================================================
    
    def print_process_to_log(self):
        try:
            try:
                line_server_def = "\t" +  self.m_server.get_srv_info(self.m_kgr_instance )
                JT_StaticLogger.exetute_logging(line_server_def)
            except:
                JT_Logger.print_exception("exception_server_def")
                
            try:
                line = self.m_LineOfProcess
                l_ref_processess =self.get_referenced_processess()
                ll = self.get_line("\t"
                    + "[KgrInstance:" + self.m_kgr_instance + "]" 
                    + "[ServerName:" + self.m_server_name + "]" 
                    + "[user_from_ps:" +   self.m_User + "]" 
                    + "[pid_from_ps:" + str(self.m_pid) + "]" 
                    + "[line_where_find:" + str(self.m_process_log_line_fullfilled) + "]"
                    #+ "[m_referenced_process_name:" + self.m_referenced_process_name + "]"
                    + "[line:" + line + "]"
                    + "[" + l_ref_processess + "]")
                    
                JT_StaticLogger.exetute_logging( ll )
            except:
                JT_Logger.print_exception("exception_server_def")
            
        except:            
            JT_Logger.print_exception("exception")
            
