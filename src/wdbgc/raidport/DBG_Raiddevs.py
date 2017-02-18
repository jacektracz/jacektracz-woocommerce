import sys
import os
import logging

from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. appcore.memory.DBG_MemoryTools import *      
from .. ports.DBG_PortConfigurationInformation import *
from .. raidport.DBG_raiddev import *        
from .. fields.DBG_FieldsMapper import *        
class DBG_RaidDevs(DBG_AdapterBase):

    def __init__(self,spar,pparent):                
        DBG_AdapterBase.__init__(self,spar)
        self.numRaidDevs = 0
        self.m_raiddevs =[]
        self.m_parent = pparent
        self.m_fields = DBG_FieldsMapper("DBG_raiddev"
                                 ,self)
        self.m_fields.add_fields_int_array([
            "numRaidDevs"])
        
    def prepare_object(self):
        self.xx_dbg("DBG_raiddev::prepare_object::in") 
        if(self.xx_is_object()==1):            
            self.m_fields.initialize_by_parent(self.m_parent)
            self.initialize_devs()
        self.xx_dbg("DBG_raiddev::prepare_object::out")
        
    def initialize_devs(self):
        self.xx_dbg("DBG_raiddev::initialize_devs::in") 
        self.numRaidDevs = DBG_MemoryTools().xx_get_int(
            self.m_parent
            ,"numRaidDevs")
        
        self.m_raiddevs = []
        if(self.numRaidDevs > 0):        
            for i in range(self.numRaidDevs):
                dd = DBG_raiddev("DBG_raiddevs")
                dd.xx_inc_tabs_ex( self.m_parent,2,"DBG_raiddevs")
                dd.xx_compute_cpp_phy_by_parent(
                    self.m_parent
                    ,"raidDevs[" +str(i) + "]")
                dd.prepare_object()
                self.m_raiddevs.append(dd)
        self.xx_dbg("DBG_raiddev::initialize_devs::out_method::")
        
        
    def print_object(self,sdbg=""):
            try:
                    self.xx_print_start("")
                    self.print_object_internal(sdbg)
                    self.xx_print_end("")
            except:
                    self.xx_exception("::print_object")
                    
    def print_object_internal(self,sdbg=""):
        self.xx_dbg("DBG_raiddev::print_object::in") 
        self.prepare_object()
        if(self.xx_is_object()==1):
            self.m_fields.print_object()
            self.print_devs();
            
        self.xx_dbg("DBG_raiddev::print_object::out")
    
        
    def print_devs(self):
        self.xx_dbg("DBG_raiddev::prepare_object")        
        if(self.numRaidDevs > 0):
            for dd_raiddev in self.m_raiddevs:
                    dd_raiddev.print_object()
                
        self.xx_dbg("DBG_raiddev::prepare_object::out")   
