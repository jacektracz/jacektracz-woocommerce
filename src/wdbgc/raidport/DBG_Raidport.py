import sys
import os

from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. ports.DBG_PortConfigurationInformation import *
from .. driver.DBG_Driver import *
from .. appsrc.ismraid.DBG_RaidIsm import *
from .. appsrc.raidtargets.DBG_RaidportTargets_PyArray import *
from .. appsrc.raidtransport.DBG_Transport_PyRaid import *
from .. appcore.config.DBG_PrintConfig import *
from .. appcore.printers.DBG_ConfigHtmlPrinter import *
from .. appcore.printers.DBG_CallStackRawPrinter import *
from .. appsrc.wcdl.DBG_RaidportSpinLock import *
from .. appsrc.ismevents.DBG_IsmTimer import *
from .. appsrc.wcdl.DBG_Timer import *
from .. appsrc.ismevents.DBG_Ism_Event import *
from .. ports.DBG_HwInitializationData import *
from .. appsrc.wcdl.DBG_WcdlLibrary import *

class DBG_Raidport(DBG_AdapterBase):

    def __init__(self,spar):                
        DBG_AdapterBase.__init__(self,spar)
        self.x_dbg("DBG_Raidport::__init__::in::")
        self.xx_set_class_name( "Raidport" )
        self.xx_set_full_class_name ( "iastora!Raidport" )
        self.xx_set_tabs(1,"DBG_Raidport")
        self.m_driver = DBG_Driver("FROM:DBG_Raidport")							
        self.m_driver.xx_set_tabs(self.xx_get_tabs() + 1,"DBG_Raidport:Driver")
        self.m_port_conf = DBG_PortConfigurationInformation("FROM::DBG_Raidport")
        self.m_raidism = DBG_RaidIsm("Parent::DBG_Raidport")
        
        self.m_exe_rtargets = 1
        self.m_raidport_targets = DBG_RaidportTargets_PyArray("Parent::DBG_Raidport",self)
        self.mTransport = DBG_Transport_PyRaid("Parent::DBG_Raidport")
        self.mNumPaths = 0
        self.mNumTargets = 0
        self.m_fields = DBG_FieldsMapper("DBG_RaidportTargets_PyArray",self)
        self.init_raidport_fields()        
        self.m_config = DBG_ConfigHtmlPrinter(self,"Parent::DBG_Raidport")
        self.mSpinLock = DBG_RaidportSpinLock(self,"Parent::DBG_Raidport")
        self.mIsmTimer = DBG_IsmTimer("Parent::DBG_Raidport",self)
        self.mIsmTimerBase = DBG_Timer("Parent::DBG_Raidport")
        self.mSuspendEvent = DBG_Ism_Event("Parent::DBG_Raidport",self)
        self.mShutdownEvent = DBG_Ism_Event("Parent::DBG_Raidport",self)
        self.mHwInitializationData  = DBG_HwInitializationData("Parent::DBG_Raidport")
        self.gHwInitializationData  = DBG_HwInitializationData("Parent::DBG_Raidport")
        self.gTransportHwInitializationData  = DBG_HwInitializationData("Parent::DBG_Raidport")
        self.m_stack = DBG_CallStackRawPrinter("Parent::DBG_Raidport",self)
        self.m_stack_short = DBG_CallStackRawPrinter("Parent::DBG_Raidport",self)
        self.m_wcdl_lib = DBG_WcdlLibrary("Parent::DBG_Raidport",self)
        
        self.x_dbg("DBG_Raidport::__init__::out::")
        
    def init_raidport_fields(self):
        self.x_dbg("DBG_Raidport::init_raidport_fields::in:")
        self.m_fields.add_fields_int_array(["mNumPaths","mNumTargets"])
        self.m_fields.add_fields_asstr_ints(["mCrashdumpHibernateMode"
                                             ,"mIsPaused"
                                             ,"mEnumerationState"
                                             ,"mFreezes"
                                             ,"mReenumerate"
                                             ,"mPowerState"
                                             ,"mPnpState"
                                             ,"mStorDevicePowerState"
                                             ,"mStorPowerAction"
                                             ,"mForcePassthrough"
                                             ,"mGoingToHibernate"
                                             ,"mFirstCrashHiberWriteIo"
                                             ,"mFirstCrashHiberReadIo"
                                             ,"mStatsHiberReadsHdd"
                                             ,"mStatsHiberReadsSsd"
                                             ,"mStatsHiberWritesSsd"
                                             ,"mStatsHiberStartIo"
                                             ,"mStatsHiberInitNvIo"
                                             ,"mStatsHiberFinializeNvIo"
                                             ,"mStatsHiberScsiIo"
                                             ,"mStatsHiberReadIo"
                                             ,"mStatsHiberWriteIo"
                                             ,"mStatsHiberPausedIo"
                                             ,"mStatsHiberPassthruIo"
                                             ,"mStatsHiberDisabledCache"                                             
                                             ])
        
        if( DBG_PrintConfig().getItem().m_is_soft_remap == 0 ):
            self.m_fields.add_fields_asstr_ints(["mSsdFound"])

        self.x_dbg("DBG_Raidport::init_raidport_fields::out:")
        
    def prepare_object_global(self):
        try:
            self.x_dbg("DBG_Raidport::prepare_object_global::in::")            
            self.xx_set_lg_compute_phy_addr( "iastora!g_raidport" )
            self.x_dbg("DBG_Raidport::prepare_object_global::out:")
        except:
            self.xx_exception("DBG_Raidport::prepare_object_global::exception::")
            
    def prepare_object(self):
        try:
            self.x_dbg("DBG_Raidport::prepare_object::in::")
            if(self.prepare_check() == 1):
                return
            self.m_config.prepare_object()
            if(self.xx_is_object() == 1):
                self.m_fields.initialize_by_parent(self)
                
                if(DBG_PrintConfig().getItem().get_print_driver() == 1):
                    self.m_driver.xx_inc_tabs(self); 
                    self.m_driver.xx_compute_phy_by_parent(self,"mDriver")
                    self.m_driver.prepare_object()
                
                self.m_port_conf.xx_inc_tabs(self); 
                self.m_port_conf.xx_compute_arr_phy_by_parent(self,"mPortConfiguration")
                self.m_port_conf.prepare_object()
                
                if(DBG_PrintConfig().getItem().get_print_raidism() == 1):
                    self.m_raidism.xx_inc_tabs(self); 
                    self.m_raidism.xx_compute_phy_by_parent(self,"mRaidIsm")
                    self.m_raidism.prepare_object()
            
                
                    
                if(DBG_PrintConfig().getItem().get_print_raid_rtargets() == 1):
                    self.mNumPaths = DBG_MemoryTools().xx_get_int(self,"mNumPaths")
                    self.mNumTargets = DBG_MemoryTools().xx_get_int(self,"mNumTargets")
                    
                    self.m_raidport_targets.set_parent(self
                                               ,self.mNumPaths
                                               ,self.mNumTargets)                    
                    self.m_raidport_targets.set_addr(self,"SELF")
                    self.m_raidport_targets.prepare_object()
                
                if(DBG_PrintConfig().getItem().get_print_raid_transport() == 1):                           
                    self.mTransport.xx_inc_tabs(self); 
                    self.mTransport.xx_compute_phy_by_parent(self,"mTransport")
                
                    
                if(DBG_PrintConfig().getItem().get_print_raid_lock() == 1):    
                    self.mSpinLock.set_addr_arr(self,"mSpinLock")
                    self.mSpinLock.prepare_object()
                    
                self.mIsmTimer.set_addr_arr(self,"mIsmTimer")
                self.mIsmTimer.prepare_object()
                
                self.mIsmTimerBase.set_addr_arr(self,"mIsmTimer")
                self.mIsmTimerBase.prepare_object()
                
                self.mSuspendEvent.set_addr_arr(self,"mSuspendEvent")
                self.mSuspendEvent.prepare_object()
                
                self.mShutdownEvent.set_addr_arr(self,"mShutdownEvent")
                self.mShutdownEvent.prepare_object()
                
                self.mHwInitializationData.set_addr_arr(self,"mHwInitializationData")
                self.mHwInitializationData.prepare_object()

                self.gHwInitializationData.set_addr_arr_static(self,"gHwInitializationData")
                self.gHwInitializationData.prepare_object()

                self.gTransportHwInitializationData.set_addr_arr_static(self,"gTransportHwInitializationData")
                self.gTransportHwInitializationData.prepare_object()

                self.m_wcdl_lib.set_addr_static(self,"Wcdl::Library::sInstance")
                self.m_wcdl_lib.prepare_object()
                
                if(DBG_PrintConfig().getItem().get_print_stacks() == 1):        
                    self.m_stack.set_parent(self)
                    self.m_stack_short.set_format("full")
                    self.m_stack.prepare_object()
                    
                    self.m_stack_short.set_parent(self)
                    self.m_stack_short.set_format("short")
                    self.m_stack_short.prepare_object()
                
                
            self.x_dbg("DBG_Raidport::prepare_object::out:")
        except:            
            self.xx_exception("DBG_Raidport::prepare_object")
            
    def print_object(self,sdbg=""):
            try:
                    self.xx_print_start("")
                    self.print_object_internal(sdbg)
                    self.xx_print_end("")
            except:
                    self.xx_exception("::print_object")
                                
    def print_object_internal(self,sdbg=""):
        try:
            self.x_dbg("DBG_Raidport::print_object::in::")
            
            self.prepare_object()
            
            self.xx_print_ptr("")
            self.m_config.print_object()
            if(self.xx_is_object() == 1):
                
                self.m_fields.print_object()
                                    
                if(DBG_PrintConfig().getItem().get_print_raid_rtargets() == 1):                        
                    self.m_raidport_targets.print_object()
                                    
                self.m_port_conf.print_object()
                
                if(DBG_PrintConfig().getItem().get_print_driver() == 1):
                    self.m_driver.print_object()

                if(DBG_PrintConfig().getItem().get_print_raidism() == 1):                
                    self.m_raidism.print_object()
                
                if(DBG_PrintConfig().getItem().get_print_raid_transport() == 1):                    
                    self.mTransport.print_object()
                    
                if(DBG_PrintConfig().getItem().get_print_raid_lock() == 1):
                    self.mSpinLock.print_object()
                    
                self.mIsmTimer.print_object()
                self.mIsmTimerBase.print_object()
                
                self.mSuspendEvent.print_object()
                self.mShutdownEvent.print_object()
                
                self.mHwInitializationData.print_object()
                
                self.gHwInitializationData.print_object()
                self.gTransportHwInitializationData.print_object()
                self.m_wcdl_lib.print_object()
                
                if(DBG_PrintConfig().getItem().get_print_stacks() == 1):        
                    self.m_stack.print_object()
                    self.m_stack_short.print_object()
                
            self.x_dbg("DBG_Raidport::print_object::out::")
        except:
            self.xx_exception("DBG_Raidport::prepare_object")
        
        
    def print_object_global(self):
        self.x_dbg("DBG_Raidport::print_object_global::out::")
        self.prepare_object_global()        
        self.prepare_object()        
        self.print_object()
        self.x_dbg("DBG_Raidport::print_object_global::out::")
        
    def get_methods(self):
                self.xx_dbg("DBG_BreakpRaidport::get_methods::method_in::")
                pp=["RaidportBuildIo"
                    ,"RaidportAdapterControl"
                    ,"RaidportInitialize"
                    ,"RaidportStartIo"
                    ,"RaidportInterrupt"
                    ,"RaidportResetBus"
                    ,"RaidportCrashHiberBuildIo"
                    ,"RaidportAdapterControl"                    
                    ,"RaidportCrashHiberInterrupt"
                    ,"RaidportCrashHiberStartIo"
                    ,"RaidportInitialize"
                    ]
                self.xx_dbg("DBG_BreakpRaidport::get_methods::method_out::")
                return pp
