import sys
import os
import logging
from .. DBG_AdapterBase import *
from .. appsrc.ismcfg.DBG_RaidMap import *
from .. appsrc.ismcache.DBG_DsMgr import *
from .. appsrc.ismcache.DBG_FsMgr import *
#from .. appsrc.ismcfg.DBG_RaidMap import *

class DBG_RaidVol(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_RaidVol::__init__::m_in::")
                self.xx_set_class_name ( "RaidVol" )
                self.xx_set_full_class_name ( "iastora!RaidVol" )
                self.m_lowMap = DBG_RaidMap("Parent::DBG_RaidVol",self)
                self.m_highMap = DBG_RaidMap("Parent::DBG_RaidVol",self)
                self.dsMgr = DBG_DsMgr("Parent::DBG_RaidVol",self)
                self.fsMgr = DBG_FsMgr("Parent::DBG_RaidVol",self)
                self.xx_dbg("DBG_RaidVol::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_RaidVol::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):                
                self.xx_dbg("DBG_RaidVol::prepare_object_internal::m_in::")
                
                if(self.xx_is_object()):
                        self.m_lowMap.set_addr(self,"lowMap")
                        self.m_lowMap.prepare_object()
                        
                        self.m_highMap.set_addr(self,"highMap")
                        self.m_highMap.prepare_object()
                        
                        self.dsMgr.set_addr(self,"dsMgr")
                        self.dsMgr.prepare_object()

                        self.fsMgr.set_addr(self,"fsMgr")
                        self.fsMgr.prepare_object()
                        
                        #self.mApstTable.xx_inc_tabs(self);                
                        #self.mApstTable.xx_compute_arr_phy_by_parent(self,"mController")
                        
                self.xx_dbg("DBG_RaidVol::prepare_object_internal::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_RaidVol::print_object::m_in::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object()):     
                        self.m_lowMap.print_object()
                        self.m_highMap.print_object()
                        self.dsMgr.print_object()
                        self.fsMgr.print_object()
                #self.mApstTable.print_object()
                self.xx_dbg("DBG_RaidVol::print_object::m_out::")
