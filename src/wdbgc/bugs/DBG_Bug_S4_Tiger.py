import sys
import os
import logging
from .. bugs.DBG_BugsBase import *

class DBG_Bug_S4_Tiger(DBG_BugsBase):
        def __init__(self,spar):                
                DBG_BugsBase.__init__(self,spar)
                self.xx_set_class_name ( "DBG_Bug_S4_Tiger" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DBG_Bug_S4_Tiger" )

        def exec_bug(self,s_arg_0,smethod=""):
                """ ccc """
                
        def exec_dispatch(self,s_arg_0,s_arg_1,s_arg_2):
                
                if(s_arg_2== "bp0"):
                        self.xx_bp("storport!RaDriverPowerIrp")
                        self.xx_bp("iastora!Transport_CrashdumpDispatchDpcRoutine")
                        self.xx_bp("iastora!Transport_DispatchDpcRoutine")
                        self.xx_bp("iastora!Raidport::suspendSubstateTransitionComplete")
                        self.xx_bp("iaStorA!Raidport_IsmSuspendCallback+0x2e")
                        self.xx_bp("iaStorA!RaidIsm::suspend")
                        self.xx_bp("iaStorA!AhciHwStorAdapterControl")
                        self.xx_bp("Raidport_IsmSuspendCallback")
                        
                        pp = ["Controller::shutdown"
                              ,"Wcdl::Timer::stop"
                              ,"iaStorA!Raidport::stopIsmTimer"
                              ,"iaStorA!Raidport_IsmSuspendCallback"
                              ,"iaStorA!Raidport_IsmSuspendCallbackEx"
                              ,"iaStorA!Raidport_IsmShutdownCallback"
                              ,"iaStorA!Raidport_IsmRemoveCallback"
                              ,"Raidport::suspendIsm"
                              ,"Raidport::~Raidport"
                              ,"RaidIsm::suspend"
                              ,"NvmePort::startIoPower"
                              ,"AhciHwStorAdapterControl"
                              ,"RaidportUnitControl"
                              ,"RaidportAdapterRaidportUnitControlControl"]
                        self.xx_bp_arr(pp)
                        
                run = 1
                
        def xx_bp(self,tt):                
                self.xx_safe_exe("bp " + tt)
             
        def bp(self,tt):                
                self.xx_safe_exe("bp " + "iaStorA!" + tt)
             
        def strorkd64(self):
                self.xx_safe_exe(".load D:\lkd\kits\wk\dbg7\storkd64.dll")
                self.xx_safe_exe("!storkd64.adapter")
                
        def get_str_dbg(self):                
                ccs = """                
        .load D:\lkd\kits\wk\8.1\Debuggers\x64\winext\pykd.pyd
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pths generic 15.0.0.9176.DEV
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py bugs s4_tiger bp0        
                """
                return ccs;
        
        