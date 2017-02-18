#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================


from JT_ProcessessDef import JT_ProcessesDef
from JT_ArgsParams import JT_ArgParams
from JT_ArgParam import JT_ArgParam    
from JT_Logger import JT_Logger
#==================================================================
#
#==================================================================

class JT_ServerDef:
    def __init__(self):
        self.m_server_name = ""
        self.m_ProcessName = ""        
        self.m_ProcessNameInPsLine = 1
        self.m_ProcessNameInArgs = 0
        self.m_KgrInstanceNameInPs = 0
        self.m_KgrInstanceNameInPargs =0
        self.m_KgrInstanceNameInPargse =0
        
        self.m_Processes = JT_ProcessesDef()
        self.m_ParamsPsLine = JT_ArgParams()
        self.m_ParamsPargsLine = JT_ArgParams()
        self.m_ParamsPargseLine = JT_ArgParams()

#==================================================================
#
#==================================================================


    def set_srv_data(self,dd,p1,p2,p3,p4,p5):
        self.m_ProcessNameInPsLine = p1
        self.m_ProcessNameInArgs = p2
        self.m_KgrInstanceNameInPs = p3
        self.m_KgrInstanceNameInPargs = p4
        self.m_KgrInstanceNameInPargse = p5
#==================================================================
#
#==================================================================

    def get_srv_info(self,p_kgr_name):
        try:
            ll = ""
            ll = ll + "[Server:" +  "("  + str(self.m_server_name ) + ")" + p_kgr_name + "]"
            ll = ll + "[Process:" +  "("  + str(self.m_ProcessName ) + ")" + p_kgr_name + "]"
            ll = ll + "[Process_in_Ps:" +  "("  + str(self.m_ProcessNameInPsLine ) + ")" + str(self.m_ProcessName ) + "]"
            ll = ll + "[Process_in_Args:" +  "("  + str(self.m_ProcessNameInArgs ) + ")" + str(self.m_ProcessName ) + "]"
            ll = ll + "[Kgr_in_Ps:" +  "(" + str(self.m_KgrInstanceNameInPs ) + ")" + p_kgr_name + "]"
            ll = ll + "[Kgr_in_Pargs:"  + "("  + str(self.m_KgrInstanceNameInPargs )  + ")" + p_kgr_name + "]"
            ll = ll + "[Kgr_in_Pargse:" +  "("  + str(self.m_KgrInstanceNameInPargse ) + ")" + p_kgr_name + "]"
                
            ll_1 = self.get_arg_info( self.m_ParamsPsLine)
            ll = ll + "[params in ps:" + ll_1 + "]"
            ll_1 = self.get_arg_info( self.m_ParamsPargsLine)
            ll = ll + "[params in pargs:" +  ll_1 + "]"
            ll_1 = self.get_arg_info( self.m_ParamsPargseLine)
            ll = ll + "[params in pargse:" +  ll_1 + "]"
                           
            return ll
        except:
            JT_Logger.print_exception("exception_server_def")
            return "exception_in_get_srv_info"
        
#==================================================================
#
#==================================================================

    def get_params_ps_line_info(self):
        try:
            ll = ""
            ll = self.get_arg_info( self.m_ParamsPsLine)
            return ll
        except:
            JT_Logger.print_exception("get_params_ps_line_info")
            return "exception_in_get_params_ps_line_info"
#==================================================================
#
#==================================================================
        
    def get_params_pargs_line_info(self):
        try:
            ll = ""
            ll = self.get_arg_info( self.m_ParamsPargsLine)
            return ll
        except:
            JT_Logger.print_exception("get_params_ps_line_info")
            return "exception_in_get_params_ps_line_info"
#==================================================================
#
#==================================================================

    def get_params_pargse_line_info(self):
        try:
            ll = ""
            ll = self.get_arg_info( self.m_ParamsPargseLine)
            return ll
        except:
            JT_Logger.print_exception("get_params_ps_line_info")
            return "exception_in_get_params_ps_line_info"
        
#==================================================================
#
#==================================================================
        
    def get_arg_info(self,p_ArgParams):
        try:
            ll = ""
            dd = JT_ArgParams()
            dd = p_ArgParams
            if(len(dd.m_Params) > 0):
                for dd_ap_ii in dd.m_Params :
                    dd_ap = JT_ArgParam()
                    dd_ap = dd_ap_ii
                    ll_ii = "[" + dd_ap.m_ParamName + "]"
                    ll = ll + ll_ii
            return ll
        except:
            JT_Logger.print_exception("exception_server_def")
            return "exception_in_err_get_arg_info"
