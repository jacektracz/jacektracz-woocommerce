import sys
import defines
import logging
from pykd import *
from defines import *
from proc_utils import *
from dbg_classess_utils import *

class DBG_DeviceFeature:
        
        def __init__(self,spointer,sfeature):                
                self.m_ptr = spointer
                self.m_feature = sfeature                                                
                
        def printObj(self):
                try:
                        #print "\t\t\t" + self.m_feature + ":"
                        link('\t\t\t',"?? @@C++(((iastora!AtaDevice*)0x" + self.m_ptr + ")->" + self.m_feature +")",self.m_feature);
                        self.printInt(".mIsSupported","",1)
                        self.printInt(".mIsAllowed","",1)
                        self.printInt(".mIsEnabled","",1)
                        self.printInt(".mId","",1)
                        self.printInt(".mEnable","",1)
                        self.printInt(".mDisable","",1)
                except:
                        print '=========================exception occured================='
                        logging.exception('')
                        print '==========================================================='
                        return
                
        def getStrPtr(self,sident):                
                s_expr_ptr = "@@C++((((iastora!AtaDevice*)0x" + self.m_ptr + ")->" + self.m_feature + ")" + sident + ")"
                return s_expr_ptr
        
        def printStr(self,s_field,s_comment,i_len):
                #return
                s_e = self.getStrPtr(s_field)
                s_val = getAsStrEx(s_e,i_len)
                if s_comment == "":
                        s_comment = s_field                
                self.printTabs(1, ""  + s_comment + ": "  + s_val);

        def printInt(self,s_field,s_comment,i_len):                
                s_e = self.getStrPtr(s_field)
                s_val = getAsInt(s_e)
                if s_comment == "":
                        s_comment = s_field                
                self.printTabs(1, "" + s_comment + ": "  + str(s_val));
                
        def printTabs(self,tbs,ss):
                if tbs == 0:
                        print "\t\t\t" + ss
                if tbs == 1:
                        print "\t\t\t\t" + ss
