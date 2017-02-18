import sys
import os
from .. fields.DBG_FieldsBase import *
                
class DBG_FieldsFormatters(DBG_FieldsBase):
        def __init__(self,pparent,sdbg):
                DBG_FieldsBase.__init__(self,pparent,sdbg)
                self.xx_dbg("DBG_FieldsFormatters.__init__")

        def strint_to_info(self, pval_str, tabsp):
                try:
                        pval = int(pval_str)
                        s_int =  ""
                        s_int = s_int + tabsp                        
                        s_int = s_int + "[" + str(pval) + "]"
                        s_int = s_int + "[" + self.to_binary(pval) + "]"
                        s_int = s_int + "[" + self.to_hex(pval) + "]"
                        return s_int
                except:
                        return "IIEXC"
                
        def int_to_info(self, dd_ii, tabsp):
                try:
                        s_int =  ""
                        s_int = s_int + tabsp
                        s_int = s_int + str(dd_ii.m_variable) 
                        s_int = s_int + "[" + str(dd_ii.m_value) + "]"
                        s_int = s_int + "[" + self.to_binary(dd_ii.m_value) + "]"
                        s_int = s_int + "[" + self.to_hex(dd_ii.m_value) + "]"
                        return s_int
                except:
                        return "IIEXC"
                                        
        def to_hex(self, n):
                try:
                        return str(hex(n))
                except:
                        return "HHEXC"

        def to_binary(self, n):
                try:
                        return str(bin(n))
                except:
                        return "BBEXC"
        
        def to_binary_1(self, n):
                return ''.join(str(1 & int(n)>> 1) for i in range(64)[::-1])
        
        def to_binary_2(self, i):

                
                try:
                        #s_bb = ''.joim(1)
                        if i == 0:
                                return "0"
                        s = ''
                        while i :
                                if i & i ==1:
                                        s = "1" +s
                                else:
                                        s = "0" +s
                                i /= 2
                        return s
                except:
                        return "XX"
