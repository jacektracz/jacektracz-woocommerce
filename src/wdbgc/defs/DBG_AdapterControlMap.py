import sys
import os
from .. DBG_AdapterBase import *
        
        
class DBG_AdapterControlMap(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_AdapterControlMap::__init__::in::")
                self.xx_set_class_name ( "DBG_AdapterControlMap" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DBG_AdapterControlMap" )
                self.xx_dbg("DBG_AdapterControlMap::__init__::out")
                self.adapter_control_map = {}
                
        def create_map(self):            

            
            self.adapter_control_map[0] = 'ScsiQuerySupportedControlTypes'
            self.adapter_control_map[1] = 'ScsiStopAdapter'
            self.adapter_control_map[2] = 'ScsiRestartAdapter'
            self.adapter_control_map[3] = 'ScsiSetBootConfig'
            self.adapter_control_map[4] = 'ScsiSetRunningConfig'
            self.adapter_control_map[5] = 'ScsiPowerSettingNotification'
            self.adapter_control_map[6] = 'ScsiAdapterPower'
            self.adapter_control_map[7] = 'ScsiAdapterPoFxPowerRequired'
            self.adapter_control_map[8] = 'ScsiAdapterPoFxPowerActive'
            self.adapter_control_map[9] = 'ScsiAdapterPoFxPowerSetFState'
            self.adapter_control_map[10] = 'ScsiAdapterPoFxPowerControl'
            self.adapter_control_map[11] = 'ScsiAdapterPrepareForBusReScan'
            self.adapter_control_map[12] = 'ScsiAdapterSystemPowerHints'
            self.adapter_control_map[13] = 'ScsiAdapterFilterResourceRequirements'
            self.adapter_control_map[14] = 'ScsiAdapterPoFxMaxOperationalPower'
            self.adapter_control_map[15] = 'ScsiAdapterPoFxSetPerfState'
            self.adapter_control_map[16] = 'ScsiAdapterSurpriseRemoval'
            self.adapter_control_map[17] = 'ScsiAdapterControlMax'
            self.adapter_control_map[0xffffffff] = 'MakeAdapterControlTypeSizeOfUlong'

