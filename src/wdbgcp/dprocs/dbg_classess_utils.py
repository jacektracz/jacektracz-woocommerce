import sys
import defines
import logging
from pykd import *
from defines import *
from proc_utils import *

def comm_start(s_i_1,s_i_2):
        try:
                print "************************************************************************"                
                print "*                START_COMMAND"
                print "*"
                print "*"
                print "*"
                print "*"
                print "*"                
                print "************************************************************************"
                
        except:
                print '=========================exception occured================='
                logging.exception('')
                print '==========================================================='
                return
        
def comm_info(s_i_1,s_i_2):
        try:
                print "-------------------------------------------------------------------------"
                print "*"
                print "*"
                print "*                        " + s_i_1       
                print "*"
                print "*"
                print "*"                
                print "-------------------------------------------------------------------------"
                
        except:
                print '=========================exception occured================='
                logging.exception('')
                print '==========================================================='
                return

def safe_exe(s_command,s_info):
        try:
                print "=========================COMMAND START==============================="
                
                print ""                
                print "command: " + s_command
                print "info: " + s_info
                print ""
                print ""
                d1 = dbgCommand(s_command)
                print d1
                print '=========================COMMAND END================================='
        except:
                print '=========================exception occured================='
                logging.exception('')
                print '==========================================================='
                return

                
