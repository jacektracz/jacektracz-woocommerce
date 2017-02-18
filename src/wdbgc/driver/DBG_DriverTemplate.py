import sys
import os
import logging
from .. DBG_AdapterBase import *       

class DBG_DriverTemplate(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_DriverTemplate::__init__::in::")
                self.xx_set_class_name ( "DriverFeatures" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DriverFeatures" )
                #self.m_psm = DBG_PortStateMachineN("Parent::DBG_DriverTemplate")
                self.xx_dbg("DBG_DriverTemplate::__init__::out")
                
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_DriverTemplate::prepare_object")        
                        #self.m_psm.xx_inc_tabs_ex(self,1,"DBG_DriverTemplate")
                        #self.m_psm.xx_compute_phy_by_parent(self,"mStateMachine")
                                                
                        self.xx_dbg("DBG_DriverTemplate::prepare_object::out")
                except:
                        self.xx_exception("DBG_DriverTemplate::prepare_object")
            
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_DriverTemplate::print_object")        
                        self.prepare_object()
                        self.xx_print_ptr("")
                        
                        #if(self.m_psm.xx_is_object()):
                        #        self.m_psm.print_object()                                                        
                        self.xx_dbg("DBG_DriverTemplate::print_object::out")
                except:
                        self.xx_exception("DBG_DriverTemplate::print_object")



