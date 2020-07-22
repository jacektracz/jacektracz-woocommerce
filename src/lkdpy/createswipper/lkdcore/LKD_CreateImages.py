import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *

from LKD_CreateFilesDatabase import *
from LKD_CatItem import *
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py


class LKD_CreateImages:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CreateImages::__init__::in::")
                self.m_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\ep_300x200"
                self.m_dst = "services_s3"
                self.m_root_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\ep_300x200"
                self.m_root_dst = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\ep_300x200_all"
                self.m_test_mode = 0
                #self.m_override_mode = False
                self.m_override_mode = True
                self.m_ds = "/"
                self.xx_dbg("LKD_CreateImages::__init__::out::")

        def exec_images(self):
                self.xx_dbg("LKD_CreateImages::exec_images::in::")
                dd_ll = self.get_files_recur(self.m_root_src,0,self.m_root_dst)
                p_dest = self.m_root_dst

                ii = 0
                for dd_ii in dd_ll:
                        self.xx_dbg("LKD_CreateImages::image::" + dd_ii.src_javafile_full_path)
                        src_fpath = dd_ii.src_javafile_full_path
                        dest_fpath = p_dest + "\\" + "img_" + str(ii) + ".jpg"                        
                        self.xx_dbg("LKD_CreateImages::image::s_dest" + dest_fpath)
                        shutil.copy(src_fpath, dest_fpath)
                        ii = ii + 1

                self.xx_dbg("LKD_CreateImages::exec_images::out::")

        def get_generic_cats_items(self, dd):
                ddh = LKD_CreateFilesDatabase()
                return ddh.get_generic_cats_items("")

        def get_files_recur(self, psrc_path_project, pcatid, pdest_java_flat_dir_path):
                fjavafiles = []
                for root,d_names,f_names in os.walk(psrc_path_project):
	                for f in f_names:
                                dd = LKD_CatItem(pcatid, psrc_path_project)
                                dd.catid = pcatid
                                dd.src_project_relative_path = psrc_path_project
                                dd.src_javafile_full_path = os.path.join(root, f)
                                dd.src_javafile_name = f
                                dd.dest_java_flat_dir_path = pdest_java_flat_dir_path
		                fjavafiles.append(dd)

                return fjavafiles

                

        def get_item(self, id,title):
                dd = LKD_CatItem(id,title)
                return dd

        def xx_dbg(self, tt):
                "" ""
                print ( tt )

        def xx_print( self, tt ):
                "" ""
                print ( tt )       
