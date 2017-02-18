import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. appsrc.ismcfg.DBG_MpbDisk_PyArray import *
from .. appsrc.ismcfg.DBG_RaidMpbTblEntry_PyArray import *

class DBG_RaidMpbTbl(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_RaidMpbTbl::__init__::m_in::")
                self.xx_set_class_name ( "RaidMpbTbl" )
                self.xx_set_full_class_name ( "iastora!RaidMpbTbl" )
                
                self.m_fields = DBG_FieldsMapper("DBG_RaidMpbTbl", self)
                
                self.currRaidDevMembers = DBG_MpbDisk_PyArray("DBG_RaidMpbTbl",self)
                self.currRaidDevMembers.set_parent_names("RaidMpbTbl")                
                self.currRaidDevMembers.set_selectors("currRaidDevMembers","currRaidDevNumMembers")
                self.currRaidDevMembers.init_object_fields()
                
                self.allDisksTbl = DBG_MpbDisk_PyArray("DBG_RaidMpbTbl",self)
                self.allDisksTbl.set_parent_names("RaidMpbTbl")
                self.allDisksTbl.set_selectors("allDisksTbl","numDisks")
                self.allDisksTbl.m_tbl_sel_type = "arr"
                self.allDisksTbl.init_object_fields()
                
                
                self.mpbTbl = DBG_RaidMpbTblEntry_PyArray("DBG_RaidMpbTbl",self)
                self.mpbTbl.set_parent_names("RaidMpbTbl")
                self.mpbTbl.set_selectors("mpbTbl","numRaidMpbs")
                self.mpbTbl.init_object_fields()
                
                self.xx_dbg("DBG_RaidMpbTbl::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_RaidMpbTbl::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_RaidMpbTbl::prepare_object_internal::")
                
                if(self.xx_is_object() == 1):
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
                                                
                        self.currRaidDevMembers.set_addr(self,"SELF")
                        self.currRaidDevMembers.prepare_object(self)
                        
                        self.allDisksTbl.set_addr(self,"SELF")
                        self.allDisksTbl.prepare_object(self)
                        
                        self.mpbTbl.set_addr(self,"SELF")
                        self.mpbTbl.prepare_object(self)
                        
                self.xx_dbg("DBG_RaidMpbTbl::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self,sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,pparent,sdbg=""):

                self.xx_dbg("DBG_RaidMpbTbl::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):                
                        self.m_fields.xx_print_fields("")
                        self.currRaidDevMembers.print_object()
                        self.allDisksTbl.print_object()
                        self.mpbTbl.print_object()
                        
                self.xx_dbg("DBG_RaidMpbTbl::print_object::m_out::")

