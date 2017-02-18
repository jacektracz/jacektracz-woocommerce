﻿import sys
import os
import logging
from .. DBG_AdapterBase import *
class DBG_ControllerConfiguration(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "CONTROLLER_CONFIGURATION" )
                self.xx_set_full_class_name ( "iastora!CONTROLLER_CONFIGURATION" )
               
        def prepare_object(self):                
                self.xx_dbg("DBG_ControllerConfiguration::prepare_object::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_ControllerConfiguration::print_object::")
                self.prepare_object()
                self.xx_print_ptr("")
