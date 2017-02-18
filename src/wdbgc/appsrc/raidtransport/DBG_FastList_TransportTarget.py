import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.raidtransport.DBG_FastListElement_TransportTarget import *

class DBG_FastList_TransportTarget(DBG_AdapterBase):
        def __init__(self, spar, pparent):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_FastList_TransportTarget::__init__::in::")
                self.xx_set_class_name ( "FastList<TransportTarget>" )
                self.xx_set_full_class_name ( "iastora!FastList<TransportTarget>" )
                
                self.m_fields = DBG_FieldsMapper("DBG_FastList_TransportTarget", self)
                
                self.mHead = DBG_FastListElement_TransportTarget("DBG_FastList_TransportTarget",self)
                self.mTail = DBG_FastListElement_TransportTarget("DBG_FastList_TransportTarget",self)                                
                
                self.create_fields()
                
                self.m_max_range = 6
                self.m_items = []
                self.xx_dbg("DBG_FastList_TransportTarget::__init__::in::")

        def create_fields(self):
                try:
                                
                        self.m_fields.add_fields_int("mElementCount")
                except:
                        self.xx_exception("DBG_FastList_TransportTarget::create_fields")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_FastList_TransportTarget::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_FastList_TransportTarget::prepare_object::")
                if(self.xx_is_object() == 1):
                        self.m_fields.set_fields_parent(self)
                        self.mHead.set_addr(self,"mHead")
                        self.mHead.prepare_object()
                        
                        self.mTail.set_addr(self,"mTail")
                        self.mTail.prepare_object()
                        self.prepare_fast_list_items()                                                
                self.xx_dbg("DBG_FastList_TransportTarget::prepare_object::out::")
                
        def prepare_fast_list_items(self):
                try:
                        self.xx_dbg("DBG_FastList_TransportTarget::prepare_fast_list_items::m_in::")
                        self.m_items = []
                        
                        sphy_tail = self.mTail.xx_get_phy_addr("")
                        dd_current = self.mHead
                        
                        if(dd_current.xx_is_object() == 0):
                                return
                        
                        self.m_items.append(dd_current)
                        
                        sphy_current = dd_current.xx_get_phy_addr("")
                        
                        if( sphy_current != sphy_tail ):
                                
                                for ii_ll in range(self.m_max_range):
                                        
                                        dd_next = DBG_FastListElement_TransportTarget("Parent::DBG_FastList_TransportTarget",self)
                                        dd_next.set_addr(dd_current,"mNext")
                                        dd_next.prepare_object()
                                        if(dd_next.xx_is_object() == 0):
                                                break
                                        
                                        self.m_items.append(dd_next)
                                        
                                        sphy_next = dd_next.xx_get_phy_addr("")
                                        if(sphy_next == sphy_tail):
                                                break
                                        else:                                                
                                                dd_current = dd_next
                                        
                        self.xx_dbg("DBG_FastList_TransportTarget::prepare_fast_list_items::m_out::")
                except:
                        self.xx_exception("DBG_FastList_TransportTarget::prepare_fast_list_items::m_exception::")

                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_FastList_TransportTarget::print_object")                                        
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_FastList_TransportTarget::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):                
                        self.m_fields.xx_print_fields("")
                        self.mHead.print_object()
                        self.mTail.print_object()
                        self.print_fast_list_items()
                self.xx_dbg("DBG_FastList_TransportTarget::print_object_internal::out::")                        

                        
        def print_fast_list_items(self):
                try:
                        self.xx_dbg("DBG_FastList_TransportTarget::print_fast_list_items::m_in::")
                        
                        for dd_ii in self.m_items:
                                dd_ii.print_object()
                                                                
                        self.xx_dbg("DBG_FastList_TransportTarget::print_fast_list_items::m_out::")
                except:
                        self.xx_exception("DBG_FastList_TransportTarget::print_fast_list_items::m_out::")
                                                
                
        def get_class_str(self):
                self.xx_dbg("DBG_FastList_TransportTarget::get_class_str::")
                
                ccstr = """
"""
                self.xx_dbg("DBG_FastList_TransportTarget::get_class_str::")
