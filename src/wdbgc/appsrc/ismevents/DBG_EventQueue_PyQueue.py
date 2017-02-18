import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.ismevents.DBG_Ism_Event import *


class DBG_EventQueue_PyQueue(DBG_AdapterBase):
        def __init__(self, spar, pparent):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_EventQueue_PyQueue::__init__::in::")
                self.xx_set_class_name ( "Queue" )
                self.xx_set_full_class_name ( "iastora!EventQueue::Queue" )
                
                self.m_fields = DBG_FieldsMapper("DBG_EventQueue_PyQueue", self)
                
                self.mFirst = DBG_Ism_Event("DBG_EventQueue_PyQueue",self)
                self.mLast = DBG_Ism_Event("DBG_EventQueue_PyQueue",self)
                
                self.m_link_items = []
                
                self.create_fields()
                
                self.m_max_range = 20
                
                self.m_items = []
                self.xx_dbg("DBG_EventQueue_PyQueue::__init__::in::")

        def create_fields(self):
                try:
                        self.xx_dbg("DBG_EventQueue_PyQueue::create_fields::in::")                        
                        #self.m_fields.add_fields_int("mElementCount")                        
                        self.xx_dbg("DBG_EventQueue_PyQueue::create_fields::out::")
                except:
                        self.xx_exception("DBG_EventQueue_PyQueue::create_fields")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_EventQueue_PyQueue::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_EventQueue_PyQueue::prepare_object::")
                if(self.xx_is_object() == 1):
                        self.m_fields.set_fields_parent(self)
                        self.mFirst.set_addr(self,"mFirst")
                        self.mFirst.prepare_object()
                        
                        self.mLast.set_addr(self,"mLast")
                        self.mLast.prepare_object()
                        self.prepare_fast_list_items()                                                
                self.xx_dbg("DBG_EventQueue_PyQueue::prepare_object::out::")
                
        def prepare_fast_list_items(self):
                try:
                        self.xx_dbg("DBG_EventQueue_PyQueue::prepare_fast_list_items::m_in::")
                        self.m_items = []
                        
                        if(self.mFirst.xx_is_object() == 0):
                                return
                        
                        if(self.mLast.xx_is_object() == 0):
                                return
                        
                        sphy_first = self.mFirst.xx_get_phy_addr("")
                        sphy_tail = self.mLast.xx_get_phy_addr("")
                        if( sphy_first == sphy_tail ):
                                return
                                
                        dd_current = self.mFirst
                        if(dd_current.xx_is_object() == 0):
                                return
                                                
                        for ii_ll in range(self.m_max_range):
                                self.m_items.append(dd_current)        
                                dd_next = self.get_next_from_current(dd_current)
                                if(dd_next == None):
                                        break
                                                                
                                dd_current = self.get_current_from_next(
                                        dd_next
                                        ,sphy_tail)
                                
                                if( dd_current == None):
                                        break
                                        
                        self.xx_dbg("DBG_EventQueue_PyQueue::prepare_fast_list_items::m_out::")
                except:
                        self.xx_exception("DBG_EventQueue_PyQueue::prepare_fast_list_items::m_exception::")

        def get_current_from_next(self,dd_next,sphy_tail):
                try:
                        self.xx_dbg("DBG_EventQueue_PyQueue::get_current_from_next::in::")
                        dd_current_out = None
                        sphy_next = dd_next.xx_get_phy_addr("")
                        if(sphy_next != sphy_tail):
                                dd_current = dd_next
                                
                        self.xx_dbg("DBG_EventQueue_PyQueue::get_current_from_next::out::")
                        return dd_current_out
                except:
                        self.xx_exception("DBG_EventQueue_PyQueue::get_current_from_next::m_exception::")
                        return None
                
        def get_next_from_current(self,dd_current):
                try:
                        self.xx_dbg("DBG_EventQueue_PyQueue::get_next_from_current::in::")
                        dd_next_out = None
                        dd_next = DBG_Ism_Event("Parent::DBG_EventQueue_PyQueue",self)
                        dd_next.set_addr(dd_current,"_next")
                        dd_next.prepare_object()
                        if(dd_next.xx_is_object() == 1):
                                dd_next_out = dd_next
                                
                        self.xx_dbg("DBG_EventQueue_PyQueue::get_next_from_current::out::")
                        return dd_next_out
                except:
                        self.xx_exception("DBG_EventQueue_PyQueue::prepare_fast_list_items::m_exception::")
                        return None
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_EventQueue_PyQueue::print_object")                                        
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_EventQueue_PyQueue::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):                
                        self.m_fields.xx_print_fields("")
                        self.mFirst.print_object()
                        self.mLast.print_object()
                        self.print_fast_list_items()
                self.xx_dbg("DBG_EventQueue_PyQueue::print_object_internal::out::")                        

                        
        def print_fast_list_items(self):
                try:
                        self.xx_dbg("DBG_EventQueue_PyQueue::print_fast_list_items::m_in::")
                        
                        for dd_ii in self.m_items:
                                dd_ii.print_object()
                                                                
                        self.xx_dbg("DBG_EventQueue_PyQueue::print_fast_list_items::m_out::")
                except:
                        self.xx_exception("DBG_EventQueue_PyQueue::print_fast_list_items::m_out::")
                                                
                
        def get_class_str(self):
                self.xx_dbg("DBG_EventQueue_PyQueue::get_class_str::")
                
                ccstr = """
"""
                self.xx_dbg("DBG_EventQueue_PyQueue::get_class_str::")
