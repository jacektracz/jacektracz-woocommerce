import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. raidism.DBG_CfgDiskList_PyList import *

class DBG_CfgDiskList(DBG_AdapterBase):
        def __init__(self,spar,pparent):
                DBG_AdapterBase.__init__(self, spar)                
                self.xx_dbg("DBG_CfgDiskList::__init__::m_in::")
                self.xx_set_class_name ( "CfgDiskList" )
                self.xx_set_full_class_name ( "iastora!CfgDiskList" )
                self.m_parent = pparent
                self.m_fields = DBG_FieldsMapper("DBG_CfgDiskList",self)
                self.m_link_list = DBG_CfgDiskList_PyList("DBG_CfgDiskList",self)
                self.xx_dbg("DBG_CfgDiskList::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_CfgDiskList::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_CfgDiskList::prepare_object_internal::m_in::")
                if(self.xx_is_object() == 1):
                        self.m_fields.initialize_by_parent(self)
                        self.m_link_list.set_addr(self,"SELF")
                        self.m_link_list.prepare_object()
                        
                self.xx_dbg("DBG_CfgDiskList::prepare_object_internal::m_out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")                        
                        self.print_object_internal(self)
                        self.xx_print_end("")                        
                except:
                        self.xx_exception("DBG_CfgSerial::print_object")                        
                                                        
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_CfgDiskList::print_object_internal::m_in::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):                        
                        self.m_fields.print_object()
                        self.m_link_list.print_object()
                self.xx_dbg("DBG_CfgDiskList::print_object_internal::m_out::")
