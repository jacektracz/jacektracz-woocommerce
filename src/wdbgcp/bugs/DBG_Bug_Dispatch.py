import sys
import os
import logging
from .. bugs.DBG_BugsBase import *
from .. bugs.DBG_Bug_AsusGaming import *
from .. bugs.DBG_Bug_Win7_Crash import *
from .. bugs.DBG_Bug_S4_Tiger import *

class DBG_Bug_Dispatch(DBG_BugsBase):
        def __init__(self,spar):                
                DBG_BugsBase.__init__(self,spar)
                self.xx_set_class_name ( "DBG_Bug_Dispatch" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DBG_Bug_Dispatch" )
                
        def exec_dispatch(self,s_arg_0,s_arg_1,s_arg_2):
                
                if(s_arg_1 == "win7crash"):
                        dd = DBG_Bug_Win7_Crash("")
                        dd.exec_dispatch(s_arg_0,s_arg_1,s_arg_2)
                        
                if(s_arg_1 == "asus"):
                        dd = DBG_Bug_AsusGaming("")
                        dd.exec_dispatch(s_arg_2)
                        
                if(s_arg_1 == "s4_tiger"):
                        dd = DBG_Bug_S4_Tiger("")
                        dd.exec_dispatch(s_arg_0,s_arg_1,s_arg_2)
                        
                run = 1
                
        def xx_bp(self,tt):                
                self.xx_safe_exe("bp " + tt)
                
        def get_str_dbg(self):                
                ccs = """                
        .load D:\lkd\kits\wk\8.1\Debuggers\x64\winext\pykd.pyd
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py bugs win7crash bp0
        
                """
                return ccs;
        
        