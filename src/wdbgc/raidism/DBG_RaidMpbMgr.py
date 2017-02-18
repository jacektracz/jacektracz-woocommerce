import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. raidism.DBG_RaidIsmDisk import *
#from .. raidism.DBG_RaidMpb import *
from .. raidism.DBG_RaidMpbTbl import *
from .. appsrc.ismcache.DBG_RaidMpb import *
class DBG_RaidMpbMgr(DBG_AdapterBase):
        def __init__(self,spar,pparent):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_RaidMpbMgr::__init__::in::")
                self.xx_set_class_name ( "RaidMpbMgr" )
                self.xx_set_full_class_name ( "iastora!RaidMpbMgr" )
                
                self.m_currDisk = DBG_RaidIsmDisk("Parent::DBG_RaidMpbMgr")
                self.m_raidMpb = DBG_RaidMpb("Parent::DBG_RaidMpbMgr",self)
                self.m_raidMpbTbl = DBG_RaidMpbTbl("Parent::DBG_RaidMpbMgr")
                self.m_fields = DBG_FieldsMapper("DBG_RaidMpbMgr"
                                         ,self)                
                self.m_fields.add_fields_int_array([
                        "currDevNo"
                        ,"mpbSize"
                        ,"familyNum"
                        ,"hasFoundNvcVol"
                        ,"hasFoundAccelVol"
                        ,"diskFoundsActive"
                        ])
                
                self.m_fields.add_fields_str("name",32)
                                
                
                self.xx_dbg("DBG_RaidMpbMgr::__init__::in::")
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_RaidMpbMgr::print_object")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_RaidMpbMgr::prepare_object_internal::")
                if(self.xx_is_object() == 1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                        self.m_currDisk.set_addr(self,"currDisk")
                        self.m_raidMpb.set_addr(self,"raidMpb")
                        self.m_raidMpbTbl.set_addr(self,"raidMpbTbl")
                self.xx_dbg("DBG_RaidMpbMgr::prepare_object_internal::out::")
                
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self,sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,pparent,sdbg=""):

                self.xx_dbg("DBG_RaidMpbMgr::print_object_internal::")
                self.prepare_object()
                self.xx_print_ptr("")
                self.m_fields.xx_print_fields("")                
                if (self.xx_is_object() ==1):                        
                        self.m_currDisk.print_object()
                        self.m_raidMpb.print_object()
                        self.m_raidMpbTbl.print_object()
                
                self.xx_dbg("DBG_RaidMpbMgr::print_object_internal::out::")                        
                        
                
        def get_class_str(self):
                self.xx_dbg("DBG_RaidMpbMgr::get_class_str::")
                
                ccstr = """
                """
                
                self.xx_dbg("DBG_RaidMpbMgr::get_class_str::")
