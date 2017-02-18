import sys
import defines
import logging
from pykd import *
from defines import *
from proc_utils import *
from dbg_classess_utils import *
from .. helpers.DBG_Utils import * 
                
class DBG_PORT_CONFIGURATION_INFORMATION:
        
        def __init__(self, spointer, sindex, sfeature):
                self.m_ptr = spointer
                self.m_port = sindex
                self.m_tabs = '\t';
                
                self.m_feature = "mConfigInfo"
                self.m_obj_access = "->"
                
        def setTabs(self,ptabs):
                self.m_tabs = ptabs;
                
        def printObj(self):
                try:
                        s_e = "@@C++(" + self.getObjPtr() + ")"
                        DBG_Utils().xx_link(self.m_tabs,"?? " + s_e ,"PORT_CONFIGURATION_INFORMATION")
                        
                except:
                        print '=========================exception occured================='
                        logging.exception('')
                        print '==========================================================='
                        return
                
        def getBaseAddr(self):
                s_expr_ptr = "((iastora!RemapPort*)iastora!g_raidport->mDriver->mDeviceExtensionList[" + str(self.m_port) + "])"
                
                return s_expr_ptr
        
        def getObjPtr(self):
                s_expr_ptr = "((" +self.getBaseAddr() + ")" + self.m_obj_access + "" + self.m_feature + ")"
                return s_expr_ptr
                
        def getFieldPtr(self,sident):
                s_expr_ptr = "((" +self.getObjPtr() + ")" + sident + ")"
                return s_expr_ptr
        
        def printStr(self,s_ident,s_comment,i_len):                
                s_e = "@@C++(" + self.getFieldPtr(s_ident) + ")"               
                s_val = DBG_Utils().xx_getAsStrEx(s_e,i_len)
                if s_comment == "":
                        s_comment = s_ident
                
                self.printTabs(1, ""  + s_comment + ": "  + s_val);
                
        def printTabs(self,tbs,ss):
                if tbs == 0:
                        print self.m_tabs + ss
                if tbs == 1:
                        print self.m_tabs + ss