import sys
from JT_Logger import JT_Logger
class JT_FIND_ARGV:
#==================================================================
#
#==================================================================

    @staticmethod    
    def print_argv(p_ii):
        JT_Logger.print_output( "[METHOD_IN][print_argv]")                
        
        
        for i_av in sys.argv:
            JT_Logger.print_output(str(i_av))        

        JT_Logger.print_output( "[METHOD_OUT][print_argv]")
         
#==================================================================
#
#==================================================================
    
    @staticmethod    
    def get_argv_pos(p_ii):
        JT_Logger.print_output( "[METHOD_IN]" 
                                       + "[get_argv_pos]" 
                                       + "[ii:" + str( p_ii ) + "]")
                
        s_val = "not_set"
        if (len(sys.argv)) > p_ii:
            s_val = sys.argv[p_ii]        

        JT_Logger.print_output( "[METHOD_OUT]" 
                                       + "[get_argv_pos]"
                                       + "[s_debug:" + str( s_val ) + "]"
                                       )
        return s_val
#==================================================================
#
#==================================================================

    @staticmethod    
    def check_argv_pos(p_ii, p_ll):
        JT_Logger.print_output( "[METHOD_IN]" 
                                       + "[check_argv_pos]" 
                                       + "[ii:" + str( p_ii ) + "]")
        is_ok = 0        
        s_arg = JT_FIND_ARGV.get_argv_pos_def ( p_ii,"not_set")
        
        for i_vv in p_ll:
            if(s_arg == i_vv):
                is_ok = 1
                break
            
        s_args_debug = ""
        for s_arg_debug in p_ll:
            s_args_debug = s_args_debug + "[" + s_arg_debug + "]"
            
        if (is_ok == 0):
            JT_Logger.print_output( "[ARGUMENT_NOT_ALLOVED_ON_POSITION]")
            JT_Logger.print_output( "[p_ii:" + str( p_ii ) + "]")                                       
            JT_Logger.print_output( "[is_ok:" + str( is_ok ) + "]")
            JT_Logger.print_output( "[argument:" + str( s_arg ) + "]")
            JT_Logger.print_output( "[arguments:" + str( s_args_debug ) + "]")                        
            sys.exit("ARGUMENT_NOT_ALLOVED_ON_POSITION")
    
        JT_Logger.print_output( "[METHOD_OUT]" 
                                       + "[check_argv_pos]")
        JT_Logger.print_output( "[p_ii:" + str( p_ii ) + "]")                                       
        JT_Logger.print_output( "[is_ok:" + str( is_ok ) + "]")
        JT_Logger.print_output( "[s_arg:" + str( s_arg ) + "]")
        JT_Logger.print_output( "[arguments:" + str( s_args_debug ) + "]")
        return is_ok
    
#==================================================================
#
#==================================================================

    @staticmethod    
    def print_argv_pos(p_ii, p_ll):
        JT_Logger.print_output( "")
        JT_Logger.print_output( "[METHOD_IN]" 
                                       + "[print_argv_pos]" 
                                       + "[ii:" + str( p_ii ) + "]")
            
        s_args_debug = ""
        for s_arg_debug in p_ll:
            s_args_debug = s_args_debug + "[" + s_arg_debug + "]"
            
        
        JT_Logger.print_output( "[METHOD_OUT][ARGUMENTS_ALLOVED_ON_POSITION]")                                            
        JT_Logger.print_output( "[arguments:" + str( s_args_debug ) + "]")                        
            
    
#==================================================================
#
#==================================================================
    
    @staticmethod
    def get_argv_pos_def(p_ii,p_def):
        JT_Logger.print_output( "[METHOD_IN]" 
                                       + "[get_argv_pos_def]" 
                                       + "[ii:" + str( p_ii ) + "]"
                                       + "[ii:" + str( p_def ) + "]")
                
        s_debug = JT_FIND_ARGV.get_argv_pos(p_ii)
        if(s_debug =="not_set"):
            s_debug = p_def

        JT_Logger.print_output( "[METHOD_OUT]" 
                                       + "[get_argv_pos_def]"
                                       + "[s_debug:" + str( s_debug ) + "]"
                                       )
        return s_debug
