    
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *


from ... appcore.printers.DBG_Base import *
from ... appcore.printers.DBG_FieldInfos import *
from ... apptools.DBG_EnvItemData import *
from ... apptools.DBG_EnvManager import *
from ... appcore.config.DBG_PrintConfig import *        
from ... appcore.memory.DBG_Utils import *

class DBG_MethodByAddrPrinter(DBG_AdapterBase):
    def __init__(self,spar, pparent):
        DBG_AdapterBase.__init__(self, spar)
        self.xx_set_class_name ( "DBG_MethodByAddrPrinter" )
        self.xx_set_full_class_name ( "DBG_MethodByAddrPrinter" )
        self.m_parent = pparent
        self.m_addr_string = ""
        self.m_method_phy_addr = ""
        self.m_method_header = ""
        self.m_messages = DBG_FieldInfos("DBG_MemoryPtr",self)
        
    def set_parent(self, pparent):
        self.xx_dbg( "DBG_MethodByAddrPrinter::set_parent::method_in::")
        self.m_parent = pparent
        self.xx_dbg( "DBG_MethodByAddrPrinter::set_parent::method_out::")
        
    def set_addr_string(self,pstr):
        self.xx_dbg( "DBG_MethodByAddrPrinter::set_addr_string::method_in::")
        self.m_addr_string = pstr
        self.xx_dbg( "DBG_MethodByAddrPrinter::set_addr_string::method_out::")
        
    def prepare_object(self):
        try:
            
            self.xx_dbg("DBG_MethodByAddrPrinter::prepare_object")
            self.get_method_phy_addr()
            self.get_method_description()
            self.m_messages.clear_messages()
            self.m_messages.add_message("m_addr_string:" + self.m_addr_string)
            self.m_messages.add_message("m_method_phy_addr:" + self.m_method_phy_addr)
            self.m_messages.add_message("header:" + self.m_method_header)
            self.xx_dbg("DBG_MethodByAddrPrinter::prepare_object")
        except:
            self.xx_exception("DBG_MethodByAddrPrinter::xx_print_link_ptr::exception::")
        
    def add_msg(self, title,tt):
        try:
            self.m_messages.add_message(str(title) + ":" + str(tt))
        except:
                self.xx_exception("DBG_FieldsMapper::add_msg::exception::")
        
    def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_FieldsMapper::print_object")
                
    def print_object_internal(self):
        try:
            self.xx_dbg( "DBG_MethodByAddrPrinter::xx_print_link_ptr::method_in::")
            self.m_messages.print_object("method")
            self.xx_dbg( "DBG_MethodByAddrPrinter::xx_print_link_ptr::method_in::")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
            
    def get_msg_info(self):
        s_i = []
        return s_i
    
    
    def get_method_phy_addr(self):
        try:
            self.m_method_phy_addr = ""
            
            s_split = self.m_addr_string.split()
            ii = 0
            
            for dd_ss in s_split:
                if(ii == 0):
                    if (dd_ss != "<function>"):
                        #print "pppppppppppppp:" + dd_ss +"]"
                        break
                    
                if(ii == 2):
                    self.m_method_phy_addr = dd_ss                
                ii = ii +1
                    
            return ""
        except:
            self.xx_exception("DBG_MethodByAddrPrinter::get_method_phy_addr::exception::")
            return ""
    
    def get_method_description(self):
        try:
            
            if( self.m_method_phy_addr == ""):
                return ""
            
            s_expr = "uf " + self.m_method_phy_addr
            s_outs = DBG_Utils().xx_dbgCommand(s_expr)
            if (s_outs != ""):
                s_split = s_outs.split()
                if(len(s_split) > 0):
                    self.m_method_header = s_split[0]                    
        except:
            self.xx_exception("DBG_MethodByAddrPrinter::get_method_description::exception::","")
            return ""
        