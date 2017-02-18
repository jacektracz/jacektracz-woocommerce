import sys
import os
from ... appcore.printers.DBG_Base import *
from ... appcore.printers.DBG_FieldInfos import *
from ... appcore.config.DBG_PrintConfig import *
from ... appcore.htmlwriters.DBG_Html import *
from ... appcore.globinfo.DBG_MainInformationsSet import *

class DBG_GlobalInformationsHtmlPrinter(DBG_Base):
    def __init__(self,pparent,sdbg):
        DBG_Base.__init__(self,pparent,sdbg)
        self.m_parent = pparent
        self.m_messages = DBG_FieldInfos("DBG_MemoryPtr",self)
        self.m_config = None
        
    def set_parent(self, pparent):
        self.xx_dbg( "DBG_GlobalInformationsHtmlPrinter::set_parent::method_in::")
        self.m_parent = pparent
        self.xx_dbg( "DBG_GlobalInformationsHtmlPrinter::set_parent::method_out::")
        
    def prepare_object(self):
        try:
            
            self.xx_dbg("DBG_GlobalInformationsHtmlPrinter::prepare_object")
            self.m_messages.set_parent(self.m_parent)
            self.m_messages.clear_array()
            arr_s = DBG_MainInformationsSet(self,"DBG_GlobalInformationsHtmlPrinter").get_infos_as_strings()
            for dd_ii in arr_s:
                self.add_msg("information",dd_ii)

            self.xx_dbg("DBG_GlobalInformationsHtmlPrinter::prepare_object")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
        
    def add_msg(self, title,tt):
        self.m_messages.add_message(title + ":" + tt)
        
    def print_object(self):
                try:                        
                        self.print_object_internal()                        
                except:
                        self.xx_exception("DBG_FieldsMapper::print_object")
                
    def print_object_internal(self):
        try:
            self.xx_dbg( "DBG_GlobalInformationsHtmlPrinter::xx_print_link_ptr::method_in::")
            self.m_messages.print_object("appcore.informations")
            self.xx_dbg( "DBG_GlobalInformationsHtmlPrinter::xx_print_link_ptr::method_in::")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")

            
            
            