import sys
import os
from .. DBG_MemoryPtr import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. appcore.memory.DBG_MemoryTools import *
from .. appcore.logging.DBG_Log import *
from .. appcore.htmlwriters.DBG_MainPrintDispatcher import *
from .. appcore.htmlwriters.DBG_Html import *
class DBG_FieldBool(DBG_MemoryPtr):
        def __init__(self,svar,ilen,stitle): 
                DBG_MemoryPtr.__init__(self,"DBG_FieldBool")
                self.m_variable = svar
                self.m_length = ilen
                self.m_value = ""
                self.m_title = stitle
                
class DBG_FieldBools(DBG_MemoryPtr):
        def __init__(self,pparent,sdbg): 
                DBG_MemoryPtr.__init__(self,sdbg)
                self.xx_dbg("DBG_FieldBools::init_object_itemernal::")
                self.xx_set_class_name ( "FieldBools" )
                self.xx_set_full_class_name ( "iastora!FieldBools" )
                self.m_parent = None
                self.m_array_items = []
                self.xx_dbg("DBG_FieldBools::init_object_itemernal::out::")
                
                #self.init_object(pparent, sdbg)
                
        def set_parent(self, pparent):
                self.m_parent = pparent
                
        def set_values(self,pints):
                
                self.xx_dbg("DBG_FieldBools::set_values::in_method::")
                for dd_ii in pints:
                        self.add_item(dd_ii,0,"")
                        
                self.xx_dbg("DBG_FieldBools::set_values::out_method::")
                
        def add_item(self, pvar,stitle = ""):
                self.xx_dbg("DBG_FieldBools::add_item::in_method::")
                dd = DBG_FieldBool(pvar,0, stitle)
                self.m_array_items.append( dd )
                self.xx_dbg("DBG_FieldBools::add_item::out_method::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_itemernal()
                except:
                        self.xx_exception("DBG_FieldBools::print_object")
                                        
        def prepare_object_itemernal(self):
                self.xx_dbg("DBG_FieldBools::prepare_object_itemernal::in::")
                self.xx_dbg("DBG_FieldBools::prepare_object_itemernal::out::")
                
        def print_object(self):
                try:
                        self.print_object_itemernal()
                except:
                        self.xx_exception("DBG_FieldBools::print_object")
                
        def print_object_itemernal(self):
                self.xx_dbg("DBG_FieldBools::print_object_itemernal::")
                self.prepare_object()
                self.xx_print_items()
                self.xx_dbg("DBG_FieldBools::print_object_itemernal::out::")                        
                        
        def xx_print_items(self):
                try:
                        self.xx_dbg("DBG_FieldBools::xx_print_items::in::")                        
                        
                        self.xx_print_items_itemernal(
                                                        self.m_parent
                                                        ,self.m_array_items
                                                        ,2)
                        
                        self.xx_dbg("DBG_FieldBools::xx_print_items::out::")                
                except:
                        self.xx_exception("DBG_FieldBools::xx_print_item_itemernal:exc::")

        def xx_print_items_itemernal(self
                                   , parent
                                   , ints_selectors
                                   , ii_tabs = 0):
                
                self.xx_dbg("DBG_FieldBools::xx_print_items_itemernal::in::")
                
                for dd_ii in ints_selectors:
                        self.xx_print_item_itemernal(parent,dd_ii,ii_tabs)
                        
                self.xx_dbg("DBG_FieldBools::xx_print_items_itemernal::out::")

                
        def xx_print_item_itemernal(self
                                  , parent
                                  , dd_ii
                                  , ii_tabs = 0):
                tabs = ""
                try:
                        self.xx_dbg("DBG_FieldBools::xx_print_item_itemernal::in::")
                        if (dd_ii.m_variable == "LINE"):
                                DBG_Html.print_field_html ( "")
                                return
                        if (dd_ii.m_variable == "EMPTY"):
                              #DBG_Html.print_field_html ( ""
                              return
                        
                        dd_ii.m_value = DBG_MemoryTools().xx_get_bool(
                                parent
                                ,       dd_ii.m_variable)
                        
                        tabsp = self.get_parent_tabs(parent,ii_tabs)        
                        DBG_Html.print_field_html_out (  tabsp + dd_ii.m_variable + ":" + str(dd_ii.m_value))
                                
                        self.xx_dbg("DBG_FieldBools::xx_print_items_itemernal::out::")
                        
                except:
                        DBG_Html.print_field_html (  tabsp + ":bool_exception" )
                        #self.xx_exception("DBG_FieldBools::xx_print_item_itemernal:exc::")
                        