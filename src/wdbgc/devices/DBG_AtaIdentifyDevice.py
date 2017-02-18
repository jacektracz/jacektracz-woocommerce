import sys
import os

from .. DBG_AdapterBase import *

#from .. nvme.DBG_AdminIdentifyControllerData import *
from .. fields.DBG_FieldsMapper import *
class DBG_AtaIdentifyDevice(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_AtaIdentifyDevice::__init__::in::")
                self.xx_set_class_name ( "_ATA_IDENTIFY_DEVICE" )
                self.xx_set_full_class_name ( "iastora!_ATA_IDENTIFY_DEVICE" )
                self.m_fields = DBG_FieldsMapper("DBG_AtaIdentifyDevice"
                                         ,self)                                
                
                self.create_init()
                #self.mIdentifyControllerData = DBG_AdminIdentifyControllerData("Parent::DBG_DriverTemplate2")
                self.xx_dbg("DBG_AtaIdentifyDevice::__init__::in::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_AtaIdentifyDevice::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_AtaIdentifyDevice::prepare_object::")
                self.m_fields.set_fields_parent(self)
                #self.mIdentifyControllerData.xx_inc_tabs(self);                
                #self.mIdentifyControllerData.xx_compute_arr_phy_by_parent(self,"mIdentifyControllerData")

                self.xx_dbg("DBG_AtaIdentifyDevice::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def create_init(self):
                try:
                        #self.m_fields.add_fields_int_array(["mPathId","mTargetId","mLun"])
                        self.m_fields.add_fields_str("model_number",40)
                        self.m_fields.add_fields_str("firmware_revision",8)
                        self.m_fields.add_fields_str("serial_number",20)
                except:
                        self.xx_exception("DBG_AtaIdentifyDevice::print_object")
                
                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_AtaIdentifyDevice::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                self.m_fields.xx_print_fields("")
                #if(self.mIdentifyControllerData.xx_is_object()):
                #        self.mIdentifyControllerData.print_object()
                self.xx_dbg("DBG_AtaIdentifyDevice::print_object_internal::out::")                        
                        
                
        def get_class_str(self):
                self.xx_dbg("DBG_AtaIdentifyDevice::get_class_str::")
                
                ccstr = """
struct _ATA_IDENTIFY_DEVICE * 0xffffe000`9e1da62a
   +0x000 general_config   : _ATA_IDENTIFY_DEVICE::<unnamed-type-general_config>
   +0x002 obsolete         : 0x3fff
   +0x004 specific_config  : 0xc837
   +0x006 obsolete1        : 0x10
   +0x008 retired1         : [2] 0
   +0x00c obsolete2        : 0x3f
   +0x00e reserved_for_compact_flash1 : [2] 0
   +0x012 retired0         : 0
   +0x014 serial_number    : [20]  "    W -DCWWA53082354"
   +0x028 retired2         : [2] 0
   +0x02c obsolete4        : 0x32
   +0x02e firmware_revision : [8]  "100.V120"
   +0x036 model_number     : [40]  "DW CDW0130BFXY0-Y1B7 1                  "
   +0x05e max_sectors_per_multiple : 0x8010
   +0x060 tcgFeatureOptions : _ATA_IDENTIFY_DEVICE::<unnamed-type-tcgFeatureOptions>
   +0x062 capabilities     : _ATA_IDENTIFY_DEVICE::<unnamed-type-capabilities>
   +0x066 obsolete5        : [2] 0
   +0x06a validity_bits    : 7
   +0x06c obsolete6        : [5] 0x3fff
   +0x076 current_max_sectors_per_multiple : 0x100
   +0x078 total_num_sectors : [4]  "???"
   +0x07c obsolete7        : 0
   +0x07e multi_word_dma_mode : 7
   +0x080 pio_modes_supported : 3
   +0x082 min_multiword_dma_transfer_cycle : 0x78
   +0x084 rec_min_multiword_dma_transfer_cycle : 0x78
   +0x086 min_pio_transfer_no_flow_ctrl : 0x78
   +0x088 min_pio_transfer_with_flow_ctrl : 0x78
   +0x08a additional_supported : _ATA_IDENTIFY_DEVICE::<unnamed-type-additional_supported>
   +0x08c reserved1        : 0
   +0x08e reserved2        : [4] 0
   +0x096 queue_depth      : 0y11111 (0x1f)
   +0x096 reserved_word_75 : 0y00000000000 (0)
   +0x098 serial_ata_capabilities : _ATA_IDENTIFY_DEVICE::<unnamed-type-serial_ata_capabilities>
   +0x09c serial_ata_features_supported : _ATA_IDENTIFY_DEVICE::<unnamed-type-serial_ata_features_supported>
   +0x09e serial_ata_features_enabled : _ATA_IDENTIFY_DEVICE::<unnamed-type-serial_ata_features_enabled>
   +0x0a0 major_version_number : 0x1fe
   +0x0a2 minor_version_number : 0
   +0x0a4 command_set_supported : _ATA_IDENTIFY_DEVICE::<unnamed-type-command_set_supported>
   +0x0aa command_set_enabled : _ATA_IDENTIFY_DEVICE::<unnamed-type-command_set_enabled>
   +0x0b0 ultra_dma_mode   : 0x407f
   +0x0b2 normal_security_erase_unit : _ATA_IDENTIFY_DEVICE::<unnamed-type-normal_security_erase_unit>
   +0x0b4 enhanced_security_erase_unit : _ATA_IDENTIFY_DEVICE::<unnamed-type-enhanced_security_erase_unit>
   +0x0b6 current_power_mgmt_value : 0x80
   +0x0b8 master_password_revision : 0xfffe
   +0x0ba hardware_reset_result : 0
   +0x0bc current_acoustic_management_value : 0
   +0x0be stream_min_request_size : 0
   +0x0c0 stream_transfer_time : 0
   +0x0c2 stream_access_latency : 0
   +0x0c4 stream_performance_granularity : [2] 0
   +0x0c8 max_48bit_lba    : [8]  "???"
   +0x0d0 streaming_transfer_time : 0
   +0x0d2 max_lba_range_entry_blocks : 0
   +0x0d4 physical_logical_sector_size : _ATA_IDENTIFY_DEVICE::<unnamed-type-physical_logical_sector_size>
   +0x0d6 acoustic_test_interseek_delay : 0
   +0x0d8 world_wide_name  : [8]  "???"
   +0x0e0 reserved_for_wwn_extention : [8]  ""
   +0x0e8 reserved4        : 0
   +0x0ea words_per_logical_sector : [4]  ""
   +0x0ee command_set_supported2 : _ATA_IDENTIFY_DEVICE::<unnamed-type-command_set_supported2>
   +0x0f0 reserved5        : [7] 0x401c
   +0x0fe removable_media_status : 0
   +0x100 security_status  : _ATA_IDENTIFY_DEVICE::<unnamed-type-security_status>
   +0x102 vendor_specific1 : [31] 0x400
   +0x140 cfa_power_mode1  : 0
   +0x142 reserved_for_compact_flash2 : [7] 0
   +0x150 device_nominal_form_factor : 0
   +0x152 data_set_management : 0
   +0x154 reserved_for_compact_flash3 : [6] 0
   +0x160 current_media_serial_number : [30] 0
   +0x19c reserved6        : [3] 0x303f
   +0x1a2 logical_sector_alignment : 0
   +0x1a4 reserved7        : [7] 0
   +0x1b2 nominal_media_rotation_rate : 0x1c20
   +0x1b4 reserved8        : [16] 0
   +0x1d4 min_num_blocks_per_microcode : 1
   +0x1d6 max_num_blocks_per_microcode : 0x1000
   +0x1d8 reserved9        : [19] 0
   +0x1fe integrity_word   : 0xaba5
                
"""
                self.xx_dbg("DBG_AtaIdentifyDevice::get_class_str::")
