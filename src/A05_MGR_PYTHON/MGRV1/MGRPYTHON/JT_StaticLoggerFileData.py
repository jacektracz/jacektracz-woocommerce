#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

class JT_StaticLoggerFileData:
    
#==================================================================
#
#==================================================================
    
    def __init__(self):
        self.m_log_file = None
        self.m_log_file_opened = 0;
        self.m_use_logger = 0;

    def copy_shallow(self,dd):
        self = dd
        
    def copy_deep(self,dd):
        self.m_log_file = dd.m_log_file
        self.m_log_file_opened = dd.m_log_file_opened;
        self.m_use_logger = dd.m_use_logger;
        
        