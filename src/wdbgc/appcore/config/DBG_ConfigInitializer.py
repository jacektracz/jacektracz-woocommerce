import sys
import os


from ... appcore.logging.DBG_ExceptionPrinter import *
from ... appcore.filewriters.DBG_FileWriter import *
from ... appcore.htmlwriters.DBG_Html import *
from ... appcore.config.DBG_PrintConfig import *
from ... appcore.exceptions.DBG_MainBase import *
from ... DBG_AdapterBase import *

class DBG_ConfigInitializer(DBG_AdapterBase):
        def __init__(self):
                DBG_AdapterBase.__init__(self,"DBG_ConfigInitializer")  
                self.m_print_steps = 1
                self.m_conf_file = "15"
                self.m_out_file_name = "15"
                

                        
        def set_configuration(
                        self
                        , s_conf_file
                        , s_out_file_name):
                
                self.xx_dbg("DBG_ConfigInitializer::set_configuration::method_in::")
                self.m_conf_file = s_conf_file
                self.m_out_file_name = s_out_file_name
                self.xx_dbg("DBG_ConfigInitializer::set_configuration::method_out::")

                
        def initialize_configuration(self):
                try:
                        self.xx_dbg("DBG_ConfigInitializer::initialize_configuration::method_in::")
                        DBG_PrintConfig().getItem().set_file(self.m_conf_file)
                        DBG_PrintConfig().getItem().read_config()
                        
                        if(self.m_out_file_name != ""):
                                DBG_PrintConfig().getItem().set_out_file_name(self.m_out_file_name)
                                
                        DBG_FileWriter.initialize_files()
                        self.xx_dbg("DBG_ConfigInitializer::initialize_configuration::method_out::")
                        
                        return 1
                except:
                        self.xx_exception_raw("DBG_ConfigInitializer::prepare_object::excp")
                        return 0
        
        def close_configuration(self):
                try:
                        self.xx_dbg("DBG_ConfigInitializer::close_configuration::method_in::")
                        DBG_FileWriter.close_files()
                        self.xx_hard_print_steps("close_files_in_exception")
                        self.xx_dbg("DBG_ConfigInitializer::close_configuration::method_out::")
                except:
                        self.xx_exception_raw("DBG_ConfigInitializer::prepare_object::excp")
                        self.xx_hard_print_steps("raw_exception")
        
        def xx_exception_raw(self,tt):
                DBG_ExceptionPrinter.print_exception(tt)
                                
        def xx_hard_print_steps(self,tt):
                if(self.m_print_steps):
                        print "===============================================>MAIN_STEPS:" + str(tt)
                                                                                        
            