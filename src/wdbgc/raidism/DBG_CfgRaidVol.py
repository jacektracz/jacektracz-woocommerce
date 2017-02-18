import sys
import os
from .. DBG_AdapterBase import *
from .. raidism.DBG_IsmPathTargetLun import *

from .. raidport.DBG_RaidVol import *

from .. fields.DBG_FieldsMapper import *
from .. appsrc.ismcfg.DBG_CfgRaidMap import *

class DBG_CfgRaidVol(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_CfgRaidVol::__init__::m_in::")
                self.xx_set_class_name ( "CfgRaidVol" )
                self.xx_set_full_class_name ( "iastora!CfgRaidVol" )
                self.m_fields = DBG_FieldsMapper("DBG_CfgRaidVol", self)
                
                
                self.m_loMap = DBG_CfgRaidMap("DBG_CfgRaidVol", self)
                self.m_hiMap = DBG_CfgRaidMap("DBG_CfgRaidVol", self)
                self.initialize_class_fields()
                self.xx_dbg("DBG_CfgRaidVol::__init__::m_out::")
                
        def initialize_class_fields(self):
                self.m_fields.add_fields_asstr_ints(["ckptId"
                                               ,"migrState"
                                               ,"dirty"
                                               ,"currMigrUnit"
                                               ,"verifyErrors"
                                               ,"verifyBadBlocks"
                                               ,"fastSyncEnabled"
                                               ,"fastSyncState"
                                               ])
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_CfgRaidVol::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_CfgRaidVol::prepare_object_internal::m_in::")                
                if(self.xx_is_object() == 1):                                        
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        
                        self.m_loMap.set_addr(self,"loMap")
                        self.m_loMap.prepare_object()
                        
                        self.m_hiMap.set_addr(self,"hiMap")
                        self.m_hiMap.prepare_object()
                        
                self.xx_dbg("DBG_CfgRaidVol::prepare_object_internal::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_CfgRaidVol::print_object_internal::m_in::")
                self.prepare_object()
                self.xx_print_ptr("")

                if(self.xx_is_object() == 1):
                        self.xx_dbg("DBG_CfgRaidVol::print_object_internal::is_obj::")
                        self.m_fields.xx_print_fields("")
                        self.m_loMap.print_object()
                        self.m_hiMap.print_object()
                        
                        
                self.xx_dbg("DBG_CfgRaidVol::print_object_internal::m_out::")
                
