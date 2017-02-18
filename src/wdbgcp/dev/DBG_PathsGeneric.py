import sys
import os
import logging
from DBG_AdapterBase import *
from DBG_AhciPortsGeneric import *
from .. ahci.DBG_Capabilities import *

class DBG_PathsGeneric(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_PathsGeneric::__init__::in::")
                self.xx_set_class_name ( "PathsGeneric" )
                self.xx_set_full_class_name ( "iastora!PathsGeneric" )
                self.m_cap = DBG_Capabilities("FROM::DBG_PathsGeneric")
                self.m_ahci_ports =  DBG_AhciPortsGeneric("FROM::DBG_PathsGeneric",self)
                self.xx_dbg("DBG_PathsGeneric::__init__::out::")
               
        
        def prepare_object(self):
                self.xx_dbg("DBG_PathsGeneric::prepare_object::in::")                
                self.m_cap.xx_inc_tabs(self);                
                self.m_cap.xx_compute_arr_phy_by_parent(self,"Capabilities")                                
                self.m_ahci_ports.prepare_object()
                self.xx_dbg("DBG_PathsGeneric::prepare_object::out::")
                
        def print_object(self):
                self.xx_dbg("DBG_PathsGeneric::print_object::in::")
                self.prepare_object()
                self.xx_print_ptr("")
                self.xx_print_ints()
                self.m_cap.print_object()
                self.m_ahci_ports.print_object()
                self.xx_dbg("DBG_PathsGeneric::print_object::out::")
                
        def xx_print_ints(self):
                self.xx_dbg("DBG_PathsGeneric::xx_print_ints::in::")
                ints = ["mPortsImplemented"]
                #DBG_WdbgItemsPrinter().xx_print_parent_hexs_by_selector(self,ints,2)
                self.xx_dbg("DBG_PathsGeneric::xx_print_ints::out::")
                