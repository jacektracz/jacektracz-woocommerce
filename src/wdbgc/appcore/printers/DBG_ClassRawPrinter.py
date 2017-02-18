import sys
import os

from ... appcore.printers.DBG_Base import *
from ... appcore.printers.DBG_FieldInfos import *
from ... appcore.config.DBG_PrintConfig import *
from ... appcore.htmlwriters.DBG_Html import *
from ... appcore.memory.DBG_Utils import *
class DBG_ClassRawPrinter(DBG_Base):
    def __init__(self,pparent,sdbg):
        DBG_Base.__init__(self, pparent, sdbg)
        self.m_parent = pparent
        self.m_messages = DBG_FieldInfos("DBG_ClassRawPrinter",self)
        
    def set_parent(self,pparent):
        self.xx_dbg( "DBG_ClassRawPrinter::set_parent::method_in::")
        self.m_parent = pparent
        self.xx_dbg( "DBG_ClassRawPrinter::set_parent::method_out::")
        
    def prepare_object(self):
        try:
            self.m_messages.clear_messages()
            self.print_class()
            self.xx_dbg("DBG_ClassRawPrinter::prepare_object")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
        
    def add_msg(self, title,tt):
        try:
            self.m_messages.add_message(str(title) + ":" + str(tt))
        except:
                self.xx_exception("DBG_FieldsMapper::add_msg::exception::")
            
        
    def print_object(self):
                try:                        
                        self.print_object_internal()                        
                except:
                        self.xx_exception("DBG_FieldsMapper::print_object")
                
    def print_object_internal(self):
        try:
            self.xx_dbg( "DBG_ClassRawPrinter::xx_print_link_ptr::method_in::")
            self.m_messages.print_object("object_raw")
            self.xx_dbg( "DBG_ClassRawPrinter::xx_print_link_ptr::method_in::")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
            
          
    def print_class(self):
        try:
            """ """
            self.m_messages.set_parent(self.m_parent)
            self.m_messages.add_message(self.m_parent.m_stored_class_ptr_by_phy_addr)
            self.m_messages.add_message(self.m_parent.m_lg_ptr)
            vv_class = DBG_Utils().get_class_info(self.m_parent.m_stored_class_ptr_by_phy_addr)
            for dd_ii in vv_class:
                self.add_msg( 'ff',dd_ii)
        except:
            self.xx_exception("print_threads::exception::")