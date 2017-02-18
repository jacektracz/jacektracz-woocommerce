import sys
import os
import logging
from .. DBG_AdapterBase import *       
from .. fields.DBG_FieldsMapper import *                
class DBG_DeviceFeatureN(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_set_class_name ( "DeviceFeature" )
                self.xx_set_full_class_name ( "iastora!DeviceFeature" )
                self.m_fields = DBG_FieldsMapper("DBG_Transport"
                                         , self)
                self.m_fields.add_fields_str("mIdName",40)                
                self.m_fields.add_fields_int_array([
                        "mId"
                        ,"mIsSupported"
                        ,"mIsAllowed"                        
                        ,"mIsEnabled"
                        ,"mEnable"
                        ,"mDisable"
                        ])
                self.xx_dbg("DBG_DeviceFeatureN::__init__::out::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal()                                
                except:
                        self.xx_exception("DBG_DeviceFeatureN::print_object")
                        
        def prepare_object_internal(self):
                self.xx_dbg("DBG_DeviceFeatureN::prepare_object::in::")
                if(self.xx_is_object()==1):
                        self.m_fields.initialize_by_parent(self)
                self.xx_dbg("DBG_DeviceFeatureN::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_DeviceFeatureN::print_object::in::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object()==1):
                        self.m_fields.print_object()
                self.xx_dbg("DBG_DeviceFeatureN::print_object::out::")                        