import sys
import defines
import logging
from pykd import *
from defines import *
from proc_utils import *

class DBG_interrupt:
    def print_interrupt_configuration():        
        print "Interrupt Configuration (what OS see)"
        try:
            output = dbgCommand("!devnode 0 1 iastora").split(' ')
            pdo = 0
            for i,word in enumerate(output) :
                    if word == 'PDO':
                            pdo = output[i+1]
                            break
                                
            output = dbgCommand("!devobj "+ pdo).split(' ')
            devext = 0
            for i,word in enumerate(output) :
                    if word == 'DevExt':
                            devext = output[i+1]
                            break
                
            output = dbgCommand("!devext "+ devext).split('\n')
                
            for i,word in enumerate(output) :
                    if 'Capabilities' in word:
                            print word
                                
                    if 'Interrupt Requirement' in word:
                            print ('\n').join(output[i:])
        except:
                print '=========================exception occured================='
                logging.exception('')
                print '==========================================================='
                return
