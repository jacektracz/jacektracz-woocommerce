import sys
import os
import logging
from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_MemoryTools import *
from .. raidport.DBG_Target import *
                
class DBG_TargetGeneric(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_TargetGeneric::__init__::in::")
                self.xx_set_class_name ( "TargetGeneric" )
                self.xx_set_full_class_name ( "iastora!TargetGeneric" )
                self.m_target = DBG_Target("FROM::DBG_TargetGeneric")
                self.xx_dbg("DBG_TargetGeneric::__init__::out::")
               
        
        def prepare_object(self,sdbg):
                self.xx_dbg("DBG_TargetGeneric::prepare_object::in::")                
                self.m_target.xx_inc_tabs(self);                
                self.m_target.xx_compute_arr_phy_by_parent(self,"mTarget")
                self.xx_dbg("DBG_TargetGeneric::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_TargetGeneric::print_object::in::")
                self.prepare_object()
                self.xx_print_ptr("")
                #self.xx_print_ints()
                self.m_target.print_object()
                self.xx_dbg("DBG_TargetGeneric::print_object::out::")
                
        def xx_print_ints(self):
                self.xx_dbg("DBG_TargetGeneric::xx_print_ints::in::")
                ints = ["mPortsImplemented"]                
                self.xx_dbg("DBG_TargetGeneric::xx_print_ints::out::")