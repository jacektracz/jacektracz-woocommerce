import sys
import os
import logging
import shutil

class LKD_CopyFiles:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CopyFiles::__init__::in::")
                self.m_src = "blogtech_x2"
                self.m_dst = "services_s3"
                self.m_root_src = ""
                self.m_root_dst = ""
                self.m_test_mode = 0
                #self.m_override_mode = False
                self.m_override_mode = True
                self.m_ds = "/"
                self.xx_dbg("LKD_CopyFiles::__init__::out::")
               
        
        def prepare_object(self):
                self.xx_dbg("LKD_CopyFiles::prepare_object::in::")
                        
                self.xx_dbg("LKD_CopyFiles::prepare_object::out::")

        def copy_files(self):
                self.xx_dbg("LKD_CopyFiles::copy_files::in::")
                        
                self.xx_dbg("LKD_CopyFiles::copy_files::out::")

        def xx_dbg(self, tt):
                "" ""
                print (tt)

        def set_roots(self,par_src, par_dst):
                self.m_src = par_src
                self.m_dst = par_dst

                psrc = self.m_src
                pdst = self.m_dst

                DS = self.m_ds

                self.m_root_src = "C:" + DS + "lkd" + DS + "ht" + DS + "apps_portal" + DS + "lkduni" + DS + "app-4" + DS + "src" + DS + "modules" + DS + "mod_ep_swipper_" + psrc
                self.m_root_dst = "C:" + DS + "lkd" + DS + "ht" + DS + "apps_portal" + DS + "lkduni" + DS + "app-4" + DS + "src" + DS + "modules" + DS + "mod_ep_swipper_" + pdst

        def cpy_one(self,par_src, par_dst):


                self.set_roots(par_src,par_dst)

                psrc = self.m_src
                pdst = self.m_dst

                DS = self.m_ds

                self.xx_dbg("LKD_CopyFiles::copy_one::__src__" + psrc)

                self.copy_file("lib" + DS + psrc + DS + "services" + DS  + "EPT_swipper_categories_md_" + psrc + ".php",
                        "lib" + DS + pdst + DS + "services" +  DS + "EPT_swipper_categories_md_" + pdst + ".php")

        def cpy_one_entity_child(self,par_src, par_dst):


                self.m_src = par_src
                self.m_dst = par_dst

                psrc = self.m_src
                pdst = self.m_dst

                DS = self.m_ds

                
                self.set_roots(par_src,par_dst)

                self.xx_dbg("LKD_CopyFiles::copy_one::__src__" + psrc)

                #self.copy_file("lib" + DS + psrc + DS + "services" + DS  + "EPT_swipper_categories_includes_" + psrc + ".php",
                #        "lib" + DS + pdst + DS + "services" +  DS + "EPT_swipper_categories_includes_" + pdst + ".php")

                self.copy_file("lib" + DS + psrc + DS + "services" + DS + "EPT_swipper_categories_" + psrc + ".php",
                        "lib" + DS + pdst + DS + "services" + DS + "EPT_swipper_categories_" + pdst + ".php")


        def cpy_all(self, par_src, par_dst, pfilter):

                self.m_src = par_src
                self.m_dst = par_dst

                psrc = self.m_src
                pdst = self.m_dst

                DS = self.m_ds

                
                self.set_roots(par_src,par_dst)


                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "selector_main"):
                        self.copy_file("lib" + DS + psrc + DS + "services" + DS  + "EPT_swipper_categories_includes_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "services" +  DS + "EPT_swipper_categories_includes_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "selector_main"):
                        self.copy_file("mod_ep_swipper_" + psrc + ".php"
                                ,"mod_ep_swipper_" + pdst + ".php")

                # return

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "c-api"):
                        self.copy_file("lib" + DS + psrc + DS +  "controller-api" + DS + "EPT_swipper_selector_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "controller-api" + DS + "EPT_swipper_selector_" + pdst + ".php")

                # return 

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "selector_main"):
                        self.copy_file("mod_ep_swipper_" + psrc + ".php"
                                ,"mod_ep_swipper_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "css"):
                        self.copy_file("assets" + DS + "css" + DS + "mod_ep_swipper_" + psrc + ".css"
                                ,"assets" + DS + "css" + DS + "mod_ep_swipper_" + pdst + ".css")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "configuration" + DS + "EPT_swipper_configuration_" + psrc + ".php"
                                ,"lib" + DS + pdst + DS + "configuration" + DS + "EPT_swipper_configuration_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "configuration" + DS + "EPT_swipper_data_config_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "configuration" + DS + "EPT_swipper_data_config_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "entity" + DS + "EPT_swipper_data_arr_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "entity" + DS + "EPT_swipper_data_arr_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "entity" + DS + "EPT_swipper_data_item_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "entity" + DS + "EPT_swipper_data_item_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "entity" + DS + "EPT_swipper_data_item_child_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "entity" + DS + "EPT_swipper_data_item_child_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "entity" + DS + "EPT_swipper_entity_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "entity" + DS + "EPT_swipper_entity_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main" or pfilter == "images"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_mdflat2_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_mdflat2_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main" or pfilter == "images"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_mdflat_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_mdflat_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main" or pfilter == "images"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_bsgenroot_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_bsgenroot_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main" or pfilter == "images"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_bsgen2_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_bsgen2_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main" or pfilter == "images"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_bsgen_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_bsgen_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main" or pfilter == "images"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_bygroups_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_mdimgs_main_bygroups_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_installer_rows_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_installer_rows_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_frame_rows_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_frame_rows_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_item_rows_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_item_rows_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_item_aws_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_item_aws_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_item_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_item_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_title_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_title_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_window_rows_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_window_rows_" + pdst + ".php")
                if(pfilter == "search-only"):
                        if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                                self.copy_file("lib" + DS + psrc + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_button_" + psrc + ".php",
                                        "lib" + DS + pdst + DS + "renders" + DS + "rows" + DS + "EPT_swipper_rend_button_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "cat_copy"):
                        self.copy_file("lib" + DS + psrc + DS + "services" + DS + "EPT_swipper_categories_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "services" + DS + "EPT_swipper_categories_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "services" + DS + "EPT_swipper_categories_executor_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "services" + DS + "EPT_swipper_categories_executor_" + pdst + ".php")                                

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "EPT_swipper_categories_matrix_"):
                        self.copy_file("lib" + DS + psrc + DS + "services" + DS + "EPT_swipper_categories_matrix_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "services" + DS + "EPT_swipper_categories_matrix_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "services" + DS + "EPT_swipper_content_filler_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "services" + DS + "EPT_swipper_content_filler_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "services" + DS  + "EPT_swipper_categories_md_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "services" +  DS + "EPT_swipper_categories_md_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS + "services" + DS  + "EPT_swipper_categories_includes_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "services" +  DS + "EPT_swipper_categories_includes_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS +  "controller" + DS + "EPT_swipper_controller_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "controller" + DS + "EPT_swipper_controller_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS +  "controller-api" + DS + "EPT_swipper_selector_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "controller-api" + DS + "EPT_swipper_selector_" + pdst + ".php")

                if(pfilter == "search-only"):
                        
                        if(pfilter == "all" or pfilter == "all-short" or  pfilter == "main"):
                                self.copy_file("lib" + DS + psrc + DS +  "controller-api" + DS + "EPT_swipper_selector_test_" + psrc + ".php",
                                        "lib" + DS + pdst + DS + "controller-api" + DS + "EPT_swipper_selector_test_" + pdst + ".php")


                if(pfilter == "all" or pfilter == "all-short-disable" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS +  "renders" + DS + "mdcontent" + DS + "EPT_swipper_render_cnt_title_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "mdcontent" + DS + "EPT_swipper_render_cnt_title_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short-disable" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS +  "renders" + DS + "mdcontent" + DS + "EPT_swipper_render_cnt_title_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "mdcontent" + DS + "EPT_swipper_render_cnt_title_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short-disable" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS +  "renders" + DS + "mdcontent" + DS + "EPT_swipper_render_mdcontent_create_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "mdcontent" + DS + "EPT_swipper_render_mdcontent_create_" + pdst + ".php")


                if(pfilter == "all" or pfilter == "all-short-disable" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS +  "renders" + DS + "mdcontent" + DS + "EPT_swipper_render_mdcontent_read_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "mdcontent" + DS + "EPT_swipper_render_mdcontent_read_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short-disable" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS +  "renders" + DS + "treerender" + DS + "EPT_swipper_rend_tree_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "treerender" + DS + "EPT_swipper_rend_tree_" + pdst + ".php")

                if(pfilter == "all" or pfilter == "all-short-disable" or  pfilter == "main"):
                        self.copy_file("lib" + DS + psrc + DS +  "renders" + DS + "treestatic" + DS + "EPT_swipper_render_treestatic_" + psrc + ".php",
                                "lib" + DS + pdst + DS + "renders" + DS + "treestatic" + DS + "EPT_swipper_render_treestatic_" + pdst + ".php")
                                

# EPT_swipper_render_mdcontent_create_md_artcnt_ma7
# treestatic EPT_swipper_render_treestatic_md_artcnt_ma7
        def copy_file(self, psrc, pdest):
            
                self.xx_dbg("[METHOD_IN]" + "[copy_file]")
                
                DS = self.m_ds

                src_fpath = self.m_root_src + DS + psrc
                dest_fpath = self.m_root_dst + DS + pdest

                self.xx_dbg("[src_fpath]" + src_fpath)
                self.xx_dbg("[dest_fpath]" + dest_fpath)

                if self.m_test_mode == 1:
                        self.xx_dbg("[return_on_test_mode]" + src_fpath)
                        return
                
                self.xx_dbg("[COPY_START]" + "[copy_file][" + src_fpath +"]")
                self.xx_dbg("[COPY_START]" + "[to_file][" + dest_fpath +"]")

                self.create_dir_path(
                        dest_fpath)

                self.copy_check_override(
                        self.m_override_mode
                        , src_fpath
                        , dest_fpath
                        , self.m_src
                        , self.m_dst)


        def create_dir_path(self, dest_fpath):
                self.xx_dbg("[METHOD_IN]" + "[inplace_change]")
                self.xx_dbg("" + "[dest_fpath][" + dest_fpath +"]")        
                dir_path = os.path.dirname(dest_fpath)

                try:
                        if os.path.isdir(dir_path):
                                self.xx_dbg("[dir_exists]" + dir_path)
                        else:                                                             
                                os.makedirs(dir_path)
                                self.xx_dbg("[dir_created]" + dir_path)
                except:
                        self.xx_dbg("[dir_exists]" + dir_path)                
                        
                
        def copy_check_override(self
                , override_mode
                , src_fpath
                , dest_fpath
                , inplace_chamge_src_postfix
                , inplace_change_dest_postfix):

                self.xx_dbg("[METHOD_IN]" + "[copy_check_override]")
                self.xx_dbg("[COPY_START]" + "[from][" + src_fpath +"]")
                self.xx_dbg("[COPY_START]" + "[to_file][" + dest_fpath +"]")

                if not override_mode:
                        if not os.path.isfile(dest_fpath):
                                self.xx_dbg("[COPY_AS_NEW_FILE]" + dest_fpath)

                                shutil.copy(src_fpath, dest_fpath)

                                self.inplace_change(
                                        dest_fpath
                                        , inplace_chamge_src_postfix
                                        , inplace_change_dest_postfix)

                                self.xx_dbg("[COPY_INPLACE_NEW]" + "[from][" + src_fpath +"]")
                                self.xx_dbg("[COPY_INPLACE_NEW]" + "[to_file][" + dest_fpath +"]")
                        else:
                                self.xx_dbg("[NOT_COPY_INPLACE_EXISTS_1]" + "[from][" + src_fpath +"]")
                                self.xx_dbg("[NOT_COPY_INPLACE_EXISTS_1]" + "[to_file][" + dest_fpath +"]")

                else:
                        if not os.path.isfile(dest_fpath) :
                                self.xx_dbg("[NOT_OVERRIDE_FILE]" + dest_fpath)

                                shutil.copy(src_fpath, dest_fpath)

                                self.inplace_change(
                                        dest_fpath
                                        , inplace_chamge_src_postfix
                                        , inplace_change_dest_postfix)

                                self.xx_dbg("[COPY_INPLACE_NEW]" + "[from][" + src_fpath +"]")
                                self.xx_dbg("[COPY_INPLACE_NEW]" + "[to_file][" + dest_fpath +"]")

                        if os.path.isfile(dest_fpath) :
                                self.xx_dbg("[OVERRIDE_FILE]" + dest_fpath)

                                shutil.copy(src_fpath, dest_fpath)

                                self.inplace_change(
                                        dest_fpath
                                        , inplace_chamge_src_postfix
                                        , inplace_change_dest_postfix)

                                self.xx_dbg("[COPY_INPLACE_OVERRIDE]" + "[from][" + src_fpath +"]")
                                self.xx_dbg("[COPY_INPLACE_OVERRIDE]" + "[to_file][" + dest_fpath +"]")


        def inplace_change_(self, filename, old_string, new_string):
                self.xx_dbg("[METHOD_CPY_REPLACE]" + "[inplace_change]")
                self.xx_dbg("[inplace_change_]" + "[from][" + old_string +"]")
                self.xx_dbg("[inplace_change_]" + "[to_file][" + old_string +"]")


                # Safely write the changed content, if found in the file
                with open(filename, 'w') as f:
                        s = f.read()
                        print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
                        s = s.replace(old_string, new_string)
                        f.write(s)

                self.xx_dbg("[METHOD_OUT]" + "[inplace_change]")

        def inplace_change(self, filename, old_string, new_string):
                self.xx_dbg("[METHOD_IN]" + "[inplace_change]")
                self.xx_dbg("" + "[inplace_change][FROM_STR:]" + old_string + "]")
                self.xx_dbg("" + "[inplace_change][TO_STR:]" + new_string + "]")

                with open(filename) as f:
                        newText = f.read().replace(old_string, new_string)

                with open(filename, "w") as f:
                        f.write(newText)

                self.xx_dbg("[METHOD_OUT]" + "[inplace_change]")

       

