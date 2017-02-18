

import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
#from .. childdir.DBG_ApstTable import *

class DBG_BbmIntvlNode(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_BbmIntvlNode::__init__::m_in::")
                self.xx_set_class_name ( "BbmIntvlNode" )
                self.xx_set_full_class_name ( "iastora!BbmIntvlNode" )
                #self.m_child_item = DBG_ApstTable("Parent::DBG_BbmIntvlNode")
                self.m_fields = DBG_FieldsMapper("DBG_BbmIntvlNode"
                                         , self)

                self.m_fields.add_fields_int_array([
                        "EMPTY"
                        ])
                
                
                self.xx_dbg("DBG_BbmIntvlNode::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_BbmIntvlNode::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_BbmIntvlNode::prepare_object_internal::")
                
                if(self.xx_is_object() == 1):
                        self.m_fields.set_fields_parent(self)                      
                        #self.m_child_item.set_addr_arr(self,"m_child_item")
                
                self.xx_dbg("DBG_BbmIntvlNode::prepare_object::m_out::")
                
        def print_object(self):
                self.xx_dbg("DBG_BbmIntvlNode::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):                
                        self.m_fields.xx_print_fields("")
                        #self.m_child_item.print_object()
                self.xx_dbg("DBG_BbmIntvlNode::print_object::m_out::")

