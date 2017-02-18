import sys
import os
import logging
from pykd import *
from .. breakp.DBG_BreakpBase import *
from .. breakp.DBG_BreakpUtils import *
from .. appcore.memory.DBG_Utils import *

from .. breakp.driver.DBG_AhciS4 import *
from .. breakp.driver.DBG_ThreadsError import *
from .. breakp.driver.DBG_BrkStorport import *
from .. breakp.driver.DBG_BrkAhci import *
from .. breakp.driver.DBG_BrkNvme import *
from .. breakp.driver.DBG_BrkChipset import *
from .. breakp.driver.DBG_BrkRaidport import *
from .. breakp.driver.DBG_BrkHandler import *
from .. breakp.driver.DBG_BrkRemapPort import *
from .. breakp.driver.DBG_BrkWdbg import *
from .. breakp.driver.DBG_ExeEnumeration import *
from .. breakp.driver.DBG_BrkRaid5Srt import *
from .. breakp.driver.DBG_BrkScsi import *
from .. breakp.driver.DBG_BrkRRT import *
from .. breakp.driver.DBG_BrkCsmiRaid5 import *
from .. breakp.driver.DBG_NvCache import *

class DBG_BreakpRaidport(DBG_BreakpBase):
        def __init__(self,spar):                
                DBG_BreakpBase.__init__(self,spar)
                self.xx_dbg("DBG_BreakpRaidport::__init__::method_in::")
                self.xx_set_class_name ( "DBG_BreakpRaidport" )
                self.xx_set_full_class_name ( "Wcdl::DBG_BreakpRaidport" )
                self.m_breaks = []
                self.m_handle_io = 0
                self.m_handle_hiber = 0
                self.m_handler = DBG_BrkHandler("",self)
                self.m_handlers = []
                self.init_handlers()
                self.xx_dbg("DBG_BreakpRaidport::__init__::method_out::")
                
        def init_handlers(self):
                self.m_handlers.append(DBG_AhciS4("",self))
                self.m_handlers.append(DBG_BrkChipset("",self))
                self.m_handlers.append(DBG_BrkHandler("",self))
                self.m_handlers.append(DBG_BrkRaidport("",self))
                self.m_handlers.append(DBG_BrkRemapPort("",self))
                self.m_handlers.append(DBG_BrkStorport("",self))
                self.m_handlers.append(DBG_BrkWdbg("",self))
                self.m_handlers.append(DBG_BrkAhci("",self))
                self.m_handlers.append(DBG_BrkNvme("",self))
                self.m_handlers.append(DBG_ThreadsError("",self))
                self.m_handlers.append(DBG_ExeEnumeration("",self))
                self.m_handlers.append(DBG_BrkRaid5Srt("",self))
                self.m_handlers.append(DBG_BrkScsi("",self))
                self.m_handlers.append(DBG_BrkRRT("",self))
                self.m_handlers.append(DBG_BrkCsmiRaid5("",self))
                self.m_handlers.append(DBG_NvCache("",self))
                
        def exec_dispatch(self
                          , s_arg_0
                          , p_app_dispatcher
                          , p_break_handler
                          , p_provided_break_handle = ""):
                
                print "================>run-brk-dispatch"
                
                if(p_provided_break_handle !=""):
                        self.m_provided_handle = p_provided_break_handle
                        
                self.exec_handlers( p_break_handler )                
                
        def exec_handlers(self,p_break_handler):
                try:
                        for dd_handler in self.m_handlers:                        
                                self.exec_handler(dd_handler
                                                  , p_break_handler)
                except:
                    self.xx_exception("exec_handlers") 
                
        def exec_handler(self,dd_handler, tt):
                try:
                        pp = dd_handler.get_dispatch(tt)
                        if(pp!= None):
                                self.xx_set_bpreakpoint_arr(pp)
                except:
                    self.xx_exception("exec_handler") 
                        
        def exec_info(self,dd_handler, tt):
                try:
                        tt = []
                        tt.append(".load D:\lkd\kits\wk\8.1\Debuggers\x64\winext\pykd.pyd")
                        tt.append(".load D:\lkd\kits\wk\10\Debuggers\x64\winext\pykd.pyd")
                        tt.append("!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pths generic 14.8.4_BLD")
                        tt.append("!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py breakp raidp CsmiRaid5")
                except:
                    self.xx_exception("exec_handler") 
                
