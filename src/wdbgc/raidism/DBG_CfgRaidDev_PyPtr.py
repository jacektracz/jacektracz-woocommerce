import sys
import os
from .. DBG_AdapterBase import *
from .. raidism.DBG_IsmPathTargetLun import *
from .. raidism.DBG_CfgSerial import *
from .. appsrc.ismraid.DBG_RaidDev_PyPtr import *
from .. raidism.DBG_CfgRaidVol import *
from .. fields.DBG_FieldsMapper import *
class DBG_CfgRaidDev_PyPtr(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_CfgRaidDev_PyPtr::__init__::m_in::")
                self.xx_set_class_name ( "CfgRaidDev" )
                self.xx_set_full_class_name ( "iastora!CfgRaidDev" )
                self.m_ptl = DBG_IsmPathTargetLun("Parent::DBG_CfgRaidDev_PyPtr")
                self.m_serial = DBG_CfgSerial("Parent::DBG_CfgRaidDev_PyPtr")
                self.m_raidVol = DBG_CfgRaidVol("Parent::DBG_CfgRaidDev_PyPtr")
                self.m_fields = DBG_FieldsMapper("DBG_CfgRaidDev_PyPtr"
                                         ,self)
                self.m_fields.add_fields_int_array(
                        ["numSubVols"
                         ,"nvCacheDirty"
                         ,"myVolRaidDevNum"
                         ,"cacheEnabled"
                         ,"cacheReadPolicy"
                         ,"cacheWritePolicy"
                         ,"nvCachePolicy"
                         ,"numDataBlocks"
                         ,"postMigrCapacity"
                         ,"status"
                         ,"reservedBlocks"
                         ,"menuAction"
                         ,"actionArg"
                         ,"deletePending"
                         ,"updateNeeded"
                         ,"cfgStatus"
                         ,"clearPrtnTblMdr"
                         ,"cngState"
                         ,"cngSubState"
                         ,"cngMasterDiskNum"
                         ,"accessFsLogInProgress"
                         ,"scrubIoMdr"                         
                        ])
                self.xx_dbg("DBG_CfgRaidDev_PyPtr::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_CfgRaidDev_PyPtr::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_CfgRaidDev_PyPtr::prepare_object_internal::m_in::")
                if(self.xx_is_object() == 1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()                        
                        self.m_ptl.xx_inc_tabs(self);                
                        self.m_ptl.xx_compute_arr_phy_by_parent(self,"ptl")                        
                        
                        self.m_serial.xx_inc_tabs(self);
                        self.m_serial.xx_compute_arr_phy_by_parent(self,"serial")
                        self.m_raidVol.set_addr(self,"raidVol")
                        self.m_raidVol.prepare_object()
                        
                        
                self.xx_dbg("DBG_CfgRaidDev_PyPtr::prepare_object_internal::m_out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_IsmPathTargetLun::print_object")                        
                                                        
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_CfgRaidDev_PyPtr::print_object_internal::m_in::")
                self.prepare_object()
                if(self.xx_is_object() == 1):
                        self.xx_print_ptr("")
                        self.m_fields.print_object()
                        self.m_ptl.print_object()
                        self.m_serial.print_object()
                        self.m_raidVol.print_object()                        
                self.xx_dbg("DBG_CfgRaidDev_PyPtr::print_object_internal::m_out::")
