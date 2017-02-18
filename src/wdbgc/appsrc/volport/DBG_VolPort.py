
import sys
import os
import logging
from ... DBG_AdapterBase import *       
from ... ports.DBG_PortConfigurationInformation import *
from ... appcore.config.DBG_PrintConfig import *
from ... appsrc.volport.DBG_VolportDisk_PyArray import *
from ... appsrc.volport.DBG_VolportVolume_PyArray import *

class DBG_VolPort(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "VolPort" )
                self.xx_set_full_class_name ( "iastora!volport::VolPort" )
                self.m_disks = DBG_VolportDisk_PyArray("", self)
                self.m_volumes = DBG_VolportVolume_PyArray("", self)
                
        def prepare_object_global(self):
                try:
                    self.x_dbg("DBG_VolPort::prepare_object_global::in::")            
                    self.xx_set_lg_compute_phy_addr( "iastora!volport::g_volport" )
                    self.x_dbg("DBG_VolPort::prepare_object_global::out:")
                except:
                    self.xx_exception("DBG_VolPort::prepare_object_global::exception::")
                
        def prepare_object(self):
                self.x_dbg("DBG_VolPort::prepare_object::method_in::")
                if(self.xx_is_object()==1):
                        self.x_dbg("DBG_VolPort::prepare_object::is_obj:")
                        #self.m_disks.set_addr_arr(self,"SELF")
                        #self.m_disks.prepare_object()
                        
                        #self.m_volumes.set_addr_arr(self,"SELF")
                        #self.m_volumes.prepare_object()
                        
                self.x_dbg("DBG_VolPort::prepare_object::method_out::")
                
        def print_object(self, sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.x_dbg("DBG_VolPort::print_object_internal::method_in::")
                self.xx_print_ptr("")
                if(self.xx_is_object()==1):
                        self.x_dbg("DBG_VolPort::print_object_internal::is_obj:")
                        #self.m_disks.print_object()
                        #self.m_volumes.print_object()
                self.x_dbg("DBG_VolPort::print_object_internal::method_out::")
                        
        def print_object_global(self):
              self.prepare_object_global()
              self.prepare_object()
              self.print_object()
              