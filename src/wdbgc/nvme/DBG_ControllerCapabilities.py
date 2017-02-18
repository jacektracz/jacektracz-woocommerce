import sys
import os
import logging
from .. DBG_AdapterBase import *
class DBG_ControllerCapabilities(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "CONTROLLER_CAPABILITIES" )
                self.xx_set_full_class_name ( "iastora!CONTROLLER_CAPABILITIES" )
               
        def prepare_object(self):                
                self.xx_dbg("DBG_ControllerCapabilities::prepare_object::")
                self.xx_dbg("DBG_ControllerCapabilities::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_ControllerCapabilities::print_object::")
                self.prepare_object()
                self.xx_print_ptr("")
                self.xx_dbg("DBG_ControllerCapabilities::print_object::out")
