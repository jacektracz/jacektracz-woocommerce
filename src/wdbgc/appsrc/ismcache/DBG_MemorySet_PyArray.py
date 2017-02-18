import sys
import os

from ... DBG_AdapterBase import *       
from ... appcore.memory.DBG_Utils import *
from ... appcore.memory.DBG_MemoryTools import *
from ... appsrc.ismcache.DBG_MemorySet import *
                
class DBG_MemorySet_PyArray(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_MemorySet_PyArray::__init__::method_in::")
                self.xx_set_class_name ( "MemoryMgr" )
                self.xx_set_full_class_name ( "iastora!MemoryMgr" )
                self.m_fields = DBG_FieldsMapper("DBG_Transport_PyRaid",self)
                
                self.m_parent = pparent
                self.m_range = 3
                self.m_array_items = []
                self.xx_dbg("DBG_MemorySet_PyArray::__init__::method_out::")       
                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_MemorySet_PyArray::set_parent::")
                self.m_parent = pparent
                self.xx_dbg("DBG_MemorySet_PyArray::set_parent::out")
                
        def prepare_object(self,pparent):
                try:
                        self.prepare_object_internal(pparent)                                
                except:
                        self.xx_exception("DBG_MemorySet_PyArray::print_object")
                                        
        def prepare_object_internal(self,pparent):
                self.xx_dbg("DBG_MemorySet_PyArray::initialize_ptr::")
                self.m_parent = pparent                
                self.clear_messages()                
                self.m_fields.set_fields_parent(self)
                self.m_fields.prepare_object()
                self.prepare_array_items()
                                
                self.xx_dbg("DBG_MemorySet_PyArray::initialize_ptr::out")
                
        def prepare_array_items(self):                
                try:
                        self.xx_dbg("DBG_MemorySet_PyArray::prepare_array_items::")                                          
                        self.m_array_items= []
                        for ii_path in range(self.m_range):
                                dd = self.get_array_item(ii_path)
                                if( dd != None):
                                        self.m_array_items.append(dd)
                                        
                        self.xx_dbg("DBG_MemorySet_PyArray::prepare_array_items::out")                                        
                except:
                        self.xx_exception("DBG_MemorySet_PyArray::prepare_array_items::exception::")                                
                
        def get_array_item(self,p_ii):
                try:
                        self.xx_dbg("DBG_MemorySet_PyArray::get_array_item::")
                        dd = DBG_MemorySet("DBG_MemorySet_PyArray",self)
                        s_selector = "memSets[" +str(p_ii) + "]"
                        dd.set_addr(self,s_selector)
                        dd.prepare_object()
                        self.xx_dbg("DBG_MemorySet_PyArray::get_array_item::out")
                        return dd
                except:
                        self.xx_exception("DBG_MemorySet_PyArray::get_array_item::exception::")
                        return None
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_MemorySet_PyArray::print_object")
                        
        def print_object_internal(self):
                self.xx_dbg("DBG_MemorySet_PyArray::print_object::")
                self.xx_print_ptr("")
                self.m_fields.print_object()
                self.print_array_items()                
                self.xx_dbg("DBG_MemorySet_PyArray::print_object::out")

        def print_array_items(self):
                self.xx_dbg("DBG_MemorySet_PyArray::print_array_items::")
                for dd_item in self.m_array_items:
                        dd_item.print_object()
                self.xx_dbg("DBG_MemorySet_PyArray::print_array_items::out::")
                
                
                