import sys
import os
import logging
from .. breakp.DBG_BreakpBase import *
from .. breakp.DBG_BreakpRaidport import *

class DBG_BreakpDispatcher(DBG_BreakpBase):
        def __init__(self,spar):                
                DBG_BreakpBase.__init__(self,spar)
                self.xx_set_class_name ( "DBG_BreakpDispatcher" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DBG_BreakpDispatcher" )
                self.xx_dbg("DBG_BreakpDispatcher::__init__::method_out::")
                
                
        def exec_dispatch(self
                          ,     s_arg_0
                          ,     p_app_dispatcher
                          ,     p_break_handler
                          ,     p_provided_break_handle):
                
                self.xx_raw_print( "================>run-DBG_BreakpDispatcher")
                self.xx_dbg("DBG_BreakpDispatcher::exec_dispatch::method_in::" + p_app_dispatcher)
                
                if(p_app_dispatcher == "raidp"):
                        self.xx_raw_print( "================>DBG_BreakpDispatcher::is-handled")
                        
                        dd = DBG_BreakpRaidport("")
                        dd.exec_dispatch(
                                s_arg_0
                                , p_app_dispatcher
                                , p_break_handler
                                , p_provided_break_handle
                                )
                else:
                        self.xx_raw_print("================>DBG_BreakpDispatcher::not-handled")
                        run = 1
                        
                self.xx_dbg("DBG_BreakpDispatcher::exec_dispatch::method_out::")                        
                
        def xx_bp(self,tt):                
                self.xx_safe_exe("bp " + tt)
                
        def xx_raw_print(self,tt):                
                print tt
                
        def get_str_dbg(self):                
                ccs = """                
        
                """
                return ccs;
        
        