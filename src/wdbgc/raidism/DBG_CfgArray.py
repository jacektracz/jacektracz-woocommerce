import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. raidism.DBG_CfgRaidDev_PyArray import *
from .. raidism.DBG_CfgDisk_PyArray import *
from .. raidism.DBG_CfgRaidDev import *
from .. raidism.DBG_CfgDisk import *
from .. appsrc.ismcfg.DBG_ArrayMpbMgr import *
from .. appsrc.ismbbm.DBG_BbmLogMgr import *

class DBG_CfgArray(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_CfgArray::__init__::m_in::")
                self.xx_set_class_name ( "CfgArray" )
                self.xx_set_full_class_name ( "iastora!CfgArray" )
                self.m_fields = DBG_FieldsMapper("DBG_CfgArray"
                                         ,self)
                
                self.m_fields.add_fields_int_array([
                        "numDisks"
                        ,"numRaidDevs"
                        ,"state"
                        ,"numFree"
                        ])
                
                self.m_cfgraiddevs = DBG_CfgRaidDev_PyArray("Parent::DBG_RaidCfgMgr")
                self.m_cfgraiddevs.xx_set_class_name ( "CfgArray" )
                self.m_cfgraiddevs.xx_set_full_class_name ( "iastora!CfgArray" )
                
                self.m_cfg_disks = DBG_CfgDisk_PyArray("Parent::DBG_RaidCfgMgr",self)
                self.m_cfg_disks.xx_set_class_name ( "CfgArray" )
                self.m_cfg_disks.xx_set_full_class_name ( "iastora!CfgArray" )
                self.m_cfg_disks.set_table_pointer("diskPtr")
                
                self.lastRaidDevMigrated = DBG_CfgRaidDev("DBG_CfgArray")
                
                self.failedDisk = DBG_CfgDisk("DBG_CfgArray")
                self.spareDisk = DBG_CfgDisk("DBG_CfgArray")
                self.mpbMgr = DBG_ArrayMpbMgr("DBG_CfgArray",self)
                self.bbmMgr  = DBG_BbmLogMgr("DBG_CfgArray",self)
                self.xx_dbg("DBG_CfgArray::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_CfgArray::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_CfgArray::prepare_object_internal::")
                if(self.xx_is_object()==1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        ird = self.m_fields.get_fields_int("numRaidDevs")
                        self.m_cfgraiddevs.set_addr(self,"SELF")
                        #self.m_cfgraiddevs.set_parent(self)
                        self.m_cfgraiddevs.set_range(ird)
                        self.m_cfgraiddevs.prepare_object()
                        
                        i_dsks = self.m_fields.get_fields_int("numDisks")
                        self.m_cfg_disks.set_parent(self)
                        self.m_cfg_disks.set_addr(self,"SELF")
                        self.m_cfg_disks.set_range(i_dsks)
                        self.m_cfg_disks.prepare_object()
                        
                        self.lastRaidDevMigrated.set_addr(self,"lastRaidDevMigrated")
                        self.lastRaidDevMigrated.prepare_object()
                        
                        self.failedDisk.set_addr(self,"failedDisk")
                        self.failedDisk.prepare_object()
                        
                        self.spareDisk.set_addr(self,"spareDisk")
                        self.spareDisk.prepare_object()
                        
                        self.spareDisk.set_addr(self,"spareDisk")
                        self.spareDisk.prepare_object()
                        
                        self.bbmMgr.set_addr(self,"bbmMgr")
                        self.bbmMgr.prepare_object()
                        
                self.xx_dbg("DBG_CfgArray::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_CfgArray::print_object::m_in::")
                self.prepare_object()
                self.xx_print_ptr("")
                
                if(self.xx_is_object()==1):
                        self.m_fields.xx_print_fields("")
                        self.m_cfgraiddevs.print_object()
                        self.m_cfg_disks.print_object()
                        self.lastRaidDevMigrated.print_object()
                        self.failedDisk.print_object()
                        self.spareDisk.print_object()
                        self.mpbMgr.print_object()
                        self.bbmMgr.print_object()
                        
                        #self.mApstTable.print_object()
                self.xx_dbg("DBG_CfgArray::print_object::m_out::")
