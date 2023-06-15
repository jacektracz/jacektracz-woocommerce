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
        #

        def execute_main_create_content_from_source(self):
                s_fun = self.get_class_name() + "::execute_main_create_from_source::"
                self.xx_dbg(s_fun + "start::")        
                
                ddh = LKD_CreateMdFilesFromSrcDatabase()
                data_items =  ddh.get_generic_cats_data("")

                for lkd_cats_group_item in data_items:
                        self.xx_dbg("cat_items_path_start_::" + lkd_cats_group_item.get_src_root_dir_path())
                        self.execute_main_create_from_source_one_items_group(
                                lkd_cats_group_item.get_src_root_dir_path(),
                                lkd_cats_group_item.get_src_root_child_cats()
                        )
                        self.xx_dbg("cat_items_path_end_::" + lkd_cats_group_item.get_src_root_dir_path())

                self.xx_dbg(s_fun + "end::")

        def execute_main_create_from_source_depr(self):

                s_fun = self.get_class_name() + "::execute_main_create_from_source::"
                self.xx_dbg(s_fun + "start::")                

                cats_items = self.get_generic_cats_items("")

                for lkd_cat_item in cats_items:
                        self.xx_dbg("cat_items_path::" + lkd_cat_item.src_project_relative_path)

                root_scr_path = self.get_generic_root("")

                self.xx_dbg(s_fun + "root_scr_path::" + root_scr_path)

                self.execute_main_create_from_source_internal(
                        cats_items
                        , root_scr_path)

                self.xx_dbg(s_fun + "end::")

        def execute_main_create_from_source_one_items_group(self,root_scr_path,cats_items):

                s_fun = self.get_class_name() + "::execute_main_create_from_source::"
                self.xx_dbg(s_fun + "start::")                

                for lkd_cat_item in cats_items:
                        self.xx_dbg("cat_items_path::" + lkd_cat_item.src_project_relative_path)                

                self.xx_dbg(s_fun + "root_scr_path::" + root_scr_path)

                self.execute_main_create_from_source_internal(
                        cats_items
                        , root_scr_path)

                self.xx_dbg(s_fun + "end::")

        def execute_main_create_from_source_internal(self, paths, root_scr_path):
                s_fun = self.get_class_name() + "::execute_main_create_from_source_internal::"
                self.xx_dbg(s_fun + "start::")                                

                for lkd_cat_item in paths:
                        self.xx_dbg("paths::" + lkd_cat_item.src_project_relative_path)

                postfixes = []    

                direct_subdirs = 0

                if( direct_subdirs == 0):
                        postfixes.append("")

                if( direct_subdirs == 1): # not-used
                        postfixes = self.get_direct_subdirs_to_execute()

                for lkd_cat_item in paths:
                        for postfix in postfixes:
                                self.create_execute_source_path_root(
                                        lkd_cat_item
                                        , postfix
                                        , root_scr_path)

                self.xx_dbg(s_fun + "end::")

        def get_direct_subdirs_to_execute():
                s_fun = self.get_class_name() + "::create_dir::"
                self.xx_dbg(s_fun + "start::")
                postfixes = []
                postfixes.append("src")
                postfixes.append("service")
                postfixes.append("api")
                postfixes.append("kafka")
                postfixes.append("scripts")
                postfixes.append("zookepeer")                        
                postfixes.append("component-test")
                postfixes.append("client")
                postfixes.append("server")
                postfixes.append("project-files")
                postfixes.append("")
                self.xx_dbg(s_fun + "end::")
                return postfixes

        
        def create_execute_source_path_root(self, lkd_cat_item, src_postfix, root_scr_path):

                self.xx_dbg("LKD_CreateMdFilesFromProjectsSrc::create_execute_source_path_root::in::")
                
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
                s_fun = self.get_class_name() + "::create_dir::"
                self.xx_dbg(s_fun + "start::")

                if os.path.isdir(dir_path):
                        self.xx_dbg("[dir_exists_no_err]" + dir_path)
                else:
                        os.makedirs(dir_path)
                        self.xx_print("dir-created" + dir_path )
                self.xx_dbg(s_fun + "end::")


        def get_class_name(self):
                return "LKD_CreateMdFilesFromProjectsSrc"

        def read_directory_subdirs_flat(self, psrc_path_project, pcatid):
                s_fun = self.get_class_name() + "::read_directory_subdirs_flat::"
                self.xx_dbg(s_fun + "in::")
                self.xx_dbg(s_fun + "in::psrc_path_project::" + psrc_path_project)
                
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

                needles_files = []                
                needles_files.append(".java")
                needles_files.append(".ts")
                needles_files.append(".js")
                needles_files.append(".yaml")
                needles_files.append(".yml")
                needles_files.append(".properties")
                # removed html
                #needles_files.append(".html")
                #needles_files.append(".htm")
                needles_files.append(".json")

                excludes_files = []
                exludes_short = 1
                exludes_long = 0

                if (exludes_long == 1 ) :
                        excludes_files = self.get_exclued_files()

                if (exludes_short == 1 ) :
                        excludes_files = self.get_exclued_files_short()

                is_valid = 1
                for exclude_file in excludes_files:
                        self.xx_dbg(s_fun + "needle:" + exclude_file)
                        
                        is_match = self.is_match(psrc_fpath, exclude_file)
                        self.xx_dbg(s_fun + "is_match_ext:" + str(is_match))
                        if( is_match == 1):
                                self.xx_dbg(s_fun + "is_valid_match_0:" + str(is_valid))
                                is_valid = 0
                                break   

                if is_valid == 0:
                        self.xx_dbg(s_fun + "is_valid_end_0:" + str(is_valid))
                        self.xx_dbg(s_fun + "end")
                        return 0

                if len(needles_files) == 0 : 
                        self.xx_dbg(s_fun + "is_valid_end_1_needles_count_0:" + str(is_valid))
                        self.xx_dbg(s_fun + "end")
                        return is_valid

                is_valid = 0
                for needle in needles_files:
                        self.xx_dbg(s_fun + "needle_in_needles:" + needle)
                        
                        is_match = self.is_match(psrc_fpath, needle)
                        self.xx_dbg(s_fun + "is_match_needle_1_ext:" + str(is_match))
                        if( is_match == 1):
                                self.xx_dbg(s_fun + "is_valid_match_needle_1:" + str(is_valid))
                                is_valid = 1
                                break   

                self.xx_dbg(s_fun + "is_valid_after_needles_end_2:" + str(is_valid))
                self.xx_dbg(s_fun + "end")

                return is_valid



        def is_match(self, psrc, needle):
                s_fun = self.get_class_name() + "::is_match::"
                self.xx_dbg(s_fun + "start")

                self.xx_dbg(s_fun + "psrc:" + psrc)
                self.xx_dbg(s_fun + "needle:" + needle)

                is_match= 0
                idxf = psrc.lower().find( needle.lower() )
                self.xx_dbg(s_fun + "idxfound:" + str(idxf))
                if( idxf >= 0):
                        is_match = 1

                self.xx_dbg(s_fun + "psrc:" + psrc)
                self.xx_dbg(s_fun + "needle:" + needle)
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

                        #
                        #
                        #if self.is_match(src_fpath,"png") == 1:
                        #        continue
                        #
                        #

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
                self.xx_dbg(s_fun + "end")


        def get_files_recur(self, psrc_path_project, pcatid, pdest_java_flat_dir_path):

                s_fun = self.get_class_name() + "::get_files_recur::"
                self.xx_dbg(s_fun + "start")
                self.xx_dbg(s_fun + "psrc_path_project:" + psrc_path_project)

                fjavafiles = []
                for root,d_names,f_names in os.walk(psrc_path_project):
	                for f in f_names:

                                self.xx_dbg(s_fun + "read_file_name:" + f)
                                self.xx_dbg(s_fun + "read_file_root:" + root)

                                dd = LKD_CatItem(pcatid, psrc_path_project)
                                dd.catid = pcatid
                                dd.src_project_relative_path = psrc_path_project
                                dd.src_javafile_full_path = os.path.join(root, f)
                                created_file_name = self.join_java_name_with_path_from_src(root,f)
                                dd.src_javafile_name = created_file_name
                                self.xx_dbg(s_fun + "created_file_name:" + created_file_name)
                                dd.dest_java_flat_dir_path = pdest_java_flat_dir_path
                                self.xx_dbg(s_fun + "pdest_java_flat_dir_path:" + pdest_java_flat_dir_path)

		                fjavafiles.append(dd)

                self.xx_dbg(s_fun + "end")

                return fjavafiles


        def join_java_name_with_path_from_src(self, file_path, file_name):
                s_fun = self.get_class_name() + "::get_files_recur::"
                self.xx_dbg(s_fun + "start")
                self.xx_dbg(s_fun + "file_name:" + file_name)
                self.xx_dbg(s_fun + "file_path:" + file_path)

                joined_name = file_name
                idx_src = file_path.find("src")
                path_from_src = ""
                if(idx_src >= 0):
                        path_from_src = file_path[idx_src:]
                        path_from_src = path_from_src.replace("//","-")
                        path_from_src = path_from_src.replace("/","-")
                        path_from_src = path_from_src.replace("\\","-")
                else:
                        path_from_src = ""                        

                joined_name = path_from_src + "___" + file_name

                self.xx_dbg(s_fun + "joined_name:" + joined_name)
                self.xx_dbg(s_fun + "start")
                return joined_name


        def create_empty_file(self, filename_src, filename_dest, pfileheader):
                s_fun = self.get_class_name() + "::create_empty_file::"
                self.xx_dbg(s_fun + "start")
                self.xx_dbg(s_fun + "filename_src:" + filename_src)
                self.xx_dbg(s_fun + "filename_dest:" + filename_dest)
                self.xx_dbg(s_fun + "pfileheader:" + pfileheader)

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

        def get_print_files_l2(self, psrc_path_project):
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

        def get_exclued_files_short(self):
                excludes_files = []
                excludes_files.append("npms")
                excludes_files.append("target")
                excludes_files.append("webpack")
                excludes_files.append(".git")
                excludes_files.append(".svg")
                excludes_files.append(".class")
                excludes_files.append(".bin")
                excludes_files.append(".png")
                excludes_files.append(".lock")
                excludes_files.append(".jar")
                excludes_files.append(".xml")
                excludes_files.append("node_modules")
                excludes_files.append("bootstrap.min.css")
                excludes_files.append("bootstrap.css")
                excludes_files.append("mvnw.cmd")
                excludes_files.append("npm.cmd")
                excludes_files.append("npm")
                excludes_files.append("gradlew")
                excludes_files.append("gradlew.bat")
                excludes_files.append("changelog.md")
                excludes_files.append("SHANGELOG.md.md")
                return excludes_files


        def get_exclued_files(self):
                excludes_files = []
                excludes_files.append("npms")
                excludes_files.append("target")
                excludes_files.append("webpack")
                excludes_files.append(".git")
                excludes_files.append(".svg")
                excludes_files.append(".class")
                excludes_files.append(".bin")
                excludes_files.append(".png")
                excludes_files.append(".lock")
                excludes_files.append(".jar")
                excludes_files.append(".xml")
                excludes_files.append("node_modules")
                excludes_files.append("bootstrap.min.css")
                excludes_files.append("bootstrap.css")
                excludes_files.append("mvnw.cmd")
                excludes_files.append("npm.cmd")
                excludes_files.append("npm")
                excludes_files.append("gradlew")
                excludes_files.append("gradlew.bat")
                excludes_files.append("changelog.md")
                excludes_files.append("SHANGELOG.md.md")

                excludes_files.append("Adres")
                excludes_files.append("Biuro")
                excludes_files.append("Biurouzytkownik")
                excludes_files.append("Createagreement")
                excludes_files.append("Danefirmy")
                excludes_files.append("Dddw")
                excludes_files.append("Dochod")
                excludes_files.append("Dokument")
                excludes_files.append("Dokwezwaniezawiadomienie")
                excludes_files.append("Efektdzialania")
                excludes_files.append("Executecreateagreement")
                excludes_files.append("GenericRowValue")
                excludes_files.append("GenericTableRow")
                excludes_files.append("IssfakturaHistoria")
                excludes_files.append("Issfaktura")
                excludes_files.append("IsspodmiotHistoria")
                excludes_files.append("Isspodmiot")
                excludes_files.append("Issuzytkownikbank")
                excludes_files.append("JhiAuthority")
                excludes_files.append("JhiPersistentAuditEvent")
                excludes_files.append("JhiUserAuthority")
                excludes_files.append("JhiUser")
                excludes_files.append("Joo2Categories")
                excludes_files.append("Joo2Content")
                excludes_files.append("Joo2Modules")
                excludes_files.append("Konfiguracjacrm")
                excludes_files.append("Kontakt")
                excludes_files.append("Koszt")
                excludes_files.append("Kwotapozyczki")
                excludes_files.append("Loanitemdef")
                excludes_files.append("Loanpaymentamounts")
                excludes_files.append("Naleznosc")
                excludes_files.append("NoClass")
                excludes_files.append("Notatka")
                excludes_files.append("Operationstatus")
                excludes_files.append("Oprepaymentbasic")
                excludes_files.append("Oprepaymet")
                excludes_files.append("Osobafizyczna")
                excludes_files.append("Planprzychodu")
                excludes_files.append("Podejrzanywpis")
                excludes_files.append("Produkt")
                excludes_files.append("Profil")
                excludes_files.append("Przedmiotprzewlaszczenia")
                excludes_files.append("Przedmiotprzewlaszczeniaumowa")
                excludes_files.append("Przewlaszczenie")
                excludes_files.append("Przewlaszczenieumowa")
                excludes_files.append("Rata")
                excludes_files.append("Skandokumentu")
                excludes_files.append("Splatanaleznosci")
                excludes_files.append("Splataraty")
                excludes_files.append("Splata")
                excludes_files.append("Systemactionctx")
                excludes_files.append("Systemaction")
                excludes_files.append("Systemfield")
                excludes_files.append("Systemgeneralctx")
                excludes_files.append("Systemparameter")
                excludes_files.append("Systemprofile")
                excludes_files.append("Systemviewprofile")
                excludes_files.append("Systemview")
                excludes_files.append("Telefon")
                excludes_files.append("Umorzenienaleznosci")
                excludes_files.append("Umorzenie")
                excludes_files.append("Umowa")
                excludes_files.append("Upowaznienie")
                excludes_files.append("Uprawnienieprofilu")
                excludes_files.append("Uprawnienie")
                excludes_files.append("Uzytkownikbank")
                excludes_files.append("Uzytkownik")
                excludes_files.append("Windykacja")
                excludes_files.append("Zatrudnienie")
                return excludes_files

# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py perform-src-files