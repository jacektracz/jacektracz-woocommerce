import sys
import os

from .. DBG_AdapterBase import *

from DBG_Parameters import *

class DBG_MiniportParameters(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_MiniportParameters::__init__::in::")
                self.xx_set_class_name ( "MiniportParameters" )
                self.xx_set_full_class_name ( "iastora!MiniportParameters" )
                self.mParameters = DBG_Parameters("Parent::DBG_MiniportParameters")
                self.xx_dbg("DBG_MiniportParameters::__init__::in::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_MiniportParameters::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_MiniportParameters::prepare_object::")

                self.mParameters.xx_inc_tabs(self);                
                self.mParameters.xx_compute_arr_phy_by_parent(self,"mParameters")

                self.xx_dbg("DBG_MiniportParameters::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.print_object_internal(self)
                except:
                        self.xx_exception("DBG_MiniportParameters::print_object")
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_MiniportParameters::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.mParameters.xx_is_object()):
                        self.mParameters.print_object()
                self.xx_dbg("DBG_MiniportParameters::print_object_internal::out::")                        
                        
                
