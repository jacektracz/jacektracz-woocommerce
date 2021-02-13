import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *

from LKD_CreateFilesDatabase import *
from LKD_CatItem import *
from LKD_MdFilesUtils import *
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py
# cd C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\ep_300x200_all_digital
#

class LKD_CreateImages:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CreateImages::__init__::in::")
                self.m_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\ep_300x200_all_digital"
                self.m_dst = "services_s3"
                self.m_root_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\ep_300x200_all_digital"
                self.m_root_dst = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\ep_300x200_all_digital_seq"
                self.m_test_mode = 0
                #self.m_override_mode = False
                self.m_override_mode = True
                self.m_ds = "/"
                self.xx_dbg("LKD_CreateImages::__init__::out::")

        def get_sclass(self):
                return "LKD_CreateImages"

        def get_dir_root_img_src_digital(self,ep_300x200_all_digital_seq):
                dir_path = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\" + ep_300x200_all_digital_seq
                return dir_path

        def create_sequential_ids(self):
                self.xx_dbg("LKD_CreateImages::create_sequential_ids::in::")
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

                self.xx_dbg("LKD_CreateImages::create_sequential_ids::out::")

        def get_generic_cats_items(self, dd):
                ddh = LKD_CreateFilesDatabase()
                return ddh.get_generic_cats_items("")

        def get_files_recur(self, psrc_path_project, pcatid, pdest_java_flat_dir_path):
		sfun = self.get_sclass() + "::get_files_recur::"
		self.xx_dbg( sfun + "start")

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

                self.xx_dbg( sfun + "end")
                return fjavafiles

                
        def get_root_for_groups( self, dd_active_cat_id ,dd_file_idx)	:

		sfun = self.get_sclass() + "::get_file_content_by_cat_id_groups::"
		self.xx_dbg( sfun + "start")
                srv_handler = LKD_MdFilesUtils("")
                dd_out = srv_handler.get_root_for_groups(  dd_active_cat_id , dd_file_idx)
                return dd_out

		self.xx_dbg( sfun + "end")
		return dd_file

        def move_digital_images_to_md(
                self
                , max_img_id_source_bucket
                , cat_id_start
                , cat_id_end):
		sfun = self.get_sclass() + "::move_digital_images_to_md::"
		self.xx_dbg( sfun + "start")

                
                ep_300x200_all_digital_seq = "ep_300x200_all_digital_seq"
                

                self.move_digital_images_to_md_impl(
                        max_img_id_source_bucket
                        ,ep_300x200_all_digital_seq
                        ,cat_id_start
                        , cat_id_end)

                self.xx_dbg( sfun + "end")

        def move_digital_images_to_md_impl(
                self
                , max_img_id_source_bucket
                , ep_300x200_all_digital_seq
                , cat_id_start
                , cat_id_end
                ):

		sfun = self.get_sclass() + "::move_digital_images_to_md_impl::"
		self.xx_dbg( sfun + "start")
                self.xx_dbg( sfun + "max_img_id_source_bucket:" + str(max_img_id_source_bucket))
                self.xx_dbg( sfun + "cat_id_start:" + str(cat_id_start))
                self.xx_dbg( sfun + "ep_300x200_all_digital_seq:" + ep_300x200_all_digital_seq)

                
                for ii in range (cat_id_start, cat_id_end, 1):
                        self.move_digital_image_to_md(
                                cat_id_start
                                , ii
                                , max_img_id_source_bucket
                                , ep_300x200_all_digital_seq)

                self.xx_dbg( sfun + "end")

        def move_digital_image_to_md(
                self
                , cat_id_start
                , cat_id
                , max_img_id_source_bucket
                , ep_300x200_all_digital_seq):

		sfun = self.get_sclass() + "::move_digital_image_to_md::"
		self.xx_dbg( sfun + "start")

                cat_id_img   = int((cat_id - cat_id_start )) % int(max_img_id_source_bucket)

                self.xx_dbg( sfun + "cat_id_img:" + str(cat_id_img))

                img_file = "img_" + str(cat_id_img) + ".jpg"
                img_file_dest = "img_300_x_200.png"
                src_path = self.get_dir_root_img_src_digital(
                        ep_300x200_all_digital_seq) + "\\" + img_file
                        
                dest_path = self.get_root_for_groups(cat_id,"0") + "\\content_idx_0\\imgs\\" + img_file_dest
                self.copy_file(src_path,dest_path)
                self.xx_dbg( sfun + "end")

        def copy_file(self, src_fpath,dest_fpath):
		sfun = self.get_sclass() + "::copy_file::"
		self.xx_dbg( sfun + "start")
                self.xx_dbg( sfun + "src_fpath:"  + src_fpath)
                self.xx_dbg( sfun + "dest_fpath:"  + dest_fpath)

                shutil.copy(src_fpath, dest_fpath)
                self.xx_dbg( sfun + "end")

        def get_item(self, id,title):
                dd = LKD_CatItem(id,title)
                return dd

        def xx_dbg(self, tt):
                "" ""
                print ( tt )

        def xx_print( self, tt ):
                "" ""
                print ( tt )       
