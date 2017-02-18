import sys
import os
from .. DBG_AdapterBase import *
        
        
class DBG_SataDeviceConsts(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_SataDeviceConst::__init__::in::")
                self.xx_set_class_name ( "DBG_SrbFunctions" )
                self.xx_set_full_class_name ( "iastora!Wcdl::Chipset" )
                self.xx_dbg("DBG_SataDeviceConst::__init__::out")

                self.SataDeviceTypeInvalid = '0'
                self.SataDeviceTypeAta = '100'
                self.SataDeviceTypeAtaUltraLowPower =  '200'
                self.SataDeviceTypeAtaHybrid = '400'
                self.SataDeviceTypeAtaPuis = '800'
                self.SataDeviceTypeAtapi = '1000'
                self.SataDeviceTypeAtapiZpodd = '2000'
                
        def create_map(self):            
            ""
            
