

import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *

from ... appsrc.ismcfg.DBG_MPB_DISK_PyArray import *
from ... appsrc.ismcache.DBG_BytestreamCfgSig import *

class DBG_RaidMpb(DBG_AdapterBase):
        def __init__(self,spar,pparent):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_RaidMpb::__init__::m_in::")
                self.xx_set_class_name ( "RaidMpb" )
                self.xx_set_full_class_name ( "iastora!RaidMpb" )
                #self.m_child_item = DBG_ApstTable("Parent::DBG_RaidMpb")
                self.m_fields = DBG_FieldsMapper("DBG_RaidMpb"
                                         , self)

                self.m_fields.add_fields_int_array([
                        "numDisks"
                        ,"numRaidDevs"
                        ,"numRaidDevsCreated"
                        ,"mpbSize"
                        ,"generationNum"
                        ])
                
                self.m_disks = DBG_MPB_DISK_PyArray("DBG_RaidMpb",self)
                self.sig = DBG_BytestreamCfgSig("DBG_RaidMpb",self)
                self.xx_dbg("DBG_RaidMpb::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_RaidMpb::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_RaidMpb::prepare_object_internal::")
                
                if(self.xx_is_object() == 1):
                        self.m_fields.set_fields_parent(self)                      
                        #self.m_child_item.set_addr_arr(self,"m_child_item")
                        self.m_disks.set_parent_names("RaidMpb")
                        self.m_disks.set_addr(self,"SELF")
                        self.m_disks.prepare_object(self)
                        
                        self.sig.set_addr_arr(self,"sig")
                        self.sig.prepare_object()
                        
                self.xx_dbg("DBG_RaidMpb::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(self,sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,pparent,sdbg=""):

                self.xx_dbg("DBG_RaidMpb::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_is_object() == 1):                
                        self.m_fields.xx_print_fields("")
                        #self.m_child_item.print_object()
                        self.m_disks.print_object()
                        self.sig.print_object()
                        
                self.xx_dbg("DBG_RaidMpb::print_object::m_out::")

