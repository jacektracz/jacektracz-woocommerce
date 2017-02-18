    
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *

from ... appcore.printers.DBG_FieldInfos import *
from ... appcore.config.DBG_PrintConfig import *        
from ... appcore.memory.DBG_Utils import *
from ... appcore.printers.DBG_MethodByAddrPrinter import *


class DBG_MethodByAddrPrinter_Manager(DBG_AdapterBase):
    def __init__(self,spar, pparent):
        DBG_AdapterBase.__init__(self, spar)
        self.xx_set_class_name ( "DBG_MethodByAddrPrinter_Manager" )
        self.xx_set_full_class_name ( "DBG_MethodByAddrPrinter_Manager" )        
        self.m_parent = pparent
        self.m_messages = DBG_FieldInfos("DBG_MethodByAddrPrinter_Manager",self)
        self.m_addresses = []
        self.m_printers = []
        
    def set_parent(self, pparent):
        self.xx_dbg( "DBG_MethodByAddrPrinter_Manager::set_parent::method_in::")
        self.m_parent = pparent
        self.xx_dbg( "DBG_MethodByAddrPrinter_Manager::set_parent::method_out::")
        
    def add_addr(self, pp):
        self.xx_dbg( "DBG_MethodByAddrPrinter_Manager::add_addr::method_in::")
        self.m_addresses.append(pp)
        self.xx_dbg( "DBG_MethodByAddrPrinter_Manager::add_addr::method_out::")
        
    def prepare_object(self):
        try:            
            self.xx_dbg("DBG_MethodByAddrPrinter_Manager::prepare_object::in::")
            for dd_addr in self.m_addresses:
                dd_printer = DBG_MethodByAddrPrinter("DBG_MethodByAddrPrinter_Manager",self)
                dd_printer.set_parent(self.m_parent)
                dd_printer.set_addr_string(dd_addr)
                dd_printer.prepare_object()
                self.m_printers.append(dd_printer)
                
            self.xx_dbg("DBG_MethodByAddrPrinter_Manager::prepare_object::out::")
        except:
            self.xx_exception("DBG_MethodByAddrPrinter_Manager::prepare_object::exception::")
        
    def print_object(self,sdbg=""):
            try:
                    self.xx_print_start("")
                    self.print_object_internal(sdbg)
                    self.xx_print_end("")
            except:
                    self.xx_exception("DBG_PnpState::print_object")

    def print_object_internal(self,sdbg=""):
            try:
                self.xx_dbg("DBG_MethodByAddrPrinter_Manager::print_object::m_in::")
                for dd_printer in self.m_printers:
                    dd_printer.print_object()                            
                self.xx_dbg("DBG_MethodByAddrPrinter_Manager::print_object::m_out::")
            except:
                    self.xx_exception("DBG_MethodByAddrPrinter_Manager::print_object_internal:exc")
