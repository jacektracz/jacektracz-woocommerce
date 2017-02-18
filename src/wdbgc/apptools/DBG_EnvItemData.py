import sys
import os
import logging
from .. apptools.DBG_ToolsBase import *
from .. appcore.config.DBG_EnvSettings import *	
class DBG_EnvItemData(DBG_ToolsBase):
        def __init__(self,spar):                
                DBG_ToolsBase.__init__(self,spar)
                self.xx_set_class_name ( "DBG_EnvItemData" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DBG_EnvItemData" )
                self.m_sympath = ""
                self.m_srcpath = ""
                self.m_description = ""
                self.m_command_set_env = ""
                self.m_command_test = ""
                self.m_date = ""
                self.m_status = 0
                self.m_selector = "X"
                self.m_exec_command = "!py D:\\lkd\komodo\\w2_2\\src\\w2\\rst_windbg_ext.py ee 15 sky1204_1"
                self.m_dump = ""
                self.m_kernel_conn = ""
                self.m_load_command = ".load D:\\lkd\\kits\\wk\\8.1\\Debuggers\\x64\\winext\\pykd.pyd"
                self.m_disk = DBG_EnvSettings().get_env_drive()
                
        def get_accel_dump(self):
                self.m_sympath = "IA.15.0.0.1010.D2"
                self.m_srcpath = "15.0.0.1012"
                self.m_description = "accel_dump"
                self.m_command_set_env = ""
                self.m_command_test = ""
                self.m_date = "2015-12-07"
                self.m_status = 0
                self.m_selector = "accel_dump"
                self.m_exec_command = "!py D:\\lkd\komodo\\w2_2\\src\\w2\\rst_windbg_ext.py ee 15 sky1204_1"
                self.m_dump = "D:\\lkd\\dumps\\accel_dum\\accel_dump.dmp"
                self.m_kernel_conn = "file"
                
        def get_15_0_0_1019(self):
                self.m_sympath = "15.0.0.1019\\debug"
                self.m_srcpath = "15.0.0.1019"
                self.m_description = "SKY 10 platform test"
                self.m_command_set_env = ""
                self.m_command_test = ""
                self.m_date = "2015-12-07"
                self.m_status = 0
                self.m_selector = "1019"
                self.m_kernel_conn = "1934"
                
        def get_kbl3_15_0_0_1012(self):
                self.m_sympath = "KBL3.15.0.0.1012\\debug"
                self.m_srcpath = "15.0.0.1012"
                self.m_description = "kbl3 platform test"
                self.m_command_set_env = ""
                self.m_command_test = ""
                self.m_date = "2015-12-07"
                self.m_status = 0
                self.m_selector = "kbl_3"
                self.m_kernel_conn = "1934"
                self.m_dump = "D:\\lkd\\dumps\\kbl_s3_dumps\\crash_dump\\kbl_running_before_dump.dmp"
                
        def get_sky_test(self):
                self.m_sympath = "15.0.0.1012"
                self.m_srcpath = "15.0.0.1012"
                self.m_description = "SKY 10 platform test"
                self.m_command_set_env = ""
                self.m_command_test = ""
                self.m_date = "2015-12-07"
                self.m_status = 0
                self.m_selector = "sky_test"
                self.m_kernel_conn = "1934"
                
        def get_sky_test_2(self):
                self.m_sympath = "MAINLINE"
                self.m_srcpath = "15.0.0.1012"
                self.m_description = "SKY 10 platform test"
                self.m_command_set_env = ""
                self.m_command_test = ""
                self.m_date = "2015-12-07"
                self.m_status = 1
                self.m_selector = "sky_test_2"
                self.m_kernel_conn = "1934"
        def get_inbox(self):
                self.m_sympath = "SRC.13.2.0.1022\v1"
                self.m_srcpath = "13.2.0.1022"
                self.m_description = "inbox,asus.iastorav[m_is_inbox = 1]"
                self.m_command_set_env = ""
                self.m_command_test = ""
                self.m_date = "2015-12-07"
                self.m_status = 1
                self.m_selector = "inbox_asus"
                self.m_exec_command = "!py D:\\lkd\komodo\\w2_2\\src\\w2\\rst_windbg_ext.py ee 14 sky1204_1"
                self.m_kernel_conn = "USB"

                
        def get_mainline(self):
                self.m_sympath = "MAINLINE"
                self.m_srcpath = "mainline"
                self.m_description = "SKY 10 platform test"
                self.m_command_set_env = ""
                self.m_command_test = ""
                self.m_date = "2015-12-08"
                self.m_status = 1
                self.m_selector = "mainline"
                self.m_kernel_conn = "1934"
                
        def get_win7(self):
                self.m_sympath = "SRC.15.0.0.1019\\debug"
                self.m_srcpath = "15.0.0.1019"
                self.m_description = "win7_4939010"
                self.m_command_set_env = ""
                self.m_command_test = ""
                self.m_date = "2015-12-07"
                self.m_status = 0
                self.m_selector = "win7_15"
                self.m_kernel_conn = "1934"
                self.m_dump = "D:\\lkd\\dumps\\win7_crash\\dmp\\memory_win7_.dmp"
                
        def get_15_0_0_1019_DEV(self):
                self.m_sympath = "SRC.15.0.0.1019.DEV\\debug"
                self.m_srcpath = "15.0.0.1019.DEV"
                self.m_description = "win7_4939010"
                self.m_command_set_env = ""
                self.m_command_test = ""
                self.m_date = "2015-12-07"
                self.m_status = 0
                self.m_selector = "win7_15_dev"
                self.m_kernel_conn = "1934"
                self.m_dump = "D:\\lkd\\dumps\\win7_crash\\dmp\\memory_win7_.dmp"
                
        def get_14_6_1_1030(self):
                self.m_sympath = "SRC.14.6.1.1030\\debug"
                self.m_srcpath = "14.6.1.1030"
                self.m_description = "win7_4939010"
                self.m_command_set_env = ""
                self.m_command_test = ""
                self.m_date = "2015-12-07"
                self.m_status = 0
                self.m_selector = "win7_14"
                self.m_kernel_conn = "1934"
                self.m_dump = "D:\\lkd\\dumps\\win7_crash\\dmp\\memory_win7_.dmp"

        def print_info(self):
                self.xx_print("ITEM" , "****************************************" )
                self.xx_print("m_selector" , str(self.m_selector) )
                self.xx_print("m_sympath:" , self.m_sympath )
                self.xx_print("m_srcpath" , self.m_srcpath )
                self.xx_print("m_description" , self.m_description )
                self.xx_print("m_command_set_env" , self.m_command_set_env )
                self.xx_print("m_command_test" , self.m_command_test )
                self.xx_print("m_date" , self.m_date )
                self.xx_print("m_status" , str(self.m_status) )
                self.xx_print("" , ".sympath " + self.get_sympath() )
                self.xx_print("" , ".srcpath " + self.get_srcpath() )
                self.xx_print("" , self.m_exec_command )
                self.xx_print("" , self.m_load_command )
                self.xx_print("m_dump" ,   self.m_dump )
                self.xx_print("m_kernel_conn" ,   self.m_kernel_conn )
                
        def get_items(self):
                """ ccc """
                l_items = []
                dd_dat = DBG_EnvItemData("")
                dd_dat.get_sky_test_2()
                l_items.append(dd_dat)
                
                dd_dat = DBG_EnvItemData("")
                dd_dat.get_sky_test()
                l_items.append(dd_dat)
                
                dd_dat = DBG_EnvItemData("")
                dd_dat.get_accel_dump()
                l_items.append(dd_dat)
                
                dd_dat = DBG_EnvItemData("")
                dd_dat.get_inbox()
                l_items.append(dd_dat)
                
                dd_dat = DBG_EnvItemData("")
                dd_dat.get_mainline()
                l_items.append(dd_dat)

                dd_dat = DBG_EnvItemData("")
                dd_dat.get_15_0_0_1019()
                l_items.append(dd_dat)
                
                dd_dat = DBG_EnvItemData("")
                dd_dat.get_kbl3_15_0_0_1012()
                l_items.append(dd_dat)

                dd_dat = DBG_EnvItemData("")
                dd_dat.get_win7()
                l_items.append(dd_dat)
                

                dd_dat = DBG_EnvItemData("")
                dd_dat.get_14_6_1_1030()
                l_items.append(dd_dat)

                dd_dat = DBG_EnvItemData("")
                dd_dat.get_15_0_0_1019_DEV()
                l_items.append(dd_dat)
                
                
                return l_items
                
        def get_sympath(self):
                s_path = "" + self.m_disk + ":\\symbols;"
                s_path = s_path + "" + self.m_disk + ":\\lkd\\builds\\" + self.m_sympath + ""
                c_drive = "D"
                
                if( c_drive == "C"):
                        s_path = s_path + ";srv*C:\\Symbols*\\\\ger.corp.intel.com\\ec\\proj\\gk\\EIG\\igk_irst_tools\\symserver\\windows"
                        s_path = s_path + ";srv*C:\\Symbols*http://msdl.microsoft.com/download/symbols;"
                        
                if( c_drive == "D"):
                        s_path = s_path + ";srv*D:\\Symbols*\\\\ger.corp.intel.com\\ec\\proj\\gk\\EIG\\igk_irst_tools\\symserver\\windows"
                        s_path = s_path + ";srv*D:\\Symbols*http://msdl.microsoft.com/download/symbols;"
                        
                return s_path
        
        def get_srcpath(self):
                s_path =  "" + self.m_disk + ":\\rst\\src_" + self.m_srcpath + "\\iRST"
                return s_path
        
        def xx_print(self,pvar, pval):
                if(pvar == ""):
                        print str(pval)
                else:                        
                        print pvar + ":" + str(pval)
        
        def get_str_dbg(self):
                ccs = """                
        iastorav in wim (2015.11.30 12:40)
            13.2.0.1022
                .sympath  D:\symbols;D:\lkd\builds\SRC.13.2.0.1022\v1;srv*C:\Symbols*\\ger.corp.intel.com\ec\proj\gk\EIG\igk_irst_tools\symserver\windows;srv*C:\Symbols*http://msdl.microsoft.com/download/symbols;
                .srcpath D:\rst\src_13.2.0.1022\iRST
                
        ed kd_storminiport_mask 0xFF
        ed kd_default_mask 0xFF
        
        .load C:\lkd\kits\10\Debuggers\x64\winext\pykd.pyd
        !py c:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pyhs accel_dump
        !py c:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ee 15c 20151219_srt_test
        
        .load D:\lkd\kits\wk\10\Debuggers\x64\winext\pykd.pyd

        .load D:\lkd\kits\wk\8.1\Debuggers\x64\winext\pykd.pyd
        
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pths win7_14
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ee 14a 20151214_win7_14
        
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pths win7_15
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ee 15 20151214_2_win7_15_running
        
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ag bp1
        
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pths win7_15
        !py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pths print
                """
                return ccs;
