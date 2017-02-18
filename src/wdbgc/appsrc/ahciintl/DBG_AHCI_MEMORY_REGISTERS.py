

import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
#from .. childdir.DBG_ApstTable import *
from ... appsrc.ahciintl.DBG_AHCI_PORT_PyObjTable import *

class DBG_AHCI_MEMORY_REGISTERS(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_AHCI_MEMORY_REGISTERS::__init__::m_in::")
                self.xx_set_class_name ( "AHCI_MEMORY_REGISTERS" )
                self.xx_set_full_class_name ( "iastora!AHCI_MEMORY_REGISTERS" )
                
                self.m_fields = DBG_FieldsMapper("DBG_AHCI_MEMORY_REGISTERS"
                                         , self)
                
                self.m_fields.add_fields_asstr_u32("IS")
                self.m_fields.add_fields_asstr_u32("PI")

                
                self.m_ports = DBG_AHCI_PORT_PyObjTable("Parent::DBG_AHCI_MEMORY_REGISTERS")
                
                self.xx_dbg("DBG_AHCI_MEMORY_REGISTERS::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_AHCI_MEMORY_REGISTERS::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_AHCI_MEMORY_REGISTERS::prepare_object_internal::")
                
                if(self.xx_is_object()==1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.m_ports.set_parent(self)
                        self.m_ports.set_range(1)
                        self.m_ports.set_addr(self,"SELF")
                        self.m_ports.prepare_object()
                        #self.m_child_item.set_addr_arr(self,"m_child_item")
                
                self.xx_dbg("DBG_AHCI_MEMORY_REGISTERS::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_AHCI_MEMORY_REGISTERS::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_AHCI_MEMORY_REGISTERS::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_is_object()==1):                
                        self.m_fields.xx_print_fields("")                        
                        self.m_ports.print_object()
                        #self.m_child_item.print_object()
                else:
                        self.xx_dbg("DBG_AHCI_MEMORY_REGISTERS::print_object::not_obj::")
                self.xx_dbg("DBG_AHCI_MEMORY_REGISTERS::print_object::m_out::")

