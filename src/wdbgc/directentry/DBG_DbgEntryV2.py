import sys
import os

from .. DBG_AdapterBase import *
from .. appcore.logging.DBG_ExceptionPrinter import *
from .. appcore.config.DBG_PrintConfig import *

from .. appcore.config.DBG_ConfigInitializer import *

from .. directentry.DBG_DbgMainObjectEntry import *

from .. directentry.DBG_DbgGenericOneObjectEntry import *

#from .. directentry.DBG_DbgGenericObjectEntry import *
#from .. DBG_DbgGenericObjectEntryExt import *

class DBG_DbgEntryV2(DBG_AdapterBase):
        def __init__(self):
                DBG_AdapterBase.__init__(self,"DBG_DbgEntryV2")  
                self.m_print_steps = 1
                self.m_conf_file = "15"
                self.m_out_file_name = "15"
                self.m_direct = "N"
                self.m_direct_module = "N"
                self.m_direct_class = "N"
                self.m_direct_addr = "N"
                
        # ee eegen
        def print_object(self, s_conf_file, s_out_file_name):                
                try:
                        self.print_object_internal(s_conf_file,s_out_file_name)
                except:
                        self.xx_exception("DBG_DbgEntryV2::prepare_object::excp")
                        
                        
        def print_object_internal(self,s_conf_file,s_out_file_name):
                try:
                        
                        self.m_conf_file = s_conf_file
                        self.m_out_file_name = s_out_file_name
                        dd = self.read_configuration()
                        
                        if(dd == 1):
                                
                                self.xx_dbg("DBG_DbgEntryV2::print_object::in::")
                                if (self.m_direct == "N"):
                                        dd_obj = DBG_DbgMainObjectEntry()
                                        dd_obj.print_object()

                                if (self.m_direct == "Y"):
                                        dd_obj = DBG_DbgGenericOneObjectEntry()
                                        dd_obj.m_c_mod =""
                                        dd_obj.m_c_class = self.m_direct_class
                                        dd_obj.m_c_addr = self.m_direct_addr
                                        dd_obj.print_object()
                                
                                self.xx_hard_print_steps("xx_print_end")
                                self.xx_dbg("DBG_DbgEntryV2::print_object::out::")
                                
                        self.close_configuration()
                        self.xx_hard_print_steps("close_files")
                        
                except:
                        try:
                                self.xx_exception_raw("DBG_DbgEntryV2::prepare_object::exception::")
                        except:                        
                                self.xx_print_exception_raw("DBG_DbgEntryV2::prepare_object::exception::")
                                
                        self.close_configuration()

        def read_configuration(self):
                try:
                        
                        dd_confi = DBG_ConfigInitializer()
                        dd_confi.set_configuration(
                                        self.m_conf_file
                                        ,self.m_out_file_name)
                        dd_confi.initialize_configuration()
                        
                        #DBG_PrintConfig().getItem().set_file(s_conf_file)
                        #DBG_PrintConfig().getItem().read_config()
                        #if(s_out_file_name != ""):
                        #        DBG_PrintConfig().getItem().set_out_file_name(s_out_file_name)
                        #DBG_FileWriter.initialize_files()
                        
                        return 1
                except:
                        self.xx_exception_raw("DBG_DbgEntryV2::prepare_object::excp")
                        return 0

        def close_configuration(self):
                try:
                        DBG_ConfigInitializer().close_configuration()
                        self.xx_hard_print_steps("close_files_in_exception")                        
                except:
                        self.xx_exception_raw("DBG_DbgEntryV2::prepare_object::excp")
                        self.xx_hard_print_steps("raw_exception")
        
        
        def xx_exception_raw(self,tt):
                DBG_ExceptionPrinter.print_exception(tt)
                
                                
        def xx_hard_print_steps(self,tt):
                if(self.m_print_steps):
                        print "===============================================>MAIN_STEPS:" + str(tt)


        def xx_print_exception_raw(self,tt):
                print tt