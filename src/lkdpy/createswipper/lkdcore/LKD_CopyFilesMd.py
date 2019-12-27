import sys
import os
import logging
import shutil

class LKD_CopyFilesMd:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CopyFiles::__init__::in::")
                self.m_src = "blogtech_x2"
                self.m_dst = "services_s3"
                self.m_root_src = ""
                self.m_root_dst = ""
                self.m_test_mode = 0
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
                print tt

        def populate_one_md(self, par_src, par_dst, p_key):

                self.m_src = par_src
                self.m_dst = par_dst

                psrc = self.m_src
                pdst = self.m_dst

                DS = self.m_ds

                self.m_root_src = ""
                self.m_root_src = self.m_root_src + "C:" + DS + "lkd" + DS + "ht" + DS + "apps_portal" + DS + "lkduni" + DS + "app-4" 
                self.m_root_src = self.m_root_src + DS + "src" + DS + "modules" + DS + "mod_ep_articles"
                self.m_root_src = self.m_root_src + DS + "content_cats" + DS + "content_markdown" 
                self.m_root_src = self.m_root_src + DS + "content_by_catid" + DS + "cat__" + psrc + DS + "components"

                self.m_root_dst = ""
                self.m_root_dst = self.m_root_dst  + "C:" + DS + "lkd" + DS + "ht" + DS + "apps_portal" + DS + "lkduni" + DS + "app-4" 
                self.m_root_dst = self.m_root_dst  + DS + "src" + DS + "modules" + DS + "mod_ep_articles"
                self.m_root_dst = self.m_root_dst  + DS + "content_cats" + DS + "content_markdown" 
                self.m_root_dst = self.m_root_dst  + DS + "content_by_catid" + DS + "cat__" + pdst + DS + "components"
                
                if p_key != "prod_splash_ps2":
                        self.copy_file("content__prod_splash_ps2.md"
                                , "content__" + p_key + ".md")

        def cpy_all(self, par_src, par_dst):

                self.m_src = par_src
                self.m_dst = par_dst

                psrc = self.m_src
                pdst = self.m_dst

                DS = self.m_ds

                self.m_root_src = ""
                self.m_root_src = self.m_root_src + "C:" + DS + "lkd" + DS + "ht" + DS + "apps_portal" + DS + "lkduni" + DS + "app-4" 
                self.m_root_src = self.m_root_src + DS + "src" + DS + "modules" + DS + "mod_ep_articles"
                self.m_root_src = self.m_root_src + DS + "content_cats" + DS + "content_markdown" 
                self.m_root_src = self.m_root_src + DS + "content_by_catid" + DS + "cat__" + psrc

                self.m_root_dst = ""
                self.m_root_dst = self.m_root_dst  + "C:" + DS + "lkd" + DS + "ht" + DS + "apps_portal" + DS + "lkduni" + DS + "app-4" 
                self.m_root_dst = self.m_root_dst  + DS + "src" + DS + "modules" + DS + "mod_ep_articles"
                self.m_root_dst = self.m_root_dst  + DS + "content_cats" + DS + "content_markdown" 
                self.m_root_dst = self.m_root_dst  + DS + "content_by_catid" + DS + "cat__" + pdst


                self.copy_file("content_idx_0" + DS + "content__0.md"
                        , "content_idx_0" + DS + "content__0.md")

                self.copy_file("content_idx_0" + DS + "content__0.txt"
                        , "content_idx_0" + DS + "content__0.txt")

                self.copy_file("title-content__0.md"
                        , "title-content__0.md")

                self.copy_file("content_pl_0" + DS + "content__0.md"
                        , "content_pl_0" + DS + "content__0.md")

                self.copy_file("content_idx_0" + DS + "imgs" + DS + "img__placeh.md"
                        , "content_idx_0" + DS + "imgs" + DS + "img__placeh.md")



        def copy_file(self, psrc, pdest):
            
                self.xx_dbg("[METHOD_IN]" + "[copy_file]")
                
                DS = self.m_ds

                src_fpath = self.m_root_src + DS + psrc
                dest_fpath = self.m_root_dst + DS + pdest

                self.xx_dbg("[src_fpath]" + src_fpath)
                self.xx_dbg("[dest_fpath]" + dest_fpath)
                
                if self.m_test_mode == 1:
                        return
                
                self.xx_dbg("[COPY_START]" + "[copy_file][" + src_fpath +"]")
                self.xx_dbg("[COPY_START]" + "[to_file][" + dest_fpath +"]")

                try:
                        shutil.copy(src_fpath, dest_fpath)
                        self.xx_dbg("[COPY_SUCCESS_0]" + "[from][" + src_fpath +"]")
                        self.xx_dbg("[COPY_SUCCESS_0]" + "[to_file][" + dest_fpath +"]")

                except IOError as io_err:
                        
                        dir_path = os.path.dirname(dest_fpath)
                        self.xx_dbg("[check_dir]" + dir_path)
                        try:
                                if os.path.isdir(dir_path):
                                        self.xx_dbg("[dir_exists_no_err]" + dir_path)
                                else:
                                
                                        os.makedirs(dir_path)

                        except:
                                self.xx_dbg("[dir_exists]" + dir_path)

                        shutil.copy(src_fpath, dest_fpath)
                        self.xx_dbg("[COPY_SUCCESS_1]" + "[from][" + src_fpath +"]")
                        self.xx_dbg("[COPY_SUCCESS_1]" + "[to_file][" + dest_fpath +"]")


        def inplace_change_(self, filename, old_string, new_string):
                self.xx_dbg("[METHOD_IN]" + "[inplace_change]")


                # Safely write the changed content, if found in the file
                with open(filename, 'w') as f:
                        s = f.read()
                        print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
                        s = s.replace(old_string, new_string)
                        f.write(s)

                self.xx_dbg("[METHOD_OUT]" + "[inplace_change]")

        def inplace_change(self, filename, old_string, new_string):
                self.xx_dbg("[METHOD_IN]" + "[inplace_change]")

                with open(filename) as f:
                        newText=f.read().replace(old_string, new_string)

                with open(filename, "w") as f:
                        f.write(newText)


        def copy_lines_from_file(self, filename_src, filename_dest, lines_from, lines_to):
                self.xx_dbg("[METHOD_IN]" + "[inplace_change]")

                self.xx_dbg("src_file_to_copy:" + filename_src)
                self.xx_dbg("filename_dest:" + filename_dest)

                self.xx_dbg("lines_from:" + str(lines_from))
                self.xx_dbg("lines_to:" + str(lines_to))

                # Safely write the changed content, if found in the file
                lout = []
                with open(filename_src, 'r') as f:
                        s = f.readlines()             
                        if(lines_from >= len(s)):
                                return

                        if(lines_to >= len(s)):
                                return

                        lout=s[lines_from:lines_to]
                        lout.append("")
                        lout.append("")
                        lout.append("")
                        lout.append( "lines :" + str(lines_from) + " " + str(lines_to))

                with open(filename_dest, 'w') as f:
                        f.writelines(lout)

                self.xx_dbg("[METHOD_OUT]" + "[inplace_change]")

        def exec_cpy_contents_mds(self):
                self.exec_cpy_content_mds(4299,4300,100,1000)

        def exec_cpy_content_mds(self, cat_id_copied, cat_idx_start, cats_copied, linescopied):

                # 4298 4409
                src_file = ""
                for x in range(cats_copied):
                        idx_start = x*linescopied -100
                        if(idx_start < 0):
                                idx_start=1

                        idx_end = (x+1)*linescopied + 100
                        
                        file_src = self.get_file_name_src(str(cat_id_copied))
                        
                        xx = cat_idx_start + x
                        file_dst = self.get_file_name(str(xx))

                        self.copy_lines_from_file(file_src,file_dst,idx_start,idx_end)

        def get_file_name(self,stridx):

                DS = "/"

                file_dest = ""
                file_dest = file_dest + "C:" + DS + "lkd" + DS + "ht" + DS + "apps_portal" + DS + "lkduni" + DS + "app-4" 
                file_dest = file_dest + DS + "src" + DS + "modules" + DS + "mod_ep_articles"
                file_dest = file_dest + DS + "content_cats" + DS + "content_markdown" 
                file_dest = file_dest + DS + "content_by_catid" + DS + "cat__" + stridx
                file_dest = file_dest + DS + "content_idx_0" 
                file_dest = file_dest + DS + "content__0.txt"

                return file_dest

        def get_file_name_src(self,stridx):

                DS = "/"

                file_dest = ""
                file_dest = file_dest + "C:" + DS + "lkd" + DS + "ht" + DS + "apps_portal" + DS + "lkduni" + DS + "app-4" 
                file_dest = file_dest + DS + "src" + DS + "modules" + DS + "mod_ep_articles"
                file_dest = file_dest + DS + "content_cats" + DS + "content_markdown" 
                file_dest = file_dest + DS + "content_by_catid" + DS + "cat__" + stridx
                file_dest = file_dest + DS + "content_idx_0" 
                file_dest = file_dest + DS + "content__0__full.txt"

                return file_dest

