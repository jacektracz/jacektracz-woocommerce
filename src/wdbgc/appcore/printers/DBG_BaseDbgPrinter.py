import sys
import os
from ... appcore.printers.DBG_Base import *
from ... appcore.memory.DBG_WdbgItemsPrinter import *

class DBG_BaseDbgPrinter(DBG_Base):
    def __init__(self,pparent,sdbg):
        DBG_Base.__init__(self,pparent,sdbg)
        self.m_parent = pparent
        
    def set_parent(self,pparent):
        self.xx_dbg( "DBG_BaseDbgPrinter::set_parent::method_in::")
        self.m_parent = pparent
        self.xx_dbg( "DBG_BaseDbgPrinter::set_parent::method_out::")
        
    def prepare_object(self):
        try:
            self.xx_dbg("DBG_BaseDbgPrinter::prepare_object")
            self.xx_dbg("DBG_BaseDbgPrinter::prepare_object")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
            
    def print_object(self,stabs=0):
        try:
            self.xx_dbg( "DBG_BaseDbgPrinter::xx_print_link_ptr::method_in::")
            self.xx_print_link_ptr()
            self.xx_print_link_variable()
            self.print_links_paths()
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
        
    def xx_print_link_ptr(self,stabs=0):
        try:
            self.xx_dbg( "DBG_BaseDbgPrinter::xx_print_link_ptr::method_in::")
            ver = 1
            sv = ""
            if( ver == 0 ):
                sv  = self.m_parent.xx_get_class_ptr("")
            if( ver== 1 ):
                sv =  self.m_parent.xx_get_class_ptr("") + ":" + self.m_parent.get_variable_from_selector_for_print()
            DBG_WdbgItemsPrinter().xx_print_link(
                sv
                ,sv
                ,self.m_parent.xx_gett(stabs))			
            
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
        
    def xx_print_link_variable(self,stabs = 0):
        try:
            self.xx_dbg( "DBG_BaseDbgPrinter::xx_print_link_variable::method_in::")
            #sv = self.m_variable;
            sc = "nc"
            try:
                sc = self.m_parent.__class__.__name__
            except:
                sc = "nc"
                
            sv = sc + ":" + self.m_parent.m_raw_variable + ":" + self.m_parent.m_class_name
                
            DBG_WdbgItemsPrinter().xx_print_link(
                self.m_parent.xx_get_class_ptr("")
                ,sv
                ,self.m_parent.xx_gett(stabs))
        except:
            self.xx_exception("xx_print_link_variable::exception::")
                            
    def print_links_paths(self): 
        try:
            self.xx_dbg( "DBG_BaseDbgPrinter::print_links_paths::method_in::")
            
            DBG_WdbgItemsPrinter().xx_print_link(
                self.m_parent.m_stored_class_ptr_by_phy_addr
                ,"PHY:" + self.m_parent.m_stored_class_ptr_by_phy_addr
                ,self.m_parent.xx_gett(1))                        
            
            DBG_WdbgItemsPrinter().xx_print_link(
                self.m_parent.m_lg_ptr
                ,"LGR:" + self.m_parent.m_lg_ptr
                ,self.m_parent.xx_gett(1))
            
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( self.m_stored_class_ptr_by_phy_addr
        except:
            self.xx_exception("print_links_paths::exception::")
    
                