import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
class DBG_RaidIsmInitParams(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_DiskIdentityData::__init__::m_in::")
                self.xx_set_class_name ( "_DiskIdentityData" )
                self.xx_set_full_class_name ( "iastora!_RAID_ISM_INIT_PARMS" )
                self.m_fields = DBG_FieldsMapper("DBG_RaidIsmInitParams"
                                         ,self)                                
                
                self.m_fields.add_fields_int_array([
                        "cachedMemSize"
                        ,"maxRaidDevs"
                        ])
                #self.mApstTable = DBG_ApstTable("Parent::DBG_DiskIdentityData")
                self.xx_dbg("DBG_DiskIdentityData::__init__::m_out::")
                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_RaidIsmInitParams::set_parent::")
                #self.m_parent = pparent
                self.xx_dbg("DBG_RaidIsmInitParams::set_parent::out")
               
        def prepare_object(self):                
                self.xx_dbg("DBG_DiskIdentityData::prepare_object::m_in::")
                
                #self.mApstTable.xx_inc_tabs(self);                
                #self.mApstTable.xx_compute_arr_phy_by_parent(self,"mController")
                self.m_fields.set_fields_parent(self)
                self.xx_dbg("DBG_DiskIdentityData::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self,sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,pparent,sdbg=""):

                self.xx_dbg("DBG_DiskIdentityData::print_object::m_in::")
                self.prepare_object()
                self.xx_print_ptr("")
                self.m_fields.xx_print_fields("")
                #self.mApstTable.print_object()
                self.xx_dbg("DBG_DiskIdentityData::print_object::m_out::")
                
                
        def get_class_str(self):
                self.xx_dbg("DBG_DiskIdentityData::get_class_str::m_in::")
                cs = """
"""

                self.xx_dbg("DBG_DiskIdentityData::get_class_str::m_out::")
