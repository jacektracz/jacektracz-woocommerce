import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *
from LKD_CatItem import *

#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py
# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py perform-src-files
# select "cats.append(self.get_item(",id,",","\"",title,"\"","))" from joo2_categories where parent_id = 11178

class LKD_CreateScrFilesData:
        def __init__(self):                                
                self.m_root = ""
                self.m_cats = []
                self.m_cat_id = 0
                self.m_selector = 0

        def get_src_root_child_cats( self ):
                return self.m_cats

        def get_src_root_dir_path( self ):
                return self.m_root

        def get_src_root_cat_id( self ):
                return self.m_cat_id                

        def get_src_root_selector( self ):
                return self.m_selector