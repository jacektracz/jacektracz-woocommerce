import sys
import os
from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_Utils import *
from .. appcore.memory.DBG_MemoryTools import *

from .. raidism.DBG_CfgRaidDev import *
from .. fields.DBG_FieldsMapper import *

class DBG_CfgRaidDev_PyArray(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_CfgRaidDev_PyArray::__init__::method_in::")
                self.xx_set_class_name ( "DBG_CfgRaidDev_PyArray" )
                self.xx_set_full_class_name ( "iastora!DBG_CfgRaidDev_PyArray" )
                self.m_parent = self
                self.m_range = 32
                self.m_array_items = []
                self.m_table_pointer = "raidDevPtr"
                self.xx_dbg("DBG_CfgRaidDev_PyArray::__init__::method_out::")       
                
        def set_parent(self, pparent):
                self.xx_dbg("DBG_CfgRaidDev_PyArray::set_parent::")
                self.m_parent = pparent
                self.xx_dbg("DBG_CfgRaidDev_PyArray::set_parent::out")
                
        def set_table_pointer(self, tp):
                self.xx_dbg("DBG_CfgRaidDev_PyArray::set_table_pointer::")
                self.m_table_pointer = tp
                self.xx_dbg("DBG_CfgRaidDev_PyArray::set_table_pointer::out")
                
        def set_range(self, prange):
                self.xx_dbg("DBG_CfgRaidDev_PyArray::set_range::in::")
                self.m_range = prange
                self.xx_dbg("DBG_CfgRaidDev_PyArray::set_range::out")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal()                                
                except:
                        self.xx_exception("DBG_CfgRaidDev_PyArray::print_object")
                                        
        def prepare_object_internal(self):
                self.xx_dbg("DBG_CfgRaidDev_PyArray::prepare_object_internal::")                
                self.m_array_items= []
                for ii in range(self.m_range):
                        dd = self.get_array_item(ii)
                        if( dd != None):
                                self.m_array_items.append(dd)
                self.xx_dbg("DBG_CfgRaidDev_PyArray::prepare_object_internal::out")
                
        def get_array_item(self,pii):
                try:
                        self.xx_dbg("DBG_CfgRaidDev_PyArray::get_array_item::")
                        dd = DBG_CfgRaidDev("DBG_CfgRaidDev_PyArray")
                        dd.xx_inc_tabs_ex( self.m_parent,2,"DBG_CfgRaidDev_PyArray")                        
                        #dd.xx_compute_arr_phy_by_parent(self.m_parent,"mPath[" +str(pii) + "]")
                        s_ptr_expr = self.m_table_pointer + "[" +str(pii) + "]"
                        dd.xx_compute_phy_by_parent(self.m_parent
                                                    ,s_ptr_expr)
                        dd.prepare_object()
                        self.xx_dbg("DBG_CfgRaidDev_PyArray::get_array_item::out")
                        return dd
                except:
                        self.xx_exception("DBG_CfgRaidDev_PyArray::get_array_item::exception::")
                        return None
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_CfgRaidDev_PyArray::print_object::")
                self.xx_print_ptr("")
                if(self.xx_is_object()==1):                
                        self.print_items()
                self.xx_dbg("DBG_CfgRaidDev_PyArray::print_object::out")

        def print_items(self):
                self.xx_dbg("DBG_CfgRaidDev_PyArray::print_items::")
                for dd_item in self.m_array_items:
                        dd_item.print_object()
                self.xx_dbg("DBG_CfgRaidDev_PyArray::print_items::out::")
                
                
                