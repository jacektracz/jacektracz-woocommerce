import sys
import os
import logging
from .. bugs.DBG_BugsBase import *

class DBG_Bug_Win7_Crash(DBG_BugsBase):
        def __init__(self,spar):                
                DBG_BugsBase.__init__(self,spar)
                self.xx_set_class_name ( "DBG_Bug_Win7_Crash" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DBG_Bug_Win7_Crash" )

        def exec_bug(self,s_arg_0,smethod=""):
                """ ccc """
                
        def exec_dispatch(self,s_arg_0,s_arg_1,s_arg_2):
                
                if(s_arg_2== "bp0"):            
                        self.xx_bp("iastora!RaidIsm::suspend")
                        self.xx_bp("iastora!Raidport::completeRaidEnumeration")
                        self.xx_bp("iastora!RaidCfgMgr::whenDiskAdded")
                        self.xx_bp("iastora!RaidIsm::diskAdded")
                        self.xx_bp("iastora!RaidCfgMgr::claimRaidVolAsNvmStor")
                        self.xx_bp("iastora!RaidCfgMgr::createNewRaidDev")
                run = 1
                
        def xx_bp(self,tt):                
                self.xx_safe_exe("bp " + tt)
             
             
        def strorkd64(self):
                self.xx_safe_exe(".load D:\lkd\kits\wk\dbg7\storkd64.dll")
                self.xx_safe_exe("!storkd64.adapter")
                
        def get_str_dbg(self):                
                ccs = """                
        .load D:\lkd\kits\wk\8.1\Debuggers\x64\winext\pykd.pyd
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pths win7_15
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py bugs win7crash bp0
        
                """
                return ccs;
        
        