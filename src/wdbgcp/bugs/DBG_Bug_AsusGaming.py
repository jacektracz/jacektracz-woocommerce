import sys
import os
import logging
from .. bugs.DBG_BugsBase import *

class DBG_Bug_AsusGaming(DBG_BugsBase):
        def __init__(self,spar):                
                DBG_BugsBase.__init__(self,spar)
                self.xx_set_class_name ( "DBG_Bug_AsusGaming" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DBG_Bug_AsusGaming" )

        def exec_bug(self,s_arg_0,smethod=""):
                """ ccc """
                
        def exec_dispatch(self,stype):
                
                if(stype== "bp0"):            
                        self.xx_safe_exe("bp iaStorAV!ZpoddDevice::timeout")
                        
                if(stype== "bp1"):
                        self.xx_safe_exe("bp iaStorAV!ZpoddDevice::timeout+0xd7")
                        #self.xx_safe_exe("bp iaStorAV!ZpoddDevice::timeout")
                        #self.xx_safe_exe("bp iaStorAV!RpiPauseDevice")
                        self.xx_safe_exe("bp Raidport::~Raidport")
                        self.xx_safe_exe("bp Raidport::Raidport")
                        self.xx_safe_exe("bp Raidport::RaidportDriverUnload")
                        self.xx_safe_exe("bp Wcdl::TimerList::insert")
                        self.xx_bp("ZpoddDevice::~ZpoddDevice")
                        self.xx_safe_exe("bp iaStorAV!Wcdl::Timer::stop+0x")
                        self.xx_safe_exe("bp iaStorAV!Wcdl::Timer::start+0xed")
                        self.xx_safe_exe("bp iaStorAV!Wcdl::Timer::HwStorTimerEx+0x2e")
                        
                if(stype== "bp2"):                        
                        self.xx_safe_exe("bp Wcdl::TimerList::HwStorTimer")
                        self.xx_safe_exe("bp Wcdl::TimerList::HwStorTimerEx")
                        self.xx_safe_exe("bp Wcdl::TimerList::checkTimers")
                        self.xx_safe_exe("bp Wcdl::TimerList::insert")
                        self.xx_safe_exe("bp iaStorAV!Wcdl::Timer::HwStorTimerEx+0x2e")
                        self.xx_safe_exe("bp iaStorAV!Wcdl::Timer::stop+0x")
                        self.xx_safe_exe("bp iaStorAV!Wcdl::Timer::start+0xed")
                        self.xx_safe_exe("bp iaStorAV!ZpoddDevice::setState+0x90")
                        self.xx_bp("ZpoddDevice::~ZpoddDevice")
                        
                if(stype== "bp3"):                        
                        self.xx_safe_exe("bp Wcdl::TimerList::HwStorTimer")
                        self.xx_safe_exe("bp Wcdl::TimerList::HwStorTimerEx")
                        
                run = 1
                
        def xx_bp(self,tt):                
                self.xx_safe_exe("bp " + tt)
                
        def get_str_dbg(self):                
                ccs = """                
        iastorav in wim (2015.11.30 12:40)
            13.2.0.1022
                .sympath  D:\symbols;D:\lkd\builds\SRC.13.2.0.1022\v1;srv*C:\Symbols*\\ger.corp.intel.com\ec\proj\gk\EIG\igk_irst_tools\symserver\windows;srv*C:\Symbols*http://msdl.microsoft.com/download/symbols;
                .srcpath D:\rst\src_13.2.0.1022\iRST

        .load D:\lkd\kits\wk\8.1\Debuggers\x64\winext\pykd.pyd
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ee 14 asusv1202_v5
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ag bp1
        
                """
                return ccs;
        
        