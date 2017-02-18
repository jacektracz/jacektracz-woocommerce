import sys
import os
import importlib

from .. DBG_AdapterBase import *

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

class DBG_DbgGenericObjectEntry(DBG_AdapterBase):
        def __init__(self):
                DBG_AdapterBase.__init__(self,"DBG_DbgGenericObjectEntry")  
                self.m_exceptions = DBG_GlobalExceptionsHtmlPrinter(self,"Parent::DBG_DbgGenericObjectEntry")
                self.m_informations = DBG_GlobalInformationsHtmlPrinter(self,"Parent::DBG_DbgGenericObjectEntry")
                self.m_env_printer = DBG_EnvItemPrinter(self,"Parent::DBG_DbgGenericObjectEntry")
                self.m_print_steps = 1
                self.m_c_mod =""
                self.m_c_class =""
                self.m_c_addr =""
                
        def print_object(self):
                
                try:
                        self.print_object_internal()
                except:
                        self.xx_exception("DBG_DbgGenericObjectEntry::prepare_object::excp")
                        
        def print_object_internal(self):
                try:
                        
                        self.xx_dbg("DBG_DbgGenericObjectEntry::print_object::in::")
                        DBG_Html.xx_print_start()                        
                        DBG_Html.xx_ols ("")
                        
                        
                        self.handle_srt_data()
                                
                        DBG_Html.xx_ole ("")
                        DBG_Html.xx_print_end()
                        self.xx_hard_print_steps("xx_print_end")
                        self.xx_dbg("DBG_DbgGenericObjectEntry::print_object::out::")
                        
                        self.xx_hard_print_steps("close_files")
                        return 1
                        
                except:
                        try:
                                self.xx_exception_raw("DBG_DbgGenericObjectEntry::prepare_object::excp")
                        except:
                                self.xx_print_exception_raw("DBG_DbgGenericObjectEntry::prepare_object::excp")
                        return 0

        def handle_srt_data(self):
                try:
                        #PHY:((iastora!Wcdl::CrashHiberMemoryDescriptor*)0xfffff801538a4630)
                        self.m_c_mod = ".. driver.DBG_CrashHiberMemoryDescriptor"
                        self.m_c_class = "DBG_CrashHiberMemoryDescriptor"
                        self.m_c_addr = "fffff801538a4630"
                        
                        dd = self.prepare_obj_by_phy_addr()
                        if (dd != None):
                                dd.print_object()
                except:
                        self.xx_exception("DBG_DbgGenericObjectEntry::prepare_object::excp")

        def prepare_obj_by_phy_addr(self):
                try:
                        
                        self.xx_dbg("DBG_DbgGenericObjectEntry::print_object::in::")
                
                        self.xx_hard_print_steps("prepare_obj_by_phy_addr::start")
                        
                        mn = self.m_c_mod
                        cn = self.m_c_class
                        saddr = self.m_c_addr
                        dd_current  = self.str_to_class(mn,cn)
                        if dd_current != None:
                                #dd_current = DBG_CfgArray("Parent::DBG_CfgArrayList_PyList")
                                dd_current.xx_compute_generic_phy_by_phy(self, "0x" + saddr,"(" + saddr +")" )
                                dd_current.prepare_object()
                        return dd_current
                
                        self.xx_hard_print_steps("prepare_obj_by_phy_addr::end")
                except:
                        self.xx_exception("DBG_DbgGenericObjectEntry::prepare_object::excp")
                        return None
                                
        def str_to_class(self,module_name, class_name):
            try:
                inst_type = 1
                if (inst_type == 0):
                        mn = module_name
                        mn = "D:\lkd\komodo\w2_2\src\w2\wdbgc\driver\DBG_CrashHiberMemoryDescriptor.py"
                        mn = ".. driver.DBG_CrashHiberMemoryDescriptor"                
                        module_ = importlib.import_module(mn)
                        class_ = getattr(module_, class_name)("",self)
                        return class_
                
                if (inst_type == 1):
                        #mn = module_name
                        fpath = "D:\lkd\komodo\w2_2\src\w2\wdbgc\driver"
                        mn = "DBG_CrashHiberMemoryDescriptor.py"
                        cn = "DBG_CrashHiberMemoryDescriptor"
                        #mn = ".. driver.DBG_CrashHiberMemoryDescriptor"                                        
                        p = __import__(fpath)
                        m = getattr(p, mn)
                        c = getattr(m, cn)
                        dd_obj = c("",self)
                        return dd_obj
            except :
                self.xx_exception("DBG_DbgGenericObjectEntry::prepare_object::excp")
                return None

        def get_class(self,fully_qualified_path, module_name, class_name, *instantiation):
            """
            Returns an instantiated class for the given string descriptors
            :param fully_qualified_path: The path to the module eg("Utilities.Printer")
            :param module_name: The module name eg("Printer")
            :param class_name: The class name eg("ScreenPrinter")
            :param instantiation: Any fields required to instantiate the class
            :return: An instance of the class
            """
            p = __import__(fully_qualified_path)
            m = getattr(p, module_name)
            c = getattr(m, class_name)
            instance = c(*instantiation)
            return instance
        
        def get_class_ex(self,module_name, class_name):
            """
            Returns an instantiated class for the given string descriptors
            :param fully_qualified_path: The path to the module eg("Utilities.Printer")
            :param module_name: The module name eg("Printer")
            :param class_name: The class name eg("ScreenPrinter")
            :param instantiation: Any fields required to instantiate the class
            :return: An instance of the class
            """
            
            fully_qualified_path = ""
            p = __import__(fully_qualified_path)
            m = getattr(p, module_name)
            c = getattr(m, class_name)
            instance = c("",self)
            return instance


        def xx_hard_print_steps(self,tt):
                if(self.m_print_steps):
                        print "===============================================>MAIN_STEPS:" + str(tt)
                        
                
        def xx_exception_raw(self,tt):
                DBG_ExceptionPrinter.print_exception(tt)


        def xx_print_exception_raw(self,tt):
                print tt