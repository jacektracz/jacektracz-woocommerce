import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *

from LKD_CreateMdFilesFromSrcDatabase import *
from LKD_CatItem import *
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py
# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py perform-src-files

class LKD_CreateMdFilesFromProjectsParent:

        def __init__(self):                                
                self.m_log_enabled = 0

        # C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py generate_src_articles_subdir

        def execute_gen_subdirs(self):
                s_method = self.gg(self.get_class_name()
                        + "execute_gen_subdirs")
                self.xx_dbg(s_method + "::in::")
                folders = self.get_folder_cat_items("")
                self.print_directory_subdirs(folders)
                self.xx_dbg(s_method + "::out::")                

        def get_folder_cat_items(self , tt):                

                s_method = self.gg(self.get_class_name() +
                        "get_folder_cat_items")

                self.xx_dbg(s_method + "::in::")

                ddh = LKD_CreateMdFilesFromSrcDatabase()
                data_items =  ddh.get_generic_cats_data("")
                folder_cat_items = []
                for lkd_articles_parent_item in data_items:

                        src_articles_parent_path = lkd_articles_parent_item.get_src_root_dir_path()
                        parent_cat_id = lkd_articles_parent_item.get_src_root_cat_id()
                        selector  = lkd_articles_parent_item.get_src_root_selector()
                        self.xx_dbg("generated_src_root::" + src_articles_parent_path)
                        self.xx_dbg("generated_parent_cat_id::" + str(parent_cat_id))

                        first_article_in_childs_list__cat_id = parent_cat_id + 1

                        self.gen_header_root(
                                src_articles_parent_path,
                                selector)

                        self.gen_header_childs(
                                src_articles_parent_path,
                                selector)

                        self.generate_one_folder_cat_items(
                                src_articles_parent_path,
                                first_article_in_childs_list__cat_id)

                        self.gen_footer_childs(
                                src_articles_parent_path)

                self.xx_dbg(s_method + "out::")
                return folder_cat_items

        def gen_header_root(
                self, 
                articles_parent_path_path,
                selector):

                self.xx_dbg_gen(" ")
                self.xx_dbg_gen("\tdef get_root_js_" + selector + "(self, dd):")
                self.xx_dbg_gen("\t\troot_src = " 
                + self.nn() 
                + articles_parent_path_path 
                + self.nn())
                self.xx_dbg_gen("\t\treturn root_src")
                self.xx_dbg_gen(" ")

        def gen_header_childs(self, 
                articles_parent_path_path,
                selector):

                self.xx_dbg_gen(" ")       
                self.xx_dbg_gen("\tdef get_cats_js_" + selector + "(self, psrc_path_project):")
                self.xx_dbg_gen("\t\tcats = []")
                self.xx_dbg_gen("\t\texclude_imported = 1")
                self.xx_dbg_gen("\t\tif exclude_imported == 1:")
                self.xx_dbg_gen("\t\t\tall_c = 0")
                self.xx_dbg_gen("\t\t\tif all_c == 1 :")

        def gen_footer_childs(self, articles_parent_path_path):

                self.xx_dbg_gen("\t\treturn cats")
                self.xx_dbg_gen("")

        def generate_one_folder_cat_items(
                self , 
                src_articles_parent_path,
                first_article_in_childs_list__cat_id):                

                s_method = self.gg(self.get_class_name() +
                        "get_folder_cat_items")

                self.xx_dbg(s_method + "::in::")

                folder_cat_items = []
                one_def_folder_cat_items = self.read_directory_subdirs(
                        src_articles_parent_path,
                        first_article_in_childs_list__cat_id)
                        
                folder_cat_items.extend(
                        one_def_folder_cat_items)                        

                self.print_directory_subdirs(
                        folder_cat_items)

                self.xx_dbg(s_method + "::out::")

        def read_directory_subdirs(self, 
                src_articles_parent_path, 
                startIdx):

                s_method = self.gg(self.get_class_name() +
                        "read_directory_subdirs")

                self.xx_dbg(s_method + "::in::")                
                self.xx_dbg(s_method + "::src_articles_parent_path::" + src_articles_parent_path)
                self.xx_dbg(s_method + "::startIdx::" + str(startIdx))

                folders = []

                dir_idx = 0
                for shortName in os.listdir(src_articles_parent_path):
                        
                        if os.path.isdir(
                                os.path.join(src_articles_parent_path, shortName)):        

                #for root,d_names,f_names in os.walk(src_articles_parent_path):
                #        dir_idx = 0
	        #        for shortName in d_names:
                                self.xx_dbg(s_method + "::added::" + str(shortName))
                                dd = self.get_item(
                                        int(startIdx) + int(dir_idx)
                                        , shortName)
                                folders.append(dd)
                                dir_idx = dir_idx + 1

                self.xx_dbg(s_method + "::out::")                        
                return folders        

               
        def print_directory_subdirs(self, folder_cat_items):

                s_method = self.gg(self.get_class_name() 
                        + "read_directory_subdirs")

                for catItem in folder_cat_items:
                        genStr = self.gg("\t\t\t\tcats.append(self.get_item(" 
                                + str(catItem.getCatId()) 
                                + ", " + self.nn() 
                                + catItem.getShortDirName() 
                                + self.nn() + "))")
                        self.xx_dbg_gen(genStr)

        def get_item(self, id,title):
                title = title.strip()
                title = title.replace(" ","-")
                dd = LKD_CatItem(id,title)
                return dd


        def nn(self):
                return "'"

        def get_class_name(self):
                return "generator::"

        def get_sclass(self):
                return "LKD_CreateMdFilesFromProjectsParent"

        def get_item(self, id,title):
                dd = LKD_CatItem(id,title)
                return dd

        def xx_dbg(self, tt):
                "" "" 
                if(self.m_log_enabled == 1 ):
                        print ( tt )
        
        def xx_dbg_gen(self, tt):
                "" ""
                print ( tt )

        def xx_print( self, tt ):
                "" ""
                print ( tt )       

        def gg(self , tt):
                return tt
