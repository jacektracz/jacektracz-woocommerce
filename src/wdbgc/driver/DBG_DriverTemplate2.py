import sys
import os

from .. DBG_AdapterBase import *

#from .. nvme.DBG_AdminIdentifyControllerData import *

class DBG_EndDeviceTarget(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_EndDeviceTarget::__init__::in::")
                self.xx_set_class_name ( "EndDeviceTarget" )
                self.xx_set_full_class_name ( "iastora!EndDeviceTarget" )
                self.m_fields = DBG_FieldsMapper("DBG_EndDeviceTarget"
                                         ,self)                                
                
                self.create_init()
                #self.mIdentifyControllerData = DBG_AdminIdentifyControllerData("Parent::DBG_DriverTemplate2")
                self.xx_dbg("DBG_EndDeviceTarget::__init__::in::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_EndDeviceTarget::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_EndDeviceTarget::prepare_object::")
                self.m_fields.set_fields_parent(self)
                #self.mIdentifyControllerData.xx_inc_tabs(self);                
                #self.mIdentifyControllerData.xx_compute_arr_phy_by_parent(self,"mIdentifyControllerData")

                self.xx_dbg("DBG_EndDeviceTarget::prepare_object::out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_EndDeviceTarget::print_object")
                        
        def create_init(self):
                try:
                        self.m_fields.add_fields_int_array(["mPathId","mTargetId","mLun"])                        
                except:
                        self.xx_exception("DBG_EndDeviceTarget::print_object")
                
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_EndDeviceTarget::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                self.m_fields.xx_print_fields("")
                #if(self.mIdentifyControllerData.xx_is_object()):
                #        self.mIdentifyControllerData.print_object()
                self.xx_dbg("DBG_EndDeviceTarget::print_object_internal::out::")                        
                        
                
        def get_class_str(self):
                self.xx_dbg("DBG_EndDeviceTarget::get_class_str::")
                
                ccstr = """
"""
                self.xx_dbg("DBG_EndDeviceTarget::get_class_str::")
