import sys
import logging
from pykd import *

class DBG_BugsUtils:
    
    def xx_safe_exe(self, s_command, s_info=""):
        try:
                self.xx_print ( "=========================COMMAND START===============================")
                
                self.xx_print ( "")                
                self.xx_print ( "command: " + s_command)
                self.xx_print ( "info: " + s_info)
                self.xx_print ( "")
                self.xx_print ( "")
                d1 = self.xx_dbgCommand(s_command)
                self.xx_print ( d1)
                self.xx_print ( '=========================COMMAND END=================================')
        except:
            self.xx_exception(localAddr,"xx_safe_exe")

    def xx_print(self,tt):
        print tt
            
    def xx_dbgCommand(self,symbol):
        try:
            #self.xx_print ( symbol
            sout = dbgCommand(symbol)
            return sout
        except:
            self.xx_exception(symbol,"xx_dbgCommand")            
            return "0"
    
            
    def xx_exception(self,symbol,method=""):            
        logging.exception("")
