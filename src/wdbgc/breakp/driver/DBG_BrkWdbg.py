import sys
import os
import logging
from pykd import *
from ... breakp.DBG_BreakpBase import *
from ... breakp.DBG_BreakpUtils import *
from ... appcore.memory.DBG_Utils import *

class DBG_BrkWdbg(DBG_BreakpBase):
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
                
                if(tt == "BrkWdbg"):
                        self.exec_methods()
                if(tt == "wdbg_load"):
                        return self.exec_methods_load()                        
                return None
        
        def exec_methods_load(self):
                pp = [
                        "sxe ld iastora"
                ]
                return pp
        def exec_methods(self):
                pp = [
                        " !adapter"
                        ,"!devobj FFFFFA80045F4C80"
                        ,"!devnode fffffa80045467c0"
                        ,"!thread fffff80002e65cc0"
                        ,"!amli lc"
                        ,"sxe ld iastora"
                ]