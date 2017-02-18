import sys
import os

from ... appcore.memory.DBG_WdbgItemsPrinter import *
from ... appcore.logging.DBG_Log import *
from ... appcore.htmlwriters.DBG_MainPrintDispatcher import *
from ... appcore.htmlwriters.DBG_Html import *

from ... appcore.printers.DBG_Base import *

class DBG_FieldInfo:
        def __init__(self,svar,ilen): 
                
                self.m_variable = svar
                self.m_length = ilen
                self.m_value = ""
                self.m_field_type = "STRING"

                
class DBG_FieldInfos(DBG_Base):
        def __init__(self,sdbg,pparent):                   
                DBG_Base.__init__(self,pparent,sdbg)
                self.xx_dbg("DBG_FieldInfos::init_object_internal::")
                self.xx_set_class_name ( "FieldInfos" )
                self.xx_set_full_class_name ( "iastora!FieldInfos" )
                self.m_parent = pparent
                self.m_items = []
                self.xx_dbg("DBG_FieldInfos::init_object_internal::out::")
                
                #self.init_object(pparent, sdbg)
                
        def clear_array(self):
                self.m_items = []
                
        def get_strings(self):
                outa = []
                for dd_ii in self.m_items:
                        outa.append(dd_ii.mvalue)
                return outa
                
                
        def set_parent(self, pparent):
                self.m_parent = pparent
                
        def set_values(self,pstrs):
                self.m_items = pstrs
      
                
        def add_message(self, pvar):
                dd = DBG_FieldInfo(pvar, 1)
                dd.m_field_type = "RAWS"
                dd.m_length = 1
                dd.m_value = pvar
                self.m_items.append( dd )
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal()
                except:
                        self.xx_exception("DBG_FieldInfos::print_object")
                                        
        def prepare_object_internal(self):
                self.xx_dbg("DBG_FieldInfos::prepare_object::")
                self.xx_dbg("DBG_FieldInfos::prepare_object::out::")

        def print_object(self,htitle="messages"):
                try:
                        DBG_Html.xx_print_props_start(htitle)
                        self.print_object_internal(self)
                        DBG_Html.xx_print_props_end(htitle)
                except:
                        self.xx_exception("DBG_FieldInfos::print_object")
                                
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_FieldInfos::print_object::")
                self.prepare_object()
                self.xx_print_items()
                self.xx_dbg("DBG_FieldInfos::print_object::out::")                        
                        
        def xx_print_items(self):
                try:
                        self.xx_dbg("DBG_FieldInfos::xx_print_items::in::")
                        if(len(self.m_items) > 0 ):
                                self.xx_dbg("DBG_FieldInfos::xx_print_items::in::>0")
                                
                                
                        self.xx_print_items_internal(
                                                        self.m_parent
                                                        ,self.m_items
                                                        ,2)
                        
                        self.xx_dbg("DBG_FieldInfos::xx_print_items::out::")                
                except:
                        self.xx_exception("DBG_FieldInfos::xx_print_int_internal:exc::")

        def xx_print_items_internal(self, parent,pitems,ii_tabs = 0):
                
                self.xx_dbg("DBG_FieldInfos::xx_print_items_internal::in::")
                
                for dd_ii in pitems:
                        self.xx_print_item_internal(
                                parent
                                ,dd_ii
                                ,ii_tabs)
                        
                self.xx_dbg("DBG_FieldInfos::xx_print_items_internal::out::")

                
        def xx_print_item_internal(self
                                  , parent
                                  , dd_ii
                                  , ii_tabs = 0):
                try:
                        self.xx_dbg("DBG_FieldInts::xx_print_int_internal::in::")                        
                        tabsp = self.get_parent_tabs(parent, ii_tabs)
                        DBG_Html.print_field_html_out (  tabsp + dd_ii.m_value ) 
                        self.xx_dbg("DBG_FieldInts::xx_print_ints_internal::out::")
                        
                except:
                        self.xx_exception("DBG_FieldInts::xx_print_int_internal:exc::")
                        
        def clear_messages(self):
                self.m_items = []