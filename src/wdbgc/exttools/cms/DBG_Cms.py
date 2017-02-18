import sys
import os

class DBG_Cms:
                                
        def get_list_dir(self, p_path):
                dirs = os.listdir(p_path)
                
#c:/python27/python     D:\lkd\komodo\w2_2\src\w2\wdbgc\exttools\cms\DBG_Cms.py

if __name__ == '__main__':
    DBG_Cms().get_list_dir("D:/lkd/komodo/w2_2/dat/arch/a05_core_docs/linux")
            