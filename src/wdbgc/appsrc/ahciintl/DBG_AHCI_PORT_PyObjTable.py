﻿import sys
import os
from ... DBG_AdapterBase import *
from ... appcore.memory.DBG_Utils import *
from ... appcore.memory.DBG_MemoryTools import *
from ... fields.DBG_FieldsMapper import *
from ... appsrc.ahciintl.DBG_AHCI_PORT import *

                
class DBG_AHCI_PORT_PyObjTable(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::__init__::method_in::")
                self.xx_set_class_name ( "AHCI_MEMORY_REGISTERS" )
                self.xx_set_full_class_name ( "iastora!AHCI_MEMORY_REGISTERS" )
                self.m_parent = self
                self.m_range = 32
                self.m_array_items = []
                self.m_table_pointer = "PortList"
                self.m_fields = DBG_FieldsMapper("DBG_RaidIsmDisk"
                                         ,self)
                
                self.m_fields.add_fields_int_array([
                        "LINE"
                        ])
                
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::__init__::method_out::")
                
        def set_table_pointer(self, tp):
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::set_table_pointer::")
                self.m_table_pointer = tp
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::set_table_pointer::out")
                
        def set_range(self,prange):
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::set_parent::")
                self.m_range = prange
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::set_parent::out")
                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::set_parent::")
                self.m_parent = pparent
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::set_parent::out")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal()                                
                except:
                        self.xx_exception("DBG_AHCI_PORT_PyObjTable::print_object")
                                        
        def prepare_object_internal(self):
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::prepare_object_internal::")
                
                self.m_fields.set_fields_parent(self)
                self.m_fields.prepare_object()                
                self.m_array_items= []
                for ii in range(self.m_range):
                        dd = self.get_array_item(ii)
                        if( dd != None):
                                self.m_array_items.append(dd)
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::prepare_object_internal::out")
                
        def get_array_item(self,pii):
                try:
                        self.xx_dbg("DBG_AHCI_PORT_PyObjTable::get_array_item::")
                        dd = DBG_AHCI_PORT("DBG_AHCI_PORT_PyObjTable")
                        
                        s_ptr_expr = self.m_table_pointer + "[" +str(pii) + "]"
                        dd.set_addr_arr(
                                self.m_parent
                                ,       s_ptr_expr)
                        dd.prepare_object()
                        self.xx_dbg("DBG_AHCI_PORT_PyObjTable::get_array_item::out")
                        return dd
                except:
                        self.xx_exception("DBG_AHCI_PORT_PyObjTable::get_array_item::exception::")
                        return None
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):                
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::print_object::")
                self.xx_print_ptr("")
                self.m_fields.print_object()
                self.print_items()
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::print_object::out")

        def print_items(self):
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::print_items::")
                for dd_transport in self.m_array_items:
                        dd_transport.print_object()
                self.xx_dbg("DBG_AHCI_PORT_PyObjTable::print_items::out::")
                
                
                