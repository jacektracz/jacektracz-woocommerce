import sys
import os
from .. DBG_MemoryPtr import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. appcore.memory.DBG_MemoryTools import *
from .. appcore.logging.DBG_Log import *
from .. appcore.htmlwriters.DBG_MainPrintDispatcher import *
from .. appcore.htmlwriters.DBG_Html import *
from .. fields.DBG_FieldsFormatters import *

class DBG_FieldString(DBG_MemoryPtr):
        def __init__(self,svar,ilen): 
                DBG_MemoryPtr.__init__(self,"DBG_FieldString")
                self.m_variable = svar
                self.m_length = ilen
                self.m_value = ""
                self.m_field_type = "STRING"

                
class DBG_FieldStrings(DBG_MemoryPtr):
        def __init__(self,pparent,sdbg): 
                DBG_MemoryPtr.__init__(self,sdbg)
                self.xx_dbg("DBG_FieldStrings::init_object_internal::")
                self.xx_set_class_name ( "FieldStrings" )
                self.xx_set_full_class_name ( "iastora!FieldStrings" )
                self.m_parent = None
                self.m_array_items = []
                self.xx_dbg("DBG_FieldStrings::init_object_internal::out::")
                
                #self.init_object(pparent, sdbg)
                
        def clear_array(self):
                self.m_array_items = []
                
        def set_parent(self, pparent):
                self.m_parent = pparent
                
        def set_values(self,pstrs):
                self.m_array_items = pstrs
                
        def add_str(self, pvar, plen):
                dd = DBG_FieldString(pvar,plen)
                dd.m_field_type = "STR"
                self.m_array_items.append( dd )
                
        def add_struni(self, pvar, plen):
                dd = DBG_FieldString(pvar,plen)
                dd.m_field_type = "STRUNI"
                self.m_array_items.append( dd )
                
        def add_uchar(self, pvar):
                dd = DBG_FieldString(pvar, 1)
                dd.m_field_type = "UCHAR"
                dd.m_length = 1
                self.m_array_items.append( dd )
                
        def add_asstr_u32(self, pvar):
                dd = DBG_FieldString(pvar, 1)
                dd.m_field_type = "U32"
                dd.m_length = 1
                self.m_array_items.append( dd )
                
        def add_asstr_int(self, pvar):
                dd = DBG_FieldString(pvar, 1)
                dd.m_field_type = "INT"
                dd.m_length = 1
                self.m_array_items.append( dd )
                
        def add_asstr_bool(self, pvar):
                dd = DBG_FieldString(pvar, 1)
                dd.m_field_type = "BOOL"
                dd.m_length = 1
                self.m_array_items.append( dd )
                
        def add_asstr_hex(self, pvar):
                dd = DBG_FieldString(pvar, 1)
                dd.m_field_type = "HEX"
                dd.m_length = 1
                self.m_array_items.append( dd )
                
        def add_asstr_addr(self, pvar):
                dd = DBG_FieldString(pvar, 1)
                dd.m_field_type = "ADDR"
                dd.m_length = 1
                self.m_array_items.append( dd )
                
        def add_asstr_addr_method(self, pvar):
                dd = DBG_FieldString(pvar, 1)
                dd.m_field_type = "ADDR_METHOD"
                dd.m_length = 1
                self.m_array_items.append( dd )
                
        def add_asstr_addr_memory(self, pvar):
                dd = DBG_FieldString(pvar, 1)
                dd.m_field_type = "ADDR_MEMORY"
                dd.m_length = 1
                self.m_array_items.append( dd )
                
        def add_asstr_addr_class(self, pvar):
                dd = DBG_FieldString(pvar, 1)
                dd.m_field_type = "ADDR_CLASS"
                dd.m_length = 1
                self.m_array_items.append( dd )
                
        def add_asstr_raw_output(self, pvar):
                dd = DBG_FieldString(pvar, 1)
                dd.m_field_type = "RAW_OUTPUT"
                dd.m_length = 1
                self.m_array_items.append( dd )
                
        def add_raw_str(self, pvar):
                dd = DBG_FieldString("RAWS", 1)
                dd.m_field_type = "RAWS"
                dd.m_variable = "RAWS"
                dd.m_length = 1
                dd.m_value = pvar
                #print pvar
                self.m_array_items.append( dd )
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal()
                except:
                        self.xx_exception("DBG_FieldStrings::print_object")
                                        
        def prepare_object_internal(self):
                self.xx_dbg("DBG_FieldStrings::prepare_object::")
                self.prepare_items(
                                self.m_parent
                                ,self.m_array_items)
                
                self.xx_dbg("DBG_FieldStrings::prepare_object::out::")
                
        def prepare_items(self, parent,pitems):                
                self.xx_dbg("DBG_FieldStrings::xx_print_strs_internal::in::")                
                for dd_ii in pitems:
                        dd_ii.m_value = self.get_field_value( parent, dd_ii )
                        
                self.xx_dbg("DBG_FieldStrings::xx_print_strs_internal::out::")
                
        def get_field_value(self, parent, dd_ii):
                outv = "None"
                isset =0
                variable = "NOT_SET_VAR"
                try:
                        self.xx_dbg("DBG_FieldStrings::get_field_value::in::")
                        variable = dd_ii.m_variable
                        if(isset == 0):
                                if (dd_ii.m_field_type == "U32"):
                                        isset = 1
                                        outv = DBG_MemoryTools().xx_get_u32(
                                                parent
                                                , dd_ii.m_variable)
                                        outv = self.get_str_ascii_int(outv)
                                        
                        if(isset == 0):
                                if (dd_ii.m_field_type == "INT"):
                                        isset = 1
                                        outv = DBG_MemoryTools().xx_get_int(
                                                parent
                                                , dd_ii.m_variable)
                                        outv = self.get_str_ascii_int(outv)
                                        
                        if(isset == 0):
                                if (dd_ii.m_field_type == "BOOL"):
                                        isset = 1
                                        outv = DBG_MemoryTools().xx_get_int(
                                                parent
                                                , dd_ii.m_variable)
                                        outv = self.get_str_ascii_int(outv)
                                        
                        if(isset == 0):
                                if (dd_ii.m_field_type == "ADDR"):
                                        isset = 1
                                        outv = DBG_MemoryTools().xx_get_as_addr(
                                                parent
                                                , dd_ii.m_variable)
                                        outv = self.get_str_ascii_int(outv)

                        if(isset == 0):
                                if (dd_ii.m_field_type == "ADDR_CLASS"):
                                        isset = 1
                                        outv = DBG_MemoryTools().xx_get_as_addr(
                                                parent
                                                , dd_ii.m_variable)
                                        outv = self.get_str_ascii_int(outv)
                                        
                        if(isset == 0):
                                if (dd_ii.m_field_type == "ADDR_METHOD"):
                                        isset = 1
                                        outv = DBG_MemoryTools().xx_get_as_addr(
                                                parent
                                                , dd_ii.m_variable)
                                        outv = self.get_str_ascii_int(outv)
                        if(isset == 0):
                                if (dd_ii.m_field_type == "ADDR_MEMORY"):
                                        isset = 1
                                        outv = DBG_MemoryTools().xx_get_as_addr(
                                                parent
                                                , dd_ii.m_variable)
                                        outv = self.get_str_ascii_int(outv)
                                        
                        if(isset == 0):
                                if (dd_ii.m_field_type == "RAW_OUTPUT"):
                                        isset = 1
                                        outv = DBG_MemoryTools().xx_get_as_raw_output(
                                                parent
                                                , dd_ii.m_variable)
                                        outv = self.get_str_ascii_int(outv)                                        
                                        
                        if(isset == 0):
                                if (dd_ii.m_field_type == "RAWS"):
                                        isset = 1
                                        outv = dd_ii.m_value
                                        self.xx_dbg("DBG_FieldStrings::xx_print_int_internal::in::")
                                
                        if(isset == 0):
                                if (dd_ii.m_field_type == "STR"):
                                        isset = 1
                                        outv =  DBG_MemoryTools().xx_get_str(
                                                parent
                                                , dd_ii.m_variable
                                                , dd_ii.m_length)
                        
                                        s_ascii = self.get_str_ascii(outv)
                                        outv = str(s_ascii)

                        if(isset == 0):
                                if (dd_ii.m_field_type == "STRUNI"):
                                        isset = 1
                                        outv =  DBG_MemoryTools().xx_get_str_unicode(
                                                parent
                                                , dd_ii.m_variable
                                                , dd_ii.m_length)
                        
                                        s_ascii = self.get_str_ascii(outv)
                                        outv = str(s_ascii)

                        if(isset == 0):  
                                isset = 1
                                outv =  DBG_MemoryTools().xx_get_str(
                                        parent
                                        , dd_ii.m_variable
                                        , dd_ii.m_length)
                        
                                s_ascii = self.get_str_ascii(outv)
                                outv = str(s_ascii)
                        
                        self.xx_dbg("DBG_FieldStrings::get_field_value::out::[]" + str(outv))
                        
                        return outv
                
                except:
                        self.xx_exception("DBG_FieldStrings::xx_print_int_internal:exc::" + str(variable))
                        return "EXCEPTION"
                
        def print_object(self):
                try:
                        self.print_object_internal(self)
                except:
                        self.xx_exception("DBG_FieldStrings::print_object")
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_FieldStrings::print_object::")
                self.prepare_object()
                self.xx_print_strs()
                self.xx_dbg("DBG_FieldStrings::print_object::out::")                        
                        
        def xx_print_strs(self):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_strs::in::")
                        
                        self.xx_print_strs_internal(
                                                        self.m_parent
                                                        ,self.m_array_items
                                                        ,2)
                        
                        self.xx_dbg("DBG_FieldStrings::xx_print_strs::out::")                
                except:
                        self.xx_exception("DBG_FieldStrings::xx_print_int_internal:exc::")

        def xx_print_strs_internal(self, parent,pitems,ii_tabs = 0):
                
                self.xx_dbg("DBG_FieldStrings::xx_print_strs_internal::in::")
                
                for dd_ii in pitems:
                        self.xx_print_str_internal(
                                parent
                                ,dd_ii
                                ,ii_tabs)
                        
                self.xx_dbg("DBG_FieldStrings::xx_print_strs_internal::out::")

                
        def xx_print_str_internal(self
                                  , parent
                                  , dd_ii
                                  , ii_tabs = 0):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_int_internal::in::")
                        
                        dd_ii.m_value = self.get_field_value( parent, dd_ii )
                        
                        tabsp = self.get_parent_tabs(parent, ii_tabs)
                        
                        if dd_ii.m_value != "None":
                                self.xx_print_str_item_internal(
                                        tabsp
                                        ,   dd_ii)
                                
                        self.xx_dbg("DBG_FieldStrings::xx_print_ints_internal::out::")
                        
                except:
                        self.xx_exception("DBG_FieldStrings::xx_print_int_internal:exc::")
                        
                
                        
        def xx_print_str_item_internal(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_int_internal::in::")
                        is_printed = 0
                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "UCHAR"):
                                        is_printed = 1
                                        self.xx_print_str_item_uchar(tabsp, dd_ii)
                                        
                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "RAWS"):
                                        is_printed = 1
                                        self.xx_print_str_item_raws(tabsp, dd_ii)
                                        
                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "INT"):
                                        is_printed = 1
                                        self.xx_print_str_item_int(tabsp, dd_ii)
                                        
                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "ADDR"):
                                        is_printed = 1
                                        self.xx_print_str_item_addr(tabsp, dd_ii)

                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "ADDR_CLASS"):
                                        is_printed = 1
                                        self.xx_print_str_item_addr_class(tabsp, dd_ii)
                                        
                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "ADDR_METHOD"):
                                        is_printed = 1
                                        self.xx_print_str_item_addr_method(tabsp, dd_ii)
                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "ADDR_MEMORY"):
                                        is_printed = 1
                                        self.xx_print_str_item_addr_memory(tabsp, dd_ii)

                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "RAW_OUTPUT"):
                                        is_printed = 1
                                        self.xx_print_str_item_raw_output(tabsp, dd_ii)
                                        
                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "BOOL"):
                                        is_printed = 1
                                        self.xx_print_str_item_int(tabsp, dd_ii)
                                        
                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "U32"):
                                        is_printed = 1
                                        self.xx_print_str_item_u32(tabsp, dd_ii)

                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "STR"):
                                        is_printed = 1
                                        self.xx_print_str_item_str(tabsp, dd_ii)

                        if(is_printed == 0 ):
                                if(dd_ii.m_field_type == "STRUNI"):
                                        is_printed = 1
                                        self.xx_print_str_item_struni(tabsp, dd_ii)
                        
                        if(is_printed == 0 ):
                                is_printed = 1
                                self.xx_print_str_item_str(tabsp, dd_ii)
                                
                        self.xx_dbg("DBG_FieldStrings::xx_print_ints_internal::out::[" + str(is_printed) + "]")                        
                except:
                        self.xx_exception("DBG_FieldStrings::xx_print_int_internal:exc::")

        def xx_print_str_item_uchar(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_ints_internal::out::")                        
                        if (len(dd_ii.m_value) > 0):
                                ch = dd_ii.m_value[0]
                                DBG_Html.print_field_html_out (  tabsp + str(dd_ii.m_variable) + ":" + str(ord(ch)))
                        else:
                                DBG_Html.print_field_html_out (  tabsp + str(dd_ii.m_variable) + ":-1" )
                        self.xx_dbg("DBG_FieldStrings::xx_print_ints_internal::out::")
                        
                except:
                        self.xx_exception("DBG_FieldStrings::xx_print_int_internal:exc::")
                        
        def xx_print_str_item_raws(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_raws::out::")
                        svar = ""
                        svar = svar + tabsp
                        svar = svar + "INFO:"
                        svar = svar + str(dd_ii.m_value)
                        if(dd_ii.m_value == "EMPTY_LINE"):
                                svar = ""
                        DBG_Html.print_field_html_out (  svar )
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_raws::out::")                        
                except:
                        self.xx_exception_printed("DBG_FieldStrings::xx_print_str_item_raws:exc::")
                        
        def xx_print_str_item_u32(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_u32::out::")
                        svar = ""
                        svar = svar + tabsp
                        svar = svar + "U32:"
                        svar = svar + dd_ii.m_variable + ":"
                        #svar = svar + str(dd_ii.m_value)        
                        svar = svar + DBG_FieldsFormatters(self,"").strint_to_info(dd_ii.m_value, "")
                        DBG_Html.print_field_html_out (  svar )
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_u32::out::")
                except:
                        self.xx_exception_printed("DBG_FieldStrings::xx_print_str_item_u32:exc::")

        def xx_print_str_item_addr(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_u32::out::")
                        svar = ""
                        svar = svar + tabsp
                        svar = svar + "ADDR:"
                        svar = svar + dd_ii.m_variable + ":"
                        svar = svar + str(dd_ii.m_value)        
                        #svar = svar + DBG_FieldsFormatters(self,"").strint_to_info(dd_ii.m_value, "")
                        DBG_Html.print_field_html_out (  svar )
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_u32::out::")
                except:
                        self.xx_exception_printed("DBG_FieldStrings::xx_print_str_item_u32:exc::")
                        
        def xx_print_str_item_addr_method(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_addr_method::in::")
                        svar = ""
                        svar = svar + tabsp
                        svar = svar + "ADDR_METHOD:"
                        svar = svar + dd_ii.m_variable + ":"
                        svar = svar + str(dd_ii.m_value)        
                        #svar = svar + DBG_FieldsFormatters(self,"").strint_to_info(dd_ii.m_value, "")
                        DBG_Html.print_field_html_out (  svar )
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_addr_method::out::")
                except:
                        self.xx_exception_printed("DBG_FieldStrings::xx_print_str_item_addr_method:exc::")
                        
        def xx_print_str_item_addr_memory(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_addr_memory::in::")
                        svar = ""
                        svar = svar + tabsp
                        svar = svar + "ADDR_MEMORY:"
                        svar = svar + dd_ii.m_variable + ":"
                        svar = svar + str(dd_ii.m_value)        
                        #svar = svar + DBG_FieldsFormatters(self,"").strint_to_info(dd_ii.m_value, "")
                        DBG_Html.print_field_html_out (  svar )
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_addr_memory::out::")
                except:
                        self.xx_exception_printed("DBG_FieldStrings::xx_print_str_item_addr_method:exc::")
                        
        def xx_print_str_item_addr_class(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_addr_class::in::")
                        svar = ""
                        svar = svar + tabsp
                        svar = svar + "ADDR_CLASS:"
                        svar = svar + dd_ii.m_variable + ":"
                        svar = svar + str(dd_ii.m_value)        
                        #svar = svar + DBG_FieldsFormatters(self,"").strint_to_info(dd_ii.m_value, "")
                        DBG_Html.print_field_html_out (  svar )
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_addr_class::out::")
                except:
                        self.xx_exception_printed("DBG_FieldStrings::xx_print_str_item_addr_class:exc::")
                        
        def xx_print_str_item_raw_output(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_raw_output::out::")
                        svar = ""
                        svar = svar + tabsp
                        svar = svar + "RAW_OUTPUT:"
                        svar = svar + dd_ii.m_variable + ":"
                        svar = svar + str(dd_ii.m_value)        
                        #svar = svar + DBG_FieldsFormatters(self,"").strint_to_info(dd_ii.m_value, "")
                        DBG_Html.print_field_html_out (  svar )
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_raw_output::out::")
                except:
                        self.xx_exception_printed("DBG_FieldStrings::xx_print_str_item_raw_output:exc::")

        def xx_print_str_item_int(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_int::out::")
                        svar = ""
                        svar = svar + tabsp
                        svar = svar + "INT:"
                        svar = svar + dd_ii.m_variable + ":"
                        #svar = svar + str(dd_ii.m_value)        
                        svar = svar + DBG_FieldsFormatters(self,"").strint_to_info(dd_ii.m_value, "")
                        DBG_Html.print_field_html_out (  svar )
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_int::out::")
                except:
                        self.xx_exception_printed("DBG_FieldStrings::xx_print_str_item_int:exc::")

        def xx_print_str_item_bool(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_bool::out::")
                        svar = ""
                        svar = svar + tabsp
                        svar = svar + "BOOL:"
                        svar = svar + dd_ii.m_variable + ":"
                        svar = svar + str(dd_ii.m_value)        
                        svar = svar + DBG_FieldsFormatters(self,"").strint_to_info(dd_ii.m_value, "")
                        DBG_Html.print_field_html_out (  svar )
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_bool::out::")
                except:
                        self.xx_exception_printed("DBG_FieldStrings::xx_print_str_item_int:exc::")

        def xx_print_str_item_str(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_ints_internal::out::")
                        svar = ""
                        svar = svar + tabsp
                        svar = svar + "STR:"
                        svar = svar + dd_ii.m_variable + ":"
                        svar = svar + str(dd_ii.m_value)
                                
                        DBG_Html.print_field_html_out (  svar )
                        self.xx_dbg("DBG_FieldStrings::xx_print_ints_internal::out::")                        
                except:
                        self.xx_exception_printed("DBG_FieldStrings::xx_print_str_item_str:exc::")

        def xx_print_str_item_struni(self, tabsp, dd_ii):
                try:
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_struni::out::")
                        svar = ""
                        svar = svar + tabsp
                        svar = svar + "STRUNI:"
                        svar = svar + dd_ii.m_variable + ":"
                        svar = svar + str(dd_ii.m_value)
                                
                        DBG_Html.print_field_html_out (  svar )
                        self.xx_dbg("DBG_FieldStrings::xx_print_str_item_struni::out::")                        
                except:
                        self.xx_exception_printed("DBG_FieldStrings::xx_print_str_item_struni:exc::")
                        
        def xx_exception_printed(self, tt):
                self.xx_exception(tt)
                s_ex = "exception:probably ascii code"
                DBG_Html.print_field_html ( s_ex )
                
        def get_str_ascii(self,tt):
            s_str_check = tt.encode('ascii', 'ignore').decode('ascii')
            return s_str_check
        
        def get_str_ascii_int(self,tt):
            s_str_check = str(tt)
            return s_str_check
        
        def fields_get_string(self,smb,from_where = ""):
                try:
                        self.xx_dbg("DBG_FieldStrings::fields_get_int::in::")
                        ddout = ""
                        for dd_ii in self.m_array_items:
                                if( dd_ii.m_variable == smb):
                                        ddout = dd_ii.m_value
                                        break
                                
                        ddout = self.get_str_ascii(ddout)
                        self.xx_dbg("DBG_FieldStrings::fields_get_int::out::")        
                        return ddout                        
                except:
                        self.xx_exception("DBG_FieldStrings::xx_print_str_item_str:exc::")
                        return ""
