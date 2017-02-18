import sys
import defines
import logging
from pykd import *
from defines import *
from proc_utils import *
def print_storport_summary():
    print 'Information taken from Storport'
    try:
                
            output = dbgCommand("!devnode 0 1 storahci").split(' ')
            pdo = 0
            found_iastora = False
            for i,word in enumerate(output) :
                    if 'storahci' in word:
                            break
                    if  word == 'PDO':
                            pdo = output[i+1]

            print 'pdo ',pdo		
            output = dbgCommand("!devstack "+ str(pdo)).split(' ')
            print output
            raidport_ext = 0
            for i,word in enumerate(output) :
                    if 'RaidPort0' in word:
                            raidport_ext = output[i-2]
                            break
            print 'raidport_ext ',raidport_ext
            print 'unit count ',getAsInt("@@c++(((storport!_RAID_ADAPTER_EXTENSION*)0x%s)->UnitList.Count)"%(raidport_ext))
            print 'last ',getAsPtr("@@c++(&((storport!_RAID_ADAPTER_EXTENSION*)0x%s)->UnitList.List)"%(raidport_ext))
            last_unit = getAsPtr("@@c++(&((storport!_RAID_ADAPTER_EXTENSION*)0x%s)->UnitList.List)"%(raidport_ext))
            print 'first ',getAsPtr("@@c++(((storport!_RAID_ADAPTER_EXTENSION*)0x%s)->UnitList.List.Blink)"%(raidport_ext))
            first_unit = getAsPtr("@@c++(((storport!_RAID_ADAPTER_EXTENSION*)0x%s)->UnitList.List.Flink)"%(raidport_ext))
            actual_unit = int(first_unit,16)
            last_unit = int(last_unit,16)
            print actual_unit
            ### Loop over units
            while actual_unit != last_unit:
                    unit_ext = actual_unit-0x30
                    print 'unit at address %x'%(unit_ext)
                    timeout = getAsHex("@@c++(((storport!_RAID_UNIT_EXTENSION*)0x%s)->PendingQueue->Queues[0].Timeout)"%('%x'%(unit_ext)))
                    print '\tTimeout ',timeout
                        
                        
                    ### loop over pending request 
                    last_request = getAsPtr("@@c++(&((storport!_RAID_UNIT_EXTENSION*)0x%s)->PendingQueue->Queues[0].List)"%('%x'%(unit_ext)))
                    #print 'first request ',getAsPtr("@@c++(((storport!_RAID_UNIT_EXTENSION*)0x%s)->PendingQueue->Queues[0].List.Blink)"%('%x'%(unit_ext)))
                    first_request = getAsPtr("@@c++(((storport!_RAID_UNIT_EXTENSION*)0x%s)->PendingQueue->Queues[0].List.Flink)"%('%x'%(unit_ext)))
                    actual_request = int(first_request,16)
                    last_request = int(last_request,16)
                        
                    while actual_request != last_request:
                            request_ext = actual_request-0x30
                            print '\trequest at address %x'%(request_ext)
                            #timeout = getAsHex("@@c++(((storport!_RAID_UNIT_EXTENSION*)0x%s)->PendingQueue->Queues[0].Timeout)"%('%x'%(request_ext)))
                            #print 'Timeout ',timeout
                                
                            srb_function = getAsHex("@@c++(((storport!_EXTENDED_REQUEST_BLOCK *)0x%s)->Srb->Function)"%('%x'%(request_ext)))
                            print '\t SRB ',getAsPtr("@@c++(((storport!_EXTENDED_REQUEST_BLOCK *)0x%s)->Srb)"%('%x'%(request_ext)))
                            srb = getAsPtr("@@c++(((storport!_EXTENDED_REQUEST_BLOCK *)0x%s)->Srb)"%('%x'%(request_ext)))
                            irp = getAsPtr("@@c++(((storport!_EXTENDED_REQUEST_BLOCK *)0x%s)->Irp)"%('%x'%(request_ext)))
                            link('\t','!irp 0x%s'%(irp),'Irp')
                            link('\t','!storsrb 0x%s'%(srb),'Srb')
                            scsi_iop = getAsHex("@@c++(((storport!_EXTENDED_REQUEST_BLOCK *)0x%s)->Srb->Cdb[0])"%('%x'%(request_ext)))
                            print '\tsrb function ',srb_function,' scsiop ',scsi_iop
                            actual_request = getAsPtr("@@c++(((storport!_LIST_ENTRY*)0x%s)->Flink)"%('%x'%(actual_request)))
                            actual_request = int(actual_request,16)
                                
                        
                    actual_unit = getAsPtr("@@c++(((storport!_LIST_ENTRY*)0x%s)->Flink)"%('%x'%(actual_unit)))
                    actual_unit = int(actual_unit,16)
    except:
            print '=========================exception occured================='
            logging.exception('')
            print '==========================================================='
            return
