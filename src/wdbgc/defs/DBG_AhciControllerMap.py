import sys
import os
from .. DBG_AdapterBase import *
        
        
class DBG_AhciControllerMap(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_SrbFunctions::__init__::in::")
                self.xx_set_class_name ( "DBG_SrbFunctions" )
                self.xx_set_full_class_name ( "iastora!Wcdl::Chipset" )
                self.m_items = {}
                self.create_map()
                self.xx_dbg("DBG_Chipset::__init__::out")
                                
        def create_map(self):
                
                self.m_items = {}
                self.m_items[int(0x0)]='Unknown'
                self.m_items[int(0x2822)]='DESKTOP_SATA'
                self.m_items[int(0x282A)]='MOBILE_SATA'
                self.m_items[int(0x2826)]='SERVER_SATA'
                
                    # Ibex Peak (5 Series/3400 Series)
                self.m_items[int(0x3B22)]='DESKTOP_IBX_AHCI'
                self.m_items[int(0x3B23)]='DESKTOP_IBX_AHCI_4P'
                self.m_items[int(0x3B24)]='DESKTOP_IBX_PREM_RAID'
                self.m_items[int(0x3B25)]='DESKTOP_IBX_RAID'
                self.m_items[int(0x3B29)]='MOBILE_IBX_AHCI_4P'
                self.m_items[int(0X3B2B)]='MOBILE_IBX_PREM_RAID'
                self.m_items[int(0x3B2C)]='MOBILE_IBX_RAID'
                self.m_items[int(0x3B2F)]='MOBILE_IBX_AHCI'
                
                    # Cougar Point (6 Series/C200 Series)
                self.m_items[int(0x1C02)]='DESKTOP_CPT_AHCI'
                self.m_items[int(0x1C03)]='MOBILE_CPT_AHCI'
                self.m_items[int(0x1C04)]='DESKTOP_CPT_RAID'
                self.m_items[int(0x1C05)]='MOBILE_CPT_RAID'
                self.m_items[int(0x1C06)]='DESKTOP_CPT_PREM_RAID'
                self.m_items[int(0x1C07)]='MOBILE_CPT_PREM_RAID'
                
                    # Cougar Point Refresh (CPT-R) - not productized
                self.m_items[int(0x1C84)]='DESKTOP_CPTR_RAID'
                self.m_items[int(0x1C85)]='MOBILE_CPTR_RAID'
                self.m_items[int(0x1C86)]='DESKTOP_CPTR_PREM_RAID'
                self.m_items[int(0x1C87)]='MOBILE_CPTR_PREM_RAID'
                
                    # Panther Point (7 Series/C216)
                self.m_items[int(0x1E02)]='DESKTOP_PPT_AHCI'
                self.m_items[int(0x1E03)]='MOBILE_PPT_AHCI'
                self.m_items[int(0x1E04)]='DESKTOP_PPT_RAID'
                self.m_items[int(0x1E05)]='MOBILE_PPT_RAID'
                self.m_items[int(0x1E06)]='DESKTOP_PPT_PREM_RAID'
                self.m_items[int(0x1E07)]='MOBILE_PPT_PREM_RAID'
                self.m_items[int(0x1E0E)]='DESKTOP_PPT_Q75_RAID'
                
                    # Patsburg HEDT (X79)
                self.m_items[int(0x1D02)]='DESKTOP_PBG_AHCI'
                self.m_items[int(0x1D04)]='DESKTOP_PBG_RAID'
                self.m_items[int(0x1D06)]='DESKTOP_PBG_PREM_RAID'
                
                    # Lynxpoint
                self.m_items[int(0x8C02)]='DESKTOP_LPT_AHCI'
                self.m_items[int(0x8C03)]='MOBILE_LPT_AHCI'
                self.m_items[int(0x8C04)]='DESKTOP_LPT_RAID'
                self.m_items[int(0x8C05)]='MOBILE_LPT_RAID'
                self.m_items[int(0x8C06)]='DESKTOP_LPT_PREM_RAID'
                self.m_items[int(0x8C07)]='MOBILE_LPT_PREM_RAID'
                self.m_items[int(0x8C0E)]='DESKTOP_LPT_R1ONLY_RAID'
                self.m_items[int(0x8C0F)]='MOBILE_LPT_R1ONLY_RAID'
                
                    # Lynxpoint Refresh
                self.m_items[int(0x8C82)]='DESKTOP_LPT_R_AHCI'
                self.m_items[int(0x8C83)]='MOBILE_LPT_R_AHCI'
                self.m_items[int(0x8C84)]='DESKTOP_LPT_R_RAID'
                self.m_items[int(0x8C85)]='MOBILE_LPT_R_RAID'
                self.m_items[int(0x8C86)]='DESKTOP_LPT_R_PREM_RAID'
                self.m_items[int(0x8C87)]='MOBILE_LPT_R_PREM_RAID'
                self.m_items[int(0x8C8E)]='DESKTOP_LPT_R_R1ONLY_RAID'
                self.m_items[int(0x8C8F)]='MOBILE_LPT_R_R1ONLY_RAID'
                
                    # Lynx Point Low Power
                self.m_items[int(0x9C03)]='MOBILE_LPT_LP_AHCI'
                self.m_items[int(0x9C05)]='MOBILE_LPT_LP_RAID'
                self.m_items[int(0x9C07)]='MOBILE_LPT_LP_PREM_RAID'
                self.m_items[int(0x9C0F)]='MOBILE_LPT_LP_R1_RAID'
                
                    # Wellsburg HEDT (X99) RPIDs
                self.m_items[int(0x8D04)]='DESKTOP_WBG_RAID'
                self.m_items[int(0x8D06)]='DESKTOP_WBG_PREM_RAID'
                
                    # Wildcat Point Low Power
                self.m_items[int(0x9C87)]='MOBILE_WPT_LP_PREM_RAID'
                
                    # Sunrise Point Low Power (SPT-LP) RPIDs
                self.m_items[int(0x9D03)]='MOBILE_SPT_LP_AHCI'
                self.m_items[int(0x9D05)]='MOBILE_SPT_LP_RAID'
                self.m_items[int(0x9D07)]='MOBILE_SPT_LP_PREM_RAID'
                self.m_items[int(0x9D0F)]='MOBILE_SPT_LP_R1_RAID'
                
                    # Sunrise Point H (SPT-H) RPIDs
                self.m_items[int(0xA102)]='DESKTOP_SPT_H_AHCI'
                self.m_items[int(0xA103)]='MOBILE_SPT_H_AHCI'
                self.m_items[int(0xA105)]='DESKTOP_SPT_H_RAID'
                self.m_items[int(0xA106)]='DESKTOP_SPT_H_PREM_RAID2'
                self.m_items[int(0xA107)]='DESKTOP_SPT_H_PREM_RAID'
                self.m_items[int(0xA10F)]='DESKTOP_SPT_H_R1_RAID'
                
                    # August Ridge
                self.m_items[int(0xF1A5)]='AUG'


        def get_str(self, smb):
                try:
                        ik = int(smb,16)
                        return self.m_items[ik]
                except:
                        self.xx_exception("DBG_ACPI::print_object")
                        return "UNKNOWN DBG_AhciControllerMap:[" + str(smb) + "][" + str(len(self.m_items)) + "]"
        