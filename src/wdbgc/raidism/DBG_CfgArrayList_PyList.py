import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. raidism.DBG_CfgArray import *
from .. raidism.DBG_ISM_LINK import *

class DBG_CfgArrayList_PyList(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_CfgArrayList_PyList::__init__::m_in::")
                self.xx_set_class_name ( "CfgArrayList" )
                self.xx_set_full_class_name ( "iastora!CfgArrayList" )
                #self.mApstTable = DBG_ApstTable("Parent::DBG_CfgArrayList_PyList")
                self.m_fields = DBG_FieldsMapper("DBG_CfgArrayList_PyList",self)
                self.m_fields.add_fields_int_array([
                        "EMPTY"
                        ])
                
                self.m_first = DBG_CfgArray("Parent::DBG_CfgArrayList_PyList")
                self.m_last = DBG_CfgArray("Parent::DBG_CfgArrayList_PyList")
                self.m_current = DBG_CfgArray("Parent::DBG_CfgArrayList_PyList")
                self.m_items = []
                self.m_link_items = []
                self.m_max_range = 4
                self.m_print_first_last = 0
                self.xx_dbg("DBG_CfgArrayList_PyList::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_CfgArrayList_PyList::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                try:
                        self.xx_dbg("DBG_CfgArrayList_PyList::prepare_object_internal::")
                        if(self.xx_is_object()==1):
                                #print "ADDR" + self.xx_get_phy_addr("")
                                self.m_fields.initialize_by_parent(self)
                                self.m_fields.prepare_object()
                                self.m_first.set_addr(self,"_first")
                                self.m_first.prepare_object()
                                self.m_last.set_addr(self,"_last")
                                self.m_last.prepare_object()
                                self.prepare_list_links()
                        self.xx_dbg("DBG_CfgArrayList_PyList::prepare_object::m_out::")
                except:
                        self.xx_exception("DBG_CfgArrayList_PyList::prepare_object_internal")

        def prepare_list_links(self):
                try:
                        self.xx_dbg("DBG_CfgArrayList_PyList::prepare_list::m_in::")
                        self.m_link_items = []
                        self.m_items = []
                        slastp = self.m_last.xx_get_phy_addr("")                        
                        dd_prev = self.m_first
                        sphy = dd_prev.xx_get_phy_addr("") 

                        self.m_items.append(dd_prev)
                        
                        if(sphy != slastp):
                                
                                for ii_ll in range(self.m_max_range):
                                        
                                        dd_link = DBG_ISM_LINK("Parent::DBG_CfgArrayList_PyList")
                                        dd_link.set_addr(dd_prev,"_next")
                                        dd_link.prepare_object()
                                        if(dd_link.xx_is_object() == 0):
                                                break
                                        
                                        saddr = dd_link.xx_get_phy_addr("")
                                        #print "oooooooooooooooooooooooooooooo:" + saddr
                                        self.m_link_items.append(dd_link)
                                        
                                        
                                        dd_current = DBG_CfgArray("Parent::DBG_CfgArrayList_PyList")                                        
                                        dd_current.xx_compute_generic_phy_by_phy(self, "0x" + saddr,"(" + saddr +")->_next" )
                                        dd_current.prepare_object()
                                        self.m_items.append(dd_current)
                                        
                                        if(sphy == slastp):
                                                break
                                        else:                                                
                                                dd_prev = dd_current
                                        
                        self.xx_dbg("DBG_CfgArrayList_PyList::prepare_list::m_out::")
                except:
                        self.xx_exception("::print_object")
                
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_CfgArrayList_PyList::print_object::m_in::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object()==1):
                        self.m_fields.print_object()
                        if( self.m_print_first_last == 1):
                                self.m_first.print_object()
                                self.m_last.print_object()
                        self.print_link_list()
                self.xx_dbg("DBG_CfgArrayList_PyList::print_object::m_out::")
                

        def print_link_list(self):
                try:
                        self.xx_dbg("DBG_CfgArrayList_PyList::print_link_list::m_in::")
                        
                        for dd_ii in self.m_items:
                                dd_ii.print_object()
                                
                        if( self.m_print_first_last == 1):        
                                for dd_ii in self.m_link_items:
                                        dd_ii.print_object()
                                
                        self.xx_dbg("DBG_CfgArrayList_PyList::print_link_list::m_out::")
                except:
                        self.xx_exception("::print_link_list")

