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
                self.m_dst = "C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles/content_cats/content_markdown/content_by_groups/cat__8000/cat__000/cat__00/cat__8000/content_idx_0/content__cats_2_add_res.md"
                self.m_root_src = ""
                self.m_root_dst = ""
                self.m_test_mode = 0
                self.m_override_mode = True
                self.m_ds = "/"
                self.xx_dbg("LKD_CopyFiles::__init__::out::")

        def class_name(self):
                return "LKD_CreateCats::"

        def xx_dbg(self, tt ):
                print tt

        def execute_main(self,tt):
                s_fun = self.class_name() + "::execute_cdirs::"
                self.xx_dbg(s_fun + "start")
                dst_file = self.m_dst
                src_file = self.m_src

                linest = self.inplace_change(
                        src_file)

                lines = self.get_lines_stripped(
                        linest)

                write_exec = 0
                if(write_exec == 1):
                        self.write_lines(
                                dst_file
                                , lines)

                self.print_lines(
                        dst_file
                        , lines)

                self.xx_dbg(s_fun + "end")

        def inplace_change(
                self
                , filename):

                s_fun = self.class_name() + "::inplace_change::"
                self.xx_dbg(s_fun + "start")
                self.xx_dbg(s_fun + "read_file " + filename)

                lines = self.get_lines(filename)
                lines_out = self.inplace_change_lines(lines)
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

                self.xx_dbg(s_fun + "end")
                return flie_lines

        def write_lines(
                self
                , filename
                , lines):

                s_fun = self.class_name() + "::write_lines::"
                self.xx_dbg(s_fun + "start")

                with open(filename, "w") as f:
                        f.writeLines( lines )


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
                                s_fun + " sp_xx " + str(sp_0) + " " + str(sp_1))

                        if(sp_0 == sp_1):
                                self.xx_dbg("cond-0-Y")
                                lines_out.append("mkdir " + curr_line_0)
                        else:
                                self.xx_dbg("cond-0-N")

                        if(sp_0 < sp_1 ):
                                self.xx_dbg("cond-1-Y")
                                lines_out.append("mkdir " + curr_line_0)       
                                lines_out.append("cd    " + curr_line_0)       
                        else:
                                self.xx_dbg("cond-1-N")

                        if(sp_0 == sp_1 + 1):
                                self.xx_dbg("cond-2-Y")
                                lines_out.append("mkdir " + curr_line_0)       
                                lines_out.append("cd   .. ")       
                        else:
                                self.xx_dbg("cond-2-N")

                        if(sp_0 == sp_1 + 2):
                                self.xx_dbg("cond-3-Y")
                                lines_out.append("mkdir " + curr_line_0)       
                                lines_out.append("cd   .. ")       
                                lines_out.append("cd   .. ")       
                        else:
                                self.xx_dbg("cond-3-N")

                        if(sp_0 == sp_1 + 3):
                                self.xx_dbg("cond-4-Y")
                                lines_out.append("mkdir " + curr_line_0)       
                                lines_out.append("cd   .. ")       
                                lines_out.append("cd   .. ")       
                                lines_out.append("cd   .. ")       
                        else:
                                self.xx_dbg("cond-4-N")

                        if(sp_0 == sp_1 + 4):
                                self.xx_dbg("cond-5-Y")
                                lines_out.append("mkdir " + curr_line_0)       
                                lines_out.append("cd   .. ")       
                                lines_out.append("cd   .. ")       
                                lines_out.append("cd   .. ")       
                        else:
                                self.xx_dbg("cond-5-N")

                        ii = ii + 1

                # lines_out.reverse()

                self.xx_dbg(s_fun + "end")
                return lines_out


        def tabs_prefix_cnt(
                self
                , line):

                s_fun = self.class_name() + "::tabs_prefix_cnt::"
                self.xx_dbg(s_fun + "start")
                cnt = len(line)
                ii = 0
                spaces = 0
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
