import sys
import os
from ... appcore.printers.DBG_Base import *
from ... appcore.printers.DBG_FieldInfos import *

class DBG_BaseHtmlPrinter(DBG_Base):
    def __init__(self,pparent,sdbg):
        DBG_Base.__init__(self,pparent,sdbg)
        self.m_parent = pparent
        self.m_messages = DBG_FieldInfos("DBG_MemoryPtr",self)
    
    def set_parent(self,pparent):
        self.xx_dbg( "DBG_BaseHtmlPrinter::set_parent::method_in::")
        self.m_parent = pparent
        self.xx_dbg( "DBG_BaseHtmlPrinter::set_parent::method_out::")
        
    def prepare_object(self):
        try:
            self.xx_dbg("DBG_BaseHtmlPrinter::prepare_object")
            self.m_messages.set_parent(self.m_parent)
            self.m_messages.add_message(self.m_parent.m_stored_class_ptr_by_phy_addr)
            self.m_messages.add_message(self.m_parent.m_lg_ptr)
            self.xx_dbg("DBG_BaseHtmlPrinter::prepare_object")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
        
                
    def print_object(self,stabs=0):
        try:
            self.xx_dbg( "DBG_BaseHtmlPrinter::xx_print_link_ptr::method_in::")
            self.m_messages.print_object("windbg_addressess")
            self.xx_dbg( "DBG_BaseHtmlPrinter::xx_print_link_ptr::method_in::")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")                        