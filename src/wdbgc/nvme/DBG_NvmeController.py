import sys
import os
import logging
from .. DBG_AdapterBase import *       
from .. fields.DBG_FieldsMapper import *
from .. appcore.config.DBG_PrintConfig import *

from .. nvme.DBG_ControllerConfiguration import *
from .. nvme.DBG_ControllerCapabilities import *
from .. nvme.DBG_ControllerRegisters import *
from .. nvme.DBG_MSIX_TABLE import *
class DBG_NvmeController(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_NvmeController::prepare_object::__init__::in::")
                self.xx_set_class_name ( "Controller" )
                self.xx_set_full_class_name ( "iastora!Controller" )               
                self.mCC = DBG_ControllerConfiguration("Parent::DBG_NvmeController")
                self.mCAP = DBG_ControllerCapabilities("Parent::DBG_NvmeController")
                self.mABar = DBG_ControllerRegisters("Parent::DBG_NvmeController")
                self.mMsixTable = DBG_MSIX_TABLE("Parent::DBG_NvmeController", self)
                self.m_fields = DBG_FieldsMapper("DBG_MSIX_TABLE", self)
                self.init_object_fields()
                self.xx_dbg("DBG_NvmeController::prepare_object::__init__::out::")
                
        def init_object_fields(self):
       
                self.xx_dbg("DBG_MSIX_TABLE::init_object_fields::in::")                                
                
                self.m_fields.add_fields_asstr_ints(["mUseSharedInterrupt"
                                                     ,"mNumOfMsiXIVGranted"
                                                     ,"mNumberOfUsedIV"
                                                     ,"mMsixTableOffset"
                                                     ,"mMsiXTableBIR"
                                                     ,"mMsiXTableSize"])
                self.xx_dbg("DBG_MSIX_TABLE::init_object_fields::m_out::")
                
        def prepare_object(self):
                self.xx_dbg("DBG_NvmeController::prepare_object::")
                if(self.xx_is_object() == 1 ):
                        self.clear_messages()
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.mCC.set_addr_arr(self,"mCC")
                        self.mCC.prepare_object()
                        
                        self.mCAP.set_addr_arr(self,"mCAP")
                        self.mCAP.prepare_object()
                        #self.mABar.xx_inc_tabs(self);
                        
                        self.mABar.set_addr_arr(self,"mABar")
                        self.mABar.prepare_object()
                        
                        self.mMsixTable.set_addr_arr(self,"mMsixTable")
                        self.mMsixTable.prepare_object()
                
                self.xx_dbg("DBG_NvmeController::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_NvmeController::print_object::")
                self.xx_print_ptr("")
                self.prepare_object()
                if(self.xx_is_object() == 1 ):                        
                        self.m_fields.print_object()
                        self.mCC.print_object()
                        self.mCAP.print_object()
                        self.mABar.print_object()
                        self.mMsixTable.print_object()
                
                self.xx_dbg("DBG_NvmeController::print_object::out::")
        
        
        def xx_obj_valid(self):
                return self.xx_is_object()