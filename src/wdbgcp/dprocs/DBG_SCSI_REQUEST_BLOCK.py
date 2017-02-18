import sys
import defines
import logging
from pykd import *
from defines import *
from proc_utils import *
from dbg_classess_utils import *
from .. helpers.DBG_Utils import  *

class DBG_SCSI_REQUEST_BLOCK:
        
        def __init__(self, spointer, sfeature):                
                self.m_ptr = spointer
                self.m_feature = sfeature                                                
                
        def printObj(self):
                try:
                        DBG_Utils().xx_link('\t\t\t',"?? @@C++(((iastora!AtaDevice*)0x" + self.m_ptr + ")->" + self.m_feature +")",self.m_feature);                        
                except:
                        print '=========================exception occured================='
                        logging.exception('')
                        print '==========================================================='
                        return
                
        def getStrPtr(self,sident):                
                s_expr_ptr = "@@C++((((iastora!AtaDevice*)0x" + self.m_ptr + ")->" + self.m_feature + ")" + sident + ")"
                return s_expr_ptr
        
        def printStr(self, s_ident, s_comment, i_len):
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
