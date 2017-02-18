import sys
import os
import ConfigParser
from ... appcore.logging.DBG_ExceptionPrinter import *
from ... appcore.config.DBG_Version import *
from ... appcore.config.DBG_PrintConfigData import *

class DBG_PrintConfig:
	
	m_data = None
	
	def getItem(self):
		try:
			if(self.__class__.m_data == None):
				self.__class__.m_data = DBG_PrintConfigData()				
			return self.__class__.m_data
		except:
				self.xx_exception("DBG_PrintConfig::getItem::excp::")
				return None
	
		
	def get_raid_targets_arr(self):
		try:
			self.xx_dbg("DBG_PrintConfig::get_raid_targets_arr::in")
			tt = self.getItem().m_raid_targets_arr
			self.xx_dbg("DBG_PrintConfig::get_raid_targets_arr::out::" + tt)
			return tt
		except:
				self.xx_exception("DBG_PrintConfig::get_raid_targets_arr::excp::")
		
	def set_raid_targets_arr(self,tt):
		try:
			self.getItem().m_raid_targets_arr = tt
		except:
				self.xx_exception("DBG_PrintConfig::set_raid_targets_arr::excp::")
			
	
	def get_version(self):
		try:
			self.xx_dbg("DBG_PrintConfig::get_version::in::")
			tt = self.getItem().m_version
			self.xx_dbg("DBG_PrintConfig::get_version::out::" + tt)
			return tt
		except:
				self.xx_exception("DBG_PrintConfig::get_version::excp::")
				return "15"
	
	
	def set_version(self,tt):
		try:
			self.getItem().m_version = tt
		except:
				self.xx_exception("DBG_PrintConfig::set_file::excp")
		
	def set_file(self,tt):
		try:
			self.getItem().m_file = tt
		except:
				self.xx_exception("DBG_PrintConfig::set_file::excp")
				
	def create_default_config(self):
		try:
			DBG_PrintConfigData().create_default_config()
		except:
				self.xx_exception("DBG_PrintConfig::get_version::excp::")
				
	def read_config(self):
		try:
			self.getItem().read_config()
		except:
				self.xx_exception("DBG_PrintConfig::get_version::excp::")
				
	def write_config(self):
		try:
			self.getItem().create_default_config()
		except:
				self.xx_exception("DBG_PrintConfig::get_version::excp::")
				
	def xx_dbg(self,tt):
		sinfo = ""		
		DBG_ExceptionPrinter.xx_dbg(sinfo + tt)
	
	def xx_exception(self,tt):
		sinfo = "["		
		DBG_ExceptionPrinter.print_exception(sinfo + tt)

				
		
	