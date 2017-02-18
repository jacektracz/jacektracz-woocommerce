import sys
import os

from ... DBG_AdapterBase import *       
from ... appcore.memory.DBG_Utils import *
from ... appcore.memory.DBG_MemoryTools import *
from ... driver.DBG_Driver import *
                
class DBG_Driver_PyArrayStaticGlobal(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::__init__::method_in::")
                self.xx_set_class_name ( "DriverList" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DriverList" )
                self.m_fields = DBG_FieldsMapper("DBG_Driver_PyArrayStaticGlobal", self)
                
                self.m_parent = pparent
                self.m_range = 1
                self.m_array_items = []
                self.init_object_fields()
                self.m_var_selector = "iastora!Wcdl::DriverList::sDriver"
                self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::__init__::method_out::")       
                
        def init_object_fields(self):
                self.xx_dbg("DBG_DriverList::init_object_fields::method_in::")                                
                self.m_fields.add_fields_asstr_u32s(["sNumDrivers"])                                                
                self.xx_dbg("DBG_DriverList::init_object_fields::method_out::")
                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::set_parent::")
                self.m_parent = pparent
                self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::set_parent::out")
                
        def prepare_object(self,pparent):
                try:
                        self.prepare_object_internal(pparent)                                
                except:
                        self.xx_exception("DBG_Driver_PyArrayStaticGlobal::print_object")
                                        
        def prepare_object_internal(self,pparent):
                self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::initialize_ptr::")
                self.m_parent = pparent                
                self.clear_messages()                
                self.m_fields.set_fields_parent(self)
                self.m_fields.prepare_object()
                self.prepare_array_items()
                                
                self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::initialize_ptr::out")
                
        def compute_range(self):
                ddp = DBG_Utils()
                ddp.m_dbg_print = 1
                self.m_range = ddp.xx_get_as_u32("iastora!Wcdl::DriverList::sNumDrivers")
                if(self.m_range > 4):
                        self.m_range = 1
                
        def prepare_array_items(self):                
                try:
                        self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::prepare_array_items::")                                          
                        self.m_array_items= []
                                
                        self.m_range = self.m_fields.get_fields_asstr_u32("sNumDrivers")                                
                        self.add_message("Wcdl::DriverList::sNumDrivers::" + str(self.m_range))
                        
                        for ii_path in range(self.m_range):
                                dd = self.get_array_item(ii_path)
                                if( dd != None):
                                        self.m_array_items.append(dd)
                                        
                        self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::prepare_array_items::out")                                        
                except:
                        self.xx_exception("DBG_Driver_PyArrayStaticGlobal::prepare_array_items::exception::")                                
                
        def get_array_item(self,p_ii):
                try:
                        self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::get_array_item::")
                        dd = DBG_Driver("DBG_Driver_PyArrayStaticGlobal")
                        s_selector = self.m_var_selector + "[" +str(p_ii) + "]"
                        dd.xx_set_lg_compute_phy_addr( s_selector)
                        dd.prepare_object()
                        self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::get_array_item::out")
                        return dd
                except:
                        self.xx_exception("DBG_Driver_PyArrayStaticGlobal::get_array_item::exception::")
                        return None
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_Driver_PyArrayStaticGlobal::print_object")
                        
        def print_object_internal(self, sdbg = ""):
                self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::print_object::")
                self.xx_print_ptr("")
                self.m_fields.print_object()
                self.print_array_items()                
                self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::print_object::out")

        def print_array_items(self):
                self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::print_array_items::")
                for dd_item in self.m_array_items:
                        dd_item.print_object()
                self.xx_dbg("DBG_Driver_PyArrayStaticGlobal::print_array_items::out::")
                
        def prepare_object_global(self, sdbg = ""):
                try:
                    self.x_dbg("DBG_Driver_PyArrayStaticGlobal::prepare_object_global::in::")            
                    self.xx_set_lg_compute_phy_addr( "iastora!Wcdl::DriverList::sDriver" )
                    self.prepare_object(self.m_parent)
                    self.x_dbg("DBG_Driver_PyArrayStaticGlobal::prepare_object_global::out:")
                except:
                    self.xx_exception("DBG_Driver_PyArrayStaticGlobal::prepare_object_global::exception::")
                
        def print_object_global(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_DriverList::print_object_global::method_in")
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                        self.xx_dbg("DBG_DriverList::print_object_global::method_end")
                except:
                        self.xx_exception("DBG_DriverList::print_object_global::exception::")
