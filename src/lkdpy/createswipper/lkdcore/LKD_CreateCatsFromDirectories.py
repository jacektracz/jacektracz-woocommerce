﻿import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *

from LKD_CreateFilesDatabase import *
from LKD_CatItem import *

#  C:/lkd/servers/installed/python27/python C:/lkd/ht/apps_w2_risk/app/src/apps_w2_w2/src/lkdpy/start_cpy.py
# C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles/content_cats/content_markdown/content_by_groups/cat__8000/cat__000/cat__00/cat__8000/content_idx_0/content__cats_2_add.md
# C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\createswipper\lkdcore\LKD_CreateCats.py

# select "cats.append(self.get_item(",id,",","\"",trim(title),"\"","))" from joo2_categories where parent_id = 11770

class LKD_CreateCatsFromDirectories:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CopyFiles::__init__::in::")
                #self.m_src = "C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles/content_cats/content_markdown/content_by_groups/cat__8000/cat__000/cat__00/cat__8000/content_idx_0/cats/content__cats_2_add.md"
                self.m_src = "C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles_data/cats/content__cats_2_add.md"
                self.m_dst_scripts = "C:/lkd/ht/apps_ctx/1"
                self.m_root_src = ""
                self.m_root_dst = ""
                self.m_test_mode = 0
                self.m_add_spaces_count = 0
                self.m_exec_remove_toc = 0
                self.m_exec_inplace_change = 1
                self.m_add_idx_prefixes = 1
                self.m_exec_write = 1
                self.m_exec_main_prepare_in_one_bucket = 0
                self.m_exec_main_prepare_in_buckets = 1
                self.m_exec_main_create_dirs = 1
                self.m_override_mode = True
                self.m_prepare_xx_to_remove_toc = False
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

        def execute_main_test(self,tt):
                s_fun = self.class_name() + "::execute_cdirs::"
                self.xx_dbg(s_fun + "start")

                src_file = self.m_src
                src_file_without_empty = src_file
                
                src_file_1 = src_file
                dst_file_standalone_1 = src_file + ".tmp.2.toc.md"
                self.execute_main_lines_with_removed_toc_from_start(
                        ""
                        , src_file_1
                        , dst_file_standalone_1)

        def execute_main(self,tt):
                s_fun = self.class_name() + "::execute_cdirs::"
                self.xx_dbg(s_fun + "start")

                src_file = self.m_src
                src_file_without_empty = src_file
                dst_file_without_empty = src_file + ".tmp.0.1.noempty.md"
                self.execute_main_lines_without_empty(
                        ""
                        , src_file_without_empty
                        , dst_file_without_empty)

                src_file_prepare_xx_to_toc = src_file
                src_file_prepare_xx_to_toc = dst_file_without_empty
                dst_file_prepare_xx_to_toc = src_file + ".tmp.0.2.prepxx.md"
                self.execute_main_lines_prepare_xx_to_toc(
                        ""
                        , src_file_prepare_xx_to_toc
                        , dst_file_prepare_xx_to_toc)

                src_file_toc = src_file
                src_file_toc = dst_file_prepare_xx_to_toc
                dst_file_standalone_toc = src_file + ".tmp.1.0.toc.md"
                self.execute_main_lines_with_removed_toc_from_start(
                        ""
                        , src_file_toc
                        , dst_file_standalone_toc)

                src_file_chars = src_file
                src_file_chars = dst_file_standalone_toc
                dst_file_standalone_chars = src_file + ".tmp.1.1.chars.md"
                self.execute_main_lines_without_special_chars(
                        ""
                        , src_file_chars
                        , dst_file_standalone_chars)

                src_file_1 = src_file
                src_file_toc_2 = dst_file_standalone_chars
                dst_file_toc_2 = src_file + ".tmp.2.toc.md"
                self.execute_main_lines_with_removed_toc_from_start(
                        ""
                        , src_file_toc_2
                        , dst_file_toc_2)

                src_file_spaces_to_break = src_file
                src_file_spaces_to_break = dst_file_toc_2
                dst_file_spaces_to_break = src_file + ".tmp.3.spacestobreak.md"
                self.execute_main_lines_spaces_to_break(
                        ""
                        , src_file_spaces_to_break
                        , dst_file_spaces_to_break)

                src_file_clear_spaces_to_break = src_file
                src_file_clear_spaces_to_break = dst_file_spaces_to_break                
                dst_file_clear_spaces_to_break = src_file + ".tmp.4.clear.clear-spaces.md"
                self.execute_main_clear_spaces_to_break(
                        ""
                        , src_file_clear_spaces_to_break
                        , dst_file_clear_spaces_to_break)

                src_file_4 = src_file
                src_file_4 = dst_file_clear_spaces_to_break
                dst_file_standalone_4 = src_file + ".tmp.5.directories.md"
                self.execute_main_lines_create_directories(
                        ""
                        , src_file_4
                        ,  dst_file_standalone_4)

                self.xx_dbg(s_fun + "end")

        def execute_main_clear_spaces_to_break(
                self
                , tt
                , psrc_file
                , pdst_file):
                s_fun = self.class_name() + "::execute_main_clear_spaces_to_break::"
                self.xx_dbg(s_fun + "start")

                src_file = psrc_file
                dst_file = pdst_file
                dst_file_bat = pdst_file + ".bat"

                lines = self.read_lines_from_file(
                        src_file)

                lines = self.get_lines_clear_spaces_to_break(
                        lines)

                self.print_lines(
                        "execute_main_clear_spaces_to_break"
                        , lines)

                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        dst_file_bat
                        , lines)

        def execute_main_lines_without_empty(
                self
                , tt
                , psrc_file
                , pdst_file):

                s_fun = self.class_name() + "::execute_main_lines_without_empty::"
                self.xx_dbg(s_fun + "start")

                src_file = psrc_file
                dst_file = pdst_file
                dst_file_bat = pdst_file + ".bat"

                lines = []

                lines = self.read_lines_from_file(
                        src_file)

                lines = self.get_lines_without_empty(
                        lines)

                self.print_lines(
                        "execute_main_clear_spaces_to_break"
                        , lines)

                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        dst_file_bat
                        , lines)                        

        def execute_main_lines_spaces_to_break(
                self
                , tt
                , psrc_file
                , pdst_file):

                s_fun = self.class_name() + "::execute_main_lines_spaces_to_break::"
                self.xx_dbg(s_fun + "start")

                src_file = psrc_file
                dst_file = pdst_file
                dst_file_bat = pdst_file + ".bat"

                lines = []
                lines = self.read_lines_from_file(
                        src_file)
               
                lines = self.get_lines_spaces_to_break(
                        lines)

                self.print_lines(
                        "execute_main_lines_spaces_to_break"
                        , lines)

                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        dst_file_bat
                        , lines)

                self.xx_dbg(s_fun + "end")


        def execute_main_lines_create_directories(
                self
                , tt
                , psrc_file
                , pdst_file):

                s_fun = self.class_name() + "::execute_main_lines_create_directories::"
                self.xx_dbg(s_fun + "start")

                # self.set_execute_main_toc("")
                # self.set_execute_main_write_mkdirs("")

                src_file = psrc_file
                dst_file = pdst_file
                dst_file_bat = pdst_file + ".bat"

                lines = []
                lines = self.read_lines_from_file(
                        src_file)
                
                lines = self.get_lines_create_directories(
                        lines)

                self.print_lines(
                        "inplace_change"
                        , lines)
                
                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        dst_file_bat
                        , lines)

                self.xx_dbg(s_fun + "end")

        # get_lines_with_removed_toc_from_start

        def execute_main_lines_with_removed_toc_from_start(
                self
                , tt
                , psrc_file
                , pdst_file):

                s_fun = self.class_name() + "::execute_main_lines_with_removed_toc_from_start::"
                self.xx_dbg(s_fun + "start")

                src_file = psrc_file
                dst_file = pdst_file                
                dst_file_bat = pdst_file + ".bat"

                lines = []
                lines = self.read_lines_from_file(
                        src_file)

                lines = self.get_lines_with_removed_toc_from_start(
                        lines)

                self.print_lines(
                        "execute_main_lines_with_removed_toc_from_start"
                        , lines)

                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        dst_file_bat
                        , lines)

                self.xx_dbg(s_fun + "end")

                return lines

        def execute_main_lines_without_toc(
                self
                , tt
                , psrc_file
                , pdst_file):

                s_fun = self.class_name() + "::execute_main_lines_without_toc::"
                self.xx_dbg(s_fun + "start")

                src_file = psrc_file
                dst_file = pdst_file                
                dst_file_bat = pdst_file + ".bat"

                lines = []
                
                lines = self.read_lines_from_file(
                        src_file)

                lines = self.get_lines_without_toc(
                        lines)

                self.print_lines(
                        "execute_main_lines_without_toc"
                        , lines)

                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        dst_file_bat
                        , lines)

                self.xx_dbg(s_fun + "end")

                return lines

        def execute_main_lines_prepare_xx_to_toc_spaces(
                self
                , tt
                , psrc_file
                , pdst_file):

                s_fun = self.class_name() + "::execute_main_lines_prepare_xx_to_toc_spaces::"
                self.xx_dbg(s_fun + "start")

                src_file = psrc_file
                dst_file = pdst_file                
                dst_file_bat = pdst_file + ".bat"

                lines = []
                
                lines = self.read_lines_from_file(
                        src_file)

                lines = self.get_lines_prepare_xx_to_toc_spaces(
                        lines)

                self.print_lines(
                        "get_lines_prepare_xx_to_toc_spaces"
                        , lines)

                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        dst_file_bat
                        , lines)

                self.xx_dbg(s_fun + "end")


        def execute_main_lines_prepare_xx_to_toc(
                self
                , tt
                , psrc_file
                , pdst_file):

                s_fun = self.class_name() + "::execute_main_lines_prepare_xx_to_toc::"
                self.xx_dbg(s_fun + "start")

                src_file = psrc_file
                dst_file = pdst_file                
                dst_file_bat = pdst_file + ".bat"

                lines = []
                
                lines = self.read_lines_from_file(
                        src_file)

                lines = self.get_lines_prepare_xx_to_toc(
                        lines)

                self.print_lines(
                        "get_lines_prepare_xx_to_toc"
                        , lines)

                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        dst_file_bat
                        , lines)

                self.xx_dbg(s_fun + "end")

        def execute_main_lines_without_special_chars(
                self
                , tt
                , psrc_file
                , pdst_file):

                s_fun = self.class_name() + "::execute_main_lines_without_special_chars::"
                self.xx_dbg(s_fun + "start")

                src_file = psrc_file
                dst_file = pdst_file                
                dst_file_bat = pdst_file + ".bat"

                lines = []
                
                lines = self.read_lines_from_file(
                        src_file)

                lines = self.get_lines_without_special_chars(
                        lines)

                self.print_lines(
                        "execute_main_lines_without_special_chars"
                        , lines)

                self.write_lines(
                        dst_file
                        , lines)

                self.create_bat_file(
                        dst_file_bat
                        , lines)

                self.xx_dbg(s_fun + "end")

        def get_lines_without_toc(
                self
                , plines):

                s_fun = self.class_name() + "::get_lines_without_toc::"
                self.xx_dbg(s_fun + "start")
                lines = plines

                self.print_lines(
                        "get_lines_without_empty"
                        , lines)

                lines = self.get_lines_with_removed_toc(
                        lines)

                return lines
        
        def get_lines_spaces_to_break(
                self
                , plines):

                s_fun = self.class_name() + "::get_lines_spaces_to_break::"
                self.xx_dbg(s_fun + "start")
                lines = plines

                self.print_lines(
                        "get_lines_spaces_to_break"
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

                lines = self.get_lines_normalize_multiple_item_direct(
                        "vvv"
                        , " "
                        , lines
                        )

                self.print_lines(
                        "get_lines_normalize_multiple_item_direct_vvv"
                        , lines)


                return lines

        def get_lines_prepare_xx_to_toc_spaces(
                self
                , lines):

                s_fun = self.class_name() + "::get_lines_prepare_xx_to_toc_spaces::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = self.get_line_prepare_xx_to_toc_spaces(
                                line)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_lines_prepare_xx_to_toc(
                self
                , lines):

                s_fun = self.class_name() + "::get_lines_prepare_xx_to_toc::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        if(self.m_prepare_xx_to_remove_toc == True):
                                line_strip = self.get_line_prepare_xx_to_toc(
                                        line)
                                lines_out.append(line_strip)  
                        else:
                                line_strip = line
                                lines_out.append(line_strip)  

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_lines_without_special_chars(
                self
                , lines):

                s_fun = self.class_name() + "::get_lines_without_special_chars::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = self.get_line_without_special_chars(
                                line)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_lines_clear_spaces_to_break(
                self
                , lines):

                s_fun = self.class_name() + "::get_lines_clear_spaces_to_break::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = self.get_line_clear_spaces_to_break(
                                line)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_line_clear_spaces_to_break(    
                self
                , line):
                s_fun = self.class_name() + "::get_line_clear_spaces_to_break::"
                self.xx_dbg(s_fun + "start")

                sp_0 = self.tabs_prefix_cnt( line )
                s_tab_prefix = self.get_tabs_prefix(sp_0)

                line = line.strip()                

                line = self.get_line_normalize_multiple_item(
                        " "
                        , line)

                line = self.get_line_with_space_to_break(
                        line)

                line = self.get_line_normalize_multiple_item(
                        "-"
                        , line)

                line = s_tab_prefix + line

                self.xx_dbg(s_fun + "end")

                return line

        def get_lines_without_empty(
                self
                , lines):

                s_fun = self.class_name() + "::get_lines_without_empty::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = line
                        if(line_strip != ""):
                                lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_lines_with_removed_toc_from_start(
                self
                , lines):

                s_fun = self.class_name() + "::get_lines_with_removed_toc_from_start::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = self.get_line_with_removed_toc_from_start(
                                line)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out
                
        def get_line_with_removed_toc_from_start(
                self
                , pline):

                s_fun = self.class_name() + "::get_line_with_removed_toc_from_start::"                
                line = pline
                lineout = pline
                i_idx = line.find("xx")
                if(i_idx > 0):
                        lineout = line[0:i_idx]

                self.xx_dbg_1(s_fun + "line:" + line)
                return lineout


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

        def get_line_prepare_xx_to_toc_spaces(
                self
                , pline):

                s_fun = self.class_name() + "::get_line_prepare_xx_to_toc_spaces::"                
                self.xx_dbg_1(s_fun + "atart")

                line = pline                

                sp_0 = self.tabs_prefix_cnt( line )
                s_tab_prefix = self.get_tabs_prefix(sp_0)
                line = line.strip()

                line = line.replace(" 1","xx")
                line = line.replace(" 2","xx")                
                line = line.replace(" 3","xx")                
                line = line.replace(" 4","xx")                
                line = line.replace(" 5","xx")                
                line = line.replace(" 6","xx")                
                line = line.replace(" 7","xx")                
                line = line.replace(" 8","xx")                
                line = line.replace(" 9","xx")                

                line = s_tab_prefix + line
                self.xx_dbg_1(s_fun + "line:" + line)                

                return line

        def get_line_prepare_spaces_to_minus(
                self
                , pline):

                s_fun = self.class_name() + "::get_line_prepare_spaces_to_minus::"                
                self.xx_dbg_1(s_fun + "atart")

                line = pline                
                line = line.strip()

                for kk in range(10):
                        line = line.replace("  "," ")

                line = line.replace(" ","-")
                s_tab_prefix = ""
                line = s_tab_prefix + line
                self.xx_dbg_1(s_fun + "line:" + line)                

                return line

        def get_line_prepare_xx_to_toc(
                self
                , pline):

                s_fun = self.class_name() + "::get_line_prepare_xx_to_toc::"                
                self.xx_dbg_1(s_fun + "atart")

                line = pline                

                sp_0 = self.tabs_prefix_cnt( line )
                s_tab_prefix = self.get_tabs_prefix(sp_0)
                line = line.strip()

                line = line.replace(" 1","xx")
                line = line.replace(" 2","xx")                
                line = line.replace(" 3","xx")                
                line = line.replace(" 4","xx")                
                line = line.replace(" 5","xx")                
                line = line.replace(" 6","xx")                
                line = line.replace(" 7","xx")                
                line = line.replace(" 8","xx")                
                line = line.replace(" 9","xx")                

                line = s_tab_prefix + line
                self.xx_dbg_1(s_fun + "line:" + line)                

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
                line = line.replace( "’","")

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

                s_fun = self.class_name() + "::create_bat_file::"
                self.xx_dbg(s_fun + "start")

                with open(filename, "w") as f:
                        f.write( "rem " + filename + "\n")
                        f.write( "cd " + self.m_dst_scripts + "" + "\n")

                        for line in lines:
                                f.write( line + "\n")

                        f.write( "cd " + self.m_dst_scripts + "" + "\n")

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

               
        def get_lines_create_directories(
                self
                , file_lines):

                s_fun = self.class_name() + "::get_lines_create_directories::"
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
                        lines_out.append("cd  .. ")       
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

        def get_print_files_to_create(self, psrc_path_project):
                for x1 in os.listdir(psrc_path_project):                        
                        p2 = psrc_path_project + "/" + x1
                        if os.path.isdir(p2): 
                                ss = "C:/lkd/ht/apps_ctx/1/"
                                x1 = self.get_line_prepare_spaces_to_minus(x1)
                                xxp = ss + x1
                                self.xx_dbg( 'mkdir ' + xxp)

        def get_crete_files_to_create(self, psrc_path_project):
                for x1 in os.listdir(psrc_path_project):                        
                        p2 = psrc_path_project + "/" + x1
                        if os.path.isdir(p2): 
                                ss = "C:/lkd/ht/apps_ctx/1/"
                                x1 = self.get_line_prepare_spaces_to_minus(x1)
                                xxp = ss + x1
                                self.xx_dbg( 'mkdir ' + xxp)
                                os.mkdir(xxp)


if __name__ == "__main__":

        ddh = LKD_CreateCats("")
        ddh.execute_main("")
