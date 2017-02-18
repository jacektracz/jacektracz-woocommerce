import sys
import os
import logging
from .. apptools.DBG_ToolsBase import *
from .. apptools.DBG_EnvItemData import *
from .. apptools.DBG_EnvManager import *
from .. appcore.config.DBG_EnvSettings import *	

class DBG_Paths(DBG_ToolsBase):
        def __init__(self,spar):                
                DBG_ToolsBase.__init__(self,spar)
                self.xx_set_class_name ( "DBG_Paths" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DBG_Paths" )                
                self.create_items()
                self.m_drive = DBG_EnvSettings().get_env_drive()

        def create_items(self):
                """ ccc """                
                
        def exec_bug(self,s_arg_0,smethod=""):
                """ ccc """
                
        def exec_dispatch(
                self
                , s_fun_selector
                , s_sympath
                , s_srcpath ):
                        
                if(s_fun_selector == "print"):
                        DBG_EnvManager("").getData().print_items()
                        
                self.run_by_selector(
                        s_fun_selector
                        ,s_sympath
                        ,s_srcpath)
                
                run = 1
                
        def run_by_selector(
                self
                , s_fun_selector
                , s_sympath
                , s_srcpath):
                if(s_fun_selector == "generic_1"):
                        dd_ii = DBG_EnvItemData("")
                        dd_ii.m_srcpath = s_sympath
                        dd_ii.m_sympath = "SRC." + s_sympath + "/debug"
                        #print "yyyyyyyyyyyyyyy:" + dd_ii.m_disk
                        #print "yyyyyyyyyyyyyyy1:" + dd_ii.m_exec_command
                        self.xx_execute( dd_ii )
                        
                if(s_fun_selector == "generic_sym_src" or s_fun_selector == "generic"):
                        dd_ii = DBG_EnvItemData("")
                        dd_ii.m_srcpath = s_srcpath
                        dd_ii.m_sympath = "SRC." + s_sympath + "/debug"
                        #print "yyyyyyyyyyyyyyy:" + dd_ii.m_disk
                        #print "yyyyyyyyyyyyyyy1:" + dd_ii.m_exec_command
                        self.xx_execute( dd_ii )
                        
                elif(s_fun_selector == "direct"):                        
                        dd_ii = DBG_EnvManager("").getData().get_by_selector( s_sympath )
                        if(dd_ii != None):
                                self.xx_execute( dd_ii )                     
                else:
                        dd_ii = DBG_EnvManager("").getData().get_by_selector(s_fun_selector)
                        if(dd_ii != None):
                                self.xx_execute( dd_ii )
                        
                
        def xx_sympath(self, psympath, psrcpath):
                s_path = "" + self.m_drive +"\\symbols;"
                s_path = s_path + "" + self.m_drive +"\\lkd\\builds\\" + psympath + ";"
                c_drive = "D"
                if( c_drive == "C"):
                        s_path = s_path + "srv*C:\\Symbols*\\\\ger.corp.intel.com\\ec\\proj\\gk\\EIG\\igk_irst_tools\\symserver\\windows"
                        s_path = s_path + ";srv*C:\\Symbols*http://msdl.microsoft.com/download/symbols;"
                
                if( c_drive == "D"):
                        s_path = s_path + "srv*D:\\Symbols*\\\\ger.corp.intel.com\\ec\\proj\\gk\\EIG\\igk_irst_tools\\symserver\\windows"
                        s_path = s_path + ";srv*D:\\Symbols*http://msdl.microsoft.com/download/symbols;"
                
                self.xx_safe_exe(".sympath " + s_path)
                self.xx_safe_exe(".reload /f iastora.sys")
                self.xx_safe_exe("!lmi iastora")
                self.xx_safe_exe(".srcpath " + "" + self.m_drive +"\\rst\\src_" + psrcpath + "\\iRST")


        def xx_execute(self, dd_dat):
                dd_dat.print_info()
                self.xx_safe_exe(".sympath " + dd_dat.get_sympath())
                self.xx_safe_exe(".reload /f iastora.sys")
                self.xx_safe_exe("!lmi iastora")
                self.xx_safe_exe(".srcpath " + dd_dat.get_srcpath() )
                #self.xx_safe_exe("ed kd_storminiport_mask 0xFF")
                #self.xx_safe_exe("ed kd_default_mask 0xFF")

                #if(dd_dat.m_exec_command != ""):
                #        self.xx_safe_exe( dd_dat.m_exec_command )        
                

        def get_str_dbg(self):
                ccs = """                
        iastorav in wim (2015.11.30 12:40)
            13.2.0.1022
                .sympath  " + self.m_drive +"\symbols;" + self.m_drive +"\lkd\builds\SRC.13.2.0.1022\v1;srv*C:\Symbols*\\ger.corp.intel.com\ec\proj\gk\EIG\igk_irst_tools\symserver\windows;srv*C:\Symbols*http://msdl.microsoft.com/download/symbols;
                .srcpath " + self.m_drive +"\rst\src_13.2.0.1022\iRST

        .load " + self.m_drive +"\lkd\kits\wk\8.1\Debuggers\x64\winext\pykd.pyd
        !py " + self.m_drive +"\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ee 14 asusv1202_v5
        !py " + self.m_drive +"\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ag bp1
        !py " + self.m_drive +"\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pths print
        
        !py " + self.m_drive +"\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ee 15 sky1204_1
        
                """
                return ccs;
        
        