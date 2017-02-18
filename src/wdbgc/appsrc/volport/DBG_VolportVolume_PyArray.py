import sys
import os
from ... DBG_AdapterBase import *       

from ... appcore.memory.DBG_Utils import *
from ... appcore.memory.DBG_MemoryTools import *
from ... appsrc.volport.DBG_VolportVolume import *
                
class DBG_VolportVolume_PyArray(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_VolportVolume_PyArray::__init__::method_in::")
                self.xx_set_class_name ( "VolPort" )
                self.xx_set_full_class_name ( "iastora!volport::VolPort" )
                self.m_fields = DBG_FieldsMapper("DBG_Transport_PyRaid",self)
                
                self.m_parent = pparent
                self.m_range_paths = 8
                self.m_range_targets = 32
                self.m_range_luns = 2
                self.m_array_items = []
                self.xx_dbg("DBG_VolportVolume_PyArray::__init__::method_out::")       
                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_VolportVolume_PyArray::set_parent::")
                self.m_parent = pparent
                self.xx_dbg("DBG_VolportVolume_PyArray::set_parent::out")
                
        def prepare_object(self,pparent):
                try:
                        self.prepare_object_internal(pparent)                                
                except:
                        self.xx_exception("DBG_VolportVolume_PyArray::print_object")
                                        
        def prepare_object_internal(self,pparent):
                self.xx_dbg("DBG_VolportVolume_PyArray::initialize_ptr::")
                self.m_parent = pparent                
                self.clear_messages()                
                self.m_fields.set_fields_parent(self)
                self.m_fields.prepare_object()
                self.prepare_array_items()
                                
                self.xx_dbg("DBG_VolportVolume_PyArray::initialize_ptr::out")
                
        def prepare_array_items(self):                
                try:
                        self.xx_dbg("DBG_VolportVolume_PyArray::prepare_array_items::")                                          
                        self.m_array_items= []
                        for ii_path in range(self.m_range_paths):
                                for ii_target in range(self.m_range_targets):
                                        for ii_lun in range(self.m_range_luns):
                                                dd = self.get_array_item(ii_path,ii_target,ii_lun)
                                                if( dd != None):
                                                        self.m_array_items.append(dd)
                                        
                        self.xx_dbg("DBG_VolportVolume_PyArray::prepare_array_items::out")                                        
                except:
                        self.xx_exception("DBG_VolportVolume_PyArray::prepare_array_items::exception::")                                
                
        def get_array_item(self,p_path, p_target, p_lun):
                try:
                        self.xx_dbg("DBG_VolportVolume_PyArray::get_array_item::")
                        dd = DBG_VolportVolume("DBG_VolportVolume_PyArray",self)
                        dd.set_addr_arr(self,"mVolumes[" +str(p_path) + "][" + str(p_target) + "][" + str(p_lun) + "]")
                        dd.prepare_object()
                        self.xx_dbg("DBG_VolportVolume_PyArray::get_array_item::out")
                        return dd
                except:
                        self.xx_exception("DBG_VolportVolume_PyArray::get_array_item::exception::")
                        return None
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_VolportVolume_PyArray::print_object")
                        
        def print_object_internal(self):
                self.xx_dbg("DBG_VolportVolume_PyArray::print_object::")
                self.xx_print_ptr("")
                self.m_fields.print_object()
                self.print_transports()                
                self.xx_dbg("DBG_VolportVolume_PyArray::print_object::out")

        def print_transports(self):
                self.xx_dbg("DBG_VolportVolume_PyArray::print_transports::")
                for dd_transport in self.m_array_items:
                        dd_transport.print_object()
                self.xx_dbg("DBG_VolportVolume_PyArray::print_transports::out::")
                
                
                