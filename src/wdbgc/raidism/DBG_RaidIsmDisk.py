import sys
import os
from .. DBG_AdapterBase import *

from .. fields.DBG_FieldsMapper import *
from .. raidism.DBG_IsmPathTargetLun import *
from .. appcore.config.DBG_PrintConfig import *
from .. appsrc.ismcfg.DBG_MemberDiskReq import *
from .. appsrc.ismcfg.DBG_MemberDiskReqList_PyList import *
from .. appsrc.ismbbm.DBG_BbmIntvlTree import *

class DBG_RaidIsmDisk(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_RaidIsmDisk::__init__::in::")
                self.xx_set_class_name ( "Disk" )
                self.xx_set_full_class_name ( "iastora!Disk" )
                self.m_ptl = DBG_IsmPathTargetLun("Parent::DBG_RaidIsmDisk")
                
                self.m_fields = DBG_FieldsMapper("DBG_RaidIsmDisk"
                                         ,self)
                
                self.m_fields.add_fields_int_array([
                        "scsiId"
                        ,"totalBlocks"
                        ,"numOwners"
                        ,"maxByteCount"
                        ,"maxFragCount"
                        ,"blockByteSize"
                        ,"physBlockByteSize"
                        ,"diskRPM"
                        ,"trimSupported"
                        ,"lbprzSupported"
                        ,"logBlockOffset"
                        ,"puisSupported"
                        ,"puisEnabled"
                        ,"diskInStandby"
                        ,"securityEnabled"                        
                        ,"detStatus"
                        ,"reqStatus"
                        ,"status"
                        ,"totalBlocks"
                        ,"deleted"
                        ,"removePending"
                        ,"minHdmDevIoCount"
                        ,"pendingMdrCount"
                        ,"mdrPriQueueSize"
                        ,"ascendingSort"
                        ,"diskIoReqsSuspended"
                        ,"deferringDiskIo"
                        ,"lastLbaAccessed"
                        ,"firstAvailableLba"
                        ,"partitionType"
                        ,"mNumPartitionsOnDisk"
                        ,"DiskAttributes"                        
                        ])
                
                if(DBG_PrintConfig().getItem().self_is_above_or_equal( 15 ) == 1):
                        self.m_fields.add_fields_int_array([
                                "claimable"])
                
                self.m_fields.add_fields_str("VendorInfo",16)
                self.m_fields.add_fields_str("ProductInfo",16)
                self.m_fields.add_fields_str("Description",16)
                self.m_fields.add_fields_str("ProductRevLevel",8)
                self.m_fields.add_fields_str("serialNum",16)
                self.readMpbMdr  = DBG_MemberDiskReq("",self)
                self.writeMpbMdr  = DBG_MemberDiskReq("",self)
                self.powerMgmtMdr   = DBG_MemberDiskReq("",self)
                self.spareTestMdr   = DBG_MemberDiskReq("DBG_RaidIsmDisk",self)
                self.writeCacheMdr   = DBG_MemberDiskReq("DBG_RaidIsmDisk",self)
                self.puisMdr   = DBG_MemberDiskReq("DBG_RaidIsmDisk",self)
                self.smartAttributesMdr   = DBG_MemberDiskReq("DBG_RaidIsmDisk",self)
                self.lastSioIssued   = DBG_MemberDiskReq("DBG_RaidIsmDisk",self)
                
                self.mdrFifo = DBG_MemberDiskReqList_PyList("DBG_RaidIsmDisk",self)
                self.mdrPriQueue  = DBG_MemberDiskReqList_PyList("DBG_RaidIsmDisk",self)
                self.bbmTree = DBG_BbmIntvlTree("DBG_RaidIsmDisk",self)
                
                self.m_handle_mdrFifo = 0
                self.xx_dbg("DBG_RaidIsmDisk::__init__::in::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_RaidIsmDisk::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_RaidIsmDisk::prepare_object::")
                if(self.xx_is_object() == 1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        self.m_ptl.set_addr_arr(self,"ptl")
                        self.m_ptl.prepare_object()
                        
                        self.readMpbMdr.set_addr(self,"readMpbMdr")
                        self.writeMpbMdr.set_addr(self,"writeMpbMdr")
                        self.powerMgmtMdr .set_addr(self,"powerMgmtMdr")
                        self.spareTestMdr.set_addr(self,"spareTestMdr")
                        self.writeCacheMdr.set_addr(self,"writeCacheMdr")
                        self.puisMdr.set_addr(self,"puisMdr")
                        self.smartAttributesMdr.set_addr(self,"smartAttributesMdr")
                        self.lastSioIssued.set_addr(self,"lastSioIssued")
                        
                        self.readMpbMdr.prepare_object()
                        self.writeMpbMdr.prepare_object()
                        self.powerMgmtMdr .prepare_object()
                        self.spareTestMdr.prepare_object()
                        self.writeCacheMdr.prepare_object()
                        self.puisMdr.prepare_object()
                        self.smartAttributesMdr.prepare_object()
                        self.lastSioIssued.prepare_object()
                        if(DBG_PrintConfig().getItem().m_handle_mdrFifo==1):
                                self.mdrFifo.set_addr_arr(self,"mdrFifo")
                                self.mdrFifo.prepare_object()
                        
                                self.mdrPriQueue.set_addr_arr(self,"mdrFifo")
                                self.mdrPriQueue.prepare_object()
                                
                        self.bbmTree.set_addr(self,"bbmTree")
                        self.bbmTree.prepare_object()
                        
                self.xx_dbg("DBG_RaidIsmDisk::prepare_object::out::")
                
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self,sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,pparent,sdbg=""):

                self.xx_dbg("DBG_RaidIsmDisk::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):
                        gb = self.get_blocks("totalBlocks")
                        self.m_fields.add_raw_str("GB:" + str(gb))
                        self.m_fields.xx_print_fields("")                        
                        self.m_ptl.print_object()
                        self.readMpbMdr.print_object()
                        self.writeMpbMdr.print_object()
                        self.powerMgmtMdr .print_object()
                        self.spareTestMdr.print_object()
                        self.writeCacheMdr.print_object()
                        self.puisMdr.print_object()
                        self.smartAttributesMdr.print_object()
                        self.lastSioIssued.print_object()
                        self.bbmTree.print_object()
                        
                        if(DBG_PrintConfig().getItem().m_handle_mdrFifo==1):
                                self.mdrFifo.print_object()
                                self.mdrPriQueue.print_object()
                                
                self.xx_dbg("DBG_RaidIsmDisk::print_object_internal::out::")                        
                        
        def get_blocks(self,pvar):
                try:
                        blocks = self.m_fields.get_fields_int(pvar)
                        gb = (blocks*512)/(1024*1024*1024)
                        dd = str(gb)
                        self.xx_dbg("DBG_DiskIdentityData::get_blocks::out::" + str(dd))
                        return dd
                except:
                        self.xx_exception("DBG_DiskIdentityData::print_object::m_blocks::")                        
                        return "-1"
                
        def get_class_str(self):
                self.xx_dbg("DBG_RaidIsmDisk::get_class_str::")
                
                ccstr = """
                """
                
                self.xx_dbg("DBG_RaidIsmDisk::get_class_str::")
