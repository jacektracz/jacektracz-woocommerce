import sys
import defines
import logging
from pykd import *
from defines import *
from proc_utils import *
from dbg_classess_utils import *

class DBG_PortStateMachine:
        
        def __init__(self, spointer, sindex,sfeature):                
                self.m_ptr = spointer
                self.m_port = sindex
                self.m_tabs = '\t\t\t';
                if sfeature != "":
                        self.m_feature = sfeature
                else:
                        self.m_feature = "mStateMachine"
                
        def setTabs(self,ptabs):
                self.m_tabs = ptabs;
                
        def printObj(self):
                try:
                        link(self.m_tabs,"?? @@C++(((iastora!AhciController*)0x" + self.m_ptr + ")->mPort[" + str(self.m_port) + "]->" + self.m_feature + ")"
                             ,"PortStateMachine:" + self.m_feature);
                except:
                        print '=========================exception occured================='
                        logging.exception('')
                        print '==========================================================='
                        return
                
        def getStrPtr(self,sident):
                s_expr_ptr = "@@C++(((iastora!AhciController*)0x" + self.m_ptr + ")->mPort[" + self.m_port + "]->mStateMachine)"                
                return s_expr_ptr
        
        def printStr(self,s_ident,s_comment,i_len):
                s_e = self.getStrPtr(s_ident)                
                s_val = getAsStrEx(s_e,i_len)
                if s_comment == "":
                        s_comment = s_ident
                
                self.printTabs(1, ""  + s_comment + ": "  + s_val);
                
        def printTabs(self,tbs,ss):
                if tbs == 0:
                        print self.m_tabs + ss
                if tbs == 1:
                        print self.m_tabs + ss
