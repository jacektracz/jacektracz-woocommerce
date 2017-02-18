﻿import sys
import os
from .. DBG_AdapterBase import *
from .. raidism.DBG_IsmPathTargetLun import *


class DBG_CfgSerial(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_CfgSerial::__init__::m_in::")
                self.xx_set_class_name ( "CfgSerial" )
                self.xx_set_full_class_name ( "iastora!CfgSerial" )
                self.m_fields = DBG_FieldsMapper("DBG_IsmPathTargetLun"
                                         ,self)
                
                self.m_fields.add_fields_str("serial",16)
                
                self.xx_dbg("DBG_CfgSerial::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_CfgSerial::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_CfgSerial::prepare_object_internal::m_in::")
                self.m_fields.set_fields_parent(self)
                #if(self.xx_is_object() == 1):                                        
                        #self.m_ptl.set_adr_arr(self,"ptl")
                
                self.xx_dbg("DBG_CfgSerial::prepare_object_internal::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_CfgSerial::print_object_internal::m_in::")
                self.prepare_object()
                self.xx_print_ptr("")

                if(self.xx_is_object() == 1):
                        self.m_fields.xx_print_fields("")
                        self.xx_dbg("DBG_CfgSerial::print_object_internal::no_obj::")
                        
                self.xx_dbg("DBG_CfgSerial::print_object_internal::m_out::")
                
