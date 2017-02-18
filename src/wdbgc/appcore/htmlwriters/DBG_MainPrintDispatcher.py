import sys
import os
import logging
from ... appcore.filewriters.DBG_FileWriter import *
from ... appcore.logging.DBG_ExceptionPrinter import *
class DBG_MainPrintDispatcher:
	
	@staticmethod    
	def xx_print_raw_and_write_div(ss):
		try:
			print ss
			DBG_FileWriter().write_to_log("<div class='el-simple'>")
			DBG_FileWriter().write_to_log(ss)
			DBG_FileWriter().write_to_log("</div>")
		except:
			tt = "[DBG_MainPrintDispatcher::xx_print_ash::]"
			DBG_ExceptionPrinter.print_exception(tt + ss)			
												