import sys
import os

from .. DBG_AdapterBase import *

from .. raidport.DBG_Raidport import *
from .. remapport.DBG_RemapPort import *
from .. appsrc.volport.DBG_VolPort import *

from .. appcore.logging.DBG_ExceptionPrinter import *
from .. appcore.filewriters.DBG_FileWriter import *
from .. appcore.htmlwriters.DBG_Html import *
from .. appcore.config.DBG_PrintConfig import *
from .. appcore.exceptions.DBG_MainBase import *

from .. appcore.printers.DBG_ExceptionHtmlPrinter import *
from .. appcore.printers.DBG_GlobalExceptionsHtmlPrinter import *
from .. appcore.printers.DBG_GlobalInformationsHtmlPrinter import *
from .. appcore.printers.DBG_EnvItemPrinter import *
from .. appsrc.driverext.DBG_Driver_PyArrayStaticGlobal import *

from .. appsrc.mmio.DBG_Mmio_Py import *

class DBG_DbgEntry(DBG_AdapterBase):
        def __init__(self):
                DBG_AdapterBase.__init__(self,"DBG_DbgEntry")  
                self.m_raidport = DBG_Raidport("from::DBG_DbgEntry")
                self.m_remapport = DBG_RemapPort("from::DBG_DbgEntry")
                self.m_volport = DBG_VolPort("from::DBG_DbgEntry")
                self.m_drivers = DBG_Driver_PyArrayStaticGlobal(DBG_DbgEntry,self)
                self.m_mmio = DBG_Mmio_Py("from::DBG_DbgEntry",self)
                self.m_exceptions = DBG_GlobalExceptionsHtmlPrinter(self,"Parent::DBG_DbgEntry")
                self.m_informations = DBG_GlobalInformationsHtmlPrinter(self,"Parent::DBG_DbgEntry")
                self.m_env_printer = DBG_EnvItemPrinter(self,"Parent::DBG_DbgEntry")
                self.m_print_steps = 1
                
        def print_object(self,s_conf_file,s_out_file_name):
                
                try:
                        """ """
                        if(s_out_file_name == "cdbg"):
                                self.check_dbg(s_conf_file,s_out_file_name)
                                return
                        
                        if(s_out_file_name == "create"):
                                DBG_PrintConfig().getItem().set_file(s_conf_file)
                                DBG_PrintConfig().getItem().write_config()
                        else:
                                self.print_object_internal(s_conf_file,s_out_file_name)
                except:
                        self.xx_exception("DBG_DbgEntry::prepare_object::excp")
                        
        def print_object_internal(self,s_conf_file,s_out_file_name):
                try:
                        
                        dd = self.read_configuration(s_conf_file,s_out_file_name)
                        if(dd==1):                        
                                self.xx_dbg("DBG_DbgEntry::print_object::in::")
                                DBG_Html.xx_print_start()
                                
                                DBG_Html.xx_ols ("")
                                if(DBG_PrintConfig().getItem().m_handle_srt_data == 1):
                                        self.handle_srt_data()
                                DBG_Html.xx_ole ("")
                                DBG_Html.xx_print_end()
                                self.xx_hard_print_steps("xx_print_end")
                                self.xx_dbg("DBG_DbgEntry::print_object::out::")
                                
                        DBG_FileWriter.close_files()
                        self.xx_hard_print_steps("close_files")
                        
                except:
                        try:
                                self.xx_exception_raw("DBG_DbgEntry::prepare_object::excp")
                        except:
                                """ """
                        try:
                                DBG_FileWriter.close_files()
                                self.xx_hard_print_steps("close_files_in_exception")
                                
                        except:
                                self.xx_exception_raw("DBG_DbgEntry::prepare_object::excp")
                                self.xx_hard_print_steps("raw_exception")


        def handle_srt_data(self):
                self.xx_hard_print_steps("handle_srt_data::start")
                                
                if(DBG_PrintConfig().getItem().m_print_raidport_main == 1):
                        self.xx_hard_print_steps("m_raidport::start")
                        self.m_raidport.print_object_global()
                        self.xx_hard_print_steps("m_raidport::end")
                else:
                        self.xx_hard_print_steps("m_raidport::not-printed")
                        
                self.xx_hard_print_steps("m_raidport")
                
                if(DBG_PrintConfig().getItem().m_print_remapport_main == 1):
                        self.xx_hard_print_steps("m_remapport::start")
                        self.m_remapport.print_object_global()
                        self.xx_hard_print_steps("m_remapport::end")
                else:
                        self.xx_hard_print_steps("m_remapport::not-printed")
                        
                self.xx_hard_print_steps("m_remapport")
                
                if(DBG_PrintConfig().getItem().m_print_volport_main == 1):
                        self.xx_hard_print_steps("m_volport::start")
                        self.m_volport.print_object_global()
                        self.xx_hard_print_steps("m_volport::end")
                else:
                        self.xx_hard_print_steps("m_volport::not-printed")
                        
                self.xx_hard_print_steps("m_volport")                
                if(DBG_PrintConfig().getItem().get_handle_global_drivers() == 1):
                        self.xx_hard_print_steps("start::m_drivers")
                        self.m_drivers.prepare_object_global()
                        self.m_drivers.print_object_global()
                        self.xx_hard_print_steps("m_drivers::end")
                else:
                        self.xx_hard_print_steps("m_drivers::not-printed")
                        
                self.xx_hard_print_steps("m_drivers")
                
                if(DBG_PrintConfig().getItem().m_print_mmio_main == 1):
                        self.xx_hard_print_steps("start:m_mmio")
                        self.m_mmio.print_object_global()
                        self.xx_hard_print_steps("end:m_mmio")
                else:
                        self.xx_hard_print_steps("m_mmio::not-printed")
                        
                self.xx_hard_print_steps("m_mmio")
                
                if(DBG_PrintConfig().getItem().m_handle_info == 1):                
                        try:
                                self.xx_hard_print_steps("m_informations::start")
                                self.m_informations.prepare_object()
                                self.m_informations.print_object()
                                self.xx_hard_print_steps("m_informations::end")
                        except:
                                self.xx_dbg("DBG_DbgEntry::print_object::skip_s::")
                else:
                        self.xx_hard_print_steps("m_informations::not-printed")
                                
                self.xx_hard_print_steps("m_informations")
                
                if(DBG_PrintConfig().getItem().m_handle_env == 1):
                        self.xx_hard_print_steps("m_env_printer::start")
                        self.m_env_printer.initialize_data_by_selector()
                        self.m_env_printer.prepare_object()
                        self.m_env_printer.print_object()
                        self.xx_hard_print_steps("m_env_printer::end")
                else:
                        self.xx_hard_print_steps("m_env_printer::not-printed")
                        
                self.xx_hard_print_steps("m_env_printer")
                
                if(DBG_PrintConfig().getItem().m_handle_exc == 1):         
                        try:
                                self.xx_hard_print_steps("m_exceptions::start::")
                                self.m_exceptions.prepare_object()
                                self.m_exceptions.print_object()
                                self.xx_hard_print_steps("m_exceptions::end::")
                        except:
                                self.xx_dbg("DBG_DbgEntry::print_object::skip_s::")
                else:
                        self.xx_hard_print_steps("m_exceptions::not-printed")
                                
                self.xx_hard_print_steps("m_exceptions")
                
                self.xx_hard_print_steps("handle_srt_data::end")
                                
        def xx_hard_print_steps(self,tt):
                if(self.m_print_steps):
                        print "===============================================>MAIN_STEPS:" + str(tt)
                        
        def check_dbg(self,s_conf_file,s_out_file_name):
                try:
                        print "DBG_DbgEntry::check_dbg::start::"
                        if(self.read_configuration(s_conf_file,s_out_file_name)==1):
                                self.xx_dbg("DBG_DbgEntry::check_dbg::in::")
                                
                        DBG_FileWriter.close_files()
                        print "DBG_DbgEntry::check_dbg::end::"
                except:
                        try:
                                self.xx_exception_raw("DBG_DbgEntry::prepare_object::excp")
                        except:
                                """ """
                        try:
                                DBG_FileWriter.close_files()
                        except:
                                self.xx_exception_raw("DBG_DbgEntry::prepare_object::excp")
        
        def read_configuration(
                        self
                        , s_conf_file
                        , s_out_file_name):
                try:
                        DBG_PrintConfig().getItem().set_file(s_conf_file)
                        DBG_PrintConfig().getItem().read_config()
                        if(s_out_file_name != ""):
                                DBG_PrintConfig().getItem().set_out_file_name(s_out_file_name)
                        DBG_FileWriter.initialize_files()
                        return 1
                except:
                        self.xx_exception_raw("DBG_DbgEntry::prepare_object::excp")
                        return 0
        
        def xx_exception_raw(self,tt):
                DBG_ExceptionPrinter.print_exception(tt)
                
            