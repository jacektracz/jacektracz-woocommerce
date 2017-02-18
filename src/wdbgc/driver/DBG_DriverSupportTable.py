import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
        
        
class DBG_DriverSupportTable(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_DriverSupportTable::__init__::in::")
                self.xx_set_class_name ( "_raid_ver" )
                self.xx_set_full_class_name ( "iastora!_raid_ver" )
                self.m_fields = DBG_FieldsMapper("DBG_Transports"
                                         ,self)
                self.m_fields.add_fields_int_array([
                        "PRN_MajorVer"
                        ,"PRN_MinorVer"
                        ,"PRN_HotFix"
                        ,"PRN_BuildNum"
                        ])
                self.xx_dbg("DBG_DriverSupportTable::__init__::out")
                
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_DriverSupportTable::prepare_object")
                        self.m_fields.initialize_by_parent(self)
                        #self.m_psm.xx_inc_tabs_ex(self,1,"DBG_DriverSupportTable")
                        #self.m_psm.xx_compute_phy_by_parent(self,"mStateMachine")
                                                
                        self.xx_dbg("DBG_DriverSupportTable::prepare_object::out")
                except:
                        self.xx_exception("DBG_DriverSupportTable::prepare_object")
            
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_DriverSupportTable::print_object")        
                        self.prepare_object()
                        self.xx_print_ptr("")
                        if(self.xx_is_object()==1):
                                self.m_fields.print_object()
                                
                        self.xx_dbg("DBG_DriverSupportTable::print_object::out")
                except:
                        self.xx_exception("DBG_DriverSupportTable::print_object")

