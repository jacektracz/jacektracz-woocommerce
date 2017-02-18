import sys
import os
import logging
from .. DBG_AdapterBase import *       
                
class DBG_ZpoddDeviceN(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "ZpoddDevice" )
                self.xx_set_full_class_name ( "iastora!ZpoddDevice" )
                
        def prepare_object(self):
                self.xx_dbg("DBG_ZpoddDeviceN::prepare_object::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_ZpoddDeviceN::print_object::")
                self.prepare_object()
                self.xx_print_ptr("")
                                                                