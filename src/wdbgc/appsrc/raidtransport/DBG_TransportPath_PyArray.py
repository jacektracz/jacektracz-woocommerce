import sys
import os
from ... DBG_AdapterBase import *       

from ... appcore.memory.DBG_Utils import *
from ... appcore.memory.DBG_MemoryTools import *
from ... appsrc.raidtransport.DBG_TransportPath import *
from ... appcore.config.DBG_PrintConfig import *
#p_all = DBG_PrintConfig().getItem().m_print_ahci_port_fields
                
class DBG_TransportPath_PyArray(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_TransportPath_PyArray::__init__::method_in::")
                self.xx_set_class_name ( "Transport" )
                self.xx_set_full_class_name ( "iastora!Transport" )
                self.m_fields = DBG_FieldsMapper("DBG_Transport_PyRaid"
                                         ,self)
                
                self.m_fields.add_fields_int("mNumPaths")
                
                self.m_parent = None
                self.m_range = 4
                self.m_array_items = []
                self.xx_dbg("DBG_TransportPath_PyArray::__init__::method_out::")       
                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_TransportPath_PyArray::set_parent::")
                self.m_parent = pparent
                self.xx_dbg("DBG_TransportPath_PyArray::set_parent::out")
                
        def prepare_object(self,pparent):
                try:
                        self.prepare_object_internal(pparent)                                
                except:
                        self.xx_exception("DBG_TransportPath_PyArray::print_object")
                                        
        def prepare_object_internal(self,pparent):
                self.xx_dbg("DBG_TransportPath_PyArray::initialize_ptr::")
                if(self.prepare_check() == 1):
                        self.xx_dbg("prepare_check::prepared_out::")
                        return
                
                self.m_parent = pparent                
                self.clear_messages()                
                self.m_fields.set_fields_parent(self)
                self.m_fields.prepare_object()
                self.prepare_array_items()
                                
                self.xx_dbg("DBG_TransportPath_PyArray::initialize_ptr::out")
                
        def prepare_array_items(self):                
                try:
                        self.xx_dbg("DBG_TransportPath_PyArray::prepare_array_items::")
                        self.m_range = self.m_fields.get_fields_int("mNumPaths")                        
                        self.m_array_items= []
                        handled_paths = self.m_range
                        
                        if (DBG_PrintConfig().getItem().m_handle_transport_paths == 0):
                                handled_paths = 1
                                
                        for ii_paths in range(handled_paths):
                                if self.path_in_range( ii_paths ) == 0:
                                        continue
                                
                                dd = self.get_array_item( ii_paths )
                                if( dd != None):
                                        self.m_array_items.append(dd)
                                        
                        self.xx_dbg("DBG_TransportPath_PyArray::prepare_array_items::out")                                        
                except:
                        self.xx_exception("DBG_TransportPath_PyArray::prepare_array_items::exception::")                                
                
        def get_array_item(self,pii):
                try:
                        self.xx_dbg("DBG_TransportPath_PyArray::get_array_item::")
                        dd = DBG_TransportPath("DBG_TransportPath_PyArray")
                        dd.xx_inc_tabs_ex( self.m_parent,2,"DBG_TransportPath_PyArray")                        
                        #dd.xx_compute_arr_phy_by_parent(self.m_parent,"mPath[" +str(pii) + "]")
                        dd.xx_compute_phy_by_parent(self.m_parent
                                                    ,"mPath[" +str(pii) + "]")
                        dd.prepare_object()
                        self.xx_dbg("DBG_TransportPath_PyArray::get_array_item::out")
                        return dd
                except:
                        self.xx_exception("DBG_TransportPath_PyArray::get_array_item::exception::")
                        return None
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_TransportPath_PyArray::print_object")
                        
        def print_object_internal(self):                
                self.xx_dbg("DBG_TransportPath_PyArray::print_object::")
                self.xx_print_ptr("")
                self.m_fields.print_object()
                self.print_transports()                
                self.xx_dbg("DBG_TransportPath_PyArray::print_object::out")

        def print_transports(self):
                self.xx_dbg("DBG_TransportPath_PyArray::print_transports::")                
                for dd_transport in self.m_array_items:                        
                        if(dd_transport.get_childs_count() > 0):
                                dd_transport.print_object()
                self.xx_dbg("DBG_TransportPath_PyArray::print_transports::out::")
                
        def path_in_range(self,p_ii):                
                return DBG_PrintConfig().getItem().path_in_range(p_ii)
                
                