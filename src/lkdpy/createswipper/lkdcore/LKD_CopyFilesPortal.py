import sys
import os
import logging
import shutil
from LKD_CopyFilesList import *

class LKD_CopyFilesPortal:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CopyFiles::__init__::in::")
                self.m_src = "blogtech_x2"
                self.m_dst = "services_s3"
                self.m_root_src = ""
                self.m_root_dst = ""
                self.m_test_mode = 0
                #self.m_override_mode = False
                self.m_override_mode = False
                self.m_error_on_source_not_exist = False
                self.m_ds = "/"
                self.xx_dbg("LKD_CopyFiles::__init__::out::")
               
        def xx_dbg(self, tt):
                "" ""
                print (tt)

        def create_cpy_portal(self, tt):
                "" ""
                self.create_cpy_articles_content("")
                self.create_cpy_lib("")
                self.create_cpy_no_swippers("")
                self.create_cpy_swippers("")

        def create_cpy_no_swippers(self, tt):
                "" ""

                handler = LKD_CopyFilesList("")
                swippers = handler.get_list_of_no_swippers()

                for dd_swipper in swippers :
                        self.create_cpy_no_swipper(dd_swipper,"")
        
        def create_cpy_swippers(self, tt):
                "" ""

                handler = LKD_CopyFilesList("")
                swippers = handler.get_list_of_swippers()

                for dd_swipper in swippers :
                        self.create_cpy_swipper(dd_swipper,"")

        # cp -r /C/lkd/ht/apps_portal/lkduni/app-4/src/libraries/joomla/mod_ep/* /C/lkd/ht/apps_portal_joo_39/apps/src/joo/libraries/joomla/mod_ep/

        def create_cpy_lib(self,  tt):

                s_root = "/C/lkd/ht/apps_portal/lkduni/app-4/src/modules/"
                s_dest = " /C/lkd/ht/apps_portal_joo_39/apps/src/joo//"
                s_swp = "libraries/joomla/mod_ep/"
                s_cpy = "cp -r " + s_root  + s_swp + "* " + s_dest + s_swp
                self.xx_dbg(s_cpy)

        def create_cpy_articles_content(self,  tt):

                s_root = "/C/lkd/ht/apps_portal/lkduni/app-4/src/modules/"
                s_dest = " /C/lkd/ht/apps_portal_joo_39/apps/src/joo//"
                s_swp = "modules/mod_ep_articles/assets"
                s_cpy = "cp -r " + s_root  + s_swp + "* " + s_dest + s_swp                
                self.xx_dbg(s_cpy)

                s_swp = "modules/mod_ep_articles/content_cats"
                s_cpy = "cp -r " + s_root  + s_swp + " " + s_dest + s_swp
                self.xx_dbg(s_cpy)

                s_swp = "modules/mod_ep_articles/lib"
                s_cpy = "cp -r " + s_root  + s_swp + " " + s_dest + s_swp
                self.xx_dbg(s_cpy)

                s_swp = "modules/mod_ep_articles"
                s_cpy = "cp  " + s_root  + s_swp + " " + s_dest + s_swp
                self.xx_dbg(s_cpy)

        def create_cpy_swipper(self, dd_swipper, tt):

                s_root = "/C/lkd/ht/apps_portal/lkduni/app-4/src/modules/"
                s_dest = " /C/lkd/ht/apps_portal_joo_39/apps/src/joo//"
                s_swp = "mod_ep_swipper_" + dd_swipper
                s_sep = "/"
                s_cpy = "cp -r " + s_root  + s_swp + " " + s_dest + s_swp

                self.xx_dbg(s_cpy)

        def create_cpy_no_swipper(self, dd_swipper, tt):

                s_root = "/C/lkd/ht/apps_portal/lkduni/app-4/src/modules/"
                s_dest = " /C/lkd/ht/apps_portal_joo_39/apps/src/joo//"
                s_swp = "" + dd_swipper
                s_sep = "/"
                s_cpy = "cp -r " + s_root  + s_swp + " " + s_dest + s_swp

                self.xx_dbg(s_cpy)
