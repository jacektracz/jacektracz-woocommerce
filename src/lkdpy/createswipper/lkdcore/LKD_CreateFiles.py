import sys
import os
import logging
import shutil

class LKD_CreateFiles:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CopyFiles::__init__::in::")
                self.m_src = "C:/lkd/ht/apps_java8_in_action/app/src/jacek-tracz-java-design-patterns"
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

        def read_directory_subdirs(self):
                
                self.xx_dbg("LKD_CopyFiles::read_directory_subdirs::in::")
                folders = []
                for r, d, f in os.walk(path):
                        for folder in d:
                                folders.append(os.path.join(r, folder))

                for f in folders:
                        print(f)

                self.xx_dbg("LKD_CopyFiles::read_directory_subdirs::out::")


        def execute_main(self):

                self.xx_dbg("LKD_CopyFiles::execute_main::in::")

                self.read_directory_subdirs_flat(self.m_src)

                self.xx_dbg("LKD_CopyFiles::execute_main::out::")

        def read_directory_subdirs_flat(self, ppath):
                self.xx_dbg("LKD_CopyFiles::read_directory_subdirs_flat::in::")
                for x in os.listdir(ppath):
                        if os.path.isfile(x): print 'f-', x
                        elif os.path.isdir(x): print 'd-', x
                        elif os.path.islink(x): print 'l-', x
                        else: print '---', x

                self.xx_dbg("LKD_CopyFiles::read_directory_subdirs_flat::out::")


        def xx_dbg(self, tt):
                "" ""
                print (tt)


       

