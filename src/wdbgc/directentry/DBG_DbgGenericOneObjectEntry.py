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


from .. driver.DBG_CrashHiberMemoryDescriptor import *
from .. appsrc.ismcachecfg.DBG_NvcPromoBlkSet import *
from .. appsrc.reqs.DBG_MemberDiskReq import *
from .. appsrc.hiber.DBG_NvCrashDmp import *
from .. appsrc.ismraid.DBG_RaidDev_PyPtr import *
from .. raidism.DBG_CfgArray import *


class DBG_DbgGenericOneObjectEntry(DBG_AdapterBase):
        def __init__(self):
                DBG_AdapterBase.__init__(self,"DBG_DbgGenericOneObjectEntry")  
                self.m_exceptions = DBG_GlobalExceptionsHtmlPrinter(self,"Parent::DBG_DbgGenericOneObjectEntry")
                self.m_informations = DBG_GlobalInformationsHtmlPrinter(self,"Parent::DBG_DbgGenericOneObjectEntry")
                self.m_env_printer = DBG_EnvItemPrinter(self,"Parent::DBG_DbgGenericOneObjectEntry")
                self.m_print_steps = 1
                self.m_c_mod =""
                self.m_c_class =""
                self.m_c_addr =""
                
        def print_object(self):
                
                try:
                        self.print_object_internal()
                except:
                        self.xx_exception("DBG_DbgGenericOneObjectEntry::prepare_object::excp")
                        
        def print_object_internal(self):
                try:
                        
                        self.xx_dbg("DBG_DbgGenericOneObjectEntry::print_object::in::")
                        DBG_Html.xx_print_start()                        
                        DBG_Html.xx_ols ("")
                        
                        
                        self.handle_srt_data()
                                
                        DBG_Html.xx_ole ("")
                        DBG_Html.xx_print_end()
                        self.xx_hard_print_steps("xx_print_end")
                        self.xx_dbg("DBG_DbgGenericOneObjectEntry::print_object::out::")
                        
                        self.xx_hard_print_steps("close_files")
                        return 1
                        
                except:
                        try:
                                self.xx_exception_raw("DBG_DbgGenericOneObjectEntry::prepare_object::excp")
                        except:
                                self.xx_print_exception_raw("DBG_DbgGenericOneObjectEntry::prepare_object::excp")
                        return 0

        def handle_srt_data(self):
                try:
                        self.xx_dbg("DBG_DbgGenericOneObjectEntry::handle_srt_data::m_in::")
                        #PHY:((iastora!Wcdl::CrashHiberMemoryDescriptor*)0xfffff801538a4630)
                        #self.m_c_addr = "fffff801538a4630"
                        saddr = self.m_c_addr
                        dd_current = self.get_dispatch_class()
                        if( dd_current != None):
                                dd_current.xx_compute_generic_phy_by_phy(self, "0x" + saddr,"(" + saddr +")" )
                                dd_current.prepare_object()                        
                                dd_current.print_object()
                                
                        self.xx_dbg("DBG_DbgGenericOneObjectEntry::handle_srt_data::m_out::")        
                except:
                        self.xx_exception("DBG_DbgGenericOneObjectEntry::prepare_object::excp")

                        
        def get_dispatch_class(self):
                try:
                        dd_c = None
                        if (self.m_c_class == "DBG_CrashHiberMemoryDescriptor"):
                                dd_c = DBG_CrashHiberMemoryDescriptor("DBG_DbgGenericOneObjectEntry",self)
                                
                         
                        if (self.m_c_class == "DBG_NvcPromoBlkSet"):
                                dd_c = DBG_NvcPromoBlkSet("DBG_DbgGenericOneObjectEntry", self)
                                
                        if (self.m_c_class == "DBG_MemberDiskReq"):
                                dd_c = DBG_MemberDiskReq("DBG_DbgGenericOneObjectEntry", self)
                         
                        if (self.m_c_class == "DBG_NvCrashDmp"):
                                dd_c = DBG_NvCrashDmp("DBG_DbgGenericOneObjectEntry", self)
                                                                        
                        if (self.m_c_class == "DBG_CfgArray"):
                                dd_c = DBG_CfgArray("DBG_DbgGenericOneObjectEntry")
                                
                        if (self.m_c_class == "DBG_RaidDev_PyPtr"):
                                dd_c = DBG_RaidDev_PyPtr("DBG_RaidDev_PyPtr", self)
                       
                       
                        return dd_c
                
                except:
                        self.xx_exception("DBG_DbgGenericOneObjectEntry::prepare_object::excp")
                        return None


        def xx_hard_print_steps(self,tt):
                if(self.m_print_steps):
                        print "===============================================>MAIN_STEPS:" + str(tt)
                        
                
        def xx_exception_raw(self,tt):
                DBG_ExceptionPrinter.print_exception(tt)


        def xx_print_exception_raw(self,tt):
                print tt
                
#!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py eegen 15 r01_srt_promo_1 DBG_CfgArray ffffe0011e8f8a80
#!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py eegen 15 r01_raid_dev DBG_RaidDev_PyPtr ffffe0011e8f8a80