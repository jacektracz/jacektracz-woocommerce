import sys
import os
from .. DBG_AdapterBase import *
class DBG_RaidArraySemReq(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_ArraySemReq::__init__::m_in::")
                self.xx_set_class_name ( "ArraySemReq" )
                self.xx_set_full_class_name ( "iastora!ArraySemReq" )
                #self.mApstTable = DBG_ApstTable("Parent::DBG_ArraySemReq")
                self.xx_dbg("DBG_ArraySemReq::__init__::m_out::")
               
        def prepare_object(self):                
                self.xx_dbg("DBG_ArraySemReq::prepare_object::m_in::")              
                
                #self.mApstTable.xx_inc_tabs(self);                
                #self.mApstTable.xx_compute_arr_phy_by_parent(self,"mController")
                
                self.xx_dbg("DBG_ArraySemReq::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_ArraySemReq::print_object::m_in::")
                self.prepare_object()
                self.xx_print_ptr("")
                #self.mApstTable.print_object()
                self.xx_dbg("DBG_ArraySemReq::print_object::m_out::")
