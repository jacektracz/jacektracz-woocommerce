import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *        
        
class DBG_AdminIdentifyControllerData(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_AdminIdentifyControllerData::__init__::in::")
                self.xx_set_class_name ( "ADMIN_IDENTIFY_CONTROLLER_DATA" )
                self.xx_set_full_class_name ( "iastora!ADMIN_IDENTIFY_CONTROLLER_DATA" )
                self.m_fields = DBG_FieldsMapper("DBG_CORE"
                                         , self)

                self.m_fields.add_fields_hex_array([
                        "VID"
                        ,"SSVID"
                        ,"ACL"
                        ,"AERL"
                        ])
                
                self.m_fields.add_fields_str("SN",20)
                self.m_fields.add_fields_str("MN",40)
                self.m_fields.add_fields_str("FR",8)
                self.m_fields.add_fields_str("IEEE",3)
                self.xx_dbg("DBG_AdminIdentifyControllerData::__init__::out")
                
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_AdminIdentifyControllerData::prepare_object")
                        if(self.xx_is_object() == 1):
                                self.m_fields.set_fields_parent(self)           
                                                
                        self.xx_dbg("DBG_AdminIdentifyControllerData::prepare_object::out")
                except:
                        self.xx_exception("DBG_AdminIdentifyControllerData::prepare_object")
            
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_AdminIdentifyControllerData::print_object")        
                        self.prepare_object()
                        self.xx_print_ptr("")
                        if(self.xx_is_object() == 1):
                                self.m_fields.print_object()                                                
                        self.xx_dbg("DBG_AdminIdentifyControllerData::print_object::out")
                except:
                        self.xx_exception("DBG_AdminIdentifyControllerData::print_object")

