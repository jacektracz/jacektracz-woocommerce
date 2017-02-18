import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *

class DBG_RaidDiskIdentityData(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_DiskIdentityData::__init__::m_in::")
                self.xx_set_class_name ( "_DiskIdentityData" )
                self.xx_set_full_class_name ( "iastora!_DiskIdentityData" )
                self.m_fields = DBG_FieldsMapper("DBG_RaidDiskIdentityData",self)
                
                self.gb = 0
                #self.mApstTable = DBG_ApstTable("Parent::DBG_DiskIdentityData")
                self.xx_dbg("DBG_DiskIdentityData::__init__::m_out::")
               
        def init_object_fields(self):
                self.xx_dbg("DBG_RaidDiskIdentityData::init_object_fields::method_in::")                
                lunh = DBG_PrintConfig().getItem().m_is_handled_lun
                self.m_fields.add_fields_str("Description",16)
                self.m_fields.add_fields_str("VendorInfo",40)
                self.m_fields.add_fields_str("ProductInfo",16)
                self.m_fields.add_fields_str("SerialNumber",20)                
                self.m_fields.add_fields_str("ProductRevLevel",8)
                
                if(DBG_PrintConfig().getItem().m_is_handled_lun == 1):
                        #self.m_fields.add_fields_str("NvmeSerialNumber",20)
                        self.m_fields.add_fields_int_array([
                                "Lun"
                                ])
                        
                self.m_fields.add_fields_int_array([
                        "PathId"
                        ,"TargetId"                        
                        ,"LINE"])
                
                self.m_fields.add_fields_int_array([
                        "claimAble"
                        ,"maxByteCount"
                        ,"TotalBlocks"
                        ,"PhysicalLocation"
                        ,"LogicalSectorByteSize"
                        ,"PhysicalSectorByteSize"
                        ,"LogicalSectorOffset"
                        ,"DiskRPM"])
                self.xx_dbg("DBG_RaidDiskIdentityData::init_object_fields::method_out::")
               
        def prepare_object(self):                
                self.xx_dbg("DBG_DiskIdentityData::prepare_object::m_in::")
                self.init_object_fields()
                self.clear_messages()
                if(self.is_valid_object() == 1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                else:
                        self.add_message("disk_id_is_not_valid")                        
                        
                self.xx_dbg("DBG_DiskIdentityData::prepare_object::m_out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self):
                self.xx_dbg("DBG_DiskIdentityData::print_object::m_in::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.is_valid_object() == 1):
                        gb = self.get_gb("TotalBlocks")
                        self.m_fields.add_raw_str("GB:" +str(gb))
                        self.m_fields.xx_print_fields("")                                
                self.xx_dbg("DBG_DiskIdentityData::print_object::m_out::")
                        
        def get_gb(self,pvar):
                try:
                        self.xx_dbg("DBG_DiskIdentityData::get_gb::")        
                        blocks = self.m_fields.get_fields_int(pvar)
                        gb = (blocks*512)/(1024*1024*1024)
                        self.xx_dbg("DBG_DiskIdentityData::get_gb::")        
                        return gb
                except:
                        self.xx_exception("DBG_DiskIdentityData::print_object::m_blocks::")
                        self.xx_dbg("DBG_DiskIdentityData::print_object::m_blocks::")
                        return 0
                
        def get_class_str(self):
                self.xx_dbg("DBG_DiskIdentityData::get_class_str::m_in::")
                cs = """
"""
                self.xx_dbg("DBG_DiskIdentityData::get_class_str::m_out::")
                
        def is_valid_object(self):
                self.xx_dbg("DBG_DiskIdentityData::is_valid_object::m_in::")
                is_c = 1
                if(is_c == 1):
                        is_c = self.xx_check_str(self,"Description",16)
                        
                if(is_c == 1):
                        is_c = self.xx_check_str(self,"SerialNumber",20)
                
                if(is_c == 1):
                        is_c = self.xx_check_str(self,"ProductInfo",16)
                        
                if(is_c == 1):
                        is_c = self.xx_check_str(self,"ProductRevLevel",8)
                        
                if(is_c == 1):
                        is_c = self.xx_check_str(self,"VendorInfo",40)
                        
                if(is_c == 1):        
                        is_c = self.xx_is_object()
                        
                self.xx_dbg("DBG_DiskIdentityData::is_valid_object::m_out::" + str(is_c))
                return is_c
                
                