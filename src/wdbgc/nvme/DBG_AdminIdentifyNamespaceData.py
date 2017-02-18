import sys
import os
from .. DBG_AdapterBase import *
                
class DBG_AdminIdentifyNamespaceData(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_AdminIdentifyNamespaceData::__init__::in::")
                self.xx_set_class_name ( "ADMIN_IDENTIFY_NAMESPACE_DATA" )
                self.xx_set_full_class_name ( "iastora!ADMIN_IDENTIFY_NAMESPACE_DATA" )
                self.xx_dbg("DBG_AdminIdentifyNamespaceData::__init__::out")
                
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_AdminIdentifyNamespaceData::prepare_object")
                        
                        #self.m_psm.xx_inc_tabs_ex(self,1,"DBG_AdminIdentifyNamespaceData")
                        #self.m_psm.xx_compute_phy_by_parent(self,"mStateMachine")
                                                
                        self.xx_dbg("DBG_AdminIdentifyNamespaceData::prepare_object::out")
                except:
                        self.xx_exception("DBG_AdminIdentifyNamespaceData::prepare_object")
            
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_AdminIdentifyNamespaceData::print_object")        
                        self.prepare_object()
                        self.xx_print_ptr("")
                        if(self.xx_is_object() == 0):
                                return
                        
                        self.xx_dbg("DBG_AdminIdentifyNamespaceData::print_object::out")
                except:
                        self.xx_exception("DBG_AdminIdentifyNamespaceData::print_object")

