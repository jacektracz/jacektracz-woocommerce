import sys
import defines
from pykd import *
from defines import *
import ctypes
c_uint8 = ctypes.c_uint8
c_uint32 = ctypes.c_uint32

IO_PATH_UNINITIALIZED  = 0
IO_PATH_HAS_COALESCER = 1
IO_PATH_HAS_VOL_CACHE = 2
IO_PATH_HAS_NV_CACHE  = 4
IO_PATH_HAS_RAIDDEV   = 8

 

def print_bitfield(bit_field):
	for i in bit_field.b._fields_:
		print i[0],' ',getattr(bit_field.b,i[0])
				


SataDeviceTypeInvalid = '0'
SataDeviceTypeAta = '100'
SataDeviceTypeAtaUltraLowPower =  '200'
SataDeviceTypeAtaHybrid = '400'
SataDeviceTypeAtaPuis = '800'
SataDeviceTypeAtapi = '1000'
SataDeviceTypeAtapiZpodd = '2000'
def print_storport_summary():
	print 'Information taken from Storport'
	output = dbgCommand("!devnode 0 1 storahci").split(' ')
	pdo = 0
	found_iastora = False
	for i,word in enumerate(output) :
		if 'storahci' in word:
			break
		if  word == 'PDO':
			pdo = output[i+1]

	print 'pdo ',pdo		
	output = dbgCommand("!devstack "+ pdo).split(' ')
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
		
	
	
def print_interrupt_configuration():
	print "Interrupt Configuration (what OS see)"
	output = dbgCommand("!devnode 0 1 iastora").split(' ')
	pdo = 0
	for i,word in enumerate(output) :
		if word == 'PDO':
			pdo = output[i+1]
			break
			
	output = dbgCommand("!devobj "+ pdo).split(' ')
	devext = 0
	for i,word in enumerate(output) :
		if word == 'DevExt':
			devext = output[i+1]
			break
	
	output = dbgCommand("!devext "+ devext).split('\n')
	
	for i,word in enumerate(output) :
		if 'Capabilities' in word:
			print word
			
		if 'Interrupt Requirement' in word:
			print ('\n').join(output[i:])
	
def print_bios_version():
	print "Information from Bios:"
	output = dbgCommand("!sysinfo smbios").split('\n')
	for i,word in enumerate(output) :
		if 'Product' in word:
			print word
		if 'BIOS Version' in word:
			print word
def getAddress(localAddr):
    res = dbgCommand("x " + localAddr)
    if res.count("\n") > 1:
        print "[-] Warning, more than one result for", localAddr
    return res.split()[3]
def link(prefix,command,label):
	#print ".printf /D \"<link cmd=\"%s\">%s</link>\\n\"" % (command,label)
	#dbgCommand(".printf /D \"<link cmd=\\\"%s\\\">%s</link>\\n\"" % (command,label));
	dprintln("%s<link cmd=\"%s\">%s</link>"%(prefix,command,label),True)
def getAsInt(symbol):
	#print symbol
	return int(dbgCommand(".printf \"\%i\","+symbol))
def getAsPtr(symbol):
	#print symbol
	return dbgCommand(".printf \"\%p\","+symbol)
def getAsHex(symbol):
	#print symbol
	return dbgCommand(".printf \"\%x\","+symbol)
def getAsStr(symbol):
	#print symbol
	return dbgCommand(".printf \"\%ma\","+symbol)
def processInfo():

   nt = module( "nt" )

   processList = typedVarList( nt.PsActiveProcessHead, "nt!_EPROCESS", "ActiveProcessLinks"  )

   for process in processList:
       print "".join( [chr(i) for i in process.ImageFileName if i != 0] )
#def print_srb(srb):

def show_menu():
	link('','!pci 140 0 17 0','PCI configuration space for Ahci Controller')

#def parse_ahci_mmio():

def read_32_bits_mmio(address):
	address_hex_string = hex(address).strip('L')
	#print '!dd '+address_hex_string+' L 1'
	value_hex_string = dbgCommand('!dd '+address_hex_string+' L 1').split(' ')[1]
	#print value_hex_string
	return value_hex_string	

def parse_ahci_mmio():
	print 'ACHI controller mmio'
	ahci_pci_cs = dbgCommand('!pci 140 0 17 0')
	list = ahci_pci_cs.split()
	abar = None
	for i,line in enumerate(list):
		if line == 'BAR5':
			abar = list[i+1]
			break
	if abar:
		print 'abar ', abar
	abar_hex = int(abar,16)
	Port1_offset = 0x180
	CAP_offset = 0x0
	CAP2_offset = 0x24
	PxCMD_offset = 0x18
	PxSSTS_offset = 0x28
	PxSCTL_offset = 0x2C
	PxDEVSLP_offset = 0x44
	PxSACT_offset = 0x34
	PxCI_offset = 0x38
	
	value_hex_string = read_32_bits_mmio(abar_hex+CAP_offset)
	print 'CAP:'
	cap = CAP()
	cap.asbyte = int(value_hex_string,16)
	print_bitfield(cap)
	print ''
	
	value_hex_string = read_32_bits_mmio(abar_hex+CAP2_offset)
	print 'CAP2:'
	cap2 = CAP2()
	cap2.asbyte = int(value_hex_string,16)
	print_bitfield(cap2)
	print ''

	value_hex_string = read_32_bits_mmio(abar_hex+Port1_offset+PxCMD_offset)
	print 'CMD:'
	pxcmd = PxCMD()
	pxcmd.asbyte = int(value_hex_string,16)
	print_bitfield(pxcmd)
	print ''
	
	value_hex_string = read_32_bits_mmio(abar_hex+Port1_offset+PxSSTS_offset)
	print 'PxSSTS:'
	pxssts = PxSSTS()
	pxssts.asbyte = int(value_hex_string,16)
	print_bitfield(pxssts)
	print ''
	
	value_hex_string = read_32_bits_mmio(abar_hex+Port1_offset+PxSCTL_offset)
	print 'PxSCTL:'
	pxsctl = PxSCTL()
	pxsctl.asbyte = int(value_hex_string,16)
	print_bitfield(pxsctl)
	print ''
	
	value_hex_string = read_32_bits_mmio(abar_hex+Port1_offset+PxDEVSLP_offset)
	print 'PxDEVSLP:'
	pxdevslp = PxDEVSLP()
	pxdevslp.asbyte = int(value_hex_string,16)
	print_bitfield(pxdevslp)
	print ''
	
	value_hex_string = read_32_bits_mmio(abar_hex+Port1_offset+PxSACT_offset)
	print 'PxSACT:'
	pxsact = PxSACT()
	pxsact.asbyte = int(value_hex_string,16)
	print_bitfield(pxsact)
	print ''
	
	value_hex_string = read_32_bits_mmio(abar_hex+Port1_offset+PxCI_offset)
	print 'PxCI:'
	pxci = PxCI()
	pxci.asbyte = int(value_hex_string,16)
	print_bitfield(pxci)
	print ''
	
	print 'Device Sleep related registers:'
	
	print 'PxCI : ',pxci.b.CI_command_issued
	print 'PxSACT : ',pxsact.b.DS_device_status
	print 'PxDEVSLP.ADSE : ',pxdevslp.b.ADSE_aggresive_device_sleep_enable
	print 'CAP2.SDS : ',cap2.b.SDS_supports_device_sleep
	print 'CAP2.SADM : ',cap2.b.SADM_supports_aggressive_device_sleep_management
	print 'PxDEVSLP.DSP : ',pxdevslp.b.DSP_device_sleep_present
	print 'PxSCTL.IPM : ',pxsctl.b.IPM_interface_power_management_transitions_allowed
	print 'PxSSTS.IPM : ',pxssts.b.IPM_interface_power_management

def run():

	if not isWindbgExt():
		if not loadDump( sys.argv[1] ):
			dprintln( sys.argv[1] + " - load failed" )
			return

	if not isKernelDebugging():
		dprintln( "not a kernel debugging" )
		return  
	if len(sys.argv)>1:
		if sys.argv[1] == 'storport':
			print_storport_summary()
		if sys.argv[1] == 'ahci_mmio':
			print 'ddddd'
			parse_ahci_mmio()
		return
	#processInfo()
	#dbgCommand('.reload')
	#dbgCommand('s -[l6]sa fffff800`cf014000 fffff800`cf687000')
	if not "MATCH" in dbgCommand('!chksym nt'):
		dbgCommand('.reload')
		dbgCommand('.reload /f iastora.sys')

	symbol_info = dbgCommand('!chksym iastora')
	#print symbol_info
	if not "MATCH" in symbol_info:
		print 'No symbols loaded for iastora'
		print dbgCommand('.reload /f iastora.sys')
		output = dbgCommand('lm m iastora').split()
		if len(output) != 4:
			string_to_search = dbgCommand("s -[l6]sa %s %s"%(output[4],output[5])).split('\n')
			print len(string_to_search)
			for line in string_to_search:
				if len( line.split()) > 0:
					line_shortened = line.split()[1]
				if '14' in line_shortened:
					print line_shortened
		dbgCommand('!sym noisy')
		print dbgCommand('.reload /f iastora.sys')
		dbgCommand('!sym quiet')
		return
	raidport_address = getAddress('iastora!g_raidport')
	secport_address = None
	index_tmp = 0
	secport_index = -1
	volport_index = -1
	radiport_index = -1
	remapport_index = -1
	ahci_controller_index = -1
	print 'len ',len(dbgCommand('x iastora!volport*'))
	if len(dbgCommand('x iastora!secport*')) > 0:
		secport_index = index_tmp
		index_tmp = index_tmp + 1
	if len(dbgCommand('x iastora!volport*')) > 0:
		volport_index = index_tmp
		index_tmp = index_tmp + 1
	if len(dbgCommand('x iastora!raidport*')) > 0:
		raidport_index = index_tmp
		index_tmp = index_tmp + 1
	if len(dbgCommand('x iastora!remapport*')) > 0:
		remapport_index = index_tmp
		index_tmp = index_tmp + 1
	if len(dbgCommand('x iastora!ahcicontroller*')) > 0:
		ahci_controller_index = index_tmp
		index_tmp = index_tmp + 1
	print 'secport_index ',secport_index
	print 'volport_index ',volport_index
	print 'raidport_index ',raidport_index
	print 'remapport_index ',remapport_index
	print 'ahci_controller_index ',ahci_controller_index

	if ahci_controller_index >= 3:
		ahci_controller = getAsPtr("@@C++(iastora!g_raidport->mDriver->mDeviceExtensionList[%i])"%(ahci_controller_index))
	elif ahci_controller_index ==1:
		ahci_controller = getAsPtr("@@C++(iastora!g_raidport->mDriver->deviceExtensionList[%i])"%(ahci_controller_index))
	print ahci_controller
		
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
#	platformDeviceID = int(getAsInt("@@C++(((iastora!AhciController*)0x%s)->mPlatformDeviceId)"%(ahci_controller)))
#	print "Platform DeviceId: %s(%s)"%(ahci_controller_version_map[platformDeviceID],hex(platformDeviceID))	
	print_interrupt_configuration()

	
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
	
	
	link('',"?? (iastora!AhciController*)0x%s"%(ahci_controller),'Ahci Controller');
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
		link("\t\t","?? @@C++(((iastora!raiddev*)0x%s)->idData)"%(raid_dev),"DiskIdentityData")
		print "\t\t\tclaimable: %i" %(getAsInt("@@C++(((iastora!raiddev*)0x%s)->idData.claimAble)"%(raid_dev)))
		
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
	print 'remapport_index ',remapport_index
	remapport_address = getAsPtr("@@C++(iastora!g_raidport->mDriver->mDeviceExtensionList[%i])"%(remapport_index))
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
			print "\t\tserial aborted command count: ",(getAsInt("@@C++(((iastora!ahciport*)((iastora!AhciController*)0x%s)->mPort[%i])->mSerialAbortedCommandCount)"%(ahci_controller,i)))
			link('\t\t',"?? (iastora!PortStateMachine*)@@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine)"%(ahci_controller,i),'PortStateMachine')
			current_state = getAsInt("@@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine->mCurrentState)"%(ahci_controller,i))
			target_state = getAsInt("@@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine->mTargetState)"%(ahci_controller,i))
			current_state_string = getAsStr("@@C++(iastora!DbgPortStateMachineStringMap[%s])"%(current_state))
			target_state_string = getAsStr("@@C++(iastora!DbgPortStateMachineStringMap[%s])"%(target_state))

			print "\t\t\tcurrent state: %s[%s] \n\t\t\ttarget state: %s[%s] "%(current_state_string,current_state,target_state_string,target_state)
			print "\t\t\tmCurrentMode: %s "%((dbgCommand("?? @@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine->mCurrentMode)"%(ahci_controller,i))).strip())
			print "\t\t\tmPreviousMode: %s "%((dbgCommand("?? @@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mStateMachine->mPreviousMode)"%(ahci_controller,i))).strip())
			if target_state == 36 and current_state != 47:
				print '\t\tEnumerated disk' 
				end_device = getAsPtr("@@C++(((iastora!AhciController*)0x%s)->mPort[%i]->mDevice)"%(ahci_controller,i))
				signature = getAsHex("@@C++(((iastora!EndDevice*)0x%s)->mSignature)"%(end_device))
				device_id_type = dbgCommand("?? @@C++(((iastora!EndDevice*)0x%s)->mDeviceIdType)"%(end_device))
				device_id_type_hex = getAsHex("@@C++(((iastora!EndDevice*)0x%s)->mDeviceIdType)"%(end_device))
				print '\t\tsignature: 0x',signature.strip(),'\n\t\tdevice_id_type: ',device_id_type.split()[1]
				if signature == '101':
					print '\t\tATA device'
					link('\t\t',"?? (iastora!AtaDevice*)0x%s"%(end_device),'AtaDevice');
					link('\t\t\t',"?? @@C++(((iastora!AtaDevice*)0x%s)->mIdentifyData)"%(end_device),'IdentifyData');
				elif signature == 'eb140101':
					print '\t\tATAPI device'
					if device_id_type_hex == SataDeviceTypeAtapi:
						link('\t\t',"?? (iastora!AtapiDevice*)0x%s"%(end_device),'AtapiDevice');
						link('\t\t\t',"?? @@C++(((iastora!AtapiDevice*)0x%s)->mIdentifyData)"%(end_device),'IdentifyData')
						print "\t\t\tAsynchronous Notification is enabled: ",getAsInt("@@C++(((iastora!AtapiDevice*)0x%s)->mAsynchronousNotificationFeature.mIsEnabled)"%(end_device));
						print "\t\t\tAsynchronous Notification supported by device: ",getAsInt("@@C++(((iastora!AtapiDevice*)0x%s)->mIdentifyData.serial_ata_features_supported.asynchronous_notification)"%(end_device))
						print "\t\t\tDIPM supported by device: ",getAsInt("@@C++(((iastora!AtapiDevice*)0x%s)->mIdentifyData.serial_ata_features_supported.DIPM)"%(end_device))
						print "\t\t\tHIPM supported by device: ",getAsInt("@@C++(((iastora!AtapiDevice*)0x%s)->mIdentifyData.serial_ata_capabilities.hipm)"%(end_device))
					elif device_id_type_hex == SataDeviceTypeAtapiZpodd:
						link('\t\t',"?? (iastora!ZpoddDevice*)0x%s"%(end_device),'ZpoddDevice');
						link('\t\t\t',"?? @@C++(((iastora!ZpoddDevice*)0x%s)->mIdentifyData)"%(end_device),'IdentifyData');
						print "\t\t\tAsynchronous Notification is enabled: ",getAsInt("@@C++(((iastora!ZpoddDevice*)0x%s)->mAsynchronousNotificationFeature.mIsEnabled)"%(end_device));
						print "\t\t\tAsynchronous Notification supported by device: ",getAsInt("@@C++(((iastora!ZpoddDevice*)0x%s)->mIdentifyData.serial_ata_features_supported.asynchronous_notification)"%(end_device))
						print "\t\t\tDIPM supported by device: ",getAsInt("@@C++(((iastora!ZpoddDevice*)0x%s)->mIdentifyData.serial_ata_features_supported.DIPM)"%(end_device))
						print "\t\t\tHIPM supported by device: ",getAsInt("@@C++(((iastora!ZpoddDevice*)0x%s)->mIdentifyData.serial_ata_capabilities.hipm)"%(end_device))
	
	
	
if __name__ == "__main__":
   run()
