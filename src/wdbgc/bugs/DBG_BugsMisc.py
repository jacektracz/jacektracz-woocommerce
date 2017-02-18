import sys
import os
import logging
from .. DBG_AdapterBase import *       
from .. helpers.DBG_Utils import *

class DBG_BugsMisc(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "Driver" )
                self.xx_set_full_class_name ( "iastora!Wcdl::Driver" )
                self.major_version = "";               
                
        def print_object(self):
                self.m_remapport.xx_inc_tabs( self,"DBG_Misc")                
                self.m_remapport.print_object()
                
        def bp_nvme(self):
                DBG_Utils().xx_safe_exe("bp NvmePort::processGetFeaturesIoctl")
                DBG_Utils().xx_safe_exe("bp iastora!NvmePort::processGetFeaturesIoctl")
                DBG_Utils().xx_safe_exe("bp SecPortStartIo")
                DBG_Utils().xx_safe_exe("bp NvmePort::processNvmIoctl")

        def bsod_classes_old(self):
                comm_info("bsod_classes","")
                
                dd_driver = DBG_IADriver()
                dd_driver.xx_set_phy_addr("ffffe000ab937510")
                
                dd_adaext = DBG_AdapterExt()
                dd_adaext.xx_set_phy_addr("ffffe000ac52e1a0")
                
                dd_devobj = DBG_DeviceObj()
                dd_devobj.xx_set_phy_addr("ffffe000ac52e050")
                
                dd_kd = DBG_storagekd("ffffe000ab937510","ffffe000ac52e1a0","ffffe000ac52e050")
                dd_kd.m_unit.xx_set_phy_addr("ffffe000ac466650")
                dd_kd.xx_disp_adapters()
                dd_kd.xx_disp_adapter()
                dd_kd.xx_disp_storloglist()
                dd_kd.xx_disp_unit()
        
        
        def bsod_classes(self):
                comm_info("bsod_classes","")
        
                dd_pp = DBG_proc()
                dd_pp.m_kd.xx_disp_adapters()
                dd_pp.m_kd.xx_disp_adapter()
                dd_pp.m_kd.xx_disp_unit()
                dd_pp.m_kd.xx_disp_storloglist()
        
        def bsod_4938847(self):
                
                
                #DBG_Utils().xx_safe_exe('!analyze -v','CHECK_SYM')
                
                DBG_Utils().xx_safe_exe('!chksym iastora','CHECK_SYM')
        
                DBG_Utils().xx_safe_exe('vertarget','[INIT__2]')
        
                DBG_Utils().xx_safe_exe('!lmi storport','[INIT__2]')
        
                DBG_Utils().xx_safe_exe('.reload storport.sys','[INIT__2]')
        
                DBG_Utils().xx_safe_exe('dd nt!kd_default_mask','[INIT__2]')
        
                DBG_Utils().xx_safe_exe('!lmi nt','[INIT__2]')
        
                DBG_Utils().xx_safe_exe('.reload ntoskrnl.exe','[INIT]')
                DBG_Utils().xx_safe_exe('!poaction','[POWER_STATE]')
                
                DBG_Utils().xx_safe_exe('!storagekd.storadapter','Display adapters[II__1]')
                
        #        comm_info("
        #Driver                 Object            Extension          State
        #-----------------------------------------------------------------
        #\Driver\iaStorA        ffffe000ac52e050  ffffe000ac52e1a0   Working
        #                  
        #                  ")
        
                          
                DBG_Utils().xx_safe_exe('!storagekd.storadapter ffffe000ac52e1a0','Display adapter 0xffffe000ac52e1a0 [DeviceObj : ffffe000ac52e050   AdapterExt: ffffe000ac52e1a0   DriverObj :  ffffe000ab937510][II__2]')
                DBG_Utils().xx_safe_exe('!storagekd.storloglist ffffe000ac52e1a0','AdapterExt[storloglist][II__9]')
                DBG_Utils().xx_safe_exe('!storagekd.storloglist ffffe000ac52e050','DeviceObj[storloglist][II__5]')
                #DBG_Utils().xx_safe_exe('!storagekd.storloglist ffffe000ab937510','DriverObj[storloglist][Invalid device obj]')        
                DBG_Utils().xx_safe_exe('!storagekd.storsrb ffffe000ac52e1a0','AdapterExt SRB[II__6]')        
                DBG_Utils().xx_safe_exe('!storagekd.storlogirp ffffe000ac52e1a0 0xffffe000bd9b1330','[II__7]')
                DBG_Utils().xx_safe_exe('!storagekd.storsrb ffffe000bb3ae4f0','[II__8]')
                DBG_Utils().xx_safe_exe('!storagekd.storunit 0xffffe000ac466650','[UNIT][II__B1]')
                DBG_Utils().xx_safe_exe('!storagekd.storsrb ffffe000bb3ae4f0','SRB=>UNITTIMEOUT[II__8]')
        
        
                DBG_Utils().xx_safe_exe('!storagekd.storsrb ffffe000bc5ad290','QUEUED')
                DBG_Utils().xx_safe_exe('!storagekd.storsrb ffffe000bb3ae4f0','COMPLETED')
                DBG_Utils().xx_safe_exe('!storagekd.storsrb ffffe000ac4f9720','LAST_EXECUTED')
                DBG_Utils().xx_safe_exe('!irp ffffe000bd9b1330','IRP')
                DBG_Utils().xx_safe_exe('!irp ffffe000badb8380','IRP')
        
                DBG_Utils().xx_safe_exe('!storagekd.storclass fffffa80043dc060 1','IRP')
                all_info = 0
                if(all_info == 1):
                        DBG_Utils().xx_safe_exe('!drvobj ffffe000ab937510','taken from DriverObj :  ffffe000ab937510][II__2][NOt_FOUND]')
                        DBG_Utils().xx_safe_exe('!drvobj ffffe000ac52e050',' [DeviceObj : ffffe000ac52e050]')
                #DBG_Utils().xx_safe_exe('!irp ffffe000bd9b1330','IRP')
                comm_info("RAIDPORT","")
                
                inf_raidport()
                
                comm_info("RAIDPORT-END","")
                
        def run_01(self):
                
                print "last srbs path = srb command"
                DBG_Utils().xx_safe_exe('!irp ffffe000bd9b1330','IRP')
                DBG_Utils().xx_safe_exe('!irp ffffe000badb8380','IRP')
        
                print "last srbs path"
                DBG_Utils().xx_safe_exe('!srb ffffe000ac4f9720 ','SRB')
                DBG_Utils().xx_safe_exe('!srb ffffe000af1c1300 ','SRB')
        
                DBG_Utils().xx_safe_exe('!srb ffffe000ba7971d0','SRB')
                DBG_Utils().xx_safe_exe('!srb ffffe000af1c1300 ','SRB')
                
                DBG_Utils().xx_safe_exe('!srb ffffe000bc5ad290','SRB')
                DBG_Utils().xx_safe_exe('!srb 0xffffe000bb3ae4f0','SRB')
        
        
        def run_srbs_path(self):
                print "last srbs path==storagekd"
        
                DBG_Utils().xx_safe_exe('!storagekd.storsrb ffffe000ac4f9720 ','SRB')
                DBG_Utils().xx_safe_exe('!storagekd.storsrb ffffe000af1c1300 ','SRB')
        
                DBG_Utils().xx_safe_exe('!storagekd.storsrb ffffe000ba7971d0','SRB')
                DBG_Utils().xx_safe_exe('!storagekd.storsrb ffffe000af1c1300 ','SRB')
                
                DBG_Utils().xx_safe_exe('!storagekd.storsrb ffffe000bc5ad290','SRB')
                DBG_Utils().xx_safe_exe('!storagekd.storsrb 0xffffe000bb3ae4f0','SRB')
                dd =512-453
                DBG_Utils().xx_safe_exe('!storagekd.storloglist ffffe000ac52e050 0 200 100','SRB')
                DBG_Utils().xx_safe_exe('!irp 0xffffe000bd9b1330','SOME_IRP')
                
                print "[1131]_[19:00:57.674] HwStorBuildIo......... SRB  : 0xffffe000ac4ac798 [FLUSH] (0/0/0), IRP: 0xffffe000bb7a59e0"
                DBG_Utils().xx_safe_exe('!irp 0xffffe000bb7a59e0','IRP_FLUSH')
                
        def test_prime(self):
                DBG_Utils().xx_safe_exe("bp iaStorA!RpiPauseDevice","")
                
        def run_all(self):
                #bp NvmePort::processGetFeaturesIoctl
                self.bsod_4938847()
                self.exec_run()
                self.run_srbs_path()

        def run_dispatch(s_arg):
                run=0
                if s_arg == 'spath':
                        DBG_BugsMisc().run_srbs_path()
                        run = 1
        
                if s_arg == 'ia':
                        DBG_BugsMisc().exec_run()
                        run = 1
        
                if s_arg == 'all':
                        DBG_BugsMisc().run_all()
                        run = 1
        
                if s_arg == 'stor':
                        DBG_BugsMisc().print_storport_summary()
                        run = 1
        
                if s_arg == 'cl':
                        DBG_BugsMisc().bsod_classes()
                        run = 1
        
                if s_arg == 'inte':
                        dd_ii = DBG_interrupt()
                        dd_ii.print_interrupt_configuration()
                        run = 1                
        
                if s_arg == 'slist':
                    dd_pp = DBG_Proc()
                    dd_pp.m_kd.xx_disp_storloglist()
                    run = 1   
        
                if s_arg == 'en':
                    dd_pp = DBG_CheckEnv()
                    dd_pp.xx_chk_env()
                    run = 1   
        
                if s_arg == 'w2':
                    #DeviceObj : ffffe0001f991050   AdapterExt: ffffe0001f9911a0   DriverObj :  ffffe0001edd4400
                    dd_pp = DBG_storagekd("","","")
                    dd_pp.set_objects("ffffe0001f991050","ffffe0001f9911a0","ffffe0001edd4400")
                    dd_pp.xx_disp_storloglist()
                    run = 1
                    
                if s_arg == 'wkli':
                    # DeviceObj : ffffe000ac52e050   AdapterExt: ffffe000ac52e1a0   DriverObj :  ffffe000ab93751
                    dd_pp2 = DBG_storagekd("","","")
                    dd_pp2.set_objects("ffffe000ac52e050","ffffe000ac52e1a0","ffffe000ab93751")
                    dd_pp2.xx_disp_storloglist()
                    run = 1
                    
                    #DeviceObj : ffffe000ac52e050   AdapterExt: ffffe000ac52e1a0   DriverObj :  ffffe000ab937510
                      
                if s_arg == "ee":
                    DBG_DbgEntry().print_object()	           
                    run = 1
                    
                #if s_arg =="m":
                #	DBG_Menu().print_menu()
                #	run = 1
                    
                if s_arg == 'h':
                    print "spath ia all stor cl inte slist "
                    run = 1
                    
                if s_arg == 'bg':
                    # DeviceObj : ffffe000ac52e050   AdapterExt: ffffe000ac52e1a0   DriverObj :  ffffe000ab93751
                    dd_pp2 = DBG_Bugs("","","")
                    dd_pp2.set_objects("ffffe000ac52e050","ffffe000ac52e1a0","ffffe000ab93751")
                    dd_pp2.xx_disp_storloglist()
                    run = 1
        
                #if run == 0:
                 #       run_all()
