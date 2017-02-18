import sys
import os
from DBG_storagekd import *         
        

class DBG_proc:
	def __init__(self):                
		self.m_kd = DBG_storagekd("ffffe000ab937510","ffffe000ac52e1a0","ffffe000ac52e050")		
		self.m_kd.m_driver.xx_set_phy_addr("ffffe000ab937510")
		self.m_kd.m_adaext.xx_set_phy_addr("ffffe000ac52e1a0")
		self.m_kd.m_devobj.xx_set_phy_addr("ffffe000ac52e050")
		self.m_kd.m_unit.xx_set_phy_addr("ffffe000ac466650")
