


import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
#from ... childdir.DBG_ApstTable import *
from ... appsrc.driverext.DBG_Driver_PyArray import *
#@F
class DBG_DriverList(DBG_AdapterBase):
        def __init__(self, spar, pparent):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_DriverList::__init__::m_in::")
                self.xx_set_class_name ( "DriverList" )
                self.xx_set_full_class_name ( "iastora!DriverList" )
                #self.m_child_item = DBG_ApstTable("Parent::DBG_DriverList")
                self.m_fields = DBG_FieldsMapper("DBG_DriverList", self)
                self.m_drivers = DBG_Driver_PyArray("Parent::DBG_Driver_PyArray",self)
                #@I
                self.init_object_fields()
                self.xx_dbg("DBG_DriverList::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_DriverList::init_object_fields::method_in::")                                
                #self.m_fields.add_fields_asstr_ints([])                                                
                self.xx_dbg("DBG_DriverList::init_object_fields::method_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_DriverList::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_DriverList::prepare_object_internal::")
                
                if(self.xx_is_object()):
                        self.m_fields.set_fields_parent(self)                      
                        #self.m_child_item.set_addr_arr(self,"m_child_item")
                        self.m_drivers.set_addr(self,"SELF")
                        self.m_drivers.prepare_object()                
                        #@P                
                self.xx_dbg("DBG_DriverList::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_DriverList::print_object::method_in")
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                        self.xx_dbg("DBG_DriverList::print_object::method_end")
                except:
                        self.xx_exception("DBG_DriverList::print_object")

        def print_object_internal(self, sdbg= ""):
                self.xx_dbg("DBG_DriverList::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_is_object()):                
                        self.m_fields.xx_print_fields("")
                        #self.m_child_item.print_object()
                        self.m_drivers.print_object()                    
                        #@R                    
                self.xx_dbg("DBG_DriverList::print_object::m_out::")
                
        def prepare_object_global(self):
                try:
                    self.x_dbg("DBG_DriverList::prepare_object_global::in::")            
                    self.xx_set_lg_compute_phy_addr( "iastora!DriverList::sDriver" )
                    self.x_dbg("DBG_DriverList::prepare_object_global::out:")
                except:
                    self.xx_exception("DBG_DriverList::prepare_object_global::exception::")

        def print_object_global(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_DriverList::print_object_global::method_in")
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                        self.xx_dbg("DBG_DriverList::print_object_global::method_end")
                except:
                        self.xx_exception("DBG_DriverList::print_object_global::exception::")
                