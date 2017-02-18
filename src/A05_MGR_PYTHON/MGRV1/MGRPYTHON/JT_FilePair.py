#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

from JT_File import JT_File
from JT_Marks import JT_Marks
class JT_FilePair:

#==================================================================
#
#==================================================================        
    
    def __init__(self):
        self.m_log_file = JT_File()
        self.m_log_file_info = JT_File()
        self.m_log_file.m_file_marks = JT_Marks()
        self.m_log_file_info.m_file_marks = JT_Marks()
        self.m_log_file.m_file_marks = JT_Marks()
        self.m_log_file_info.m_file_marks = JT_Marks()

#==================================================================
#
#==================================================================        
        
    def set_marks(self, p_mark_start,p_mark_end):
        self.m_log_file.m_file_marks.m_mark_start = p_mark_start
        self.m_log_file.m_file_marks.m_mark_end = p_mark_end

#==================================================================
#
#==================================================================        
        