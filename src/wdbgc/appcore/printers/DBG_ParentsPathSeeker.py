import sys
import os
from ... appcore.printers.DBG_Base import *
from ... appcore.printers.DBG_FieldInfos import *
from ... appcore.config.DBG_PrintConfig import *

class DBG_ParentsPathSeeker(DBG_Base):
    def __init__(self,pparent,sdbg):
        DBG_Base.__init__(self,pparent,sdbg)
        self.m_parent = pparent        
        self.m_messages = DBG_FieldInfos("DBG_MemoryPtr",self)
        self.m_def_range = 20
        self.m_full_path = ""
    def set_parent(self, pparent):
        self.m_parent = pparent
        
    def get_full_path(self):
        return self.m_full_path
    
    def prepare_object(self):
        try:
            self.xx_dbg("DBG_ParentsPathSeeker::prepare_object")
            
            spath = self.get_full_objects_path(self.m_parent)
            self.m_full_path = spath
            self.m_messages.set_parent(self.m_parent)
            self.m_messages.add_message(spath)
            self.xx_dbg("DBG_ParentsPathSeeker::prepare_object")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
        
                
    def print_object(self,stabs=0):
        try:
            self.xx_dbg( "DBG_ParentsPathSeeker::xx_print_link_ptr::method_in::")
            self.m_messages.print_object("path")
            self.xx_dbg( "DBG_ParentsPathSeeker::xx_print_link_ptr::method_in::")
        except:
                self.xx_exception("xx_print_link_ptr::exception::")
            
    def get_full_objects_path(self,pparent,def_range =20):
        try:
            self.xx_dbg("DBG_ParentsPathSeeker::get_full_objects_path::in::")
            
            dd_itemsr = self.get_full_objects_array(pparent, def_range)
            sout = ""
            for dd_item in dd_itemsr:
                    s_par = ""
                    s_par = s_par + ( "(" + dd_item.__class__.__name__ )
                    s_par = s_par + ( ":" + dd_item.m_class_name + ")" )
                    s_par = s_par + ( dd_item.m_raw_variable + "->" )
                    
                    sout = sout + s_par
                    
            return sout		
            self.xx_dbg("DBG_ParentsPathSeeker::get_full_objects_path::out::")
        except:
            self.xx_exception("[print_full_path::exception]")
            return "exception"
        
    def get_full_objects_array(self,pparent,def_range =20):
        try:
            self.xx_dbg("DBG_ParentsPathSeeker::get_full_objects_array::in::")
            dd_item = pparent
            
            dd_items = []
            for ii in range( def_range ):
                    if(dd_item == None):
                        break
                    dd_items.append(dd_item)
                    if(hasattr(dd_item,"m_parent")):
                        dd_item = dd_item.m_parent
                    else:
                        break
            
            dd_itemsr = reversed(dd_items)
            return dd_itemsr		
            self.xx_dbg("DBG_ParentsPathSeeker::get_full_objects_array::out::")
        except:
            self.xx_exception("[print_full_path::exception]")
            return None
        
    
    def get_object_title(self,dd_item):
        try:
            self.xx_dbg("DBG_ParentsPathSeeker::get_object_title::in::")
            sout = ""
            s_par = ""
            s_par = s_par + ( "(" + dd_item.__class__.__name__ )
            if(hasattr(dd_item,"m_class_name")):
                s_par = s_par + ( ":" + dd_item.m_class_name + ")" )
            if(hasattr(dd_item,"m_raw_variable")):                
                s_par = s_par + ( dd_item.m_raw_variable + "" )
                
            if(hasattr(dd_item,"m_selector_for_print")):
                s_par = s_par + ( ":" + dd_item.m_selector_for_print + ")" )

            if(DBG_PrintConfig().getItem().m_show_lg_address == 1):
                if(hasattr(dd_item,"m_lg_ptr")):
                    s_par = s_par + ( ":" + dd_item.m_lg_ptr + ")" )
                
            s_par = s_par + ( "(" + str(dd_item.m_number_of_child_ex) + ")" +"" )
            
            sout = sout + s_par
            self.xx_dbg("DBG_ParentsPathSeeker::get_object_title::out::")
            return sout		
            
        except:
            self.xx_exception("[DBG_ParentsPathSeeker::add_exc_to_full_path::exception]")
            return "exception"
    
    def add_exc_to_full_path(self,pparent,tt):
        try:
            self.xx_dbg("DBG_ParentsPathSeeker::add_exc_to_full_path::in::")
            def_range = self.m_def_range
            dd_itemsr = self.get_full_objects_array(pparent, def_range)            
            for dd_item in dd_itemsr:
                try:
                    if(hasattr(dd_item,"add_exc_to_path")):
                        dd_item.add_exc_to_path(tt)
                except:                    
                    self.xx_exception("[DBG_ParentsPathSeeker::add_exc_to_full_path::item::exception]")
                    
            self.xx_dbg("DBG_ParentsPathSeeker::add_exc_to_full_path::out::")
        except:
            self.xx_exception("[DBG_ParentsPathSeeker::add_exc_to_full_path::exception]")
            
        
                        