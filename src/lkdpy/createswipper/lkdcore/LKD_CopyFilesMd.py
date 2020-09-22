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
                print( tt )

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
                self.m_root_dst = self.m_root_dst  + DS + "content_tmp" + DS + "cat__" + pdst + DS + "components"
                

                if p_key != "prod_splash_ps2":
                        self.static_copy_file(
                                self.m_root_src
                                , self.m_root_dst
                                , "content__prod_splash_ps2.md"
                                , "content__" + p_key + ".md")

        def dechodbg( self, tt):
                """ """
                self.xx_dbg(tt)

        def get_root_for_groups( self, dd_active_cat_id ,dd_file_idx)	:

		sfun = self.get_sclass() + "::get_file_content_by_cat_id_groups::"
		self.xx_dbg( sfun + "start")
		self.xx_dbg( sfun + "active_cat_id" + str(dd_active_cat_id ))

		dd_rest = dd_active_cat_id

		dd_mod_1000 = self.get_int(dd_active_cat_id , 1000)

		dd_rest = dd_rest - ( dd_mod_1000 * 1000)
		self.xx_dbg( sfun + "__resolve_groups__mod_1000__[" + str(dd_mod_1000 )+ "]")
		self.xx_dbg( sfun + "__resolve_groups__mod_1000_rest__[" + str(dd_rest) + "]")

		dd_mod_100 = self.get_int(dd_rest , 100)
		dd_rest = dd_rest - ( dd_mod_100 * 100)

		self.xx_dbg( sfun + "__resolve_groups__mod_100__[" + str(dd_mod_100) + "]")
		self.xx_dbg( sfun + "__resolve_groups__mod_100_rest__[" + str(dd_rest) + "]")

		dd_mod_10 = self.get_int(dd_rest , 10)
		dd_rest = dd_rest - ( dd_mod_10 * 10)

		self.xx_dbg( sfun + "__resolve_groups__mod_10__[" + str(dd_mod_10 )+ "]")
		self.xx_dbg( sfun + "__resolve_groups__mod_10_rest__[" + str(dd_rest) + "]")

		dd_mod_1 = dd_rest

		self.xx_dbg( sfun + "__resolve_groups__mod_1__[" + str(dd_mod_1) + "]")
		self.xx_dbg( sfun + "__resolve_groups__mod_1_rest__[" + str(dd_rest) + "]")		

		dd_DS1 =  "/"
		dd_file = ""
		dd_file =  dd_file + "C:"
                dd_file =  dd_file +  dd_DS1 + "lkd"
                dd_file =  dd_file +  dd_DS1 + "ht"
                dd_file =  dd_file +  dd_DS1 + "apps_portal"
                dd_file =  dd_file +  dd_DS1 + "lkduni"
                dd_file =  dd_file +  dd_DS1 +  "app-4" 
                dd_file =  dd_file +  dd_DS1 + "src"
		dd_file =  dd_file  + dd_DS1 + "modules"
		dd_file =  dd_file  + dd_DS1 + "mod_ep_articles"
		dd_file =  dd_file  + dd_DS1 + "content_cats"
		dd_file =  dd_file  + dd_DS1 + "content_markdown"
		dd_file =  dd_file  + dd_DS1 + "content_by_groups"
		dd_file =  dd_file  + dd_DS1 + "cat__" + str(dd_mod_1000) + "000"
		dd_file =  dd_file  + dd_DS1 + "cat__" + str(dd_mod_100) + "00"
		dd_file =  dd_file  + dd_DS1 + "cat__" + str(dd_mod_10) + "0"
		dd_file =  dd_file  + dd_DS1 + "cat__" + str(dd_active_cat_id) + ""
		#dd_file =  dd_file  + dd_DS1 + "content_idx_" + str(dd_file_idx) + "" 
		#dd_file =  dd_file  + dd_DS1 + "content__" + str(dd_file_idx) + ".md"

		self.xx_dbg( sfun + "check_file_parsedown_md_x8::" + dd_file)
		self.xx_dbg( sfun + "end")
		return dd_file

        def get_sclass(self):
                return "MD_PArser"

	def get_int( self, dd_start_idx, dd_step ):

		sfun = self.get_sclass() + "::get_step::"
		self.xx_dbg( sfun + "start")		

                dd_iout = int(round(dd_start_idx / dd_step))

		self.xx_dbg( sfun + "end")
		return dd_iout

	def get_step( dd_start_idx, dd_step ):

		sfun = self.get_sclass() + "::get_step::"
		self.xx_dbg( sfun + "start")		
		dd_iout = 0
                dd_i = 1 
		while (true):

                        if (dd_i > 10 ):
                                break

                        dd_i = dd_i + 1
			dd_i100 = dd_i * dd_step
			if(dd_i100 > dd_start_idx):
				dd_iout = dd_i -1
				break
		
		self.xx_dbg( sfun + "end")
		return dd_iout
	
        def cpy_all_calculate_root_scr_no_groups(self, par_src):

                psrc = par_src

                DS = self.m_ds

                self.m_root_src = ""
                self.m_root_src = self.m_root_src + "C:" + DS + "lkd" + DS + "ht" + DS + "apps_portal" + DS + "lkduni" + DS + "app-4" 
                self.m_root_src = self.m_root_src + DS + "src" + DS + "modules" + DS + "mod_ep_articles"
                self.m_root_src = self.m_root_src + DS + "content_cats" + DS + "content_markdown" 
                self.m_root_src = self.m_root_src + DS + "content_by_catid" + DS + "cat__" + str(psrc)
                
                return self.m_root_src

        def cpy_all(self, par_src, par_dst):

                DS = self.m_ds

                self.m_src = par_src
                self.m_dst = par_dst

                root_src = self.cpy_all_calculate_root_scr_no_groups(
                        par_src)

                root_dst = self.get_root_for_groups(par_dst, 0)

                self.static_copy_file( 
                        root_src
                        , root_dst
                        , "content_idx_0" + DS + "content__0.md"
                        , "content_idx_0" + DS + "content__0.md")

                self.static_copy_file( 
                        root_src
                        , root_dst
                        , "content_idx_0" + DS + "content__0.txt"
                        , "content_idx_0" + DS + "content__0.txt")

                self.static_copy_file( 
                        root_src
                        , root_dst
                        , "title-content__0.md"
                        , "title-content__0.md")

                self.static_copy_file( 
                        root_src
                        , root_dst
                        , "content_pl_0" + DS + "content__0.md"
                        , "content_pl_0" + DS + "content__0.md")

                self.static_copy_file( 
                        root_src
                        , root_dst
                        , "content_idx_0" + DS + "imgs" + DS + "img__placeh.md"
                        , "content_idx_0" + DS + "imgs" + DS + "img__placeh.md")

        def copy_file(self, psrc, pdest):
            
                self.xx_dbg("[METHOD_IN]" + "[copy_file]")
                
                DS = self.m_ds
                self.static_copy_file(
                        self.m_root_src
                        , self.m_root_dst
                        , psrc
                        , pdest)


        def static_copy_file(self, p_root_src, p_root_dst, psrc, pdest):
            
                self.xx_dbg("[METHOD_IN]" + "[static_copy_file]")
                
                DS = self.m_ds

                src_fpath = p_root_src + DS + str(psrc)
                dest_fpath = p_root_dst + DS + str(pdest)

                self.xx_dbg("[src_fpath]" + src_fpath)
                self.xx_dbg("[dest_fpath]" + dest_fpath)
                
                if self.m_test_mode == 1:
                        return
                
                self.xx_dbg("[COPY_START]" + "[src_fpath][" + src_fpath +"]")
                self.xx_dbg("[COPY_START]" + "[to_file][" + dest_fpath +"]")

                try:
                        if not os.path.exists(dest_fpath):
                                shutil.copy(src_fpath, dest_fpath)
                                self.xx_dbg("[COPY_SUCCESS_0]" + "[from][" + src_fpath +"]")
                                self.xx_dbg("[COPY_SUCCESS_0]" + "[to_file][" + dest_fpath +"]")
                        else:
                                self.xx_dbg("[NOT_COPY_FILE_EXISTS_]" + "[from][" + src_fpath +"]")
                                self.xx_dbg("[NOT_COPY_FILE_EXISTS_]" + "[to_file][" + dest_fpath +"]")

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

                        if not os.path.exists(dest_fpath):
                                shutil.copy(src_fpath, dest_fpath)
                                self.xx_dbg("[COPY_SUCCESS_1]" + "[from][" + src_fpath +"]")
                                self.xx_dbg("[COPY_SUCCESS_1]" + "[to_file][" + dest_fpath +"]")
                        else:
                                self.xx_dbg("[NOT_COPY_FILE_EXISTS_]" + "[from][" + src_fpath +"]")
                                self.xx_dbg("[NOT_COPY_FILE_EXISTS_]" + "[to_file][" + dest_fpath +"]")


        def copy_lines_from_file(self, filename_src, filename_dest, lines_from, lines_to):
                self.xx_dbg("[METHOD_IN]" + "[inplace_change]")

                self.xx_dbg("src_file_to_copy:" + filename_src)
                self.xx_dbg("filename_dest:" + filename_dest)

                self.xx_dbg("lines_from:" + str(lines_from))
                self.xx_dbg("lines_to:" + str(lines_to))

                # Safely write the changed content, if found in the file
                lout = []
                with open(filename_src, "r") as f:
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

                with open(filename_dest, "w") as f:
                        f.writelines(lout)

                self.xx_dbg("[METHOD_OUT]" + "[inplace_change]")

        def exec_cpy_contents_mds(self):
                self.exec_cpy_content_mds(4299,4300,110,1000)

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

        def exec_cpy_mds(self):
                # 4298 4409
                src_file = ""
                for x in range(2):
                        xx = 6002 + x
                        self.cpy_all("4299",str(xx))


        def exec_cpy_one(self,idnew):
                self.cpy_all("4299",str(idnew))


        def exec_cpy_many(self, ii_start, ii_max):
                iimax = ii_max
                ii = ii_start
                while( True ):
                        if( ii > iimax):
                                break
                        self.cpy_all(4299,ii)
                        ii = ii + 1

        def copy_one_file(self, par_src, par_dst, file_key):

                DS = self.m_ds

                root_src = self.get_root_for_groups(par_src, 0)
                root_dst = self.get_root_for_groups(par_dst, 0)                

                self.static_copy_file(
                        root_src
                        , root_dst
                        , "content_idx_0" + DS + file_key + ".md"
                        , "content_idx_0" + DS + file_key + ".md"
                        )


        def create_md(self, tt):
                
                self.copy_one_file(2222,4818,"content__rel_items_0")
                self.copy_one_file(2222,4818,"content__rel_tags_0")

        def create_md_all(self, tt,range_start,range_end):
                return
                ddh = LKD_CopyFilesMd("")
                for x in range( range_end ):
                        if(x != 2222):
                                self.copy_one_file(2222,x,"content__rel_items_0")
                                self.copy_one_file(2222,x,"content__rel_tags_0")

if __name__ == "__main__":


        ddh = LKD_CopyFilesMd("")
        ddh.copy_one_file("2222","2223","content__rel_items_0")
        ddh.copy_one_file("2222","2223","content__rel_tags_0")