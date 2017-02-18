import sys
import os

from appcore.memory.DBG_Utils import *
from DBG_MemoryPtr import *
from DBG_DriverObjectBase import *
#from fields.DBG_FieldsMapper import *
       
class DBG_AdapterBase(DBG_DriverObjectBase):
		def __init__(self,spar):                
			DBG_DriverObjectBase.__init__(self,spar)
			self.xx_set_class_name ( "_RAID_ADAPTER_EXTENSION" )

