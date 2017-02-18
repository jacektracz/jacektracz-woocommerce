import sys
import os
from ... appcore.memory.DBG_Utils import *
from ... appcore.memory.DBG_MemoryTools import *
from ... appcore.logging.DBG_Log import *
from ... appcore.htmlwriters.DBG_MainPrintDispatcher import *
class DBG_WdbgItemsPrinter:            
	
	def xx_print_link(self,sptr,stitle,stabs =""):
		try:
			DBG_Utils().xx_link(self.get_tabs_from_string(stabs),"?? " + sptr,stitle);
		except:
			DBG_Log().xx_exc("DBG_WdbgItemsPrinter::xx_print_enum:excp:")
					
	def get_tabs_from_string(self,st):
		try:
			return st
		except:			
			return "DBG_WdbgItemsPrinter::exc_get_tabs_from_string:"
		
	def get_tabs_from_int(self,st=0):
		try:
			sv= ""		
			for i in range(st):
				sv = sv + "\t"
			return sv
		except:			
			return "DBG_WdbgItemsPrinter::exc_get_tabs_from_int:"