
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.ismcachecfg.DBG_NvcActivePrb_PyArray import *
from ... appsrc.ismcachecfg.DBG_NvcPrbEntryIdxList_PyArray import *

class DBG_NvcPromoBlkSet(DBG_AdapterBase):
        def __init__(self,spar, pparent):
                DBG_AdapterBase.__init__(self, spar)
                self.xx_dbg("DBG_NvcPromoBlkSet::__init__::m_in::")
                
                self.xx_set_class_name ( "NvcPromoBlkSet" )
                self.xx_set_full_class_name ( "iastora!NvcPromoBlkSet" )
                
                self.m_fields = DBG_FieldsMapper("DBG_NvcPromoBlkSet", self)
                self.init_object_fields()
                
                self.activePrb  = DBG_NvcActivePrb_PyArray("DBG_RaidMpbTbl",self)
                self.activePrb.set_parent_names("NvcPromoBlkSet")                
                self.activePrb.set_selectors("activePrb ","numPromoBlkEntries")
                self.activePrb.init_object_fields()

                self.prbLruTable   = DBG_NvcPrbEntryIdxList_PyArray("DBG_RaidMpbTbl",self)
                self.prbLruTable.set_parent_names("NvcPromoBlkSet")                
                self.prbLruTable.set_selectors("prbLruTable  ","numPromoBlkEntries")
                self.prbLruTable.init_object_fields()
                
                self.xx_dbg("DBG_NvcPromoBlkSet::__init__::m_out::")

        def init_object_fields(self):
                self.xx_dbg("DBG_NvcPromoBlkSet::init_object_fields::in::")                                
                #self.m_fields.add_fields_asstr_u32("mIntervalInMilliseconds")
                self.xx_dbg("DBG_NvcPromoBlkSet::init_object_fields::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_NvcPromoBlkSet::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_NvcPromoBlkSet::prepare_object_internal::")                                
                if(self.xx_obj_valid() == 1 ):
                        self.clear_messages()
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.prepare_object()
     
                        self.activePrb.set_addr(self,"SELF")
                        self.activePrb.prepare_object(self)

                        self.prbLruTable.set_addr(self,"SELF")
                        self.prbLruTable.prepare_object(self)
                        
                self.xx_dbg("DBG_NvcPromoBlkSet::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_NvcPromoBlkSet::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_NvcPromoBlkSet::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_obj_valid() == 1 ):                                                        
                        self.m_fields.print_object()
                        self.activePrb.print_object()
                        self.prbLruTable.print_object()
                        
                self.xx_dbg("DBG_NvcPromoBlkSet::print_object::m_out::")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_NvcPromoBlkSet::xx_obj_valid::m_in::")
                i_valid = self.xx_is_object()
                self.xx_dbg("DBG_NvcPromoBlkSet::xx_obj_valid::m_out::" + str(i_valid))
                return i_valid
        
