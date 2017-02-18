import sys
import os
import logging
from .. DBG_AdapterBase import *       
from DBG_DriverSupportTable import *

class DBG_DriverFeature(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_DriverFeature::__init__::in::")
                self.xx_set_class_name ( "DriverFeature" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DriverFeature" )
                #self.m_psm = DBG_DriverSupportTable("Parent::DBG_DriverFeature")
                self.xx_dbg("DBG_DriverFeature::__init__::out")
                
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_DriverFeature::prepare_object")
                        
                        #self.m_psm.xx_inc_tabs_ex(self,1,"DBG_DriverFeature")
                        #self.m_psm.xx_compute_arr_phy_by_parent(self,"mDriverSupportTable")
                                                
                        self.xx_dbg("DBG_DriverFeature::prepare_object::out")
                except:
                        self.xx_exception("DBG_DriverFeature::prepare_object")
            
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_DriverFeature::print_object")
                        self.prepare_object()
                        self.xx_print_ptr("")
                        
                        #if(self.m_psm.xx_is_object()):
                        #        self.m_psm.print_object()
                        
                        self.xx_dbg("DBG_DriverFeature::print_object::out")
                except:
                        self.xx_exception("DBG_DriverFeature::print_object")
