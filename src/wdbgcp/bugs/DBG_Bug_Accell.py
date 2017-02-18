import sys
import os
import logging
from .. .. wdbgc.DBG_AdapterBase import *       
from .. .. wdbgc.helpers.DBG_Utils import *
from .. .. wdbgc.storagekd.DBG_storagekd import *
from .. bugs.DBG_BugsBase import *

class DBG_Bug_Accell(DBG_BugsBase):
        def __init__(self,spar):                
                DBG_BugsBase.__init__(self,spar)
                self.xx_set_class_name ( "DBG_Bug_Accell" )
                self.xx_set_full_class_name ( "iastora!" )
                self.major_version = "";               
                self.m_type = "all"
        def print_object(self):
                self.m_remapport.xx_inc_tabs( self,"DBG_Driver")                
                self.m_remapport.print_object()
                
        def bp_nvme(self):
                DBG_Utils().xx_safe_exe("bp NvmePort::processGetFeaturesIoctl","")
                DBG_Utils().xx_safe_exe("bp iastora!NvmePort::processGetFeaturesIoctl","")
                DBG_Utils().xx_safe_exe("bp SecPortStartIo","")
                DBG_Utils().xx_safe_exe("bp NvmePort::processNvmIoctl","")

        def exec_bug(self,s_arg_0,smethod=""):
                self.m_type = "long"                
                self.m_type = "normal"
                self.m_type = "set"
                self.m_type = "bp"
                types = ["er-main","long","normal","set","bp","set","bp","bpm","info","err"]
                self.m_type = "stor"
                if(smethod != ""):
                        self.m_type = smethod
                self.exec_bug_internal(
                        self.m_type)
                
        def exec_bug_internal(self,stype):
                if(stype == "stlog" ):
                        DBG_Utils().xx_safe_exe("!storagekd.storadapter","")
                        DBG_Utils().xx_safe_exe("!storadapter ffffe000a0d1a1a0","")
                        
                        dd_pp2 = DBG_storagekd("","","")
                        #DeviceObj : ffffe00174935050   AdapterExt: ffffe001749351a0   DriverObj :  ffffe00173fdd7f0 
                        dd_pp2.set_objects("ffffe00174935050","ffffe000a0d1a1a0","ffffe00173fdd7f0")
                        dd_pp2.xx_disp_storloglist()
                
                if(stype == "stor"):
                        DBG_Utils().xx_safe_exe("!storagekd.storadapter","")
                        DBG_Utils().xx_safe_exe("!storadapter ffffe000d0fd61a0","")
                        dd_pp2 = DBG_storagekd("","","")                        
                        
                        dd_pp2.set_objects("ffffe000d0fd6050","ffffe000d0fd61a0","ffffe000d0fe2c60")
                        dd_pp2.xx_disp_storloglist()
                        
                        #DBG_Utils().xx_safe_exe('!storagekd.storsrb 0xffffe0017c130b80','SRB')
                        
                        #DBG_Utils().xx_safe_exe('!storagekd.storsrb 0xffffe0017b44f510','SRB')
                
                if(stype == "all"):
                        DBG_Utils().xx_safe_exe('!stacks 2 iastora','STACKS')
                        DBG_Utils().xx_safe_exe('!analyze -v',"analyze")

                if(stype== "set"):
                
                        DBG_Utils().xx_safe_exe('ed Kd_IHVVIDEO_Mask 0x8',"set")
                        
                        DBG_Utils().xx_safe_exe('ed Kd_storminiport_mask f',"set")
                        
                if(stype== "bp"):
                        DBG_Utils().xx_safe_exe("bp NvmePort::processGetFeaturesIoctl","")
                        DBG_Utils().xx_safe_exe("bp iastora!NvmePort::processGetFeaturesIoctl","")
                        DBG_Utils().xx_safe_exe("bp SecPortStartIo","")
                        DBG_Utils().xx_safe_exe("bp NvmePort::processNvmIoctl","")
                        DBG_Utils().xx_safe_exe("bp CfgRaidDev::setNvCachePolicyAction","")
                        DBG_Utils().xx_safe_exe("bp CfgArray::doVolAction","")
                        DBG_Utils().xx_safe_exe("bp CfgArray::gotVolActionsArrayLock","")
                        #DBG_Utils().xx_safe_exe("bp EventQueue::drainQueue","")
                        DBG_Utils().xx_safe_exe("bp RemapPort::callStartIoWithPathIdMap","")
                        DBG_Utils().xx_safe_exe("bp RaidRequest::start","")
                        DBG_Utils().xx_safe_exe("bl","")
                        DBG_Utils().xx_safe_exe("ba 1","")
                        DBG_Utils().xx_safe_exe("bd 1","")
                        DBG_Utils().xx_safe_exe("bl","")
                        
                if(stype== "bpm"):        
                        DBG_Utils().xx_safe_exe("bp iaStorA!CfgRaidDev::setNvCachePolicyAction+0x1e","start cache")
                        DBG_Utils().xx_safe_exe("bp iaStorA!CfgRaidDev::setNvCachePolicyAction+0x321","stop cache")
                        DBG_Utils().xx_safe_exe("bp iaStorA!EventQueue::drainQueue+0x27","queue")
                        DBG_Utils().xx_safe_exe("bl","")
                        
                if(stype== "err"):                                
                        DBG_Utils().xx_safe_exe("bp RaidRequest::createPNPAddress","err method")
                        DBG_Utils().xx_safe_exe("bp NvCacheMgr::replenishFreePrb","err method")
                        
                if(stype== "ptl"):                                        
                        DBG_Utils().xx_safe_exe("bp RaidCfgMgr::trigger","errptl")
                        DBG_Utils().xx_safe_exe("bp NvCacheMgr::printResourceTable"
                                                ,"errptl[d:\rst\src_15.0.0.1010.d2\irst\sse_storage\driver\source\ism\nvrwcache.cpp]")                        
                        DBG_Utils().xx_safe_exe("bp CfgRaidDev::setNvCachePolicyAction","b1")
                        DBG_Utils().xx_safe_exe("bp RaidCfgMgr::doDiskAction","b2")
                        DBG_Utils().xx_safe_exe("bp CfgRaidDev::setMenuAction","b3")
                        
                if(stype== "del"):
                        DBG_Utils().xx_safe_exe("bp RaidIsm::deleteRaidDev","b4")
                        DBG_Utils().xx_safe_exe("bp RaidDev::noticeDelet","b4")
                        DBG_Utils().xx_safe_exe("bp RaidIsm::deleteRaidDev","b4")
                        DBG_Utils().xx_safe_exe("bp RaidIsm::volumeDeletedDone","b4")
                        DBG_Utils().xx_safe_exe("bp RaidCfgMgr::volumeDeleted","b4")
                        
                if(stype== "dbg_bug"):
                        DBG_Utils().xx_safe_exe("bp iaStorA!RaidCfgMgr::trigger+0x3fa","create volume")
                        DBG_Utils().xx_safe_exe("bp RaidCfgMgr::gotSemsForCreateVol","b4")
                        DBG_Utils().xx_safe_exe("bp RaidCfgMgr::createNewRaidDev","b4")
                        DBG_Utils().xx_safe_exe("bp RaidIsm::generatePtl","b4")
                        DBG_Utils().xx_safe_exe("bp iaStorA!RaidIsm::generatePtl+0x14b","root cause")
                        
                if(stype== "dbg_root"):
                        DBG_Utils().xx_safe_exe("bp iaStorA!RaidIsm::generatePtl+0x14b","root cause")
                        DBG_Utils().xx_safe_exe("bp Raidport::startIsm","root cause")
                        DBG_Utils().xx_safe_exe("bp isSystemPtl","root cause")
                        DBG_Utils().xx_safe_exe("bp iaStorA!RaidIsm::generatePtl+0x19","root cause")
                        DBG_Utils().xx_safe_exe("bp iaStorA!host::isSystemPtl+0x17","root cause")
                        DBG_Utils().xx_safe_exe("bp iaStorA!Raidport::getSystemDeviceTarget+0x9","root cause")
                        DBG_Utils().xx_safe_exe("bp Raidport::unitControl","root cause")
                        DBG_Utils().xx_safe_exe("bp iaStorA!Raidport::getSystemDeviceTarget+0x9","root cause")
                        DBG_Utils().xx_safe_exe("bp iaStorA!Raidport::unitControl+0x1c1","root cause")
                        DBG_Utils().xx_safe_exe("bp iaStorA!Raidport::unitControl+0x242","root cause")
                        DBG_Utils().xx_safe_exe("bp iaStorA!volport::VolPort::unitControl","root cause")
                        DBG_Utils().xx_safe_exe("bp Raidport::revertToPassthroughTarget","root cause")
                        
                if(stype== "dbg_raidinit"):                        
                        DBG_Utils().xx_safe_exe("bp iaStorA!RaidIsmInitialize","root cause[sse_storage\..\ism\hostismintf.cpp]")
                        DBG_Utils().xx_safe_exe("bp iaStorA!RaidIsmGetInitParms","root cause[sse_storage\..\ism\hostismintf.cpp]")
                        DBG_Utils().xx_safe_exe("bp Raidport::startIsm","sse_storage_raidport\..\raidport.cpp")
                        
                if(stype== "info"):                
                        print self.get_str_dbg()
                run = 1
                
        def get_str_dbg(self):
                
                ccs = """
                SUMMARY
                !py C:\lkd\komodo\w2\src\w2\rst_windbg_ext.py er del
                Critical error detected c0000374
                [ETW_AHCI] MiniportParameters::readRegistryParameters - Parameter Out of Range: HybridHintReset != 0, NOT set!
                
                
                ULONG RaidRequest::createPNPAddress
                KDTARGET:
                """
                ccs = ccs + """
        [232]_[04:30:58.134] HwStorBuildIo......... SRB  : 0xffffe0017c1c8c70 [EXECUTE SCSI][SCSI/SEND EVENT][QueueAction: 0x00][QueueTag: 0xFE] (0/2/0), IRP: 0xffffe0017c725b20
        [233]_[04:30:58.134] SpNotifyReqComplete... SRB  : 0xffffe0017c1c8c70 [EXECUTE SCSI][SCSI/SEND EVENT][Invalid request][SCSISTAT 0x00] (0/2/0), IRP: 0xffffe0017c725b20
        [234]_[04:30:58.134] HwStorStartIo......... SRB  : 0xffffe0017c1c8c70 [EXECUTE SCSI][SCSI/SEND EVENT][QueueAction: 0x00][QueueTag: 0xFE] (0/2/0), IRP: 0xffffe0017c725b20
        [235]_[04:30:58.134] HwStorBuildIo......... SRB  : 0xffffe0017c130b80 [EXECUTE SCSI][SCSI/SEND EVENT][QueueAction: 0x00][QueueTag: 0xB2] (6/0/0), IRP: 0xffffe0017c725b20
        [236]_[04:30:58.134] SpNotifyReqComplete... SRB  : 0xffffe0017c130b80 [EXECUTE SCSI][SCSI/SEND EVENT][Error][SCSISTAT 0x02] (6/0/0), IRP: 0xffffe0017c725b20
        [237]_[04:30:58.134] HwStorStartIo......... SRB  : 0xffffe0017c130b80 [EXECUTE SCSI][SCSI/SEND EVENT][QueueAction: 0x00][QueueTag: 0xB2] (6/0/0), IRP: 0xffffe0017c725b20
        [238]_[04:30:58.134] HwStorBuildIo......... SRB  : 0xffffe0017b44f510 [IO CONTROL] (0/0/0), IRP: 0x0000000000000000                
                """
                ccs = ccs + """
        3: kd> !storagekd.storsrb 0xffffe0017c130b80
        Function 0xED [<invalid>] SRB: 0xffffe0017c130b80  OriginalRequest: 0x0000000500000005  DataBuffer/Length: 0xffffe0017c130b98 / 0x7C8D1740
        PTL: (224, 255, 255)  SRB Status: 7C [<invalid>]
                
                """
                ccs = ccs + """
        command: !storagekd.storsrb 0xffffe0017b44f510
        info: SRB


        Function 0xAE [<invalid>] SRB: 0xffffe0017b44f510  OriginalRequest: 0x0000000000000000  DataBuffer/Length: 0xffffe0017c8075c0 / 0x00000054
        PTL: (224, 255, 255)  SRB Status: 7C [<invalid>]

                
                """
                
                ccs = ccs + """
                
        C:\rst\src_15.0.0.1010\iRST\sse_storage\driver\source\ism\eventqueue.cpp
        void EventQueue::drainQueue()
        {
            Event *event;
        
            // Note we do not remove the event from the queue until after it has been
            // executed.
            while ((event = mQueue.first()) != nullptr) {
        
                event->callEvent();
        
                if (gKillThread) {
                    return;
                }
        
                // The event's execution is complete.  Now we can remove the event from
                //  the event FIFO - but only after acquiring the event queue's spinlock
                //  to protect against contention from another context adding events to
                //  the FIFO.
                host::LockHandle handle = host::LockHandle();
                host::acquireLock(handle);
                event = mQueue.getFirst();
                host::putBuffer(mEventBufferPool, event);
                host::releaseLock(handle);
        
                if (mStallCount) {
                    break;
                }
            }
        }

        
        
        c:\rst\src_15.0.0.1010\irst\sse_storage\driver\source\ism\cfgparms.cpp
        case RaidCfgMgr::SetNvCacheMode:
        result = cfgRaidDev->setNvCachePolicyAction((NvCacheMode) actionArg);
        if (result == Ok) {
            storeMpbNeeded = true;
        }
        cfgRaidDev->setMenuAction(RaidCfgMgr::NoneVolume);
        break;
                
                """
                return ccs;