import sys
import os
from dprocs.proc_classess import *

def run_dispatch(s_arg,s_arg_1,s_arg_2):
        exec_run()

if __name__ == "__main__":
	
		s_arg_0 ='ee'
		s_arg_1 =''
		s_arg_2 =''
		if len(sys.argv) > 1:
				s_arg_0 = sys.argv[1]
		if len(sys.argv) > 2:
				s_arg_1 = sys.argv[2]
				
		if len(sys.argv) > 3:
				s_arg_2 = sys.argv[3]
				
		run_dispatch(s_arg_0,s_arg_1,s_arg_2)
		#!py C:\lkd\komodo\w2\src\w2\rst_windbg_ext.py ee