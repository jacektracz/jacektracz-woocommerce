import sys
import os
import logging
from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_MemoryTools import *
from .. appsrc.raidtargets.DBG_RaidTarget import *
from DBG_raiddev import *
#from DBG_PassThroughTarget import *
                
class DBG_Target(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_Target::__init__::in::")
                self.xx_set_class_name ( "Target" )
                self.xx_set_full_class_name ( "iastora!Target" )
                self.mType = 0
                self.m_raid_target = DBG_RaidTarget("Parent::DBG_Target")
                #self.m_pt_target = DBG_PassThroughTarget("Parent::DBG_Target")
                self.m_raiddev = DBG_raiddev("Parent::DBG_Target")
                #self.m_target = DBG_Target("FROM::DBG_Target")
                self.xx_dbg("DBG_Target::__init__::out::")
                       
        def prepare_object(self):
                self.xx_dbg("DBG_Target::prepare_object::in::")
                self.mType = DBG_MemoryTools().xx_get_int(self,"mType")
                        
                        #self.m_pt_target.xx_inc_tabs(self);
                        #self.m_pt_target.xx_compute_arr_phy_by_parent(self,"SELF")
                        
                if (self.mType == 0):
                        self.m_raid_target.xx_inc_tabs(self);                
                        self.m_raid_target.xx_compute_arr_phy_by_parent(self,"mRaidDev")
                        
                        self.m_raiddev.xx_inc_tabs(self);                
                        self.m_raiddev.xx_compute_arr_phy_by_parent(self,"mRaidDev")
                
                self.xx_dbg("DBG_Target::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_Target::print_object::in::")
                self.prepare_object()
                self.xx_print_ptr("")
                #self.xx_print_ints()
                if (self.mType == 0):
                        self.m_raid_target.print_object()
                self.xx_dbg("DBG_Target::print_object::out::")
                
        def xx_print_ints(self):
                self.xx_dbg("DBG_Target::xx_print_ints::in::")
                ints = ["xx"]                
                self.xx_dbg("DBG_Target::xx_print_ints::out::")