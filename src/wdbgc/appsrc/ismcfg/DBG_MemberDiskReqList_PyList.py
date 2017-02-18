import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... raidism.DBG_ISM_LINK import *
from ... appsrc.ismcfg.DBG_MemberDiskReq import *


class DBG_MemberDiskReqList_PyList(DBG_AdapterBase):
        def __init__(self,spar,pparent):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_MemberDiskReqList_PyList::__init__::m_in::")
                self.xx_set_class_name ( "MemberDiskReqList" )
                self.xx_set_full_class_name ( "iastora!MemberDiskReqList" )
                #self.mApstTable = DBG_ApstTable("Parent::DBG_MemberDiskReqList_PyList")
                self.m_fields = DBG_FieldsMapper("DBG_MemberDiskReqList_PyList",self)
                self.m_fields.add_fields_int_array([
                        "EMPTY"
                        ])
                
                self.m_first = DBG_MemberDiskReq("Parent::DBG_MemberDiskReqList_PyList",self)
                self.m_last = DBG_MemberDiskReq("Parent::DBG_MemberDiskReqList_PyList",self)
                self.m_current = DBG_MemberDiskReq("Parent::DBG_MemberDiskReqList_PyList",self)
                self.m_items = []
                self.m_link_items = []
                self.m_max_range = 4
                self.m_print_first_last = 1
                self.xx_dbg("DBG_MemberDiskReqList_PyList::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_MemberDiskReqList_PyList::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                try:
                        self.xx_dbg("DBG_MemberDiskReqList_PyList::prepare_object_internal::")
                        if(self.xx_is_object()==1):
                                
                                #print "ADDR" + self.xx_get_phy_addr("")
                                self.m_fields.initialize_by_parent(self)
                                self.m_fields.prepare_object()
                                
                                self.m_first.set_addr(self,"_first")
                                self.m_first.prepare_object()
                                
                                self.m_last.set_addr(self,"_last")
                                self.m_last.prepare_object()
                                
                                self.prepare_list_links()
                                
                        self.xx_dbg("DBG_MemberDiskReqList_PyList::prepare_object::m_out::")
                except:
                        self.xx_exception("DBG_MemberDiskReqList_PyList::prepare_object_internal")

        def prepare_list_links(self):
                try:
                        self.xx_dbg("DBG_MemberDiskReqList_PyList::prepare_list::m_in::")
                        self.m_link_items = []
                        self.m_items = []
                                               
                        dd_prev_obj = self.m_first
                        curr_addr_obj = dd_prev_obj.xx_get_phy_addr("")
                        
                        last_addr_obj = self.m_last.xx_get_phy_addr("") 

                        self.m_items.append(dd_prev_obj)
                        
                        if(curr_addr_obj != last_addr_obj):
                                self.compute_list(
                                        dd_prev_obj
                                        ,last_addr_obj)
                                
                        self.xx_dbg("DBG_MemberDiskReqList_PyList::prepare_list::m_out::")
                except:
                        self.xx_exception("::print_object")
                
        def compute_list(self,p_dd_prev_obj,p_last_addr_obj):
                
                try:
                        dd_prev_obj = p_dd_prev_obj
                        #re-assigned on tail loop
                        for ii_ll in range(self.m_max_range):
                                
                                dd_link = self.get_next_link_obj(
                                        dd_prev_obj)
                                
                                if(dd_link.xx_is_object() == 0):
                                        break
                                
                                self.m_link_items.append(dd_link)
                                
                                addr_link_obj = dd_link.xx_get_phy_addr("")
                                
                                dd_current_obj = self.get_obj_from_link(
                                        addr_link_obj)                                
                                
                                self.m_items.append(dd_current_obj)
                                curr_addr_obj = dd_current_obj.xx_get_phy_addr("")
                                
                                if(curr_addr_obj == p_last_addr_obj):
                                        break
                                else:                                                
                                        dd_prev_obj = dd_current_obj                                                                
                except:
                        self.xx_exception("::print_object")
                        
        def get_next_link_obj(self,dd_prev_obj):
                dd_link = DBG_ISM_LINK("Parent::DBG_MemberDiskReqList_PyList")
                dd_link.set_addr(dd_prev_obj,"_next")
                dd_link.prepare_object()
                return dd_link

        def get_obj_from_link(self,addr_link_obj):
                self.xx_dbg("DBG_MemberDiskReqList_PyList::get_obj_from_link::m_in::")
                dd_current_obj = DBG_MemberDiskReq("list",self)
                dd_current_obj.xx_compute_generic_phy_by_phy(
                        self
                        , "0x" + addr_link_obj
                        ,"(" + addr_link_obj +")->_next" )
                
                dd_current_obj.prepare_object()
                self.xx_dbg("DBG_MemberDiskReqList_PyList::get_obj_from_link::m_out::")
                return dd_current_obj
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_MemberDiskReqList_PyList::print_object::m_in::")
                #self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object()==1):
                        self.m_fields.print_object()
                        if( self.m_print_first_last == 1):
                                self.m_first.print_object()
                                self.m_last.print_object()
                        self.print_link_list()
                self.xx_dbg("DBG_MemberDiskReqList_PyList::print_object::m_out::")
                

        def print_link_list(self):
                try:
                        self.xx_dbg("DBG_MemberDiskReqList_PyList::print_link_list::m_in::")
                        
                        for dd_ii in self.m_items:
                                dd_ii.print_object()
                                
                        if( self.m_print_first_last == 1):        
                                for dd_ii in self.m_link_items:
                                        dd_ii.print_object()
                                
                        self.xx_dbg("DBG_MemberDiskReqList_PyList::print_link_list::m_out::")
                except:
                        self.xx_exception("::print_link_list")

