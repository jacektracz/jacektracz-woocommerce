import sys
import os
from .. DBG_MemoryPtr import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. appcore.memory.DBG_MemoryTools import *
from .. appcore.logging.DBG_Log import *
from .. appcore.htmlwriters.DBG_MainPrintDispatcher import *
from .. fields.DBG_FieldsFormatters import *

class DBG_FieldInt(DBG_MemoryPtr):
        def __init__(self,svar,ilen,stitle): 
                DBG_MemoryPtr.__init__(self,"DBG_FieldInt")
                self.m_variable = svar
                self.m_length = ilen
                self.m_value = -1
                self.m_title = stitle
                
class DBG_FieldInts(DBG_MemoryPtr):
        def __init__(self,pparent,sdbg): 
                DBG_MemoryPtr.__init__(self,sdbg)
                self.xx_dbg("DBG_FieldInts::init_object_internal::")
                self.xx_set_class_name ( "FieldInts" )
                self.xx_set_full_class_name ( "iastora!FieldInts" )
                self.m_parent = None
                self.m_array_items = []
                self.xx_dbg("DBG_FieldInts::init_object_internal::out::")
                
                #self.init_object(pparent, sdbg)
                
        def set_parent(self, pparent):
                self.m_parent = pparent
                
        def set_values(self,pints):
                for dd_ii in pints:
                        self.add_int(dd_ii,0,"")
                
        def add_int(self, pvar,stitle = ""):
                dd = DBG_FieldInt(pvar,0, stitle)
                self.m_array_items.append( dd )
                
        def print_object(self):
                try:
                        self.print_object_internal()
                except:
                        self.xx_exception("DBG_FieldInts::print_object")
                
        def print_object_internal(self):
                self.xx_dbg("DBG_FieldInts::print_object_internal::")
                self.prepare_object()
                self.xx_print_ints()
                self.xx_dbg("DBG_FieldInts::print_object_internal::out::")                        
                        
        def xx_print_ints(self):
                try:
                        self.xx_dbg("DBG_FieldInts::xx_print_ints::in::")                        
                        
                        self.xx_print_ints_internal(
                                                        self.m_parent
                                                        ,self.m_array_items
                                                        ,2)
                        
                        self.xx_dbg("DBG_FieldInts::xx_print_ints::out::")                
                except:
                        self.xx_exception("DBG_FieldInts::xx_print_int_internal:exc::")

        def xx_print_ints_internal(self
                                   , parent
                                   , ints_selectors
                                   , ii_tabs = 0):
                
                self.xx_dbg("DBG_FieldInts::xx_print_ints_internal::in::")
                
                for dd_ii in ints_selectors:
                        self.xx_print_int_internal(parent,dd_ii,ii_tabs)
                        
                self.xx_dbg("DBG_FieldInts::xx_print_ints_internal::out::")

                
        def xx_print_int_internal(self
                                  , parent
                                  , dd_ii
                                  , ii_tabs = 0):
                tabsp =""
                try:
                        self.xx_dbg("DBG_FieldInts::xx_print_int_internal::in::")
                        if (dd_ii.m_variable == "LINE"):
                                DBG_Html.print_field_html ( "*" )
                                return
                        if (dd_ii.m_variable == "EMPTY"):
                                #DBG_Html.print_field_html ( ""
                                return
                        
                        dd_ii.m_value = DBG_MemoryTools().xx_get_int(                                
                                parent
                                ,       dd_ii.m_variable)
                        
                        tabsp = self.get_parent_tabs(parent,ii_tabs)
                        #print "tabs:[" + tabsp + "]"
                        s_int = DBG_FieldsFormatters(self,"").int_to_info(dd_ii, tabsp)
                        
                        DBG_Html.print_field_html_out (  s_int )
                                
                        self.xx_dbg("DBG_FieldInts::xx_print_ints_internal::out::")
                        
                except:
                        DBG_Html.print_field_html ( tabsp + "int_exception")
                        
                        
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_FieldInts::prepare_object::in::")                        
                        
                        self.xx_prepare_ints_internal(
                                                        self.m_parent
                                                        ,self.m_array_items
                                                        ,2)
                        
                        self.xx_dbg("DBG_FieldInts::prepare_object::out::")                
                except:
                        self.xx_exception("DBG_FieldInts::prepare_object:exc::")

        def xx_prepare_ints_internal(self
                                   , parent
                                   , ints_selectors
                                   , ii_tabs = 0):
                
                self.xx_dbg("DBG_FieldInts::xx_prepare_ints_internal::in::")
                
                for dd_ii in ints_selectors:
                        self.xx_prepare_int_internal(parent,dd_ii,ii_tabs)
                        
                self.xx_dbg("DBG_FieldInts::xx_prepare_ints_internal::out::")


        def xx_prepare_int_internal(self
                                  , parent
                                  , dd_ii
                                  , ii_tabs = 0):
                try:
                        self.xx_dbg("DBG_FieldInts::xx_prepare_int_internal::in::")
                        if (dd_ii.m_variable == "LINE"):                                
                                return
                        if (dd_ii.m_variable == "EMPTY"):                                
                                return                        
                        dd_ii.m_value = DBG_MemoryTools().xx_get_int(
                                parent
                                ,       dd_ii.m_variable)
                        
                        self.xx_dbg("DBG_FieldInts::xx_prepare_int_internal::out::")
                        
                except:
                        self.xx_exception("DBG_FieldInts::xx_prepare_int_internal:exc::")

        def fields_get_int(self,smb,from_where=""):
                try:
                        self.xx_dbg("DBG_FieldInts::fields_get_int::in::")
                        ddout = -1
                        for dd_ii in self.m_array_items:
                                if( dd_ii.m_variable == smb):
                                        ddout = dd_ii.m_value
                                        break
                                
                        #DBG_Html.print_field_html ( from_where + ":field_out:" + smb + ":" + str(   ddout )
                        self.xx_dbg("DBG_FieldInts::fields_get_int::out::")        
                        return ddout                        
                except:
                        return -1