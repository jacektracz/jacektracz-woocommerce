import sys
import os
#from wdbgc.storagekd.DBG_Proc import *
#from wdbgc.storagekd.DBG_storagekd import *        
from wdbgc.directentry.DBG_DbgEntry import *
from wdbgc.directentry.DBG_DbgEntryV2 import *
from wdbgc.bugs.DBG_Bug_Dispatch import *
from wdbgc.breakp.DBG_BreakpDispatcher import *
from wdbgc.apptools.DBG_Paths import *

def run_dispatch(s_arg_0,s_arg_1,s_arg_2,s_arg_3,s_arg_4):
        run=0
              
        if s_arg_0 == "eev1":
                DBG_DbgEntry().print_object(s_arg_1,s_arg_2)
                run = 1

        if s_arg_0 == "ee":
                DBG_DbgEntryV2().print_object(s_arg_1,s_arg_2)
                run = 1
        
        if s_arg_0 == "eegen":
                ddg = DBG_DbgEntryV2()
                ddg.m_direct = "Y"
                ddg.m_direct_class = s_arg_3
                ddg.m_direct_addr = s_arg_4
                ddg.print_object(s_arg_1,s_arg_2)
                run = 1
            
        if s_arg_0 == "eeg":
                ddgr = DBG_graidport("main")
                ddgr.prepare_object()
                ddgr.print_object()
                #DBG_graidport().print_object()	           
                run = 1
        
        if s_arg_0 == 'bugs':
            
            dd = DBG_Bug_Dispatch("ag")
            dd.exec_dispatch(s_arg_0
                             ,s_arg_1
                             ,s_arg_2)
        
        if s_arg_0 == 'breakp':
            
            dd = DBG_BreakpDispatcher("ag")            
            dd.exec_dispatch(s_arg_0
                             ,s_arg_1
                             ,s_arg_2
                             ,s_arg_3)
            
        if s_arg_0 == 'pths':
                dd = DBG_Paths("ag")
                #generic_sym_src,generic
                s_fun_selector = s_arg_1
                s_sympath = s_arg_2
                s_srcpath = s_arg_3           
                dd.exec_dispatch(
                        s_fun_selector
                        , s_sympath
                        , s_srcpath)
                
                run = 1			

if __name__ == "__main__":
	
        s_arg_0 ='ee'
        s_arg_1 =''
        s_arg_2 =''
        s_arg_3 =''
        s_arg_4 =''
        
        if len(sys.argv) > 1:
                s_arg_0 = sys.argv[1]
        if len(sys.argv) > 2:
                s_arg_1 = sys.argv[2]
                
        if len(sys.argv) > 3:
                s_arg_2 = sys.argv[3]
                
        if len(sys.argv) > 4:
                s_arg_3 = sys.argv[4]
                
        if len(sys.argv) > 5:
                s_arg_4 = sys.argv[5]
                
        run_dispatch(s_arg_0,s_arg_1,s_arg_2,s_arg_3,s_arg_4)
        #!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py eegen 15 r01_srt_one_2 DBG_CrashHiberMemoryDescriptor fffff801538a4630
        #!py C:\lkd\komodo\w2\src\w2\rst_windbg_ext.py ee
        #!py C:\lkd\komodo\w2\src\w2\rst_windbg_ext.py bugs win7 bp0
        #!py C:\lkd\komodo\w2\src\w2\rst_windbg_ext.py bugs asus bp0
        