import sys
import os

from .. DBG_AdapterBase import *

class DBG_DirsHelper(DBG_AdapterBase):
        def __init__(self):
                DBG_AdapterBase.__init__(self,"DBG_CmsDispatcher")  
                self.m_print_steps = 1
                self.m_conf_file = "15"
                self.m_out_file_name = "15"

                                                
        def get_list_dir(self, p_path):                
                for root, dirs, files in os.walk(p_path, topdown=True):
                        for name in dirs:
                            print(os.path.join(root, name))
                            
                            
        def get_child_dirs(self, p_path):
                ll = []
                for filename in os.listdir(p_path):
                    ll.append(filename)                    
                return ll
        
        def get_child_files(self, p_path):
                ll = []
                for filename in os.listdir(p_path):
                    ll.append(filename)        
                return ll
            