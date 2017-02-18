import sys
import os        
from .. DBG_AdapterBase import *

class DBG_Base_EnumState(DBG_AdapterBase):
        def __init__(self, sdbginfo):
                DBG_AdapterBase.__init__(self,sdbginfo)                
                self.xx_dbg("DBG_CompletionQueue::__init__::m_in::")
                self.xx_set_class_name ( "DBG_Base_EnumState" )
                self.xx_set_full_class_name ( "iastora!DBG_Base_EnumState" )
                
                self.m_items = []
                self.m_mapper_in = None
                self.m_mapper_out = None
                self.m_smb = ""
                self.m_smb_value = 0
                self.m_value_out = ""
                
        def get_value_out(self):
                return self.m_value_out
                
        def set_items(self, pitems):
                self.m_items = []
                for dd_ii in pitems:
                        self.m_items.append(dd_ii)
                
        def prepare_object(self, pmapper_in, psmb):
                try:
                        self.m_mapper_in = pmapper_in                        
                        self.m_smb = psmb
                        self.m_smb_value = self.m_mapper_in.get_fields_asstr_int(psmb)
                        
                        self.m_value_out = self.get_str(self.m_smb_value)
                except:
                        self.xx_exception("DBG_Base_EnumState::prepare_object::exception::")

        def get_description(self):
                s_out = str(self.m_smb) + "[" + str(self.m_smb_value) + "][" + str(self.m_value_out) + "]"
                return s_out
        
        def get_str(self, smb):
                try:
                        if(smb >=0 and smb < len(self.m_items)):
                                return self.m_items[smb]
                        else:
                                return "NOT_SET"
                except:
                        return "NOT_SET"
        