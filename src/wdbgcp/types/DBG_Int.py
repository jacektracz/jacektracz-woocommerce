import sys
import os

import logging
from pykd import *
from defines import *
from .. helpers.DBG_Utils import *
from DBG_MemoryPtr import *
from DBG_WdbgItemsPrinter import *
		
class DBG_Int(DBG_MemoryPtr, pparent, svariable, stitle):
    
    def __init__(self,svariable,stitle):
        DBG_MemoryPtr.__init__(self,spar)
        self.m_parent = pparent
        self.m_int_variable = svariable
        self.m_int_title = stitle        
                
    def print_object(self,stabs = 0):
        DBG_WdbgItemsPrinter().xx_print_int(
                                self.m_parent.xx_get_class_ptr("")
                                ,self.m_int_variable
                                ,self.m_int_title
                                ,self.xx_gett(stabs))

class DBG_Str(DBG_MemoryPtr, pparent, svariable, stitle, slen):
    
    def __init__(self,svariable,stitle):
        DBG_MemoryPtr.__init__(self,spar)
        self.m_parent = pparent
        self.m_cl_variable = svariable
        self.m_cl_title = stitle        
        self.m_cl_len = slen
        
    def print_object(self,stabs = 0):                
        DBG_WdbgItemsPrinter().print_str(
                                self.m_parent.xx_get_class_ptr("")
                                ,self.m_int_variable
                                ,self.m_int_title
                                ,self.m_cl_len
                                ,self.xx_gett(stabs))
        
class DBG_Enum(DBG_MemoryPtr, pparent, svariable, stitle):
    
    def __init__(self,svariable,stitle):
        DBG_MemoryPtr.__init__(self,spar)
        self.m_parent = pparent
        self.m_cl_variable = svariable
        self.m_cl_title = stitle        
        self.m_cl_len = 20
        
    def print_object(self,stabs = 0):        
        DBG_WdbgItemsPrinter().print_enum(
                                self.m_parent.xx_get_phy_addr_str("")
                                ,self.m_int_variable
                                ,self.m_int_title
                                ,self.m_cl_len
                                ,self.xx_gett(stabs))

class DBG_Hex(DBG_MemoryPtr, pparent, svariable, stitle, slen):
    
    def __init__(self,svariable,stitle):
        DBG_MemoryPtr.__init__(self,spar)
        self.m_parent = pparent
        self.m_cl_variable = svariable
        self.m_cl_title = stitle        
        self.m_cl_len = slen
        
    def print_object(self,stabs = 0):                
        DBG_WdbgItemsPrinter().print_hex(
                                self.m_parent.xx_get_class_ptr("")
                                ,self.m_int_variable
                                ,self.m_int_title
                                ,self.m_cl_len
                                ,self.xx_gett(stabs))
        