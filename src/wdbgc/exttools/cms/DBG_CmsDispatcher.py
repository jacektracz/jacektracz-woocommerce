﻿import sys
import os


from ... appcore.logging.DBG_ExceptionPrinter import *
from ... appcore.config.DBG_PrintConfig import *
from ... appcore.exceptions.DBG_MainBase import *
from ... appcore.printers.DBG_ExceptionHtmlPrinter import *
from ... appcore.config.DBG_ConfigInitializer import *


from ... DBG_AdapterBase import *
class DBG_CmsDispatcher(DBG_AdapterBase):
        def __init__(self):
                DBG_AdapterBase.__init__(self,"DBG_CmsDispatcher")  
                self.m_print_steps = 1
                self.m_conf_file = "15"
                self.m_out_file_name = "15"
                
        def dispatch_apps(self, s_conf_file, s_out_file_name):
                
                try:
                        """ """
                        if(s_out_file_name == "cdbg"):
                                self.main_check_dbg(s_conf_file,s_out_file_name)
                                return 1
                        
                        if(s_out_file_name == "create"):
                                DBG_PrintConfig().getItem().set_file(s_conf_file)
                                DBG_PrintConfig().getItem().write_config()
                                return 1
                        return 0
                
                except:
                        self.xx_exception("DBG_CmsDispatcher::prepare_object::excp")

        def close_configuration(self):
                try:
                        DBG_ConfigInitializer().close_configuration()
                        self.xx_hard_print_steps("close_files_in_exception")                        
                except:
                        self.xx_exception_raw("DBG_CmsDispatcher::prepare_object::excp")
                        self.xx_hard_print_steps("raw_exception")
        
        def read_configuration(
                        self
                        , s_conf_file
                        , s_out_file_name):
                try:
                        
                        dd_confi = DBG_ConfigInitializer()
                        dd_confi.set_configuration(s_conf_file,s_out_file_name)
                        
                        return 1
                except:
                        self.xx_exception_raw("DBG_CmsDispatcher::prepare_object::excp")
                        return 0
        
        def xx_exception_raw(self,tt):
                DBG_ExceptionPrinter.print_exception(tt)
                
                                
        def xx_hard_print_steps(self,tt):
                if(self.m_print_steps):
                        print "===============================================>MAIN_STEPS:" + str(tt)
                        
        def main_check_dbg(self,s_conf_file,s_out_file_name):
                try:
                        print "DBG_CmsDispatcher::main_check_dbg::start::"
                        if(self.read_configuration(s_conf_file,s_out_file_name)==1):
                                self.xx_dbg("DBG_CmsDispatcher::main_check_dbg::in::")
                                
                        DBG_FileWriter.close_files()
                        print "DBG_CmsDispatcher::main_check_dbg::end::"
                except:
                        try:
                                self.xx_exception_raw("DBG_CmsDispatcher::prepare_object::excp")
                        except:
                                """ """
                        try:
                                DBG_FileWriter.close_files()
                        except:
                                self.xx_exception_raw("DBG_CmsDispatcher::prepare_object::excp")
                                
        def get_list_dir(self, p_path):
                for root, dirs, files in os.walk(p_path, topdown=True):
                        #for name in files:
                        #    print(os.path.join(root, name))
                        for name in dirs:
                            print(os.path.join(root, name))

                
#c:/python27/python     D:\lkd\komodo\w2_2\src\w2\wdbgc\exttools\cms\DBG_CmsDispatcher.py

if __name__ == '__main__':
    DBG_CmsDispatcher().get_list_dir("D:\lkd\komodo\w2_2\dat\arch\a05_core_docs\linux")
            