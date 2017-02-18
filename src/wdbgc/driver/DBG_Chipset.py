import sys
import os
from .. DBG_AdapterBase import *        
from .. defs.DBG_ChipsetIdMap import *
from .. fields.DBG_FieldsMapper import *
from .. appcore.config.DBG_PrintConfig import *

class DBG_Chipset(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_Chipset::__init__::in::")
                self.xx_set_class_name ( "Chipset" )
                self.xx_set_full_class_name ( "iastora!Wcdl::Chipset" )
                self.m_fields = DBG_FieldsMapper("DBG_ChipsetId"
                                         ,self)
                
                if(DBG_PrintConfig().getItem().self_is_above_or_equal( 15 ) == 1):
                        self.m_fields.add_fields_int_array([
                                "mChipsetId"                                
                                ])
                        
                self.m_fields.add_fields_int_array([                                        
                        "LINE"
                        ])
                        
                self.mChipsetId = 0
                self.xx_dbg("DBG_Chipset::__init__::out")
                
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_Chipset::prepare_object")
                        if(self.xx_is_object() == 1):
                                self.m_fields.initialize_by_parent(self)
                                self.mChipsetId = self.m_fields.get_fields_int("mChipsetId")                                
                        self.xx_dbg("DBG_Chipset::prepare_object::out")
                except:
                        self.xx_exception("DBG_Chipset::prepare_object")
            
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_Chipset::print_object")        
                        self.prepare_object()
                        self.xx_print_ptr("")
                        if(self.xx_is_object() == 1):
                                chn = DBG_ChipsetIdMap("").get_str(self.mChipsetId)
                                self.m_fields.add_raw_str( "Chipset:" + chn)
                                self.m_fields.print_object()
                                
                                
                        self.xx_dbg("DBG_Chipset::print_object::out")
                except:
                        self.xx_exception("DBG_Chipset::print_object")

