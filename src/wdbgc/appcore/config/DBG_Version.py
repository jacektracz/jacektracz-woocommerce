import sys
import os
import ConfigParser
from ... appcore.logging.DBG_ExceptionPrinter import *

class DBG_Version:
	
	def __init__(self):
		self.m_ver = [15,0,0,1000]
		self.m_range = 4
		
	def self_is_above_or_equal(self, dd_v):
		self.xx_dbg("DBG_Version::self_is_above_or_equal::in::")
		is_ab = 1
		for ii in range(self.m_range):
			ii_c = self.m_ver[ii]
			ii_v = dd_v.m_ver[ii]
			if(ii_c < ii_v):
				is_ab = 0
				break
		self.xx_dbg("DBG_Version::self_is_above_or_equal::out::" + str(is_ab))			
		return is_ab
	
	def is_equal(self, dd_v):
		self.xx_dbg("DBG_Version::is_equal::in::")
		is_ab = 1
		for ii in range(self.m_range):
			ii_c = self.m_ver[ii]
			ii_v = dd_v.m_ver[ii]
			if(ii_c != ii_v):
				is_ab = 0
				break
		self.xx_dbg("DBG_Version::is_equal::out::" + str(is_ab))
		return is_ab
	
	
	def self_is_above(self, dd_v):
		self.xx_dbg("DBG_Version::self_is_above::in::")
		self_is_ab = 1
		for ii in range(self.m_range):
			ii_c = self.m_ver[ii]
			ii_v = dd_v.m_ver[ii]
			if(ii_c <= ii_v):
				self_is_ab = 0
				break
		self.xx_dbg("DBG_Version::self_is_above::out::" + str(self_is_ab))
		return self_is_ab
	
	def set_vv(self, ii , val):
		self.m_ver[ii] = val
	
	
	def xx_dbg(self,tt):
		sinfo = ""		
		DBG_ExceptionPrinter.xx_dbg(sinfo + str(tt))
	
	def xx_exception(self,tt):
		sinfo = "["		
		DBG_ExceptionPrinter.print_exception(sinfo + str(tt))
