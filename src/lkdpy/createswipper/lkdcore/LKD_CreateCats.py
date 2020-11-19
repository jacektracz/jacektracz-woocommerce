import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *

from LKD_CreateFilesDatabase import *
from LKD_CatItem import *
#  C:/lkd/servers/installed/python27/python C:/lkd/ht/apps_w2_risk/app/src/apps_w2_w2/src/lkdpy/start_cpy.py
# C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles/content_cats/content_markdown/content_by_groups/cat__8000/cat__000/cat__00/cat__8000/content_idx_0/content__cats_2_add.md
# C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\createswipper\lkdcore\LKD_CreateCats.py
class LKD_CreateCats:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CopyFiles::__init__::in::")
                self.m_src = "C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles/content_cats/content_markdown/content_by_groups/cat__8000/cat__000/cat__00/cat__8000/content_idx_0/content__cats_2_add.md"
                self.m_src_short = "C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles/content_cats/content_markdown/content_by_groups/cat__8000/cat__000/cat__00/cat__8000/content_idx_0/content__cats_2_add_short.md"
                self.m_dst = "C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles/content_cats/content_markdown/content_by_groups/cat__8000/cat__000/cat__00/cat__8000/content_idx_0/content__cats_2_add_dst.md"
                self.m_dst_bat = "C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles/content_cats/content_markdown/content_by_groups/cat__8000/cat__000/cat__00/cat__8000/content_idx_0/content__cats_2_add_dst.bat"
                self.m_root_src = ""
                self.m_root_dst = ""
                self.m_test_mode = 0
                self.m_add_spaces_count = 0
                self.m_exec_remove_toc = 0
                self.m_exec_inplace_change = 1
                self.m_add_idx_prefixes = 1
                self.m_exec_write = 1
                self.m_exec_main_prepare_in_one_bucket = 0
                self.m_exec_main_prepare_in_buckets = 0
                self.m_exec_main_create_dirs = 1
                self.m_override_mode = True
                self.m_ds = "/"
                self.xx_dbg("LKD_CopyFiles::__init__::out::")

        def class_name(self):
                return "LKD_CreateCats::"

        def xx_dbg(self, tt ):
                s_fun = self.class_name() + "::set_execute_main_toc::"
                print tt

        def xx_dbg_1(self, tt ):
                s_fun = self.class_name() + "::set_execute_main_toc::"
                # print tt

        def xx_dbg_line(self, tt ):
                s_fun = self.class_name() + "::set_execute_main_toc::"
                print tt

        def set_execute_main_toc(self, tt):
                s_fun = self.class_name() + "::set_execute_main_toc::"
                self.xx_dbg(s_fun + "start")
                self.m_exec_remove_toc = 1
                self.m_exec_inplace_change = 0
                self.m_add_spaces_count = 0

        def set_execute_main_write_mkdirs(self, tt):
                s_fun = self.class_name() + "::set_execute_main_write_mkdirs::"
                self.xx_dbg(s_fun + "start")
                self.m_exec_remove_toc = 0
                self.m_exec_inplace_change = 1
                self.m_add_spaces_count = 0

        def execute_main(self,tt):
                s_fun = self.class_name() + "::execute_cdirs::"
                self.xx_dbg(s_fun + "start")

                if self.m_exec_main_prepare_in_one_bucket == 1:
                        self.execute_main_prepare_in_one_bucket("")

                if self.m_exec_main_prepare_in_buckets == 1:
                        self.execute_main_prepare_in_buckets("")

                if self.m_exec_main_create_dirs == 1:
                        self.execute_main_create_dirs("")

                self.xx_dbg(s_fun + "end")


        def execute_main_prepare_in_one_bucket(self,tt):
                s_fun = self.class_name() + "::execute_main_prepare_in_one_bucket::"
                self.xx_dbg(s_fun + "start")

                dst_file = self.m_dst                
                dst_file_bat = self.m_dst_bat
                src_file = self.m_src

                lines = self.read_lines_from_file(
                        src_file)

                lines = self.get_lines_clear_normalized(
                        lines)

                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        dst_file_bat
                        , lines)

                self.print_lines(
                        dst_file
                        , lines)

        def execute_main_prepare_in_buckets(self,tt):
                s_fun = self.class_name() + "::execute_main_prepare_in_buckets::"
                self.xx_dbg(s_fun + "start")


                dst_file = self.m_dst
                src_file = self.m_src_short
                src_file = self.m_src

                lines = []
                lines = self.read_lines_from_file(
                        src_file)
               
                lines = self.get_lines_clear_normalized_in_buckets(
                        lines)

                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        self.m_dst_bat
                        , lines)

                self.print_lines(
                        dst_file
                        , lines)

                self.xx_dbg(s_fun + "end")


        def execute_main_create_dirs(self,tt):
                s_fun = self.class_name() + "::execute_main_create_dirs::"
                self.xx_dbg(s_fun + "start")

                # self.set_execute_main_toc("")
                # self.set_execute_main_write_mkdirs("")

                dst_file = self.m_dst
                src_file = self.m_src_short
                src_file = self.m_src

                lines = []
                lines = self.read_lines_from_file(
                        src_file)

                self.print_lines(
                        "read_lines_from_file"
                        , lines)
                
                lines = self.inplace_change_lines(
                        lines)

                self.print_lines(
                        "inplace_change"
                        , lines)

                
                self.print_lines(
                        "get_lines_to_write"
                        , lines)

                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        self.m_dst_bat
                        , lines)

                self.print_lines(
                        dst_file
                        , lines)

                self.xx_dbg(s_fun + "end")
        
        def get_lines_clear_normalized_in_buckets(
                self
                , plines):

                s_fun = self.class_name() + "::get_lines_clear_normalized_in_buckets::"
                self.xx_dbg(s_fun + "start")
                lines = plines
                lines = self.get_lines_without_empty(
                        lines)

                self.print_lines(
                        "get_lines_without_empty"
                        , lines)

                lines = self.get_lines_with_removed_toc(
                        lines)

                self.print_lines(
                        "get_lines_with_removed_toc"
                        , lines)

                lines = self.get_lines_normalize_multiple_item_direct(
                        "  "
                        , " "
                        , lines
                        )

                self.print_lines(
                        "get_lines_normalize_multiple_item"
                        , lines)

                lines = self.get_lines_space_to_break(
                        lines)

                self.print_lines(
                        "get_lines_space_to_break"
                        , lines)

                lines = self.get_lines_normalize_multiple_item_direct(
                        "--"
                        , "-"
                        , lines
                        )

                self.print_lines(
                        "get_lines_normalize_multiple_item_direct"
                        , lines)

                lines = self.get_lines_without_special_chars(
                        lines)

                self.print_lines(
                        "get_lines_without_special_chars"
                        , lines)                
                return lines


        def get_lines_clear_normalized(
                self
                , lines):

                s_fun = self.class_name() + "::get_lines_clear_normalized::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = self.get_line_clear_normalized(
                                line)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out


        def get_lines_without_special_chars(
                self                
                , lines):

                s_fun = self.class_name() + "::print_lines_stripped::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:
                        line_strip = line.rstrip()
                        line_strip = self.get_line_without_special_chars(
                                line_strip)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out


        def get_line_clear_normalized(    
                self
                , line):
                s_fun = self.class_name() + "::get_line_clear_normalized::"
                self.xx_dbg(s_fun + "start")

                sp_0 = self.tabs_prefix_cnt( line )
                s_tab_prefix = self.get_tabs_prefix(sp_0)

                line = line.strip()                

                line = self.get_line_with_removed_toc(
                        line)

                line = self.get_line_normalize_multiple_item(
                        " "
                        , line)

                line = self.get_line_with_space_to_break(
                        line)

                line = self.get_line_normalize_multiple_item(
                        "-"
                        , line)

                line = self.get_line_without_special_chars(
                        line)


                line = s_tab_prefix + line

                self.xx_dbg(s_fun + "end")

                return line

        def get_lines_without_empty(
                self
                , lines):

                s_fun = self.class_name() + "::get_lines_with_removed_toc::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = line
                        if(line_strip != ""):
                                lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_lines_with_removed_toc(
                self
                , lines):

                s_fun = self.class_name() + "::get_lines_with_removed_toc::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = self.get_line_with_removed_toc(
                                line)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_lines_space_to_break(
                self
                , lines):

                s_fun = self.class_name() + "::get_lines_space_to_break::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = self.get_line_with_space_to_break(
                                line)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_lines_normalize_multiple_item_direct(
                self
                , p_from
                , p_to
                , lines):

                s_fun = self.class_name() + "::get_lines_normalize_multiple_item_direct::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = self.get_line_normalize_multiple_item_direct(
                                p_from
                                ,p_to
                                ,line)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_lines_normalize_multiple_item(
                self
                , p_item
                , lines):

                s_fun = self.class_name() + "::get_lines_normalize_multiple_item::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = self.get_line_normalize_multiple_item(
                                p_item
                                ,line)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_line_with_removed_toc(
                self
                , pline):

                s_fun = self.class_name() + "::get_line_with_removed_toc::"                
                line = pline

                sp_0 = self.tabs_prefix_cnt( line )
                s_tab_prefix = self.get_tabs_prefix(sp_0)
                line = line.strip()

                for kk in range(4):
                        for ii in range(10):
                                s_toc = ".." + str(ii)
                                line = line.replace(s_toc, " ")
                                s_toc = ". ." + str(ii)
                                line = line.replace(s_toc, " ")
                                s_toc = " " + str(ii)
                                line = line.replace(s_toc, "xx")
                                s_toc = "xx" + str(ii)
                                line = line.replace(s_toc, "xx")

                line = line.replace( "xx","")

                line = s_tab_prefix + line

                self.xx_dbg_1(s_fun + "line:" + line)
                return line

        
        def get_line_normalize_multiple_item(    
                self
                , s_item
                , line):
                s_fun = self.class_name() + "::get_line_normalize_multiple_item::"
                self.xx_dbg(s_fun + "start")

                sp_0 = self.tabs_prefix_cnt( line )
                s_tab_prefix = self.get_tabs_prefix(sp_0)
                line = line.strip()

                for kk in range(10):
                        s_from = s_item + s_item
                        s_to = s_item
                        line = line.replace( s_from, s_to)

                line = s_tab_prefix + line

                self.xx_dbg(s_fun + "end")
                return line

        def get_line_normalize_multiple_item_direct(    
                self
                , s_from
                , s_to
                , line):
                s_fun = self.class_name() + "::get_line_normalize_multiple_item_direct::"
                self.xx_dbg(s_fun + "start")

                self.xx_dbg(s_fun + "replace_from[" + s_from + "]")
                self.xx_dbg(s_fun + "replace_to[" + s_to + "]")

                sp_0 = self.tabs_prefix_cnt( line )
                s_tab_prefix = self.get_tabs_prefix(sp_0)
                line = line.strip()

                self.xx_dbg_1(s_fun + "line_to_replace[" + line + "]")

                for kk in range(10):                        
                        line = line.replace( s_from, s_to)

                line = s_tab_prefix + line

                self.xx_dbg_1(s_fun + "line_replaced[" + line + "]")

                self.xx_dbg(s_fun + "end")
                return line


        def get_line_with_breaks_to_space(
                self
                , pline):

                s_fun = self.class_name() + "::get_line_with_breaks_to_space::"                
                self.xx_dbg_1(s_fun + "start")
                line = pline
                line = line.replace("-"," ")
                self.xx_dbg_1(s_fun + "start")
                return line

        def get_line_with_space_to_break(
                self
                , pline):

                s_fun = self.class_name() + "::get_line_with_space_to_break::"                
                self.xx_dbg_1(s_fun + "start")
                line = pline

                sp_0 = self.tabs_prefix_cnt( line )
                s_tab_prefix = self.get_tabs_prefix(sp_0)
                line = line.strip()

                line = line.replace(" ","-")

                line = s_tab_prefix + line

                self.xx_dbg_1(s_fun + "start")
                return line

        def get_line_with_breaks_to_empty(
                self
                , pline):

                s_fun = self.class_name() + "::get_line_with_breaks_to_space::"                
                self.xx_dbg_1(s_fun + "start")
                line = pline
                sp_0 = self.tabs_prefix_cnt( line )
                s_tab_prefix = self.get_tabs_prefix(sp_0)
                line = line.strip()

                line = line.replace("-","")

                line = s_tab_prefix + line
                self.xx_dbg_1(s_fun + "start")
                return line

        def get_line_without_special_chars(
                self
                , pline):

                s_fun = self.class_name() + "::get_line_without_special_chars::"                
                self.xx_dbg_1(s_fun + "atart")

                line = pline                

                sp_0 = self.tabs_prefix_cnt( line )
                s_tab_prefix = self.get_tabs_prefix(sp_0)
                line = line.strip()

                line = line.replace("?","")                
                line = line.replace(";","")
                line = line.replace(",","")
                line = line.replace(":","")
                line = line.replace("[","")
                line = line.replace("]","")
                line = line.replace("(","")
                line = line.replace(")","")
                line = line.replace("~","")
                line = line.replace("`","")                
                line = line.replace("!","")                
                line = line.replace("@","")                
                line = line.replace("#","")
                line = line.replace("$","")                
                line = line.replace("%","")                
                line = line.replace("^","")                
                line = line.replace("&","")
                line = line.replace("*","")                
                line = line.replace("(","")                
                line = line.replace(")","")                
                #line = line.replace("_","")                
                
                line = line.replace("+","")                
                line = line.replace("=","")                
                line = line.replace("{","")                
                line = line.replace("[","")                
                line = line.replace("]","")                
                line = line.replace("}","")                

                line = line.replace(":","")                
                line = line.replace(";","")                
                line = line.replace('"',"")                
                line = line.replace("<","")                
                line = line.replace(",","")                
                line = line.replace(">","")                                
                line = line.replace("?","")
                line = line.replace("/","")
                line = line.replace("|","")
                line = line.replace( "xx","")

                line = s_tab_prefix + line
                self.xx_dbg_1(s_fun + "line:" + line)                

                return line
        
        def get_idx_prefix(
                self
                , p_ii):

                s_fun = self.class_name() + "::get_idx_prefix::"
                self.xx_dbg(s_fun + "start")                             
                s_ii = "ABCDEFGHIJKLMNOPQRSTUWXYZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
                s_out = ""
                if(p_ii < 100 ):
                        for kk in range(10):
                                kk_bound  = kk * 10
                                if(kk_bound > p_ii):
                                        s_out = s_ii[kk:kk+1]
                                        break

                if s_out == "":
                        for kk in range(10):
                                kk_bound  = kk * 100
                                if(kk_bound > p_ii):
                                        s_out = s_ii[10 + kk:10 + kk + 1]
                                        break

                return s_out      

        def read_lines_from_file(
                self
                , filename):

                s_fun = self.class_name() + "::read_lines_from_file::"
                self.xx_dbg(s_fun + "start")

                file_lines = []
                with open(filename) as f:
                        file_lines = f.readlines()

                lines_out = self.get_lines_stripped(
                        file_lines)

                self.xx_dbg(s_fun + "end")
                return lines_out

        def create_bat_file(
                self
                , filename
                , lines):

                s_fun = self.class_name() + "::write_lines::"
                self.xx_dbg(s_fun + "start")

                with open(filename, "w") as f:
                        f.write( "rem " + filename + "\n")
                        f.write( "cd C:/lkd/ht/apps_ctx/1" + "\n")

                        for line in lines:
                                f.write( line + "\n")

                        f.write( "cd C:/lkd/ht/apps_ctx/1" + "\n")

                self.xx_dbg(s_fun + "end")


        def write_lines(
                self
                , filename
                , lines):

                s_fun = self.class_name() + "::write_lines::"
                self.xx_dbg(s_fun + "start")

                with open(filename, "w") as f:
                        for line in lines:
                                f.write( line + "\n")

                self.xx_dbg(s_fun + "end")

        def rstrip_lines(
                self
                , filename
                , lines):

                s_fun = self.class_name() + "::write_lines::"
                self.xx_dbg(s_fun + "start")

                for line in lines:
                        line_strip = line.rstrip()
                        self.xx_dbg(line_strip)        

                self.xx_dbg(s_fun + "end")

        def print_lines(
                self         
                , dbg_info       
                , lines):

                s_fun = self.class_name() + "::print_lines_stripped::"
                self.xx_dbg(s_fun + "start")
                self.xx_dbg_line(s_fun + dbg_info +"-start")
                lines_out = []
                for line in lines:
                        self.xx_dbg_line(" line:" + line)

                self.xx_dbg_line(s_fun + dbg_info +"-end")

                self.xx_dbg(s_fun + "end")
                return lines_out


        def get_lines_stripped(
                self                
                , lines):

                s_fun = self.class_name() + "::print_lines_stripped::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:
                        line_strip = line.rstrip()
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out

               
        def inplace_change_lines(
                self
                , file_lines):

                s_fun = self.class_name() + "::inplace_change_lines::"
                self.xx_dbg(s_fun + "start")

                lines_out = []

                cnt = len(file_lines)
                cnt_idx = cnt -1
                self.xx_dbg(s_fun + " lines_count " + str(cnt))

                ii = 0
                while ii < cnt_idx :

                        lines_out_tmp = self.get_line_inplace_dir(
                                ii
                                , file_lines)

                        idx_0 = ii
                        curr_line_0 = file_lines[ idx_0 ]

                        self.xx_dbg(s_fun + " line_start_to_change:[" + curr_line_0 + "]")

                        for line_t in lines_out_tmp:
                                self.xx_dbg_line(" line_changed_tmp:[" + line_t + "]")

                        for line_t in lines_out_tmp:
                               lines_out.append(line_t)

                        ii = ii + 1

                # lines_out.reverse()

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_line_inplace_dir(
                self                
                , ii
                , file_lines
                ):

                s_fun = self.class_name() + "::get_tabs_prefix::"
                lines_out = []
                idx_0 = ii
                idx_1 = ii + 1
                curr_line_0 = file_lines[ idx_0 ]
                curr_line_1 = file_lines[ idx_1 ]

                sp_0 = self.tabs_prefix_cnt(curr_line_0)
                sp_1 = self.tabs_prefix_cnt(curr_line_1)

                self.xx_dbg(
                        s_fun + " check_line_ii[idx_0:" + str(idx_0) + "]")

                self.xx_dbg(
                        s_fun + " check_line_ii[idx_1:" + str(idx_1) + "]")

                self.xx_dbg(
                        s_fun + " check_line" 
                        + "[curr_line_0:" + str(curr_line_0) + "]" 
                        + "[" + str(sp_0) + "]" )

                self.xx_dbg(
                        s_fun + " check_line" 
                        + "[curr_line_1:" + str(curr_line_1) + "]" 
                        + "[" + str(sp_1) + "]")

                self.xx_dbg(
                        s_fun + " sp_xx " + str(sp_0) + "-" + str(sp_1))

                if (self.m_add_spaces_count == 1 ):
                        curr_line_0 = curr_line_0 + "-" + str(sp_0)

                s_tab_prefix = self.get_tabs_prefix(sp_0)

                s_idx_prefix = self.get_idx_prefix(ii + 1)

                s_full_idx_prefix = ""
                if self.m_add_idx_prefixes == 1:
                        s_full_idx_prefix = s_idx_prefix + str(ii+1) + "" + "-"
                        
                curr_line_0_stripped = curr_line_0.strip()

                curr_line_0_a =  s_tab_prefix + s_full_idx_prefix + curr_line_0_stripped

                if(sp_0 == sp_1):
                        self.xx_dbg("cond-0-Y")
                        lines_out.append("mkdir " + curr_line_0_a)
                else:
                        self.xx_dbg("cond-0-N")

                if(sp_0 < sp_1 ):
                        self.xx_dbg("cond-1-Y")
                        lines_out.append("mkdir " + curr_line_0_a)       
                        lines_out.append("cd    " + curr_line_0_a)       
                else:
                        self.xx_dbg("cond-1-N")

                if(sp_0 == sp_1 + 1):
                        self.xx_dbg("cond-2-Y")
                        lines_out.append("mkdir " + curr_line_0_a)       
                        lines_out.append("cd   .. ")       
                else:
                        self.xx_dbg("cond-2-N")

                if(sp_0 == sp_1 + 2):
                        self.xx_dbg("cond-3-Y")
                        lines_out.append("mkdir " + curr_line_0_a)       
                        lines_out.append("cd   .. ")       
                        lines_out.append("cd   .. ")       
                else:
                        self.xx_dbg("cond-3-N")

                if(sp_0 == sp_1 + 3):
                        self.xx_dbg("cond-4-Y")
                        lines_out.append("mkdir " + curr_line_0_a)       
                        lines_out.append("cd   .. ")       
                        lines_out.append("cd   .. ")       
                        lines_out.append("cd   .. ")       
                else:
                        self.xx_dbg("cond-4-N")

                if(sp_0 == sp_1 + 4):
                        self.xx_dbg("cond-5-Y")
                        lines_out.append("mkdir " + curr_line_0_a)       
                        lines_out.append("cd   .. ")       
                        lines_out.append("cd   .. ")       
                        lines_out.append("cd   .. ")       
                else:
                        self.xx_dbg("cond-5-N")          

                #self.xx_dbg(s_fun + "start")
                return lines_out

        def get_tabs_prefix(
                self                
                ,cnt):

                s_fun = self.class_name() + "::get_tabs_prefix::"
                #self.xx_dbg(s_fun + "start")
                out_line = ""
                ii=0
                while ii < cnt :
                        out_line = out_line  + "\t"
                        ii = ii + 1
                #self.xx_dbg(s_fun + "end")

                return out_line

        def tabs_prefix_cnt(
                self
                , pline):

                s_fun = self.class_name() + "::tabs_prefix_cnt::"
                self.xx_dbg(s_fun + "start")
                
                ii = 0
                spaces = 0
                line = pline.replace("    ","\t")
                cnt = len(line)
                while ii < cnt - 1:
                        spc = line[ii:ii+1]
                        if(spc == ' '):
                                spaces = spaces + 1
                                ii = ii + 1
                                continue

                        if(spc == '\t'):
                                spaces = spaces + 1
                                ii = ii + 1
                                continue                                
                        break

                self.xx_dbg(s_fun + "end_spaces [" + str(spaces) + "][" + line + "]")

                return spaces

if __name__ == "__main__":

        ddh = LKD_CreateCats("")


        ddh.execute_main("")
