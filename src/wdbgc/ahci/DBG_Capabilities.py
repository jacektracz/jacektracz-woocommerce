import sys
import os

from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_MemoryTools import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. fields.DBG_FieldsMapper import *
class DBG_Capabilities(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "AHCI_HBA_CAPABILITIES" )
                self.xx_set_full_class_name ( "iastora!AHCI_HBA_CAPABILITIES" )               
                self.NP = 0
                self.NCS = 0
                self.m_fields = DBG_FieldsMapper("DBG_EndDevice"
                                         , self)
                
                self.m_fields.add_fields_int_array(
                        ["NP","NCS","SXS","EMS","CCCS","SSC","Raw"]
                        )                
                self.xx_dbg("DBG_Capabilities::__init__::out::")
                
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_Capabilities::prepare_object::in::")
                        if(self.xx_is_object()==1):
                                self.m_fields.initialize_by_parent(self)
                                self.NP = DBG_MemoryTools().xx_get_int(self,"NP")
                                self.NCS = DBG_MemoryTools().xx_get_int(self,"NCS")
                        self.xx_dbg("DBG_Capabilities::prepare_object::out::")
                except:
                        self.xx_exc("DBG_Capabilities::print_object")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_Capabilities::print_object::in::")
                        self.prepare_object()
                        if(self.xx_is_object()==1):
                                self.xx_print_ptr("")                
                                self.m_fields.print_object()
                        self.xx_dbg("DBG_Capabilities::print_object::out::")
                except:
                        self.xx_exception("DBG_Capabilities::print_object")
                                         
                        
                        