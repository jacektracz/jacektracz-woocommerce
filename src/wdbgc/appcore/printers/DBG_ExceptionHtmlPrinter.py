import sys
import os
from ... appcore.printers.DBG_Base import *
from ... appcore.printers.DBG_FieldInfos import *
from ... appcore.config.DBG_PrintConfig import *
from ... appcore.htmlwriters.DBG_Html import *
from ... appcore.exceptions.DBG_MainExceptionsSet import *
from ... appcore.exceptions.DBG_ExceptionsData import *

class DBG_ExceptionHtmlPrinter(DBG_Base):
    def __init__(self,pparent,sdbg):
        DBG_Base.__init__(self,pparent,sdbg)
        self.m_parent = pparent
        self.m_messages = DBG_FieldInfos("DBG_MemoryPtr",self)
        self.m_exceptions = DBG_ExceptionsData()
        self.m_config = None
        
    def set_parent(self,pparent):
        self.xx_dbg( "DBG_ExceptionHtmlPrinter::set_parent::method_in::")
        self.m_parent = pparent
        self.xx_dbg( "DBG_ExceptionHtmlPrinter::set_parent::method_out::")
        
    def prepare_object(self):
        try:
            
            self.xx_dbg("DBG_StatelPrinter::prepare_object")
            self.m_messages.set_parent(self.m_parent)
            self.m_messages.clear_array()
            arr_s = self.get_exceptions().get_strings()
            for dd_ii in arr_s:
                self.add_msg("exception",dd_ii)                    

            self.xx_dbg("DBG_StatelPrinter::prepare_object")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
        
    def add_msg(self, title,tt):
        self.m_messages.add_message(title + ":" + tt)
        
    def print_object(self):
                try:                        
                        self.print_object_internal()                        
                except:
                        self.xx_exception("DBG_FieldsMapper::print_object")
                
    def print_object_internal(self):
        try:
            self.xx_dbg( "DBG_StatelPrinter::xx_print_link_ptr::method_in::")
            self.m_messages.print_object("appcore.exceptions")
            self.xx_dbg( "DBG_StatelPrinter::xx_print_link_ptr::method_in::")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
            
    def add_exception(self,tt):
        try:
            #sex1 = repr(traceback.extract_stack())
            s_exc = repr(traceback.format_stack())
            maxdef = DBG_PrintConfig().getItem().get_max_obj_stored_errors()
            is_stored = self.get_exceptions().get_len()
            if(is_stored < maxdef):                
                self.get_exceptions().add_exception(tt + ":" + str(s_exc))
        except:
            self.xx_exception("DBG_MainExceptionsSet::getItem::excp::")
            
    def get_exceptions(self):
        try:
            return self. m_exceptions
        except:
                self.xx_exception("DBG_MainExceptionsSet::get_exceptions::excp::")
                return None
            