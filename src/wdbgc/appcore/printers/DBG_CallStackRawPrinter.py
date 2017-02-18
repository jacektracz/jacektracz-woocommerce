import sys
import os

from ... appcore.printers.DBG_Base import *
from ... appcore.printers.DBG_FieldInfos import *
from ... appcore.config.DBG_PrintConfig import *
from ... appcore.htmlwriters.DBG_Html import *
from ... appcore.memory.DBG_Utils import *
class DBG_CallStackRawPrinter(DBG_Base):
    def __init__(self,pparent,sdbg):
        DBG_Base.__init__(self, pparent, sdbg)
        self.m_parent = pparent
        self.m_messages = DBG_FieldInfos("DBG_CallStackRawPrinter",self)
        self.m_format = "full"
        
    def set_parent(self,pparent):
        self.xx_dbg( "DBG_CallStackRawPrinter::set_parent::method_in::")
        self.m_parent = pparent
        self.xx_dbg( "DBG_CallStackRawPrinter::set_parent::method_out::")
        
    def set_format(self,pp):
        self.xx_dbg( "DBG_CallStackRawPrinter::set_parent::method_in::")
        self.m_format = pp
        self.xx_dbg( "DBG_CallStackRawPrinter::set_parent::method_out::")
        
    def prepare_object(self):
        try:
            self.m_messages.clear_messages()
            self.prepare_data()
            self.xx_dbg("DBG_CallStackRawPrinter::prepare_object")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
            
    def prepare_data(self):
        try:
            """ """
            s_expr = "kP"
            if(self.m_format == "short"):
                s_expr = "k"
            vv_class = DBG_Utils().get_stack("k")
            for dd_ii in vv_class:
                self.add_msg( '',dd_ii)
        except:
            self.xx_exception("print_threads::exception::")
            
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
            self.xx_dbg( "DBG_CallStackRawPrinter::xx_print_link_ptr::method_in::")
            self.m_messages.print_object("call_stack_" + self.m_format)
            self.xx_dbg( "DBG_CallStackRawPrinter::xx_print_link_ptr::method_in::")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
            
          
   