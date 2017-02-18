#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================
from JT_Marks import JT_Marks
class JT_File:
    
    def __init__(self):
        """__init_"""
        
        self.m_file_marks = JT_Marks()
        self.m_full_path = ""
        self.m_full_bck_path = ""
        self.m_dir = ""
        self.m_kgr = ""
        self.m_file = ""
        self.aa = "1"

#==================================================================
#
#==================================================================        
        
    def get_marks(self):
            
        return self.m_file_marks
#==================================================================
#
#==================================================================        

    def set_marks(self,p_dd):
        self.m_file_marks = p_dd
    
#==================================================================
#
#==================================================================        
