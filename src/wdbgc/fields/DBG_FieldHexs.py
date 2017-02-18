import sys
import os
from .. DBG_MemoryPtr import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. appcore.memory.DBG_MemoryTools import *
from .. appcore.logging.DBG_Log import *
from .. appcore.htmlwriters.DBG_MainPrintDispatcher import *
from .. appcore.htmlwriters.DBG_Html import *
from .. fields.DBG_FieldsFormatters import *
class DBG_FieldHex(DBG_MemoryPtr):
        def __init__(self,svar,ilen,stitle): 
                DBG_MemoryPtr.__init__(self,"DBG_FieldHex")
                self.m_variable = svar
                self.m_length = ilen
                self.m_value = -1
                self.m_title = stitle
                
class DBG_FieldHexs(DBG_MemoryPtr):
        def __init__(self,pparent,sdbg): 
                DBG_MemoryPtr.__init__(self,sdbg)
                self.xx_dbg("DBG_FieldHexs::init_object_internal::")
                self.xx_set_class_name ( "FieldHexs" )
                self.xx_set_full_class_name ( "iastora!FieldHexs" )
                self.m_parent = None
                self.m_array_items = []
                self.xx_dbg("DBG_FieldHexs::init_object_internal::out::")
                
                #self.init_object(pparent, sdbg)
                
        def set_parent(self, pparent):
                self.m_parent = pparent
                
        def set_values(self,pints):
                for dd_ii in pints:
                        self.add_item(dd_ii,0,"")
                
        def add_item(self, pvar,stitle = ""):
                dd = DBG_FieldHex(pvar,0, stitle)
                self.m_array_items.append( dd )
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal()
                except:
                        self.xx_exception("DBG_FieldHexs::print_object")
                        
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_FieldHexs::prepare_object::in::")                        
                        
                        self.xx_prepare_items_internal(
                                                        self.m_parent
                                                        ,self.m_array_items
                                                        ,2)
                        
                        self.xx_dbg("DBG_FieldHexs::prepare_object::out::")                
                except:
                        self.xx_exception("DBG_FieldHexs::prepare_object:exc::")

        def xx_prepare_items_internal(self
                                   , parent
                                   , ints_selectors
                                   , ii_tabs = 0):
                
                self.xx_dbg("DBG_FieldHexs::xx_prepare_items_internal::in::")
                
                for dd_ii in ints_selectors:
                        self.xx_prepare_item_internal(
                                parent
                                ,dd_ii
                                ,ii_tabs)
                        
                self.xx_dbg("DBG_FieldHexs::xx_prepare_items_internal::out::")


        def xx_prepare_item_internal(self
                                  , parent
                                  , dd_ii
                                  , ii_tabs = 0):
                try:
                        self.xx_dbg("DBG_FieldHexs::xx_prepare_item_internal::in::")
                        if (dd_ii.m_variable == "LINE"):                                
                                return
                        if (dd_ii.m_variable == "EMPTY"):                                
                                return                        
                        dd_ii.m_value = DBG_MemoryTools().xx_get_hex(
                                parent
                                ,       dd_ii.m_variable)
                        
                        self.xx_dbg("DBG_FieldHexs::xx_prepare_item_internal::out::")
                        
                except:
                        self.xx_exception("DBG_FieldHexs::xx_prepare_item_internal:exc::")
                                        
                
        def print_object(self):
                try:
                        self.print_object_internal()
                except:
                        self.xx_exception("DBG_FieldHexs::print_object")
                
        def print_object_internal(self):
                self.xx_dbg("DBG_FieldHexs::print_object_internal::")
                self.prepare_object()
                self.xx_print_items()
                self.xx_dbg("DBG_FieldHexs::print_object_internal::out::")                        
                        
        def xx_print_items(self):
                try:
                        self.xx_dbg("DBG_FieldHexs::xx_print_items::in::")                        
                        
                        self.xx_print_items_internal(
                                                        self.m_parent
                                                        ,self.m_array_items
                                                        ,2)
                        
                        self.xx_dbg("DBG_FieldHexs::xx_print_items::out::")                
                except:
                        self.xx_exception("DBG_FieldHexs::xx_print_item_internal:exc::")

        def xx_print_items_internal(self
                                   , parent
                                   , ints_selectors
                                   , ii_tabs = 0):
                
                self.xx_dbg("DBG_FieldHexs::xx_print_items_internal::in::")
                
                for dd_ii in ints_selectors:
                        self.xx_print_item_internal(parent,dd_ii,ii_tabs)
                        
                self.xx_dbg("DBG_FieldHexs::xx_print_items_internal::out::")

                
        def xx_print_item_internal(self
                                  , parent
                                  , dd_ii
                                  , ii_tabs = 0):
                try:
                        self.xx_dbg("DBG_FieldHexs::xx_print_item_internal::in::")
                        if (dd_ii.m_variable == "LINE"):
                                DBG_Html.print_field_html ( "" )
                                return
                        
                        if (dd_ii.m_variable == "EMPTY"):
                              #DBG_Html.print_field_html ( ""
                              return
                      
                        dd_ii.m_value = DBG_MemoryTools().xx_get_int(
                                parent
                                ,       dd_ii.m_variable)
                        
                        tabsp = self.get_parent_tabs(parent,ii_tabs)
                        
                        s_int = DBG_FieldsFormatters(self,"").int_to_info(dd_ii, tabsp)
                        
                        DBG_Html.print_field_html_out ( s_int )
                                
                        self.xx_dbg("DBG_FieldHexs::xx_print_items_internal::out::")
                        
                except:
                        self.xx_exception("DBG_FieldHexs::xx_print_item_internal:exc::")

        def to_hex(self, n):
                try:
                        return str(hex(n))
                except:
                        return "HHXX"

        def to_binary(self, n):
                try:
                        return str(bin(n))
                except:
                        return "BBXX"

        def to_binary_1(self, n):
                return ''.join(str(1 & int(n)>> 1) for i in range(64)[::-1])
        
        def to_binary_2(self, i):
                
                try:
                        #s_bb = ''.joim(1)
                        if i == 0:
                                return "0"
                        s = ''
                        while i :
                                if i & i ==1:
                                        s = "1" +s
                                else:
                                        s = "0" +s
                                i /= 2
                        return s
                except:
                        return "XX"
           
        def fields_get_hex(self,smb,from_where=""):
                self.xx_dbg("DBG_FieldHexs::fields_get_hex::in::")
                ddout = -1
                for dd_ii in self.m_array_items:
                        #DBG_Html.print_field_html ( "arr:" + dd_ii.m_variable
                        #DBG_Html.print_field_html ( "smb:" + smb
                        if( dd_ii.m_variable == smb):
                                ddout = dd_ii.m_value
                                break
                        
                #DBG_Html.print_field_html ( from_where + ":field_out:" + smb + ":" + str(   ddout )
                self.xx_dbg("DBG_FieldHexs::fields_get_hex::out::")        
                return ddout                        
                        