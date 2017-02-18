import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *

class DBG_IsmPathTargetLun(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_IsmPathTargetLun::__init__::in::")
                self.xx_set_class_name ( "ISM_PATH_TARGET_LUN" )
                self.xx_set_full_class_name ( "iastora!ISM_PATH_TARGET_LUN" )
                
                self.m_fields = DBG_FieldsMapper("DBG_IsmPathTargetLun"
                                         ,self)
                
                self.m_fields.add_fields_int_array([
                        "pid"
                        ,"tid"
                        ,"lun"
                        ])
                
                self.xx_dbg("DBG_IsmPathTargetLun::__init__::in::")
                        
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_IsmPathTargetLun::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_IsmPathTargetLun::prepare_object::")
                self.m_fields.set_fields_parent(self)
                if(self.xx_is_object() == 1 and self.get_use_without_childs() == 0):
                        self.m_fields.prepare_object()
                #self.mPath.set_parent(self)
                #self.mPath.prepare_object(self)

                self.xx_dbg("DBG_IsmPathTargetLun::prepare_object::out::")
                
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self,sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,pparent,sdbg=""):

                self.xx_dbg("DBG_IsmPathTargetLun::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1 and self.get_use_without_childs() == 0):
                        self.m_fields.xx_print_fields("")
                #self.mPath.print_object()
                self.xx_dbg("DBG_IsmPathTargetLun::print_object_internal::out::")                        
                        
                
        def get_class_str(self):
                self.xx_dbg("DBG_IsmPathTargetLun::get_class_str::")
                
                ccstr = """
                """
                
                self.xx_dbg("DBG_IsmPathTargetLun::get_class_str::")
