import sys
import defines
import logging
from pykd import *
from defines import *
from proc_utils import *
from dbg_classess_utils import *
from .. helpers.DBG_Utils import  *

class DBG_ATA_IDENTIFY_DEVICE_DATA:
		
		def __init__(self):
				self.m_expr = "?? @@C++(((iastora!AtaDevice*)0x%s)->mIdentifyData)"
				self.m_ptr = ""
				self.m_obj_expr = ""
				
		def setPointer(self,p_ptr):
				self.m_ptr = p_ptr
				
		def createObjExpr(self):
				self.m_obj_expr = self.m_expr % self.m_ptr
				
		def printObj(self):
				try:                        
						self.printStr(".firmware_revision","Firmware",8)
						self.printStr(".serial_number","",20)
						self.printStr(".model_number","",40)
				except:
						print '=========================exception occured================='
						logging.exception('')
						print '==========================================================='
						return
				
		def getStrPtr(self,sident):
				s_expr_ptr = "@@C++((((iastora!AtaDevice*)0x" + self.m_ptr + ")->mIdentifyData)" + sident + ")"
				#print s_expr_ptr
				return s_expr_ptr
		
		def printStr(self,s_ident,s_comment,i_len):
				s_e = self.getStrPtr(s_ident)                
				s_val = DBG_Utils().xx_getAsStrEx(s_e,i_len)
				if s_comment == "":
						s_comment = s_ident
				
				self.printTabs(1, ""  + s_comment + ": "  + s_val);
				
		def printTabs(self,tbs,ss):
				if tbs == 0:
						print "\t\t\t" + ss
				if tbs == 1:
						print "\t\t\t\t" + ss

