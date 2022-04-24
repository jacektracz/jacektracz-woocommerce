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
# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py create-sequential-ids

# 
# C:\lkd\ht\apps_portal\lkduni\app-4\src\modules\mod_ep_articles\content_cats\content_markdown\content_by_groups\cat__8000\cat__000\cat__00\cat__8000\content_idx_0\imgs_seq_scr\
#
#

class LKD_CreateImages:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CreateImages::__init__::in::")
                #self.m_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\ep_300x200_all_digital"
                #self.m_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\300x200_white"
                self.m_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_articles\\content_cats\\content_markdown\\content_by_groups\\cat__8000\\cat__000\\cat__00\\cat__8000\\content_idx_0\\imgs\\300x200_white"
                self.m_dst = "services_s3"
                # self.m_root_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\ep_300x200_all_digital"
                #self.m_root_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\300x200_white"
                self.m_root_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_articles\\content_cats\\content_markdown\\content_by_groups\\cat__8000\\cat__000\\cat__00\\cat__8000\\content_idx_0\\imgs\\300x200_white"
                #self.m_root_dst = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\ep_300x200_all_digital_seq"
                #self.m_root_dst = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\300x200_white_seq"
                self.m_root_dst = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_articles\\content_cats\\content_markdown\\content_by_groups\\cat__8000\\cat__000\\cat__00\\cat__8000\\content_idx_0\\imgs\\300x200_white_seq"
                self.m_test_mode = 0
                #self.m_override_mode = False
                self.m_override_mode = True
                self.m_root_sequential_ids_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_articles\\content_cats\\content_markdown\\content_by_groups\\cat__8000\\cat__000\\cat__00\\cat__8000\\content_idx_0\\imgs_seq_scr\\"
                self.m_root_sequential_ids_dst = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_articles\\content_cats\\content_markdown\\content_by_groups\\cat__8000\\cat__000\\cat__00\\cat__8000\\content_idx_0\\imgs_seq_dst\\"
                self.m_ds = "/"
                self.xx_dbg("LKD_CreateImages::__init__::out::")

        def move_images_for_ctx(self):
                root_dir ="C:\\lkd\\ht\\apps_ctx\\1\\"
                root_catid = 15883
                self.move_images_for_child_directories(root_dir, root_catid)

        def move_images_for_child_directories(self, proot_dir, p_catid,pstartidx):
                s_method = "LKD_CreateImages::move_images_for_child_directories"
                self.xx_dbg(s_method + "::in::proot_dir:" + proot_dir)
                self.xx_dbg(s_method + "::in::root_catid:" + str(p_catid))
                self.xx_dbg(s_method + "::in::pstartidx:" + str(pstartidx))

                pcatid = int(p_catid)
                ii = 0
                for x1 in os.listdir(proot_dir):                        
                        p2 = proot_dir + "/" + x1
                        self.xx_dbg(s_method + "::in::p2:" + p2)
                        if os.path.isdir(p2): 
                                self.xx_dbg(s_method + "::id::" + str(pcatid + ii) + "::dir::" + str(p2))
                                self.xx_dbg(s_method + "::id::" + str(pcatid + ii))                                
                                self.move_images_for_directory(p2, pcatid + ii, pstartidx)
                                ii = ii + 1
                        else:
                                self.xx_dbg(s_method + "::in::not_is_dir:p2:" + str(p2))
                self.xx_dbg(s_method + "::out::")

        def move_images_for_directory(self, p_dir, pcatid, pstartidx):
                s_method = "LKD_CreateImages::move_images_for_directory"
                self.xx_dbg(s_method + "::in::")                
                self.m_root_sequential_ids_src = p_dir

                srv_handler = LKD_MdFilesUtils("")
                dd_active_cat_id = pcatid
                dd_file_idx = 0                

                root_sequential_ids_dst = srv_handler.get_root_for_groups(  
                        dd_active_cat_id , 
                        dd_file_idx)

                root_sequential_ids_dst  = root_sequential_ids_dst  + "\\content_idx_0\\imgs"

                self.xx_dbg(s_method + "::src::" + p_dir)
                self.xx_dbg(s_method + "::dest::" + root_sequential_ids_dst)
                start_idx = pstartidx
                self.xx_dbg(s_method + "::start_idx::" + str(start_idx))
                
                self.move_sequential_ids(
                        p_dir
                        , root_sequential_ids_dst
                        ,start_idx)
                self.xx_dbg(s_method + "::out::")

        def move_sequential_ids(self,src_path,dst_path,start_idx):
                self.xx_dbg("LKD_CreateImages::move_sequential_ids::in::")

                dd_ll = self.get_files_recur(
                        src_path
                        ,0
                        ,dst_path)

                p_dest = dst_path

                ii = start_idx
                for dd_ii in dd_ll:
                        # self.xx_dbg("LKD_CreateImages::image::" + dd_ii.src_javafile_full_path)
                        src_fpath = dd_ii.src_javafile_full_path
                        dest_fpath = p_dest + "\\" + "img__" + str(ii) + ".png"                        
                        self.xx_dbg("=====================================================================>>>")
                        self.xx_dbg("LKD_CreateImages::image::s_src" + src_fpath)
                        self.xx_dbg("LKD_CreateImages::image::s_dest" + dest_fpath)
                        self.xx_dbg("<<<=====================================================================")
                        shutil.copy(src_fpath, dest_fpath)
                        ii = ii + 1

                self.xx_dbg("LKD_CreateImages::create_sequential_ids::out::")

        def get_sclass(self):
                return "LKD_CreateImages"

        def get_dir_root_img_src_digital(self,ep_300x200_all_digital_seq):
                dir_path = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\" + ep_300x200_all_digital_seq
                return dir_path

        def set_dirs_sequential_imgs_raw(self):
                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::in::")
                #self.m_root_sequential_ids_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_articles\\content_cats\\content_markdown\\content_by_groups\\cat__8000\\cat__000\\cat__00\\cat__8000\\content_idx_0\\imgs_seq_scr\\"
                self.m_root_sequential_ids_src = "C:\\lkd\\ht\\apps_ctx\\1\\Lakida-Knowledge-Base-Tech-Episodes-Topics\\Lakida-Knowledge-Base-Tech-Episodes-Resources\\Lakida-Knowledge-Base-Tech-Episodes\\Kubernetes-Resources\\"
                self.m_root_sequential_ids_src = "Installing-Ethereum-On-Kubernetes"

                self.m_root_sequential_ids_dst = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_articles\\content_cats\\content_markdown\\content_by_groups\\cat__8000\\cat__000\\cat__00\\cat__8000\\content_idx_0\\imgs_seq_dst\\"
                srv_handler = LKD_MdFilesUtils("")
                dd_active_cat_id = 15850
                dd_file_idx = 0
                self.m_root_sequential_ids_dst = srv_handler.get_root_for_groups(  dd_active_cat_id , dd_file_idx)
                self.m_root_sequential_ids_dst  = self.m_root_sequential_ids_dst  + "\\content_idx_0\\imgs"
                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::src::" + self.m_root_sequential_ids_src)
                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::det::" + self.m_root_sequential_ids_dst)
                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::out::")


        def set_dirs_sequential_imgs(self):
                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::in::")                
                s_root = "C:\\lkd\\ht\\lkd_screens\\app\\src\\lkd-screens\\"
                s_leaf = "CSharp-Examples-Episode-1"
                l_cat_id = 15869
                self.set_dirs_sequential_imgs_generic(l_cat_id, s_root,s_leaf)                
#
#

#
#
#

        def set_dirs_sequential_imgs_generic(self, catid, path_root,path_file):
                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::in::")
                #self.m_root_sequential_ids_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_articles\\content_cats\\content_markdown\\content_by_groups\\cat__8000\\cat__000\\cat__00\\cat__8000\\content_idx_0\\imgs_seq_scr\\"
                self.m_root_sequential_ids_src = path_root + path_file 
                srv_handler = LKD_MdFilesUtils("")
                dd_active_cat_id = catid
                dd_file_idx = 0
                self.m_root_sequential_ids_dst = dd_out = srv_handler.get_root_for_groups(  dd_active_cat_id , dd_file_idx)
                self.m_root_sequential_ids_dst  = self.m_root_sequential_ids_dst  + "\\content_idx_0\\imgs"
                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::src::" + self.m_root_sequential_ids_src)
                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::det::" + self.m_root_sequential_ids_dst)
                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::out::")


        def create_sequential_ids_screens(self):
                self.xx_dbg("LKD_CreateImages::create_sequential_ids_screens::in::")

        def create_sequential_ids(self):
                self.xx_dbg("LKD_CreateImages::create_sequential_ids::in::")

                src_path = self.m_root_sequential_ids_src
                dst_path = self.m_root_sequential_ids_dst
                start_idx = 30

                dd_ll = self.get_files_recur(
                        src_path
                        ,0
                        ,dst_path)

                p_dest = dst_path

                ii = start_idx
                for dd_ii in dd_ll:
                        # self.xx_dbg("LKD_CreateImages::image::" + dd_ii.src_javafile_full_path)
                        src_fpath = dd_ii.src_javafile_full_path
                        dest_fpath = p_dest + "\\" + "img__" + str(ii) + ".png"                        
                        self.xx_dbg("=====================================================================>>>")
                        self.xx_dbg("LKD_CreateImages::image::s_src" + src_fpath)
                        self.xx_dbg("LKD_CreateImages::image::s_dest" + dest_fpath)
                        self.xx_dbg("<<<=====================================================================")
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
