
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
class DBG_AHCI_PORT(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_AHCI_PORT::__init__::m_in::")
                self.xx_set_class_name ( "AHCI_PORT" )
                self.xx_set_full_class_name ( "iastora!AHCI_PORT" )
                self.m_fields = DBG_FieldsMapper("DBG_AHCI_PORT"
                                         , self)

                self.m_fields.add_fields_asstr_u32("CLB.Raw")
                self.m_fields.add_fields_asstr_u32("CLBU")
                self.m_fields.add_fields_asstr_u32("FB.Raw")
                self.m_fields.add_fields_asstr_u32("FBU")
                self.m_fields.add_fields_asstr_u32("IS.Raw")
                self.m_fields.add_fields_asstr_u32("IE.Raw")
                self.m_fields.add_fields_asstr_u32("CMD.Raw")
                self.m_fields.add_fields_asstr_u32("TFD.Raw")
                self.m_fields.add_fields_asstr_u32("SIG.Raw")
                self.m_fields.add_fields_asstr_u32("SSTS.Raw")
                self.m_fields.add_fields_asstr_u32("SCTL.Raw")
                self.m_fields.add_fields_asstr_u32("SERR.Raw")
                self.m_fields.add_fields_asstr_u32("SACT")
                self.m_fields.add_fields_asstr_u32("CI")
                self.m_fields.add_fields_asstr_u32("SNTF.Raw")
                self.m_fields.add_fields_asstr_u32("DEVSLP.Raw")
                self.m_print_fields = 0
                self.m_valid = 0
                self.xx_dbg("DBG_AHCI_PORT::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_AHCI_PORT::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_AHCI_PORT::prepare_object_internal::")
                self.m_valid = self.xx_obj_valid()
                
                if(self.print_ahci_obj_fields()):                        
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                
                self.xx_dbg("DBG_AHCI_PORT::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_AHCI_PORT::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_AHCI_PORT::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.m_valid != 1):
                        self.add_message("object_is_not_valid")
                else:
                        self.add_message("object_is_valid")
                                        
                if(self.print_ahci_obj_fields()):
                        self.m_fields.xx_print_fields("")
                                
                self.xx_dbg("DBG_AHCI_PORT::print_object::m_out::")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_AHCI_PORT::xx_obj_valid::m_in::")
                i_check = self.xx_check_u32(self,"CI")
                self.xx_dbg("DBG_AHCI_PORT::xx_obj_valid::m_out::" + str(i_check))
                return i_check
        
        def print_ahci_obj_fields(self):
                self.xx_dbg("DBG_AHCI_PORT::print_ahci_obj_fields::m_in::")
                pp = 0
                p_all = DBG_PrintConfig().getItem().m_print_ahci_port_fields
                if(self.xx_is_object()== 1 and
                   (self.m_valid == 1 or  p_all == 1)):
                        pp = 1
                        
                self.xx_dbg("DBG_AHCI_PORT::print_ahci_obj_fields::m_out::" + str(pp))
                return pp
