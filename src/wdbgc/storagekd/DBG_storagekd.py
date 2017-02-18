import sys
import os
import logging

from .. DBG_MemoryPtr import *
from .. DBG_DriverObjectBase import *
from .. appcore.memory.DBG_Utils import *
from DBG_CheckEnv import *
from DBG_IADriver import *      
from DBG_AdapterEx import *
from DBG_DeviceObj import *
from DBG_Unit import *
                
class DBG_storagekd:
		def __init__(self, adriver, aext, adevobj):
			self.set_objects(adevobj,aext,adriver)

		def set_objects(self,  adevobj,aext, adriver):
			self.m_driver = DBG_IADriver()
			self.m_driver.xx_set_phy_addr(adriver)
            
			self.m_adaext = DBG_AdapterExt()
			self.m_adaext.xx_set_phy_addr(aext)
            
			self.m_devobj = DBG_DeviceObj()
			self.m_devobj.xx_set_phy_addr(adevobj)
    
			self.m_unit = DBG_Unit()
			self.m_unit.xx_set_phy_addr("")
                
		def xx_disp_adapters(self):
				DBG_Utils().xx_safe_exe('!storagekd.storadapter','Display adapters[II__1]')
                
		def xx_disp_adapter(self):
				self.m_adaext.xx_disp_adapter()
                
		def xx_disp_storloglist(self):
				self.m_devobj.xx_disp_storloglist()

		def xx_disp_unit(self):
				self.m_unit.xx_disp_unit()

		def xx_exec_test(self):
			self.xx_disp_adapters()
			self.xx_disp_storloglist()

		def xx_disp_adapter(self, pparent):
			try:
				self.xx_dbg("DBG_DriverObjectBase::xx_disp_adapter::in::")
				DBG_Utils().xx_safe_exe("!storagekd.storadapter " + pparent.xx_get_phy_addr("") + "","xx_dips_adapter")
				self.xx_dbg("DBG_DriverObjectBase::xx_disp_adapter::out::")
			except:
				self.xx_exception("DBG_DriverObjectBase::xx_print_link::exception::")
		
		def xx_disp_unit(self, pparent):
			try:
				DBG_Utils().xx_safe_exe("!storagekd.storunit " + pparent.xx_get_phy_addr("") + "","xx_dips_unit")
			except:
				self.xx_exception("DBG_DriverObjectBase::xx_print_link::exception::")
				
		def xx_disp_storloglist(self, pparent):
			try:
				self.xx_dbg("DBG_DriverObjectBase::xx_disp_storloglist")
				DBG_Utils().xx_safe_exe("!storagekd.storloglist " + pparent.xx_get_phy_addr("") + " 0 200 100",'SRB')
				self.xx_dbg("DBG_DriverObjectBase::xx_disp_storloglist::out::")
			except:
				self.xx_exception("DBG_DriverObjectBase::xx_print_link::exception::")

