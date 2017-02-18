import sys
import os
import logging
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. appcore.config.DBG_PrintConfig import *

from .. nvme.DBG_ControllerConfiguration import *
from .. nvme.DBG_ControllerCapabilities import *
from .. nvme.DBG_ControllerStatus import *
class DBG_ControllerRegisters(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "CONTROLLER_REGISTERS" )
                self.xx_set_full_class_name ( "iastora!CONTROLLER_REGISTERS" )
                self.mCC = DBG_ControllerConfiguration("Parent::DBG_NvmeController")
                self.mCAP = DBG_ControllerCapabilities("Parent::DBG_NvmeController")
                self.mCSTS = DBG_ControllerStatus("Parent::DBG_NvmeController")
                self.m_fields = DBG_FieldsMapper("DBG_MSIX_TABLE", self)
               
        def prepare_object(self):                
                self.xx_dbg("DBG_ControllerRegisters::prepare_object::in::")
                if(self.xx_is_object()==1):
                        
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.mCC.set_addr_arr(self,"CC")
                        self.mCC.prepare_object()
        
                        self.mCAP.set_addr_arr(self,"CAP")
                        self.mCAP.prepare_object()
                        
                        self.mCSTS.set_addr_arr(self,"CSTS")
                        self.mCSTS.prepare_object()
                
                self.xx_dbg("DBG_ControllerRegisters::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_ControllerRegisters::print_object::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object()==1):
                        self.m_fields.print_object()
                        self.mCAP.print_object()
                        self.mCC.print_object()
                        self.mCSTS.print_object()
