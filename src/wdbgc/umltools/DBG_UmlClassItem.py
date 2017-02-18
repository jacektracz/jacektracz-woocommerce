import sys
import os
import logging
from pykd import *
from .. umltools.DBG_UmlBase import *
from .. umltools.DBG_UmlAttrItems import *
from .. umltools.DBG_UmlClassRefItems import *

class DBG_UmlClassItem(DBG_UmlBase):
        def __init__(self,spar):                
                DBG_UmlBase.__init__(self,spar)
                self.xx_dbg("DBG_UmlClassItem::__init__::method_in::")
                self.xx_set_class_name ( "DBG_UmlClassItem" )
                self.xx_set_full_class_name ( "Wcdl::DBG_UmlClassItem" )
                self.m_class_name = ""
                self.m_attrs = DBG_UmlAttrItems("")
                self.m_refs = DBG_UmlClassRefItems("")
                self.xx_dbg("DBG_UmlClassItem::__init__::method_out::")                

                        
        def exec_info(self,dd_handler, tt):
                try:
                        tt = []
                except:
                    self.xx_exception("exec_handler") 
                
