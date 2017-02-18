
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *

class DBG_RaidportSpinLock(DBG_AdapterBase):
        def __init__(self,pparent,spar):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_RaidportSpinLock::__init__::m_in::")
                self.xx_set_class_name ( "Wcdl::SpinLock" )
                self.xx_set_full_class_name ( "iastora!Wcdl::SpinLock" )
                
                self.m_fields = DBG_FieldsMapper("DBG_RaidportSpinLock"
                                                 , self)
                
                self.m_fields.add_fields_asstr_int("mLock")
                
                self.m_print_fields = 1
                self.m_valid = 1
                self.xx_dbg("DBG_RaidportSpinLock::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_RaidportSpinLock::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_RaidportSpinLock::prepare_object_internal::")
                #self.m_valid = self.xx_obj_valid()
                
                if(self.xx_is_object() == 1):                        
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                
                self.xx_dbg("DBG_RaidportSpinLock::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_RaidportSpinLock::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_RaidportSpinLock::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):
                        self.m_fields.print_object()
                                
                self.xx_dbg("DBG_RaidportSpinLock::print_object::m_out::")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_RaidportSpinLock::xx_obj_valid::m_in::")
                i_check = 1
                self.xx_dbg("DBG_RaidportSpinLock::xx_obj_valid::m_out::" + str(i_check))
                return i_check
        
