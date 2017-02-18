from JT_Logger import JT_Logger

class JT_FIND_Headers:
    def trace_header(self,ss):
        JT_Logger.trace_hard_level_16 ( 'find_basename')            
        JT_Logger.trace_hard_level_16 ( '/*==================================================================*/')
        JT_Logger.trace_hard_level_16 ( '/*')            
        JT_Logger.trace_hard_level_16 ( '/*                            ' + ss)            
        JT_Logger.trace_hard_level_16 ( '/*')            
        JT_Logger.trace_hard_level_16 ( '/*==================================================================*/')

    def print_finding_header_path(self,p_str_header):
        """print_finding_header_path"""        
        JT_Logger.print_output("\t/*=========================================================================/")
        JT_Logger.print_output("\t/*")
        JT_Logger.print_output("\t/*")
        JT_Logger.print_output("\t/*" + p_str_header + "            ")
        JT_Logger.print_output("\t/*")
        JT_Logger.print_output("\t/*")
        JT_Logger.print_output("\t/*=========================================================================/")

    #=============================================================
    #
    #                                    PRINT_HEADER PORT
    #
    #=============================================================

    def print_finding_header_ext(self,p_str_header):
        """print_finding_header_ext"""        
        JT_Logger.print_output("\t\t/*=========================================================================/")
        JT_Logger.print_output("\t\t/*")
        JT_Logger.print_output("\t\t/*" + p_str_header + "            ")
        JT_Logger.print_output("\t\t/*")
        JT_Logger.print_output("\t\t/*=========================================================================/")
    #======================================================================================================
    #
    #                                    PRINT_HEADER MASK
    #
    #======================================================================================================

    def print_finding_header_short(self,p_str_header):
        """print_finding_header_ext"""        
        JT_Logger.print_output("/*=========================================================================/")
        JT_Logger.print_output("/*" + p_str_header + "            ")
        JT_Logger.print_output("/*=========================================================================/")

    #======================================================================================================
    #
    #                                    PRINT_HEADER MASK
    #
    #======================================================================================================

    def print_finding_header(self,p_str_header):
        """print_finding_header"""
        JT_Logger.print_output("/*=========================================================================/")
        JT_Logger.print_output("/*")
        JT_Logger.print_output("/*")
        JT_Logger.print_output("/*")
        JT_Logger.print_output("/*" + p_str_header + "            ")
        JT_Logger.print_output("/*")
        JT_Logger.print_output("/*")
        JT_Logger.print_output("/*")            
        JT_Logger.print_output("/*=========================================================================/")
