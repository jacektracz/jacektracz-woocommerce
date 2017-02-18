#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

from JT_File import JT_File
from JT_FilePair import JT_FilePair
from JT_Logger import JT_Logger
from JT_Logger import JT_StaticLogger

from datetime import datetime
#==================================================================
#
#==================================================================
        
class JT_FilesPairs:
#==================================================================
#
#==================================================================
    
    def __init__(self):
        self.m_files = []

#==================================================================
#
#==================================================================
    
    def get_date_for_file(self):
        dt = datetime.now()
        s_log_file = JT_StaticLogger.get_line(             
            "_Y_" + str(dt.year)    
            + "_MTH_" +  str( dt.month )
            + "_D_" + str(dt.day) 
            + "_H_" + str(dt.hour) 
            + "_M_" + str(dt.minute) 
            + "_S_" + str(dt.second) )
        
        return s_log_file
    
#==================================================================
#
#==================================================================

    def add_log_file_ex(self,p_dir,p_kgr,p_file,p_ext):
        JT_Logger.trace_method("[METHOD_IN][add_log_file_ex].[v1]")
        dd = JT_File()
        JT_Logger.trace_method("[METHOD_IN][add_log_file_ex].[v2]")
        s_ff = p_dir + "/" + p_kgr + "/" + p_file + "." + p_ext
        dd.m_full_path = s_ff
        
        JT_Logger.trace_method("[METHOD_IN][add_log_file_ex].[v3]" 
                               + "[s_ff:" + s_ff + "]")
        
        JT_Logger.trace_method("[METHOD_IN][add_log_file_ex]" 
                               + "[m_full_path:" + dd.m_full_path + "]")
        
        
        s_date = ".bckp." + self.get_date_for_file()
        s_ff_b = p_dir + "/" + p_kgr + "/" + p_file + "." + p_ext + s_date
        JT_Logger.trace_method("[METHOD_IN][add_log_file_ex]" + "[s_ff_b:" + s_ff_b + "]")
        
        
        dd.m_full_bck_path = s_ff_b
        
        dd_fp = JT_FilePair()
        dd_fp.m_log_file = dd
        
        dd_info = JT_File()
        dd_info.m_full_path = s_ff = p_dir + "/" + p_kgr + "/logs_info/" + p_file + "." + p_ext        
        dd_fp.m_log_file_info = dd_info
        JT_Logger.trace_method("[METHOD_IN][add_log_file_ex]" 
                               + "[m_full_bck_path:" + dd.m_full_bck_path + "]")
        
        self.m_files.append( dd_fp )
