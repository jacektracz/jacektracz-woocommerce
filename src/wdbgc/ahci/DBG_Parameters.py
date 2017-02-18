import sys
import os

from .. DBG_AdapterBase import *
from .. appcore.config.DBG_PrintConfig import *
#from .. nvme.DBG_AdminIdentifyControllerData import *
from .. fields.DBG_FieldsMapper import *
class DBG_Parameters(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_Parameters::__init__::in::")
                self.xx_set_class_name ( "Parameters" )
                self.xx_set_full_class_name ( "iastora!Parameters" )
                self.m_fields = DBG_FieldsMapper("DBG_Parameters"
                                         , self)
                self.create_init()
                #self.mIdentifyControllerData = DBG_AdminIdentifyControllerData("Parent::DBG_DriverTemplate2")
                
                self.xx_dbg("DBG_Parameters::__init__::in::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_Parameters::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_Parameters::prepare_object::")
                self.m_fields.set_fields_parent(self)
                #self.mIdentifyControllerData.xx_inc_tabs(self);                
                #self.mIdentifyControllerData.xx_compute_arr_phy_by_parent(self,"mIdentifyControllerData")

                self.xx_dbg("DBG_Parameters::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.print_object_internal(self)
                except:
                        self.xx_exception("DBG_Parameters::print_object")
                        
        def create_init(self):
                try:
                        if(DBG_PrintConfig().getItem().m_print_miniport_params == "1"):
                                self.create_array_ports_info()
                                
                        self.m_fields.add_fields_int_array(
                                ["WriteCache","ZpoddEnabled","DmaSetupAutoActivate"])
                        
                except:
                        self.xx_exception("DBG_Parameters::print_object")
                
        def create_array_ports_info(self):
                
                try:
                        self.m_fields.set_fields_parent(self)
                        self.xx_dbg("DBG_Parameters::create_array_ports_info::in::")
                        
                        for ii_pp in range(6):
                                self.m_fields.add_fields_int("ANEnable[" + str(ii_pp) +"]")
                                self.m_fields.add_fields_int("HIPM[" + str(ii_pp) +"]")
                                self.m_fields.add_fields_int("DIPM[" + str(ii_pp) +"]")
                                self.m_fields.add_fields_int("SIPM[" + str(ii_pp) +"]")
                                self.m_fields.add_fields_int("LPMState[" + str(ii_pp) +"]")
                                self.m_fields.add_fields_int("LPMDState[" + str(ii_pp) +"]")
                                self.m_fields.add_fields_int("GTF[" + str(ii_pp) +"]")
                                self.m_fields.add_fields_int("ASREnable[" + str(ii_pp) +"]")
                                self.m_fields.add_fields_int("DevSlp[" + str(ii_pp) +"]")
                                #self.m_fields.add_fields_int("DevSlpMDAT[" + str(ii_pp) +"]")
                                self.m_fields.add_fields_int("CsDeviceNotification[" + str(ii_pp) +"]")
                                #self.m_fields.add_fields_int("EnterCsApmLevel[" + str(ii_pp) +"]")
                                #self.m_fields.add_fields_int("ExitCsApmLevel[" + str(ii_pp) +"]")
                                
                                self.m_fields.add_fields_int("LINE")
                                
                        self.xx_dbg("DBG_Parameters::create_array_ports_info::out::")
                        
                except:
                        self.xx_exception("DBG_Parameters::print_object")

                
        def print_object_internal(self,pparent):
                self.xx_dbg("DBG_Parameters::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                self.m_fields.xx_print_fields("")
                #if(self.mIdentifyControllerData.xx_is_object()):
                #        self.mIdentifyControllerData.print_object()
                self.xx_dbg("DBG_Parameters::print_object_internal::out::")                        
                        
                
        def get_class_str(self):
                self.xx_dbg("DBG_Parameters::get_class_str::")
                
                ccstr = """
struct _Parameters * 0xffffe000`5bfcf668
   +0x000 NCQEnable        : 1
   +0x004 SurpriseRemovalOk : [6] 0xffffffff
   +0x01c ANEnable         : [6] 1
   +0x034 HIPM             : [6] 1
   +0x04c DIPM             : [6] 1
   +0x064 SIPM             : [6] 0x4b
   +0x07c LPMState         : [6] 0
   +0x094 LPMDState        : [6] 1
   +0x0ac GTF              : [6] 1
   +0x0c4 ASREnable        : [6] 1
   +0x0dc DevSlp           : [6] 1
   +0x0f4 DevSlpMDAT       : [6] 0xffffffff
   +0x10c DevSlpDETO       : [6] 0xffffffff
   +0x124 DevSlpDITO       : [6] 0xffffffff
   +0x13c DevSlpDITOsmall  : [6] 0xffffffff
   +0x154 DevSlpDeviceOverride : [6] 0
   +0x16c CsDeviceNotification : [6] 1
   +0x184 EnterCsApmLevel  : [6] 0xffffffff
   +0x19c ExitCsApmLevel   : [6] 0xffffffff
   +0x1b4 CsDeviceSleepIdleTimeoutInMS : DeviceSerialValueArr
   +0x730 DeviceSleepIdleTimeoutInMS : DeviceSerialValueArr
   +0xcac DeviceSleepExitTimeoutInMS : DeviceSerialValueArr
   +0x1228 MinimumDeviceSleepAssertionTimeInMS : DeviceSerialValueArr
   +0x17a4 FullApsHandling  : 0
   +0x17a8 FUAEnable        : 0
   +0x17ac DLAE             : 1
   +0x17b0 AutoPartialSlumber : 0xffffffff
   +0x17b4 AdvancedPowerManagment : 0xffffffff
   +0x17b8 EnableAutoPartialSlumberOverride : 0
   +0x17bc OverrideTrimSupport : 0
   +0x17c0 MediaStatusNotification : 0
   +0x17c4 WriteCache       : 1
   +0x17c8 DmaSetupAutoActivate : 1
   +0x17cc ZpoddEnabled     : 1
   +0x17d0 ZpoddIdleTimeout : 0x3c
   +0x17d4 IgnoreFua        : 1
   +0x17d8 DeviceSleep      : 1
   +0x17dc DeviceSleepCs    : 1
   +0x17e0 DeviceSleepBiosConfig : 0xffffffff
   +0x17e4 AoacTimeout      : 0x1e
   +0x17e8 HybridHintingDisabled : 0
   +0x17ec HybridHintSkuOverride : 0
   +0x17f0 HybridHintReset  : 0xffffffff
   +0x17f4 HiberFileHintDisable : 0
"""
                self.xx_dbg("DBG_Parameters::get_class_str::")
