from datetime import datetime
from JT_Logger import JT_Logger

class JT_FIND_Timestamp:
    
    #==================================================================
    #
    #==================================================================
        
    def create_stamp(self):
        JT_Logger.trace_hard_level_16 ( '[create_stamp]')
        dt = datetime.now()
        
        s_stamp = self.get_str( "ST_" 
                                + str(dt.year) + "_" 
                                + str(dt.month) + "_" 
                                + str(dt.day) + "_" 
                                + str(dt.hour) + "_" 
                                + str(dt.minute) + "_" 
                                + str(dt.second))
        
        JT_Logger.trace_hard_level_16 ( '[create_stamp]' + "[" + s_stamp + "]")
        return s_stamp
    
    def get_str(self,p_ss):
        return p_ss