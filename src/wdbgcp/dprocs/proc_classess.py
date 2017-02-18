import sys
import defines
import logging
from pykd import *
from defines import *
from proc_utils import *
                        
def print_bios_version():
	print "Information from Bios:"
	output = dbgCommand("!sysinfo smbios").split('\n')
	for i,word in enumerate(output) :
		if 'Product' in word:
			print word
		if 'BIOS Version' in word:
			print word

	

def processInfo():

   nt = module( "nt" )

   processList = typedVarList( nt.PsActiveProcessHead, "nt!_EPROCESS", "ActiveProcessLinks"  )

   for process in processList:
       print "".join( [chr(i) for i in process.ImageFileName if i != 0] )
#def print_srb(srb):
	
def exec_run():

	if not isWindbgExt():
		if not loadDump( sys.argv[1] ):
			dprintln( sys.argv[1] + " - load failed" )
			return

	if not isKernelDebugging():
		dprintln( "not a kernel debugging" )
		return  
	#if len(sys.argv)>1:
	#	if sys.argv[1] == 'storport':
	#		print_storport_summary()
	#	return  
	#processInfo()
	dbgCommand('.reload')
	#dbgCommand('s -[l6]sa fffff800`cf014000 fffff800`cf687000')
	symbol_info = dbgCommand('lm m iastora')
	#print symbol_info
	if "(no symbols)" in symbol_info:
		print 'No symbols loaded for iastora'
		output = dbgCommand('lm m iastora').split()
		if len(output) != 4:
			string_to_search = dbgCommand("s -[l6]sa %s %s"%(output[4],output[5])).split('\n')
			print len(string_to_search)
			for line in string_to_search:
				if len( line.split()) > 0:
					line_shortened = line.split()[1]
				if '14' in line_shortened:
					print line_shortened
		return
	
	raidport_address = getAddress('iastora!g_raidport')
	ahci_controller = getAsPtr('@@C++(iastora!g_raidport->mDriver->mDeviceExtensionList[3])')
	
        
	major_version = getAsInt('@@C++(iastora!g_raidport->mDriver->mFeatures.mDriverSupportTable.PRN_MajorVer)')
	minor_version = getAsInt('@@C++(iastora!g_raidport->mDriver->mFeatures.mDriverSupportTable.PRN_MinorVer)')
	hotfix_version = getAsInt('@@C++(iastora!g_raidport->mDriver->mFeatures.mDriverSupportTable.PRN_HotFix)')
	build_version = getAsInt('@@C++(iastora!g_raidport->mDriver->mFeatures.mDriverSupportTable.PRN_BuildNum)')
	#print_useful_command_links()
	print_bios_version()
	print "RST: ",major_version,'.',minor_version,'.',hotfix_version,'.',build_version
	#print "OS:  ",dbgCommand('?? @@C++(iastora!g_raidport->mDriver->mOsVersion)').split()[1]
	print "",dbgCommand('vertarget').split('\n')[0].strip(),'\n',dbgCommand('vertarget').split('\n')[1].strip()
	#print "Chipset: ",dbgCommand('?? @@C++(iastora!g_raidport->mDriver->mFeatures.currentChipset)').split()[1]
	platformDeviceID = int(getAsInt("@@C++(((iastora!AhciController*)0x%s)->mPlatformDeviceId)"%(ahci_controller)))
	print "Platform DeviceId: %s(%s)"%(ahci_controller_version_map[platformDeviceID],hex(platformDeviceID))	
	

	
	#res = dbgCommand('.printf "%p",iastora!g_raidport');
	#print raidport_address, ahci_controller
	link('','?? iastora!wcdl::DriverList::sDriver','DriverList')
	link('','?? iastora!g_raidport->mDriver','mDriver')
	link('','?? iastora!g_raidport->mDriver->mFeatures','DriverFeatures')
	link('','?? (iastora!secport::SecPort*)iastora!g_raidport->mDriver->mDeviceExtensionList[0]','SecPort')
	
	
	######## Printing RaidPort targets #########
	link('',"?? (iastora!raidport*)%s"%(raidport_address),'Raidport');
	print '\t',dbgCommand('?? iastora!g_raidport->mPowerState').strip()
	#print '\t',dbgCommand('?? iastora!g_raidport->mPowerSubstate')
	print '\t',dbgCommand('?? iastora!g_raidport->mPnpState').strip()
	#print '\t',dbgCommand('?? iastora!g_raidport->mPnpSubstate')
	print '\t',dbgCommand('?? iastora!g_raidport->mEnumerationState').strip()
	print '\tIs paused: ',getAsInt("@@C++(iastora!g_raidport->mIsPaused)")
	print '\tReenumerate: ',getAsInt("@@C++(iastora!g_raidport->mReenumerate)")
	print '\tFreezes: ',getAsInt("@@C++(iastora!g_raidport->mFreezes)")
	num_paths = getAsInt('@@c++(iastora!g_raidport->mNumPaths)')
	num_targets = getAsInt('@@c++(iastora!g_raidport->mNumTargets)')
	
	link('','?? (iastora!AhciController*)iastora!g_raidport->mDriver->mDeviceExtensionList[3]','AhciController');
	print "\tnumPath %i numTargets %i"%(num_paths,num_targets)
	print "\tports implemented %s"%(getAsHex("@@C++(((iastora!AhciController*)0x%s)->PortsImplemented)"%(ahci_controller)))
				
	print ''			
	######### Printing Ism  #######################
	link('','?? @@c++((iastora!RaidIsm*)iastora!g_raidport->mRaidIsm)','ISM');
	num_raid_devs = getAsInt("@@c++(((iastora!RaidIsm*)iastora!g_raidport->mRaidIsm)->numRaidDevs)")
	print '\tNumber of raid devs: ',num_raid_devs
	for i in range(num_raid_devs):
		raid_dev = getAsPtr("@@c++(((iastora!RaidIsm*)iastora!g_raidport->mRaidIsm)->raidDevs[%i])"%(i))
		link('\t',"?? @@c++(((iastora!RaidIsm*)iastora!g_raidport->mRaidIsm)->raidDevs[%i])"%(i),"RaidDev[%i]"%(i))
		link("\t\t","?? @@C++(((iastora!raiddev*)0x%s)->ioPathMgr)"%(raid_dev),"IOPathManager")
		ioPathMembers = getAsInt("@@C++(((iastora!raiddev*)0x%s)->ioPathMgr->ioPathMembers)"%(raid_dev))
		print '\t\t\tiopathmembers: ',ioPathMembers
		if ioPathMembers & IO_PATH_HAS_RAIDDEV:
			link("\t\t\t","?? @@C++(((iastora!raiddev*)0x%s)->ioPathMgr->raidDev)"%(raid_dev),"RaidDev")
		if ioPathMembers & IO_PATH_HAS_COALESCER:
			link("\t\t\t","?? @@C++(((iastora!raiddev*)0x%s)->ioPathMgr->ioCoalescer)"%(raid_dev),"Coalescer")
		if ioPathMembers & IO_PATH_HAS_VOL_CACHE:
			link("\t\t\t","?? @@C++(((iastora!raiddev*)0x%s)->ioPathMgr->volCache)"%(raid_dev),"Vol Cache")
		if ioPathMembers & IO_PATH_HAS_NV_CACHE:
			link("\t\t\t","?? @@C++(((iastora!raiddev*)0x%s)->ioPathMgr->nvCache)"%(raid_dev),"NV Cache")
		
		
		print "\t\tSerial number: %s" %(getAsStr("@@C++(((iastora!raiddev*)0x%s)->serialNo)"%(raid_dev)))
		print "\t\tRaid level: %s" %(getAsInt("@@C++(((iastora!raiddev*)0x%s)->raidVol->lowMap->raidLevel)"%(raid_dev)))
		print "\t\tNumber of disks: %s" %(getAsInt("@@C++(((iastora!raiddev*)0x%s)->array->numDisks)"%(raid_dev)))
		numDisks = getAsInt("@@C++(((iastora!raiddev*)0x%s)->array->numDisks)"%(raid_dev))
		for j in range(numDisks):
			print "\t\tDisk[%i]"%(j)
			print "\t\t\tVendor Info: %s" %(getAsStr("@@C++(((iastora!raiddev*)0x%s)->array->diskPtr[%i]->cldev->VendorInfo)"%(raid_dev,j)))
			print "\t\t\tDescription: %s" %(getAsStr("@@C++(((iastora!raiddev*)0x%s)->array->diskPtr[%i]->cldev->Description)"%(raid_dev,j)))
			print "\t\t\tSerial num: %s" %(getAsStr("@@C++(((iastora!raiddev*)0x%s)->array->diskPtr[%i]->cldev->serialNum)"%(raid_dev,j)))
			status = getAsInt("@@C++(((iastora!raiddev*)0x%s)->array->diskPtr[%i]->cldev->status)"%(raid_dev,j))
			for key,value in disk_state_map.iteritems():
				if status & value:
					print "\t\t\t",key
		print "\t\tNumber of RaidDevs: %s" %(getAsInt("@@C++(((iastora!raiddev*)0x%s)->array->numRaidDevs)"%(raid_dev)))
		link("\t\t","?? @@C++(((iastora!raiddev*)0x%s)->raidVol)"%(raid_dev),"RaidVol")
		print "\t\t\tState: %s" %(dbgCommand("?? @@C++(((iastora!raiddev*)0x%s)->raidVol->state)"%(raid_dev)).split()[1])
		print "\t\t\tMigration type: %s" %(dbgCommand("?? @@C++(((iastora!raiddev*)0x%s)->raidVol->migrType)"%(raid_dev)).split()[1])
		
	if getAsInt("@@c++(((iastora!RaidIsm*)iastora!g_raidport->mRaidIsm)->nvCacheMgr)") !=0 :
		for i in range(4):
			if getAsInt("@@c++(((iastora!RaidIsm*)iastora!g_raidport->mRaidIsm)->nvCacheMgr->attachedClients[%i])"%(i)) != 0:
				print '\tfound NVCache ',i
				link('\t',"?? @@c++(((iastora!RaidIsm*)iastora!g_raidport->mRaidIsm)->nvCacheMgr->attachedClients[%i])"%(i),"NVCache")
			

	print ''
	######### Printing RemapPort Transports #######################
	link('','?? (iastora!RemapPort*)iastora!g_raidport->mDriver->mDeviceExtensionList[2]','RemapPort');
	remapport_address = getAsPtr('@@c++(iastora!g_raidport->mDriver->mDeviceExtensionList[2])');

    #	
	for i in range(4):
		if(getAsInt("@@C++(((iastora!remapport*)0x%s)->mTransport[%i].mTransportOn)"%(remapport_address,i))!=0):
			link('\t',"?? @@C++(((iastora!remapport*)0x%s)->mTransport[%i])"%(remapport_address,i),"Transport[%i]"%(i))
			type = getAsInt("@@C++(((iastora!remapport*)0x%s)->mTransport[%i].mType)"%(remapport_address,i))
			output = dbgCommand("?? @@C++(((iastora!remapport*)0x%s)->mTransport[%i].mType)"%(remapport_address,i))
			print "\t\t",output.strip().split()[1]
			output = dbgCommand("?? @@C++(((iastora!remapport*)0x%s)->mTransport[%i].mInterface)"%(remapport_address,i))
			print "\t\t",output.strip().split()[1]
			#output = dbgCommand("?? @@C++(((iastora!remapport*)0x%s)->mTransport[%i].mInterruptMode)"%(remapport_address,i))
		#	print "\t\tCycleRouterIndex: ",getAsInt("@@C++(((iastora!remapport*)0x%s)->mTransport[%i].mCycleRouterIndex)"%(remapport_address,i))
			#print "\t\tInterrupt mode: ",output.strip().split()[1]
		#	print "\t\tMSIX offset: ",getAsInt("@@C++(((iastora!remapport*)0x%s)->mTransport[%i].mMSIxOffset)"%(remapport_address,i))
		#	print "\t\tNumOfMSsixInterruptsVectors: ",getAsInt("@@C++(((iastora!remapport*)0x%s)->mTransport[%i].mNumOfMSsixInterruptsVectors)"%(remapport_address,i))
		#	print "\t\tUseSharedInterruptVector: ",getAsInt("@@C++(((iastora!remapport*)0x%s)->mTransport[%i].mUseSharedInterruptVector)"%(remapport_address,i))
			if type == 2:
				link('\t\t',"?? @@C++((iastora!AhciController*)((iastora!remapport*)0x%s)->mTransport[%i].mDeviceExtension)"%(remapport_address,i),'AhciController')
			elif type == 3:
				link('\t\t',"?? @@C++((iastora!NvmePort*)((iastora!remapport*)0x%s)->mTransport[%i].mDeviceExtension)"%(remapport_address,i),'NvmePort')

			
	print ''
	
######### Printing AhciPorts #################
	link('','?? (iastora!AhciController*)iastora!g_raidport->mDriver->mDeviceExtensionList[3]','AhciController');
	
	for i in range(6):
		print 'PORT[',i,']'
		if(getAsInt("@@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine)"%(ahci_controller,i))!=0):
			
			print "\t\tDefault or registry HIPM: %i"%(getAsInt("@@C++(((iastora!AhciController*)0x%s)->mMiniportParameters.mParameters.HIPM[%i])"%(ahci_controller,i)))	
			print "\t\tDefault or registry DIPM: %i"%(getAsInt("@@C++(((iastora!AhciController*)0x%s)->mMiniportParameters.mParameters.DIPM[%i])"%(ahci_controller,i)))
			print "\t\tDefault or registry SIPM: %i"%(getAsInt("@@C++(((iastora!AhciController*)0x%s)->mMiniportParameters.mParameters.SIPM[%i])"%(ahci_controller,i)))
			print "\t\tDefault or registry ANEnable: %i"%(getAsInt("@@C++(((iastora!AhciController*)0x%s)->mMiniportParameters.mParameters.ANEnable[%i])"%(ahci_controller,i)))
		
			#print '\tnot nullptr port machine at port ',i
			link('\t',"?? (iastora!AhciPort*)@@C++(((iastora!AhciController*)0x%s)->mPort[%i])"%(ahci_controller,i),'AhciPort')
			print "\t\tgenStepDownCount: %i"%(getAsInt("@@C++(((iastora!ahciport*)((iastora!AhciController*)0x%s)->mPort[%i])->genStepDownCount)"%(ahci_controller,i)))
			print "\t\tPort Supports ZPODD: ",(dbgCommand("?? @@C++(((iastora!ahciport*)((iastora!AhciController*)0x%s)->mPort[%i])->mPortSupportsZpodd)"%(ahci_controller,i)))	.strip()
			print "\t\tZPODD Acpi capable: ",(dbgCommand("?? @@C++(((iastora!ahciport*)((iastora!AhciController*)0x%s)->mPort[%i])->mZpoddAcpiCapable)"%(ahci_controller,i))).strip()
			link('\t\t',"?? (iastora!PortStateMachine*)@@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine)"%(ahci_controller,i),'PortStateMachine')
			
			
			current_state = getAsInt("@@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine->mCurrentState)"%(ahci_controller,i))
			target_state = getAsInt("@@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine->mTargetState)"%(ahci_controller,i))
			current_state_string = getAsStrDbg("@@C++(iastora!DbgPortStateMachineStringMap[%s])"%(current_state))
			target_state_string = getAsStr("@@C++(iastora!DbgPortStateMachineStringMap[%s])"%(target_state))

			print "\t\t\tcurrent state: %s[%s] \n\t\t\ttarget state: %s[%s] "%(current_state_string,current_state,target_state_string,target_state)
			print "\t\t\tmCurrentMode: %s "%((dbgCommand("?? @@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine->mCurrentMode)"%(ahci_controller,i))).strip())
			print "\t\t\tmCurrentState: %s "%((dbgCommand("?? @@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine->mCurrentState)"%(ahci_controller,i))).strip())						
			print "\t\t\tmPreviousMode: %s "%((dbgCommand("?? @@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine->mPreviousMode)"%(ahci_controller,i))).strip())
			
			
			if target_state == 36 and current_state != 47:
				print '\t\tEnumerated disk' 
				end_device = getAsPtr("@@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mDevice)"%(ahci_controller,i))
				signature = getAsHex("@@C++(((iastora!EndDevice*)0x%s)->mSignature)"%(end_device))
				device_id_type = dbgCommand("?? @@C++(((iastora!EndDevice*)0x%s)->mDeviceIdType)"%(end_device))
				print '\t\tsignature: 0x',signature.strip(),'\n\t\tdevice_id_type: ',device_id_type.split()[1]
				if signature == '101':
					print '\t\tATA device'
					link('\t\t',"?? (iastora!AtaDevice*)0x%s"%(end_device),'AtaDevice');
					link('\t\t\t',"?? @@C++(((iastora!AtaDevice*)0x%s)->mIdentifyData)"%(end_device),'IdentifyData');
										
				elif signature == 'eb140101':
					print '\t\tATAPI device'
					if device_id_type == SataDeviceTypeAtapi:
						link('\t\t',"?? (iastora!AtapiDevice*)0x%s"%(end_device),'AtapiDevice');
						link('\t\t\t',"?? @@C++(((iastora!AtapiDevice*)0x%s)->mIdentifyData)"%(end_device),'IdentifyData')
						print "\t\t\tAsynchronous Notification is enabled: ",getAsInt("@@C++(((iastora!AtapiDevice*)0x%s)->mAsynchronousNotificationFeature.mIsEnabled)"%(end_device));
						print "\t\t\tAsynchronous Notification supported by device: ",getAsInt("@@C++(((iastora!AtapiDevice*)0x%s)->mIdentifyData.serial_ata_features_supported.asynchronous_notification)"%(end_device))
						print "\t\t\tDIPM supported by device: ",getAsInt("@@C++(((iastora!AtapiDevice*)0x%s)->mIdentifyData.serial_ata_features_supported.DIPM)"%(end_device))
						print "\t\t\tHIPM supported by device: ",getAsInt("@@C++(((iastora!AtapiDevice*)0x%s)->mIdentifyData.serial_ata_capabilities.hipm)"%(end_device))
					elif device_id_type == SataDeviceTypeAtapiZpodd:
						link('\t\t',"?? (iastora!ZpoddDevice*)0x%s"%(end_device),'ZpoddDevice');
						link('\t\t\t',"?? @@C++(((iastora!ZpoddDevice*)0x%s)->mIdentifyData)"%(end_device),'IdentifyData');
						print "\t\t\tAsynchronous Notification is enabled: ",getAsInt("@@C++(((iastora!ZpoddDevice*)0x%s)->mAsynchronousNotificationFeature.mIsEnabled)"%(end_device));
						print "\t\t\tAsynchronous Notification supported by device: ",getAsInt("@@C++(((iastora!ZpoddDevice*)0x%s)->mIdentifyData.serial_ata_features_supported.asynchronous_notification)"%(end_device))
						print "\t\t\tDIPM supported by device: ",getAsInt("@@C++(((iastora!ZpoddDevice*)0x%s)->mIdentifyData.serial_ata_features_supported.DIPM)"%(end_device))
						print "\t\t\tHIPM supported by device: ",getAsInt("@@C++(((iastora!ZpoddDevice*)0x%s)->mIdentifyData.serial_ata_capabilities.hipm)"%(end_device))
	
	
	for i in range(num_paths):
		for j in range(num_targets):
			type = getAsInt("@@C++(iastora!g_raidport->mTarget[%i][%i]->mType)"%(i,j))
			#print i,' ',j, '',type
			if type == 0:
				raidtarget = getAsPtr("@@c++(((iastora!RaidTarget *)(iastora!g_raidport->mTarget[%i][%i]))->mRaidDev)"%(i,j))
				print '\tFound PassthroughTarget'
				print "\t\tSystem device: %s" %(getAsInt("@@c++(((iastora!RaidTarget *)(iastora!g_raidport->mTarget[%i][%i]))->mIsSystemDevice)"%(i,j)))
				passthroughtarget = getAsPtr("@@c++(((iastora!PassthroughTarget *)(iastora!g_raidport->mTarget[%i][%i])))"%(i,j))
				print '\t\tmTransport ',getAsPtr("@@c++(((iastora!PassthroughTarget  *)0x%s)->mEndDeviceTarget->mTransport)"%(passthroughtarget))
			elif type == 2:
				print '\tFound RaidTarget'
				raidtarget = getAsPtr("@@c++(((iastora!RaidTarget *)(iastora!g_raidport->mTarget[%i][%i]))->mRaidDev)"%(i,j))
				print "\t\tSystem device: %s" %(getAsInt("@@c++(((iastora!RaidTarget *)(iastora!g_raidport->mTarget[%i][%i]))->mIsSystemDevice)"%(i,j)))
				print "\t\tSerial number: %s" %(getAsStr("@@C++(((iastora!raiddev*)0x%s)->serialNo)"%(raidtarget)))
				print "\t\tRaid level: %s" %(getAsInt("@@C++(((iastora!raiddev*)0x%s)->raidVol->lowMap->raidLevel)"%(raidtarget)))
				print "\t\tNumber of disks: %s" %(getAsInt("@@C++(((iastora!raiddev*)0x%s)->array->numDisks)"%(raidtarget)))


def inf_raidport():

        print '\tmGoingToHibernate: ',getAsInt("@@C++(iastora!g_raidport->mGoingToHibernate)")
