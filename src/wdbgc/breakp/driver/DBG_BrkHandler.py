import sys
import os
import logging
from pykd import *
from ... breakp.DBG_BreakpBase import *
from ... breakp.DBG_BreakpUtils import *
from ... appcore.memory.DBG_Utils import *

class DBG_BrkHandler(DBG_BreakpBase):
        def __init__(self,spar, pparent):                
                DBG_BreakpBase.__init__(self,spar)
                self.xx_dbg("DBG_BreakpRaidport::__init__::method_in::")
                self.xx_set_class_name ( "DBG_BreakpRaidport" )
                self.xx_set_full_class_name ( "Wcdl::DBG_BreakpRaidport" )
                self.m_breaks = []
                self.m_handle_io = 0
                self.m_handle_hiber = 0                
                self.xx_dbg("DBG_BreakpRaidport::__init__::method_out::")
                
        def get_dispatch(self,tt):
                if(tt == "brkhandler"):
                        self.set_handles()
                return None

        def set_handles(self):
                """ ccc """
                self.xx_dbg("DBG_BreakpRaidport::set_handles::method_in::")
                i_test = 1
                self.xx_set_handle_ex("RaidportUnitControl",self.handle_RaidportUnitControl)
                #if(i_test == 1):
                #        return
                self.xx_set_handle_ex("RaidportAdapterControl",self.handle_RaidportAdapterControl)
                self.xx_set_handle_ex("RaidportInterrupt",self.handle_RaidportInterrup)
                self.xx_set_handle_ex("RaidportInitialize",self.handle_RaidportInitialize)
                self.xx_set_handle_ex("RaidportResetBus",self.handle_RaidportResetBus)
                
                if(self.m_handle_io == 1):
                        self.xx_set_handle_ex("RaidportBuildIo",self.handle_RaidportBuildIo)
                        self.xx_set_handle_ex("RaidportStartIo",self.handle_RaidportStartIo)                        
                self.xx_dbg("DBG_BreakpRaidport::set_handles::method_out::")
                
        def get_dispatch(self,tt):
                return None
                
        def handle_RaidportInterrup(self,args):
                
                self.print_method( "handle_RaidportInterrup")
                return False
        
        def handle_RaidportInitialize(self,args):
                
                self.print_method( "handle_RaidportInitialize" )
                return False
        
        def handle_RaidportResetBus(self,args):
                
                self.print_method(  "handle_RaidportResetBus")
                return False
        
        def handle_RaidportBuildIo(self,args):
                
                self.print_method(  "handle_RaidportBuildIo")
                return False
        
        def handle_RaidportStartIo(self,args):
                
                self.print_method(  "handle_RaidportStartIo")
                return False
        
        def handle_RaidportUnitControl(self,args):
                
                self.print_method(  "handle_RaidportUnitControl")
                return False
        
        def handle_RaidportAdapterControl(self,args):
                
                self.print_method( "handle_RaidportAdapterControl")
                return False
