import sys
import os
from ... appcore.printers.DBG_Base import *
from ... appcore.printers.DBG_FieldInfos import *

class DBG_StatePrinter(DBG_Base):
    def __init__(self,pparent,sdbg):
        DBG_Base.__init__(self,pparent,sdbg)
        self.m_parent = pparent
        self.m_messages = DBG_FieldInfos("DBG_MemoryPtr",self)
    
    def set_parent(self,pparent):
        self.m_parent = pparent
        
    def prepare_object(self):
        try:
            self.m_messages.set_parent(self.m_parent)
            self.xx_dbg("DBG_StatelPrinter::prepare_object")
            self.add_msg( "m_lg_ptr",self.m_parent.m_lg_ptr )
            self.add_msg( "m_phy_addr", self.m_parent.m_phy_addr )
            self.add_msg( "m_class_name", self.m_parent.m_class_name )
            self.add_msg( "m_full_class_name", self.m_parent.m_full_class_name )
            self.add_msg( "m_variable", self.m_parent.m_variable )
            self.add_msg( "m_class_descr", self.m_parent.m_class_descr)
            self.add_msg( "m_variable_accessor", self.m_parent.m_variable_accessor)
            self.add_msg( "m_parent_phy_addr", self.m_parent.m_parent_phy_addr )
            self.add_msg( "m_parent_lg_addr", self.m_parent.m_parent_lg_addr )
            self.add_msg( "m_addr_computation_type", self.m_parent.m_addr_computation_type )
            self.add_msg( "m_tabs",str(self.m_parent.m_tabs) )            
            self.add_msg( "m_stored_class_ptr_by_phy_addr", self.m_parent.m_stored_class_ptr_by_phy_addr )
            self.add_msg( "m_raw_variable", self.m_parent.m_raw_variable )            
            self.add_msg( "m_stored_class_ptr_by_phy_addr", self.m_parent.m_stored_class_ptr_by_phy_addr)
            self.add_msg( "m_is_dump", self.m_parent.m_is_dump)
            self.add_msg( "m_is_inbox", self.m_parent.m_is_inbox)
            
            self.xx_dbg("DBG_StatelPrinter::prepare_object")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
        
    def add_msg(self, title,tt):
        self.m_messages.add_message(title + ":" + str(tt))
        
    def print_object(self,stabs=0):
        try:
            self.xx_dbg( "DBG_StatelPrinter::xx_print_link_ptr::method_in::")
            self.m_messages.print_object("state")
            self.xx_dbg( "DBG_StatelPrinter::xx_print_link_ptr::method_in::")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
            
