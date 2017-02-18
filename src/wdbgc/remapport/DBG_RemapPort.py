
import sys
import os
import logging
from .. DBG_AdapterBase import *       
from .. ports.DBG_PortConfigurationInformation import *
from .. remapport.DBG_Transports import *
from .. remapport.DBG_Transports_Glob_Array import *
from .. ports.DBG_HwInitializationData import *
from .. appcore.config.DBG_PrintConfig import *
class DBG_RemapPort(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "remapport" )
                self.xx_set_full_class_name ( "iastora!remapport" )
                
                self.m_transports = DBG_Transports("FROM::DBG_RemapPort")
                self.m_transports_glob = DBG_Transports_Glob_Array("FROM::DBG_RemapPort")
                
                self.m_port_conf = DBG_PortConfigurationInformation("FROM::DBG_RemapPort")
                self.sAhciHwInitializationData = DBG_HwInitializationData("FORM::DBG_Transport")
                self.sNvmeHwInitializationData = DBG_HwInitializationData("FORM::DBG_Transport")
                self.gRemapPortHwInitializationData = DBG_HwInitializationData("FORM::DBG_Transport")
                
        def prepare_object_global(self):
                try:
                    self.x_dbg("DBG_RemapPort::prepare_object_global::in::")            
                    self.xx_set_lg_compute_phy_addr( "iastora!RemapPort::sInstance" )
                    self.x_dbg("DBG_RemapPort::prepare_object_global::out:")
                except:
                    self.xx_exception("DBG_RemapPort::prepare_object_global::exception::")
                
        def prepare_object(self):
                self.x_dbg("DBG_RemapPort::prepare_object::in::")
                if(self.prepare_check() == 1):
                        return
                
                if(self.xx_is_object()==1):
                        if( DBG_PrintConfig().getItem().m_is_soft_remap == 0 ):
                                self.m_transports.set_addr(self,"SELF")
                                self.m_transports.prepare_object(self)

                        if( DBG_PrintConfig().getItem().m_is_soft_remap == 1 ):
                                self.m_transports_glob.set_addr(self,"SELF")
                                self.m_transports_glob.prepare_object(self)
                        
                        self.m_port_conf.xx_inc_tabs(self);
                        if(DBG_PrintConfig().getItem().self_is_above_or_equal( 15 ) == 1):
                                self.m_port_conf.set_addr(self,"mConfigInfo")
                                self.m_port_conf.prepare_object()
                                
                        self.sAhciHwInitializationData.set_addr_arr(self,"sAhciHwInitializationData")
                        self.sAhciHwInitializationData.prepare_object()
                        
                        self.sNvmeHwInitializationData.set_addr_arr(self,"sNvmeHwInitializationData")
                        self.sNvmeHwInitializationData.prepare_object()
                        
                        #self.gRemapPortHwInitializationData.set_addr_arr_static(self,"gRemapPortHwInitializationData")
                        #self.gRemapPortHwInitializationData.prepare_object()
                        
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.prepare_object()

                self.xx_print_ptr("")
                if(self.xx_is_object()==1):
                        
                        if(DBG_PrintConfig().getItem().self_is_above_or_equal( 15 ) == 1):
                                self.m_port_conf.print_object()
                                
                        if( DBG_PrintConfig().getItem().m_is_soft_remap == 0 ):                        
                                self.m_transports.print_object()

                        if( DBG_PrintConfig().getItem().m_is_soft_remap == 1 ):
                                self.m_transports_glob.print_object()
                                
                        self.sAhciHwInitializationData.print_object()
                        self.sNvmeHwInitializationData.print_object()
                        #self.gRemapPortHwInitializationData.print_object()
                        
        def print_object_global(self):
              self.prepare_object_global()
              self.prepare_object()
              self.print_object()
              