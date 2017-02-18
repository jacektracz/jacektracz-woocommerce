import sys
import os
import logging
from .. DBG_AdapterBase import *
from .. helpers.DBG_MemoryTools import *


                
class DBG_RaidportTarget_PyManager(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_RaidportTarget_PyManager::__init__::in::")
                self.xx_set_class_name ( "RaidportTarget" )
                self.xx_set_full_class_name ( "iastora!RaidportTarget" )
                #self.m_target = DBG_Target("FROM::DBG_RaidportTarget_PyManager")
                self.xx_dbg("DBG_RaidportTarget_PyManager::__init__::out::")
               
        
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_RaidportTarget_PyManager::prepare_object::in::")                
                        #self.m_target.xx_inc_tabs(self);                
                        #self.m_target.xx_compute_arr_phy_by_parent(self,"mTarget")
                        self.xx_dbg("DBG_RaidportTarget_PyManager::prepare_object::out::")
                except:
                        self.xx_exception("DBG_RaidportTarget_PyManager::prepare_object")
                
        def print_object(self):
                try:
                        self.xx_dbg("DBG_RaidportTarget_PyManager::print_object::in::")
                        self.prepare_object()
                        self.xx_print_ptr("")
                        #self.xx_print_ints()
                        #self.m_target.print_object()
                        self.xx_dbg("DBG_RaidportTarget_PyManager::print_object::out::")
                except:
                        self.xx_exception("DBG_RaidportTarget_PyManager::print_object")
                        
        def xx_print_ints(self):
                try:                
                        self.xx_dbg("DBG_RaidportTarget_PyManager::xx_print_ints::in::")
                        ints = ["mPortsImplemented"]                
                        self.xx_dbg("DBG_RaidportTarget_PyManager::xx_print_ints::out::")
                except:
                        self.xx_exception("DBG_RaidportTarget_PyManager::xx_print_ints")
                