import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *

from LKD_CreateFilesDatabase import *
from LKD_CatItem import *
from LKD_MdFilesUtils import *
from LKD_CreateMdFilesFromSrcDatabase import *

#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py
# cd C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_images\\assets\\ep_300x200_all_digital
# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py create-sequential-ids

# 
# C:\lkd\ht\apps_portal\lkduni\app-4\src\modules\mod_ep_articles\content_cats\content_markdown\content_by_groups\cat__8000\cat__000\cat__00\cat__8000\content_idx_0\imgs_seq_scr\
#
#

class LKD_CreateImagesData:

        def __init__(self, spar):
                self.m_image_in_article_idx = 0

class LKD_CreateImages:

        def __init__(self, spar):
                self.xx_dbg("LKD_CreateImages::__init__::in::")
                self.m_src = self.get_dir_src_default()
                self.m_dst = "services_s3"
                self.m_root_src = self.get_dir_root_src_default()
                self.m_root_dst = self.get_dir_root_desc_default()

                self.m_test_mode = 0
                #self.m_override_mode = False
                self.m_override_mode = True
                self.m_root_sequential_ids_src = self.get_dir_imgs_seqr_dest()
                self.m_root_sequential_ids_dst = self.get_dir_imgs_seq_dest()

                self.m_ds = "/"
                self.xx_dbg("LKD_CreateImages::__init__::out::")


        #       =================================================================== 
        #
        #
        #       ===================================================================
        def get_dir_src_default(self):

                dd = self.gg(
                        self.gg("C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\" )
                        + self.gg("modules\\mod_ep_articles\\content_cats\\" )
                        + self.gg("content_markdown\\content_by_groups\\cat__8000\\" )
                        + self.gg("cat__000\\cat__00\\cat__8000\\" )
                        + self.gg("content_idx_0\\imgs\\300x200_white"))
                return dd

        def get_dir_root_src_default(self):

                dd = self.gg(
                        self.gg("C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\" )
                        + self.gg("modules\\mod_ep_articles\\content_cats\\" )
                        + self.gg("content_markdown\\content_by_groups\\cat__8000\\" )
                        + self.gg("cat__000\\cat__00\\cat__8000\\content_idx_0\\imgs\\300x200_white"))
                return dd

        def get_dir_root_desc_default(self):
                dd = self.gg(self.gg("C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\" )
                        + self.gg("modules\\mod_ep_articles\\content_cats\\" )
                        + self.gg("content_markdown\\content_by_groups\\cat__8000\\" )
                        + self.gg("cat__000\\cat__00\\cat__8000\\content_idx_0\\" )
                        + self.gg("imgs\\300x200_white_seq"))
                return dd

        def get_dir_imgs_seqr_dest(self):

                dd = self.gg(
                        self.gg("C:\\lkd\\ht\\apps_portal\\" )
                        + self.gg("lkduni\\app-4\\src\\modules\\" )
                        + self.gg("mod_ep_articles\\" )
                        + self.gg("content_cats\\content_markdown\\" )
                        + self.gg("content_by_groups\\" )
                        + self.gg("cat__8000\\cat__000\\cat__00\\cat__8000\\" )
                        + self.gg("content_idx_0\\imgs_seq_scr\\"))

                return dd

        def get_dir_imgs_seq_dest(self):
                dd = self.gg(
                        self.gg("C:\\lkd\\ht\\apps_portal\\" )
                        + self.gg("lkduni\\app-4\\src\\modules\\" )
                        + self.gg("mod_ep_articles\\" )
                        + self.gg("content_cats\\content_markdown\\" )
                        + self.gg("content_by_groups\\" )
                        + self.gg("cat__8000\\cat__000\\" )
                        + self.gg("cat__00\\cat__8000\\" )
                        + self.gg("content_idx_0\\imgs_seq_dst\\"))

                return dd

        def get_dir_root_img_src_digital(self, ep_300x200_all_digital_seq):
                dir_path = self.gg(
                        self.gg("C:\\lkd\\ht\\apps_portal\\")
                        + self.gg("lkduni\\app-4\\src\\")
                        + self.gg("modules\\mod_ep_images\\assets\\") 
                        + ep_300x200_all_digital_seq)
                return dir_path

        def gg(self, tt):
                return tt

        def set_dirs_sequential_imgs(self):
                self.xx_dbg("LKD_CreateImages::" 
                        + "set_dirs_sequential_imgs::in::")                
                s_root = "C:\\lkd\\ht\\lkd_screens\\app\\src\\lkd-screens\\"
                s_leaf = "CSharp-Examples-Episode-1"
                l_cat_id = 15869
                self.set_dirs_sequential_imgs_generic(
                        l_cat_id, 
                        s_root,
                        s_leaf)                

        #       =================================================================== 
        #
        #
        #       ===================================================================

        def move_images_for_ctx(self):
                root_dir ="C:\\lkd\\ht\\apps_ctx\\1\\"
                root_catid = 16112
                test_only = 1
                start_img_idx = 0
                self.move_images_for_article_child_directories(
                        root_dir, 
                        root_catid,
                        start_img_idx,
                        test_only)

        #       =================================================================== 
        #
        #       ===================================================================

        def execute_main_create_from_source(self,test_run):
                s_fun = self.gg(self.get_class_name() 
                        + self.gg("::execute_main_create_from_source::"))

                self.xx_dbg(s_fun + "start::")        
                
                ddh = LKD_CreateMdFilesFromSrcDatabase()
                data_items =  ddh.get_generic_cats_data("")

                for lkd_cats_group_item in data_items:

                        src_root = lkd_cats_group_item.get_src_root_dir_path()
                        cats_items = lkd_cats_group_item.get_src_root_child_cats()

                        self.xx_dbg("src_root::" + src_root)

                        self.execute_main_create_images_for_groups(
                                src_root,
                                cats_items,                                
                                test_run)

                        self.xx_dbg("cat_items_path_end_::" + src_root)

                self.xx_dbg(s_fun + "end::")

        #       =================================================================== 
        #
        #       ===================================================================

        def execute_main_create_images_for_groups(
                self,
                root_scr_path,
                cats_items,                
                test_run):

                s_fun = self.gg(
                        self.get_class_name() 
                        + "::execute_main_create_from_source::")

                self.xx_dbg(s_fun + "start::")                

                for cat_item_data in cats_items:
                        self.xx_dbg("cat_items_path::" 
                        + cat_item_data.src_project_relative_path)                

                self.xx_dbg(s_fun + "root_scr_path::" + root_scr_path)

                self.execute_main_create_images_for_groups_internal(
                        cats_items
                        , root_scr_path                        
                        , test_run)

                self.xx_dbg(s_fun + "end::")

        #       =================================================================== 
        #
        #       ===================================================================

        def execute_main_create_images_for_groups_internal(
                self, 
                cat_items_data, 
                root_scr_path,                
                test_run):

                s_fun = self.gg(
                        self.get_class_name() 
                        + "::execute_main_create_images_for_groups_internal::")

                self.xx_dbg(s_fun + "start::")                                

                for cat_item_data in cat_items_data:
                        self.xx_dbg("paths::" 
                        + cat_item_data.src_project_relative_path)

                postfixes = []    

                direct_subdirs = 0

                if( direct_subdirs == 0):

                        postfixes.append("")

                if( direct_subdirs == 1): # not-used-so-far

                        postfixes = self.get_direct_subdirs_to_execute()

                for cat_item_data in cat_items_data:

                        self.create_images_for_article(
                                cat_item_data
                                , ""
                                , root_scr_path + "\\" + cat_item_data.src_project_relative_path
                                , test_run)


                self.xx_dbg(s_fun + "end::")

        #       =================================================================== 
        #
        #       ===================================================================

        def create_images_for_article(
                self, 
                cat_item_data, 
                src_postfix, 
                root_scr_path,                
                test_run):

                s_method = "LKD_CreateImages::create_images_for_article"
                self.xx_dbg(s_method + "::in::root_scr_path:" + root_scr_path)
                self.xx_dbg(s_method + "::in::destination_cat_id:" 
                + str(cat_item_data.catid) )
                destination_cat_id = cat_item_data.catid 
                self.move_images_for_article_child_directories(
                        root_scr_path,
                        destination_cat_id,                        
                        test_run)

                self.xx_dbg(s_method + "::end::root_scr_path:" + root_scr_path)

                
        #       =================================================================== 
        #
        #       ===================================================================

        def move_images_for_article_child_directories(
                self, 
                root_src_article_path, 
                destination_cat_id,                 
                test_run):

                s_method = self.gg(
                        "LKD_CreateImages::" 
                        + "move_images_for_article_child_directories")

                self.xx_dbg(s_method + "::in::root_src_article_path:" 
                        + root_src_article_path)

                self.xx_dbg(s_method + "::in::destination_cat_id:" 
                        + str(destination_cat_id))
                                
                
                if os.path.isdir(root_src_article_path): 

                        self.xx_dbg(s_method 
                                + "::in::not_is_dir:root_src_article_path:" 
                                + str(root_src_article_path))

                        images_in_article_data = LKD_CreateImagesData("")

                        self.xx_dbg(s_method + "::id::" 
                                + str(destination_cat_id) 
                                + "::dir::" + str(root_src_article_path))
                                
                        self.move_images_for_article_directories(
                                root_src_article_path, 
                                destination_cat_id, 
                                images_in_article_data,
                                test_run
                                )
                        
                else:
                        self.xx_dbg(s_method + "::in::not_is_dir:root_src_article_path:" + str(root_src_article_path))

                self.xx_dbg(s_method + "::out::")

                
        #       =================================================================== 
        #
        #       ===================================================================


        def move_images_for_article_directories(
                self, 
                root_src_article_path, 
                pcatid_dest, 
                images_in_article_data,
                test_run):

                s_method = self.gg(
                        "LKD_CreateImages::" 
                        + "move_images_for_article_directories")

                self.xx_dbg(s_method + "::in::")                
                
                self.xx_dbg(s_method + "::pcatid_dest::" + str(pcatid_dest))                

                srv_handler = LKD_MdFilesUtils("")
                dd_active_cat_id = pcatid_dest
                dd_file_idx = 0                

                root_sequential_ids_dst = srv_handler.get_root_for_groups(  
                        dd_active_cat_id , 
                        dd_file_idx)

                root_sequential_ids_dst  = self.gg(
                        root_sequential_ids_dst  
                        + "\\content_idx_0\\imgs")

                self.xx_dbg(s_method + "::src::" + root_src_article_path)
                self.xx_dbg(s_method + "::dest::" + root_sequential_ids_dst)
                
                self.copy_images_from_source_to_article(
                        root_src_article_path
                        , root_sequential_ids_dst
                        , images_in_article_data
                        , test_run)

                self.xx_dbg(s_method + "::out::")
                
        #       =================================================================== 
        #
        #       ===================================================================


        def copy_images_from_source_to_article(
                self,
                src_files_full_path,
                dst_path,
                images_in_article_data,
                test_run):

                self.xx_dbg("LKD_CreateImages::" 
                        + "copy_images_from_source_to_article::in::")


                self.xx_dbg("LKD_CreateImages::" 
                        + "src_files_full_path::" + src_files_full_path)

                images_in_source_article_list = self.get_img_files_from_source_recurr(
                        src_files_full_path
                        ,0
                        ,dst_path)

                p_dest = dst_path

                for image_in_source_article in images_in_source_article_list:

                        src_fpath = image_in_source_article.src_javafile_full_path

                        dest_fpath = self.gg(p_dest + "\\" + "img__" 
                                + str(images_in_article_data.m_image_in_article_idx) + ".png")

                        self.xx_dbg("=======================================" 
                                + "==============================>>>")

                        self.xx_dbg_lv_0("LKD_CreateImages::image::s_src" + src_fpath)
                        self.xx_dbg_lv_0("LKD_CreateImages::image::s_dest" + dest_fpath)

                        self.xx_dbg("<<<====================================" 
                                + "=================================")

                        if test_run == 1:
                             self.xx_dbg("LKD_CreateImages::image::only-test-run:" + dest_fpath)
                        else:
                                self.xx_dbg("LKD_CreateImages::image::copy-files:" + dest_fpath)   
                                shutil.copy(src_fpath, dest_fpath)

                        images_in_article_data.m_image_in_article_idx = images_in_article_data.m_image_in_article_idx + 1

                self.xx_dbg("LKD_CreateImages::" 
                        + "copy_images_from_source_to_article::out::")
                
        #       =================================================================== 
        #
        #       ===================================================================


        def get_sclass(self):
                return "LKD_CreateImages"


                
        #       =================================================================== 
        #
        #       ===================================================================


        def set_dirs_sequential_imgs_generic(
                self, 
                catid, 
                path_root, 
                path_file):

                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::in::")
                #self.m_root_sequential_ids_src = "C:\\lkd\\ht\\apps_portal\\lkduni\\app-4\\src\\modules\\mod_ep_articles\\content_cats\\content_markdown\\content_by_groups\\cat__8000\\cat__000\\cat__00\\cat__8000\\content_idx_0\\imgs_seq_scr\\"
                self.m_root_sequential_ids_src = path_root + path_file 
                srv_handler = LKD_MdFilesUtils("")
                dd_active_cat_id = catid
                dd_file_idx = 0
                self.m_root_sequential_ids_dst = srv_handler.get_root_for_groups(  
                        dd_active_cat_id, 
                        dd_file_idx)

                self.m_root_sequential_ids_dst  = self.gg(self.m_root_sequential_ids_dst  
                        + "\\content_idx_0\\imgs")

                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::src::" 
                        + self.m_root_sequential_ids_src)

                self.xx_dbg("LKD_CreateImages::set_dirs_sequential_imgs::det::" 
                        + self.m_root_sequential_ids_dst)

                self.xx_dbg("LKD_CreateImages::" 
                        + "set_dirs_sequential_imgs::out::")

                
        #       =================================================================== 
        #
        #       ===================================================================


        def create_sequential_ids_screens(self):
                self.xx_dbg("LKD_CreateImages::create_sequential_ids_screens::in::")
                
        #       =================================================================== 
        #
        #       ===================================================================



        def get_generic_cats_items(self, dd):
                ddh = LKD_CreateFilesDatabase()
                return ddh.get_generic_cats_items("")
                
        #       =================================================================== 
        #
        #       ===================================================================


        def get_img_files_from_source_recurr(
                self, 
                psrc_path_project, 
                pcatid, 
                pdest_java_flat_dir_path):

		sfun = self.get_sclass() + "::get_img_files_from_source_recurr::"

                self.xx_dbg( sfun + "start")
		self.xx_dbg( sfun + "psrc_path_project::" + psrc_path_project)

                fjavafiles = []
                for root,d_names,f_names in os.walk(psrc_path_project):
	                for f in f_names:
                                dd = LKD_CatItem(pcatid, psrc_path_project)
                                dd.catid = pcatid
                                dd.src_project_relative_path = psrc_path_project
                                dd.src_javafile_full_path = os.path.join(root, f)
                                dd.src_javafile_name = f
                                dd.dest_java_flat_dir_path = pdest_java_flat_dir_path

                                if ("png" in dd.src_javafile_name):
                                        self.xx_dbg( sfun + "::append-image-src::" + dd.src_javafile_name)
		                        fjavafiles.append(dd)
                                else:
                                        self.xx_dbg( sfun + "::skipped-image-src::" + dd.src_javafile_name)


                self.xx_dbg( sfun + "end")
                return fjavafiles

                
        #       =================================================================== 
        #
        #       ===================================================================

                
        def get_root_for_groups( 
                self, 
                dd_active_cat_id ,
                dd_file_idx)	:

		sfun = self.gg(self.get_sclass() 
                        + "::get_file_content_by_cat_id_groups::")

		self.xx_dbg( sfun + "start")
                srv_handler = LKD_MdFilesUtils("")
                dd_out = srv_handler.get_root_for_groups(  
                        dd_active_cat_id , 
                        dd_file_idx)

                return dd_out

		self.xx_dbg( sfun + "end")
		return dd_file
                
        #       =================================================================== 
        #
        #       ===================================================================


        def move_digital_images_to_md(
                self
                , max_img_id_source_bucket
                , cat_id_start
                , cat_id_end):

		sfun = self.gg(self.get_sclass() 
                        + "::move_digital_images_to_md::")

		self.xx_dbg( sfun + "start")
                
                ep_300x200_all_digital_seq = "ep_300x200_all_digital_seq"                

                self.move_digital_images_to_md_impl(
                        max_img_id_source_bucket
                        ,ep_300x200_all_digital_seq
                        ,cat_id_start
                        , cat_id_end)

                self.xx_dbg( sfun + "end")
                
        #       =================================================================== 
        #
        #       ===================================================================


        def move_digital_images_to_md_impl(
                self
                , max_img_id_source_bucket
                , ep_300x200_all_digital_seq
                , cat_id_start
                , cat_id_end
                ):

		sfun = self.gg(self.get_sclass() 
                        + "::move_digital_images_to_md_impl::")

		self.xx_dbg( sfun + "start")
                self.xx_dbg( sfun + "max_img_id_source_bucket:" 
                        + str(max_img_id_source_bucket))

                self.xx_dbg( sfun + "cat_id_start:" 
                        + str(cat_id_start))

                self.xx_dbg( sfun + "ep_300x200_all_digital_seq:" 
                        + str(ep_300x200_all_digital_seq))

                
                for ii in range (cat_id_start, cat_id_end, 1):

                        self.move_digital_image_to_md(
                                cat_id_start
                                , ii
                                , max_img_id_source_bucket
                                , ep_300x200_all_digital_seq)

                self.xx_dbg( sfun + "end")
                
        #       =================================================================== 
        #
        #       ===================================================================


        def move_digital_image_to_md(
                self
                , cat_id_start
                , cat_id
                , max_img_id_source_bucket
                , ep_300x200_all_digital_seq):

		sfun = self.gg(
                        self.get_sclass() 
                        + "::move_digital_image_to_md::")

		self.xx_dbg( sfun + "start")

                cat_id_img   = int((cat_id - cat_id_start )) % int(max_img_id_source_bucket)

                self.xx_dbg( sfun + "cat_id_img:" + str(cat_id_img))

                img_file = "img_" + str(cat_id_img) + ".jpg"
                img_file_dest = "img_300_x_200.png"
                src_files_full_path = self.get_dir_root_img_src_digital(
                        ep_300x200_all_digital_seq) + "\\" + img_file
                        
                dest_path = self.gg(
                        self.get_root_for_groups(cat_id,"0") 
                        + "\\content_idx_0\\imgs\\" 
                        + img_file_dest)

                self.copy_file(
                        src_files_full_path,
                        dest_path)

                self.xx_dbg( sfun + "end")
                
        #       =================================================================== 
        #
        #       ===================================================================


        def copy_file(self, src_fpath,dest_fpath):
		sfun = self.gg(self.get_sclass() 
                + "::copy_file::")

		self.xx_dbg( sfun + "start")
                self.xx_dbg( sfun + "src_fpath:"  + src_fpath)
                self.xx_dbg( sfun + "dest_fpath:"  + dest_fpath)

                shutil.copy(
                        src_fpath, 
                        dest_fpath)

                self.xx_dbg( sfun + "end")
                
        #       =================================================================== 
        #
        #       ===================================================================


        def get_item(self, id,title):
                dd = LKD_CatItem(id,title)
                return dd
                
        #       =================================================================== 
        #
        #       ===================================================================


        def xx_dbg(self, tt):
                "" ""                
                print ( tt )

        def xx_dbg_lv_0(self, tt):
                "" ""
                print ( tt )
                
        #       =================================================================== 
        #
        #       ===================================================================

        def get_class_name(self):
                return "LKD_GetImages::"

        def xx_print( self, tt ):
                "" ""
                print ( tt )       


# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py create_images_for_source_files