import sys
import os
import logging
from pykd import *
from .. umltools.DBG_UmlBase import *

class DBG_UmlAttrItem(DBG_UmlBase):
        def __init__(self,spar):                
                DBG_UmlBase.__init__(self,spar)
                self.xx_dbg("DBG_UmlAttrItem::__init__::method_in::")
                self.xx_set_class_name ( "DBG_UmlAttrItem" )
                self.xx_set_full_class_name ( "Wcdl::DBG_UmlAttrItem" )
                self.xx_dbg("DBG_UmlAttrItem::__init__::method_out::")
                

                        
        def exec_info(self,dd_handler, tt):
                try:
                        tt = []
                except:
                    self.xx_exception("exec_handler") 
                
