import sys
import os
from .. appcore.memory.DBG_Utils import *
from .. appcore.memory.DBG_MemoryTools import *
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. raidism.DBG_RaidIsmDisk import *
                
class DBG_RaidIsmDiskTable(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_RaidIsmDiskTable::__init__::method_in::")
                self.xx_set_class_name ( "DiskTable" )
                self.xx_set_full_class_name ( "iastora!DiskTable" )
                self.m_parent = self
                self.m_range = 32
                self.numEntries = 0
                self.m_array_items = []
                
                self.m_fields = DBG_FieldsMapper("DBG_RaidIsmDisk"
                                         ,self)
                
                self.m_fields.add_fields_int_array([
                        "numEntries"
                        ])
                
                self.xx_dbg("DBG_RaidIsmDiskTable::__init__::method_out::")       
                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_RaidIsmDiskTable::set_parent::")
                self.m_parent = pparent
                self.xx_dbg("DBG_RaidIsmDiskTable::set_parent::out")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal()                                
                except:
                        self.xx_exception("DBG_RaidIsmDiskTable::print_object")
                                        
        def prepare_object_internal(self):
                self.xx_dbg("DBG_RaidIsmDiskTable::prepare_object_internal::")
                
                self.m_fields.set_fields_parent(self)
                self.m_fields.prepare_object()
                self.numEntries = self.m_fields.get_fields_int("numEntries")
                self.m_array_items= []
                for ii in range(self.numEntries):
                        dd = self.get_array_item(ii)
                        if( dd != None):
                                self.m_array_items.append(dd)
                self.xx_dbg("DBG_RaidIsmDiskTable::prepare_object_internal::out")
                
        def get_array_item(self,pii):
                try:
                        self.xx_dbg("DBG_RaidIsmDiskTable::get_array_item::")
                        dd = DBG_RaidIsmDisk("DBG_RaidIsmDiskTable")
                        dd.xx_inc_tabs_ex( self,2,"DBG_RaidIsmDiskTable")
                        #dd.xx_compute_arr_phy_by_parent(self.m_parent,"mPath[" +str(pii) + "]")
                        dd.xx_compute_phy_by_parent(self
                                                    ,"disks[" +str(pii) + "]")
                        dd.prepare_object()
                        self.xx_dbg("DBG_RaidIsmDiskTable::get_array_item::out")
                        return dd
                except:
                        self.xx_exception("DBG_RaidIsmDiskTable::get_array_item::exception::")
                        return None
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self,sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,pparent,sdbg=""):
                
                self.xx_dbg("DBG_RaidIsmDiskTable::print_object::")
                self.xx_print_ptr("")
                self.m_fields.print_object()
                self.print_items()
                self.xx_dbg("DBG_RaidIsmDiskTable::print_object::out")

        def print_items(self):
                self.xx_dbg("DBG_RaidIsmDiskTable::print_items::")
                for dd_transport in self.m_array_items:
                        dd_transport.print_object()
                self.xx_dbg("DBG_RaidIsmDiskTable::print_items::out::")
                
                
                