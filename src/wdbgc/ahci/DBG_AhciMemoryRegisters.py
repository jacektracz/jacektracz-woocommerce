import sys
import os

from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_MemoryTools import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. fields.DBG_FieldsMapper import *
from .. appsrc.ahciintl.DBG_AhciHbaCapabilities import *
from .. appsrc.ahciintl.DBG_AHCI_PORT_PyObjTable import *
class DBG_AhciMemoryRegisters(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "AHCI_MEMORY_REGISTERS" )
                self.xx_set_full_class_name ( "iastora!AHCI_MEMORY_REGISTERS" )               
                self.m_fields = DBG_FieldsMapper("DBG_AhciMemoryRegisters"
                                         ,self)
                self.m_fields.add_fields_asstr_u32("IS")
                self.m_fields.add_fields_asstr_u32("PI")
                self.m_fields.add_fields_asstr_u32("CCC_PORTS")
                
                self.mCAP = DBG_AhciHbaCapabilities("DBG_AhciMemoryRegisters")
                self.m_ports = DBG_AHCI_PORT_PyObjTable("Parent::DBG_AHCI_MEMORY_REGISTERS")
                self.xx_dbg("DBG_AhciMemoryRegisters::__init__::out::")
                
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_AhciMemoryRegisters::prepare_object::in::")
                        if(self.xx_is_object()==1):
                                self.m_fields.initialize_by_parent(self)
                                self.mCAP.set_addr_arr(self,"CAP")
                                self.mCAP.prepare_object()
                                
                                self.m_ports.set_parent(self)
                                self.m_ports.set_range(6)
                                self.m_ports.set_addr(self,"SELF")
                                self.m_ports.prepare_object()
                                
                        self.xx_dbg("DBG_AhciMemoryRegisters::prepare_object::out::")
                except:
                        self.xx_exc("DBG_AhciMemoryRegisters::print_object")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_AhciMemoryRegisters::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_AhciMemoryRegisters::print_object::in::")
                        self.prepare_object()
                        if(self.xx_is_object()==1):
                                self.xx_print_ptr("")                
                                self.m_fields.print_object()
                                self.mCAP.print_object()
                                self.m_ports.print_object()
                                
                        self.xx_dbg("DBG_AhciMemoryRegisters::print_object::out::")
                except:
                        self.xx_exception("DBG_AhciMemoryRegisters::print_object")
                                         
                        
                        