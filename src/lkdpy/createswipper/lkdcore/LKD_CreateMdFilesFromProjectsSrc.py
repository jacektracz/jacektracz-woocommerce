import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *

from LKD_CreateMdFilesFromSrcDatabase import *
from LKD_CatItem import *
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py
# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py perform-src-files

class LKD_CreateMdFilesFromProjectsSrc:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::__init__::in::")
                self.m_src = "C:/lkd/ht/apps_java8_in_action/app/src/jacek-tracz-java-design-patterns"
                self.m_dst = "services_s3"
                self.m_root_src = ""
                self.m_root_dst = ""
                self.m_test_mode = 0
                #self.m_override_mode = False
                self.m_override_mode = True
                self.m_ds = "/"
                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::__init__::out::")
               
        def get_generic_cats_items(self, dd):
                # return self.get_cats_espn("")
                # return self.get_cats_j8p("")
                # return self.get_cats_sbms("")
                # return self.get_cats_spring_pets("")
                # return self.get_cats_fineract("")
                ddh = LKD_CreateMdFilesFromSrcDatabase()
                return ddh.get_generic_cats_items("")

        def get_generic_root(self, dd):
                # return self.get_root_espn()
                # return self.get_root_j8p()
                # return self.get_root_sbms("")
                # return self.get_root_pets("")
                # return self.get_root_fineract("")
                ddh = LKD_CreateMdFilesFromSrcDatabase()
                return ddh.get_generic_root("")

        
        def prepare_object(self):
                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::prepare_object::in::")
                        
                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::prepare_object::out::")

        #def get_generic_cats_items(self,dd)
        #        return self.get_cats_espn("")

        #def get_generic_root(self,dd)
        #        return self.get_root_espn()

        def execute_main_create_from_source(self):

                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::execute_main_create_from_source::in::")

                paths = self.get_generic_cats_items("")
                postfixes = []    
                direct_subdirs = 0

                if( direct_subdirs == 0):
                        postfixes.append("")

                if( direct_subdirs == 1):
                        postfixes.append("src")
                        postfixes.append("service")
                        postfixes.append("api")
                        postfixes.append("component-test")
                        postfixes.append("client")
                        postfixes.append("server")
                        postfixes.append("project-files")

                for lkd_cat_item in paths:
                        for postfix in postfixes:
                                self.create_execute_source_path_root(lkd_cat_item, postfix)

                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::execute_main::out::")

        def create_execute_source_path_root(self, lkd_cat_item, src_postfix):

                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::create_execute_source_path_root::in::")
                root_scr_path = self.get_generic_root("")
                postfix_2_add = ""
                if( src_postfix != ""):
                        postfix_2_add = "/" + src_postfix

                src_path = root_scr_path + "/" + lkd_cat_item.src_project_relative_path + postfix_2_add

                self.xx_print("read-dir:" + src_path)

                java_files = self.read_directory_subdirs_flat(
                        src_path
                        , lkd_cat_item.catid)

                dd_cxatpath = LKD_CopyFilesMd("")
                rootpath = dd_cxatpath.get_root_for_groups(lkd_cat_item.catid, "0")
                self.xx_print(rootpath)
                dest_java_flat_dir_path = rootpath + "/content_idx_0/javafiles/flat" 
                dest_java_root_idx_0_dir_path = rootpath + "/content_idx_0"

                self.copy_javafiles(
                        java_files)

                self.create_javafiles_md(
                        java_files  
                        , dest_java_root_idx_0_dir_path)

                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::create_execute_source_path_root::out::")


        def create_dir(self, dir_path):

                if os.path.isdir(dir_path):
                        self.xx_dbg("[dir_exists_no_err]" + dir_path)
                else:
                        os.makedirs(dir_path)
                        self.xx_print("dir-created" + dir_path )

        def get_class_name(self):
                return "LKD_CreateMdFilesFromProjectsSrc"

        def read_directory_subdirs_flat(self, psrc_path_project, pcatid):
                s_fun = self.get_class_name() + "::read_directory_subdirs_flat::"
                self.xx_dbg(s_fun + "in::")
                
                print psrc_path_project
                java_files = []
                if(os.path.isdir(psrc_path_project) == False):
                        self.xx_dbg(s_fun + "no-directory-found-" + psrc_path_project)
                        self.xx_dbg(s_fun + "EXIT_ON_START-" + psrc_path_project)
                        return java_files

                print "execute lkd_cat_item"

                dd_cxatpath = LKD_CopyFilesMd("")

                rootpath = dd_cxatpath.get_root_for_groups(pcatid, "0")

                self.xx_print(rootpath)

                dest_java_flat_dir_path = rootpath + "/content_idx_0/javafiles/flat" 

                dest_java_root_idx_0_dir_path = rootpath + "/content_idx_0"

                self.xx_print(dest_java_flat_dir_path)

                self.create_dir(dest_java_flat_dir_path)

                java_files = self.get_files_recur(
                                psrc_path_project
                                , pcatid
                                ,       dest_java_flat_dir_path)


                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::read_directory_subdirs_flat::out::")

                return java_files

        def get_print_files_recur(self,psrc_path_project):
                for x in os.listdir(psrc_path_project):
                        if os.path.isfile(x): print 'f-', x
                        elif os.path.isdir(x): print 'd-', x
                        elif os.path.islink(x): print 'l-', x
                        else: print '---', x

        def copy_javafiles(self, file_items):
                s_fun = self.get_class_name() + "::copy_javafiles::"
                self.xx_dbg(s_fun + "start")
                
                for file_item in file_items:
                        src_fpath = file_item.src_javafile_full_path

                        if(self.check_file_is_valid(src_fpath) == 0):
                                self.xx_dbg(s_fun + "missed_file:" + src_fpath)
                                continue

                        dest_fpath = file_item.dest_java_flat_dir_path + "/" + file_item.src_javafile_name
                        
                        if (len(dest_fpath) > 256):
                                return 0

                        self.xx_dbg("copy-from:" + src_fpath)
                        self.xx_dbg("copy-to:" + dest_fpath)

                        shutil.copy(src_fpath, dest_fpath)

                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::copy_javafiles::out::")

        def check_file_type_is_valid(self, psrc_fpath):
                s_fun = self.get_class_name() + "::check_file_is_valid::"
                self.xx_dbg(s_fun + "start")

        def check_file_is_valid(self, psrc_fpath):
                s_fun = self.get_class_name() + "::check_file_is_valid::"
                self.xx_dbg(s_fun + "start")

                self.xx_dbg(s_fun + "psrc_fpath:" + psrc_fpath)

                if (len(psrc_fpath) > 256):
                        return 0

                
                needles = []
                needles.append("target")
                needles.append(".git")
                needles.append("node_modules")
                is_valid = 1
                for needle in needles:
                        self.xx_dbg(s_fun + "needle:" + needle)
                        
                        is_match = self.is_match(psrc_fpath, needle)
                        self.xx_dbg(s_fun + "is_match_ext:" + str(is_match))
                        if( is_match == 1):
                                is_valid = 0
                                break
                
                self.xx_dbg(s_fun + "is_valid_end:" + str(is_valid))
                self.xx_dbg(s_fun + "end")
                return is_valid

        def is_match(self, psrc, needle):
                s_fun = self.get_class_name() + "::is_match::"
                self.xx_dbg(s_fun + "start")

                self.xx_dbg(s_fun + "psrc:" + psrc)
                self.xx_dbg(s_fun + "needle:" + needle)

                is_match= 0
                idxf = psrc.find( needle )
                self.xx_dbg(s_fun + "idxf:" + str(idxf))
                if( idxf >= 0):
                        is_match = 1

                self.xx_dbg(s_fun + "is_match:" + str(is_match))

                self.xx_dbg(s_fun + "end")
                return is_match

        def create_javafiles_md(self, file_items , dest_java_root_idx_0_dir_path):
                s_fun = self.get_class_name() + "::create_javafiles_md::"
                self.xx_dbg(s_fun + "start")
                ii = 0
                for file_item in file_items:

                        self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::create_javafiles_md::execute_one_item_start::")

                        src_fpath = file_item.src_javafile_full_path

                        src_fpath = file_item.src_javafile_full_path
                        if(self.check_file_is_valid(src_fpath) == 0):
                                self.xx_dbg(s_fun + "missed_onf_file_item:" + src_fpath)
                                continue

                        dest_fpath = file_item.dest_java_flat_dir_path + "/" + "content__java_files.md"

                        dest_root_fpath = dest_java_root_idx_0_dir_path + "/" + "content__java_files.md"

                        self.xx_dbg("copy-from:" + src_fpath)
                        self.xx_dbg("copy-to:" + dest_fpath)    
                        file_header = "### Source File: " + file_item.src_javafile_name                        

                        if (ii == 1):                                
                                self.create_empty_file(src_fpath, dest_fpath , file_header)
                                self.create_empty_file(src_fpath, dest_root_fpath , file_header)

                        self.copy_lines_from_file(src_fpath, dest_fpath , file_header)

                        self.copy_lines_from_file(src_fpath, dest_root_fpath , file_header)

                        self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::create_javafiles_md::execute_one_item_end::")
                        ii = ii + 1

                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::create_javafiles_md::out::")


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

        def create_empty_file(self, filename_src, filename_dest, pfileheader):
                lout = []
                with open(filename_dest, "w") as f:
                        f.writelines(lout)

        def copy_lines_from_file(self, filename_src, filename_dest, pfileheader):
                self.xx_dbg("[METHOD_IN]" + "[inplace_change]")

                self.xx_dbg("src_file_to_copy:" + filename_src)
                self.xx_dbg("filename_dest:" + filename_dest)


                # Safely write the changed content, if found in the file
                lout = []
                with open(filename_src, "r") as f:
                        lines = f.readlines()                         
                        lout.append("\r\n")
                        lout.append("\r\n")
                        lout.append(pfileheader)
                        lout.append("\r\n")
                        lout.append("\r\n")
                        lout.append("```Java")
                        lout.append("\r\n")
                        for line in lines:
                                lout.append(line)
                        lout.append("\r\n")
                        lout.append("```")

                with open(filename_dest, "a") as f:
                        f.writelines(lout)

                self.xx_dbg("[METHOD_OUT]" + "[inplace_change]")

        def read_directory_subdirs_only(self, psrc_path_project):
                #self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::read_directory_subdirs_flat::in::")
                print psrc_path_project

                if(os.path.isdir(psrc_path_project) == False):
                        return

                print "execute lkd_cat_item"

                for x in os.listdir(psrc_path_project):
                        if os.path.isdir(x): 
                                print x

                #self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::read_directory_subdirs_flat::out::")

                

        def get_item(self, id,title):
                dd = LKD_CatItem(id,title)
                return dd

        def xx_dbg(self, tt):
                "" ""
                print ( tt )

        def xx_print( self, tt ):
                "" ""
                print ( tt )       

        def read_directory_subdirs(self):

                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::read_directory_subdirs::in::")
                folders = []
                for r, d, f in os.walk(lkd_cat_item):
                        for folder in d:
                                folders.append(os.path.join(r, folder))

                for f in folders:
                        print(f)

                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::read_directory_subdirs::out::")


        def print_cats_for_dirs_db(self, tt):                
                psrc_path_project = "C:/lkd/ht/apps_spring_pro_jpa_2/app/src/pro-jpa-2/examples"
                #self.print_cats_for_dirs_lvl2(psrc_path_project)
                #self.a(psrc_path_project)
                #self.get_print_files_recur(psrc_path_project)
                self.get_print_files_l2(psrc_path_project)


        def print_cats_for_dirs(self, psrc_path_project):                
                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::print_cats_for_dirs::in::")
                for currentpath, folders, files in os.walk(psrc_path_project):
                        for folder in folders:
                                self.xx_dbg(folder)

        def print_cats_for_dirs_lvl2(self, psrc_path_project):                
                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::print_cats_for_dirs::in::")
                for folders in os.listdir(psrc_path_project):
                        for folder in folders:
                                self.xx_dbg(folder) 
                                if os.path.isdir(folder):
                                        self.xx_dbg(folder)                                


        def get_print_files_recur(self,psrc_path_project):
                for x in os.listdir(psrc_path_project):
                        if os.path.isfile(x): print 'f-', x
                        elif os.path.isdir(x): print 'd-', x
                        elif os.path.islink(x): print 'l-', x
                        else: print '---', x

        def get_print_files_l2(self,psrc_path_project):
                for x1 in os.listdir(psrc_path_project):                        
                        p2 = psrc_path_project + "/" + x1
                        if os.path.isdir(p2): 
                                print '    ', x1                                
                                for x2 in os.listdir(p2):    
                                        p3 = p2 + "/" + x2    
                                        if os.path.isdir(p3): 
                                                print '         ', x2

        def a(self,path):
                list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]
                # print(len(list_subfolders_with_paths))


        def b():
                list_subfolders_with_paths = [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
                # print(len(list_subfolders_with_paths))


        def c():
                list_subfolders_with_paths = []
                for root, dirs, files in os.walk(path):
                        for dir in dirs:
                                list_subfolders_with_paths.append( os.path.join(root, dir) )
                        break
                # print(len(list_subfolders_with_paths))

        def d():
                list_subfolders_with_paths = glob.glob(path + '/*/')
        # print(len(list_subfolders_with_paths))

        def e():
                list_subfolders_with_paths = list(filter(os.path.isdir, [os.path.join(path, f) for f in os.listdir(path)]))
        # print(len(list(list_subfolders_with_paths)))

        def f():
                p = pathlib.Path(path)
                list_subfolders_with_paths = [x for x in p.iterdir() if x.is_dir()]
                # print(len(list_subfolders_with_paths))
