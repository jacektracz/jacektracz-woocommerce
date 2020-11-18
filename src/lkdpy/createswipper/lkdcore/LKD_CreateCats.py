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
                self.m_root_src = ""
                self.m_root_dst = ""
                self.m_test_mode = 0
                self.m_add_spaces_count = 1
                self.m_exec_remove_toc = 0
                self.m_exec_inplace_change = 1
                self.m_exec_write = 1
                self.m_override_mode = True
                self.m_ds = "/"
                self.xx_dbg("LKD_CopyFiles::__init__::out::")

        def class_name(self):
                return "LKD_CreateCats::"

        def xx_dbg(self, tt ):
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

                # self.set_execute_main_toc("")
                self.set_execute_main_write_mkdirs("")

                dst_file = self.m_dst
                src_file = self.m_src_short
                src_file = self.m_src

                lines = []
                lines = self.get_lines(
                        src_file)

                lines = self.get_lines_stripped(
                        lines)

                lines = self.get_lines_proper_dir_with_spaces(
                        lines)

                if( self.m_exec_remove_toc == 1 ):
                        lines = self.get_removed_toc_lines(
                                lines)


                if( self.m_exec_inplace_change == 1 ):
                        lines = self.inplace_change(
                                lines)

                lines = self.get_lines_stripped(
                        lines)
                
                if( self.m_exec_write == 1 ):
                        self.write_lines(
                                dst_file
                                , lines)

                self.print_lines(
                        dst_file
                        , lines)

                self.xx_dbg(s_fun + "end")

        def get_idx_prefix(
                self
                , p_ii):

                s_fun = self.class_name() + "::get_idx_prefix::"
                self.xx_dbg(s_fun + "start")                             
                s_ii = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
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

        def get_removed_toc_lines(
                self
                , lines):

                s_fun = self.class_name() + "::get_removed_toc_lines::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:                        
                        line_strip = self.get_removed_toc_line(
                                line)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_removed_toc_line(
                self
                , pline):

                s_fun = self.class_name() + "::get_removed_toc_line::"                
                line = pline
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
                return line

        def get_proper_line_dir_with_spaces(
                self
                , pline):

                s_fun = self.class_name() + "::get_proper_line_dir_with_spaces::"                
                line = pline
                line = line.replace("?","")
                line = line.replace("-","")
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
                
                return line

        def get_proper_dir_line_remove_spaces(
                self
                , pline):

                s_fun = self.class_name() + "::get_proper_dir_line_remove_spaces::"
                self.xx_dbg(s_fun + "start")

                line = pline
                line = line.strip()
                line = line.replace( " ","-")
                

                self.xx_dbg(s_fun + "end")
                return line

        def inplace_change(
                self
                , lines):

                s_fun = self.class_name() + "::inplace_change::"
                self.xx_dbg(s_fun + "start")

                        
                lines_out = self.inplace_change_lines(
                        lines)

                self.xx_dbg(s_fun + "end")
                return lines_out

        def get_lines(
                self
                , filename):

                s_fun = self.class_name() + "::inplace_change::"
                self.xx_dbg(s_fun + "start")

                flie_lines = []
                with open(filename) as f:
                        flie_lines = f.readlines()

                lines_out = self.get_lines_stripped(
                        flie_lines)

                self.xx_dbg(s_fun + "end")
                return lines_out

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

        def print_lines(
                self
                , filename
                , lines):

                s_fun = self.class_name() + "::write_lines::"
                self.xx_dbg(s_fun + "start")

                for line in lines:
                        line_strip = line.rstrip()
                        self.xx_dbg(line_strip)        

                self.xx_dbg(s_fun + "end")

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

        def get_lines_proper_dir_with_spaces(
                self                
                , lines):

                s_fun = self.class_name() + "::print_lines_stripped::"
                self.xx_dbg(s_fun + "start")
                lines_out = []
                for line in lines:
                        line_strip = line.rstrip()
                        line_strip = self.get_proper_line_dir_with_spaces(
                                line_strip)
                        lines_out.append(line_strip)      

                self.xx_dbg(s_fun + "end")
                return lines_out


        def inplace_change_lines(
                self
                , flie_lines):

                s_fun = self.class_name() + "::inplace_change_lines::"
                self.xx_dbg(s_fun + "start")

                lines_out = []

                cnt = len(flie_lines)
                cnt_idx = cnt -1
                self.xx_dbg(s_fun + " lines_count " + str(cnt))

                ii = 0
                while ii < cnt_idx :
                        idx_0 = ii
                        idx_1 = ii + 1
                        curr_line_0 = flie_lines[ idx_0 ]
                        curr_line_1 = flie_lines[ idx_1 ]

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

                        s_prefix = self.get_tabs_prefix(sp_0)

                        curr_line_0 = self.get_proper_line_dir_with_spaces(
                                curr_line_0)

                        curr_line_0 = self.get_proper_dir_line_remove_spaces(
                                curr_line_0)

                        s_idx_prefix = self.get_idx_prefix(ii + 1)
                        curr_line_0_a = s_prefix + s_idx_prefix + str(ii+1) + "" + "-" + curr_line_0

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

                        ii = ii + 1

                # lines_out.reverse()

                self.xx_dbg(s_fun + "end")
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
