import sys
import os
from .. DBG_AdapterBase import *
from .. raidism.DBG_CfgSerial import *
from .. raidism.DBG_RaidIsmDisk import *
from .. appsrc.ismcfg.DBG_DiskMpbMgr import *
from .. raidism.DBG_CfgSerial import *
class DBG_CfgDisk(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_CfgDisk::__init__::m_in::")
                self.xx_set_class_name ( "CfgDisk" )
                self.xx_set_full_class_name ( "iastora!CfgDisk" )
                self.m_serial = DBG_CfgSerial("Parent::DBG_CfgDisk")
                
                self.m_cldev = DBG_RaidIsmDisk("Parent::DBG_CfgDisk")
                self.mpbMgr = DBG_DiskMpbMgr("DBG_CfgDisk",self)
                self.serial = DBG_CfgSerial("DBG_CfgDisk_Ex")
                self.xx_dbg("DBG_CfgDisk::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_CfgDisk::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_CfgDisk::prepare_object_internal::m_in::")
                if(self.xx_is_object() == 1):                
                        
                        self.m_serial.set_addr_arr(self,"serial")
                        self.m_serial.prepare_object()
                        
                        self.m_cldev.set_addr(self,"cldev")
                        self.m_cldev.prepare_object()
                        
                        self.mpbMgr.set_addr(self,"mpbMgr")
                        self.mpbMgr.prepare_object()                        
                
                        self.serial.set_addr_arr(self,"serial")
                        self.serial.prepare_object()                        
                
                self.xx_dbg("DBG_CfgDisk::prepare_object_internal::m_out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")                        
                        self.print_object_internal(self)
                        self.xx_print_end("")                        
                except:
                        self.xx_exception("DBG_CfgSerial::print_object")                        
                                                        
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_CfgDisk::print_object_internal::m_in::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):                        
                        self.m_serial.print_object()
                        self.m_cldev.print_object()
                        self.mpbMgr.print_object()
                        self.serial.print_object()       
                self.xx_dbg("DBG_CfgDisk::print_object_internal::m_out::")
