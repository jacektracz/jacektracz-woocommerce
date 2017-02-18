import sys
import os
from .. DBG_AdapterBase import *
        
        
class DBG_UnitControlMap(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_UnitControlMap::__init__::in::")
                self.xx_set_class_name ( "DBG_UnitControlMap" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DBG_UnitControlMap" )
                self.xx_dbg("DBG_UnitControlMap::__init__::out")
                self.unit_control_map = {}
                
        def create_map(self):            

            self.unit_control_map[0] = 'ScsiQuerySupportedUnitControlTypes'
            self.unit_control_map[1] = 'ScsiUnitUsage'
            self.unit_control_map[2] = 'ScsiUnitStart'
            self.unit_control_map[3] = 'ScsiUnitPower'
            self.unit_control_map[4] = 'ScsiUnitPoFxPowerInfo'
            self.unit_control_map[5] = 'ScsiUnitPoFxPowerRequired'
            self.unit_control_map[6] = 'ScsiUnitPoFxPowerActive'
            self.unit_control_map[7] = 'ScsiUnitPoFxPowerSetFState'
            self.unit_control_map[8] = 'ScsiUnitPoFxPowerControl'
            self.unit_control_map[9] = 'ScsiUnitRemove'
            self.unit_control_map[10] = 'ScsiUnitSurpriseRemoval'
            self.unit_control_map[11] = 'ScsiUnitControlMax'
            self.unit_control_map[0xffffffff] = 'MakeUnitControlTypeSizeOfUlong'

