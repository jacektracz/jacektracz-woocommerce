import sys
import os

        
class DBG_RaidIsmDef:
    def xx_dbg(self,pss):
        """ """
    def get_class_disk_str(self):
        self.xx_dbg("DBG_DiskIdentityData::get_class_str::m_in::")
        cs = """
        """        
    def get_class__RAID_ISM_INIT_PARMS_str(self):
        
        self.xx_dbg("DBG_DiskIdentityData::get_class_str::m_in::")
        cs = """
                typedef struct _RAID_ISM_INIT_PARMS
{
    UINT_PTR pCachedMem;           // Start of cached memory block for
                                   //  ISM allocation
    UINT_PTR pNonCachedMem;        // Start of non-cached memory block for
                                   //  ISM allocation
    unsigned long cachedMemSize;   // Size of cached memory block
    unsigned long nonCachedMemSize;// Size of cached memory block

    unsigned long maxDiskSglFrags; // Max number of SGL memory fragments

    unsigned long minimizeSize;    // If false, ISM will use the "MAX" defaults
                                   //  it was compiled with
                                   // Else it will use the following
                                   //  "Max" value fields to help minimize
                                   //  its size.
    unsigned long maxMdrs;         // Max MemberDiskReq blocks (MDRs)
    unsigned long maxRaid0Reqs;    // Max Raid0Reqs
    unsigned long maxRaid5Reqs;    // Max Raid5Reqs
    unsigned long maxRaidDgReqs;   // Max RaidDgReqs
    unsigned long maxDisks;        // Max physical disks
    unsigned long maxDisksInRaid;   // Max disks in RAID array.
    unsigned long maxRaidDevs;     // Max RAID volumes
    unsigned long maxArrays;       // Max arrays
    unsigned long maxPagePoolSize; // Max num of pages in page pool
    bool          bbmSupported;    // Whether the ISM should use BBM logs or not
    bool          nvmSupported;    // Whether the ISM should use NVM or not
    unsigned long legacyPlatform;  // Indicates if the OROM is a legacy platform
                                   // that supports attributes or not
    bool          g2TbDiskSupported; // >2TB disk support for OROM
    bool          patrolEnabled;   // is Read Patrol Enabled.
    bool          rohiEnabled;     // whether Rebuild on Hot Insert enabled or not
    unsigned long smartPollPeriod; // Interval between SMART pollings in seconds
    bool          trimRaid0Supported; // RAID0 Trim support
    bool          aoacSupported;   // AOAC feature support
    bool          fastEnumSupported; // Accel MPB written to SSD for SDR0
    bool          fastEnumEnabled; // OROM detects that Accel MPB on SSD for SDR0
    unsigned long cStateTransitionsEnabled; // Lake Tiny feature support
    bool          nvcMultiFrameSupported;   // OROM supports NvCache MultiFrame Metadata
    bool          ffsEnabled;     // BIOS iFFS (Rapid Start Technology) enabled on plaform
    unsigned long systemDramSizeinGb; // Total installed DRAM on the system
    
    unsigned long BbmLogEventThresh;
} RAID_ISM_INIT_PARMS, *PRAID_ISM_INIT_PARMS;

"""

        self.xx_dbg("DBG_DiskIdentityData::get_class_str::m_out::")
    
    def get_class__DiskIdentityData_str(self):
        self.xx_dbg("DBG_DiskIdentityData::get_class_str::m_in::")
        cs = """
struct _DiskIdentityData * 0xffffe000`5c664020
   +0x000 TotalBlocks      : 0x1dca800
   +0x008 deviceContext    : 0xffffe000`5c664d88 Void
   +0x010 maxByteCount     : 0x20000
   +0x014 claimAble        : 1
   +0x015 SerialNumber     : [20]  "Volume_0001"
   +0x029 NvmeSerialNumber : [20]  ""
   +0x03d VendorInfo       : [16]  "IntelNvm       "
   +0x04d ProductInfo      : [40]  "Raid 0 Volume"
   +0x075 Description      : [16]  "Volume_0001"
   +0x085 ProductRevLevel  : [8]  "1.0.00"
   +0x08d PathId           : 0 ''
   +0x08e TargetId         : 0x8 ''
   +0x08f Lun              : 0 ''
   +0x090 PhysicalLocation : 0 ''
   +0x094 LogicalSectorByteSize : 0x200
   +0x098 PhysicalSectorByteSize : 0x200
   +0x09c LogicalSectorOffset : 0
   +0x0a0 DiskAttributes   : 0 ''
   +0x0a1 AtaLocked        : 0
   +0x0a2 OpalLocked       : 0
   +0x0a3 TcgSupported     : 0
   +0x0a4 EncryptionState  : 0
   +0x0a6 EncryptionMigrState : 0
   +0x0a8 DiskRPM          : 1
   +0x0ac DataSetManagement : 0
   +0x0b0 MaxCountLBARangeEntries : 0
   +0x0b4 LbprzSupport     : 0
   +0x0b6 SmartEnabled     : 0 ''
   +0x0b8 PuisSupported    : 0
   +0x0ba PuisEnabled      : 0
   +0x0bc SecurityEnabled  : 0
"""

        self.xx_dbg("DBG_DiskIdentityData::get_class_str::m_out::")    

    def get_raidism_str(self):
        ccs = """
class RaidIsm : public MemoryAllocator {
public:
    enum PowerSource { PowerSourceAc, PowerSourceDc, PowerSourceUnknown };
private:
    static RaidIsm* _instance;          // Instance of RaidIsm object
    RAID_ISM_INIT_PARMS initParms;      // ISM Initialization values
    RaidDev* raidDevs[MAX_RAID_DEVICES]; // Raid devices controlled by this ISM
#define RAIDDEV_ENTRY_DELETED ((RaidDev*)0)

    int numRaidDevs;                    // Current size of raidDevs[] (both
                                        //  active and deleted entries)
    
    static __declspec(align( HOST_PAGE_SIZE )) U8 bitBucket[MAX_TRANSFER_LENGTH];

    MemoryMgr* memoryMgr;               // Memory blocks manager for ISM
    RaidMpbMgr* mpbMgr;                 // Mpb manager
    RaidCfgMgr* cfgMgr;                 // RaidCfg manager
    CoalMgr* coalMgr;                   // Coalesce manager
    CacheMgr* cacheMgr;                 // Cache manager
    NvCacheMgr* nvCacheMgr;             // NVM Cache manager
    IntervalTimer* intervalTimer;       // 
    EventQueue      mEventQueue;

    U32 cacheSizeInKB;                  // Size of common memory pool for use
                                        //  by all volume caches
    U32 disableAllDiskWrites;           // If true disable all disk writes for
                                        //  simulating dirty shutdown
    PowerSource systemPowerSource;      // Describes the current power source
    bool neverSpinDownHdd;              // Describes the current setting for disk spindown

    U16 sioReqStatus;                   // ReqStatus from latest RaidIsm::startIo
    U16 sioDetStatus;            
  
    U16 adapterTids[MAX_SCSI_BUS_ADAPTERS];
    int numScsiAdapters;

    Event getReqComp;                   // 

    DiskTable diskTable;                // Table of all disks, present or not,
                                        //  including pass-thrus

    MemberDiskReqPool freeMdrs;         // Free MemberDiskReq blocks
    MemberDiskReqPool freeMdrsSaved;    // Free MemberDiskReq blocks for restoration 
                                        // after hibernation
    
    MapReqList mapReqsPendingMdrs;      // List of MapReqs waiting for
                                        //  free MemberDiskReq blocks
    CkptMgrPool* freeCkptMgrPool;       // Free checkpoint managers
    DsMgrPool* freeDsMgrPool;           // Free checkpoint managers
    FsMgrPool* freeFsMgrPool;           // Free fast sync managers

    RaidReqPool* freeRaidReqPool[NumRaidReqTypes]; // Free Pools of RaidReqs
    EventFifo* getReqCompEventFifo[NumRaidReqTypes]; // Events awaiting free RaidReqs
    int reqCountPct[NumRaidReqTypes];   // Percentage used to scale back 
                                        //  RaidVol::maxReqCountAllowed based on
                                        //  ratio of how many RaidReqs created at
                                        //  startup to how many RaidReqs are
                                        //  actually needed currently
    int numRaid0Reqs;
    int numRaid5Reqs;
    int numRaidDgReqs;
    int numReserved3050Mdrs;            // Must be at least this many free MDRs
                                        //  for MapReq::allocMemberDiskReqs to
                                        //  allocate MDRs for a Raid30/50 map.
    int numFreeMdrs;                    // Number of MDRs in freeMdrs pool
    bool configInitialized;             // Set after boot-time config is read
    int numActiveGenlMigrs;             // Num of general migrations going on
    bool smartPollingInProgress;        // Currently getting SMART status on 
                                        //  all non-passthru disks
    MemberDiskReq* smartStatusMdr;      // Used for getting disk SMART status

    void* hostDrvrContext;              // Context ptr for when enumComplete done

    U32 maxDiskSglMemFrags;             // ISM will not build SGLs to send to 
                                        //  disks via IsmToHost_StartIo with
                                        //  > this number of memory fragments
    
    TimerEvent* storeMpbIntervalCall;
    
    TimerEvent* smartIntervalCall;

    TimerEvent* setAcPowerCall;         // TimerEvent to set AC power for RRT

    EventFifo freeEvents;
    U16 minHdmFragCount;                // Min of max buffer frags for any HDM

    SuspendReason suspendReason; 
    bool selfSuspending;                // ISM is in process of suspending
    bool suspended;                     // All Arrays are suspended and ISM
                                        //  waiting for enumComplete to restart
    int arraySuspendsOut;               // Counts how many Arrays are still 
                                        //  in the process of suspending
    bool suspendHiddenArrays;           // Flag used for sequencing the suspend
                                        //  of all arrays: suspend OS-visible
                                        //  arrays followed by hidden ones.
    int updateRaidPtlOut;
    bool puisShutDown;
    Event suspendDoneComp;
    Event shutdownNotifyComp;

    Event powerMgmtComp;
    int powerMgmtOpsInProgress;
    int diskNumPwrMgmt;
    U16 powerMgmtStatus;                // Result of last call to powerMgmt()
    Disk::PowerState powerMgmtOp;
    bool nonArrayDiskPwrUpdateInProg;
    void doDiskPowerMgmt();
    EVENT_PROLOG_H(diskPowerMgmtDone, Disk* dev);
    void diskPowerMgmtDone(Disk* dev);

    // Storage for Power Mgr registry settings
    U32 powerSecondsToSpindown;
    U32 powerSpindownIfTargetOnlyIdle;
    U32 powerHistoryDepth;

    U32 mSrtAggressiveD3Timeout{0}; // D3 timeout for HDD for SRT in CS on DC
    U32 mSrtSemiAggressiveD3Timeout{0}; // D3 timeout for HDD for SRT in CS on AC
    U32 mSrtF1Latency{0};
    U32 mSrtAggressiveCleanAreaSize{0};  // clean area size in APS (number of PRBs)
    U32 mSrtCacheCleaningD3Timeout{0}; // D3 timeout for HDD for SRT in CS on cache cleaning

    bool spinUpInProgress;
    bool csEntered{false}; // indicator if we are in connected standby mode

public:
    U32 getPowerSecondsToSpindown() const { return powerSecondsToSpindown; }
    void setPowerSecondsToSpindown(U32 seconds) { powerSecondsToSpindown = seconds;    }
    U32 getPowerSpindownIfTargetOnlyIdle() const { return powerSpindownIfTargetOnlyIdle; }
    U32 getPowerHistoryDepth() const { return powerHistoryDepth; }

    U32 getSrtAggressiveD3Timeout() const { return mSrtAggressiveD3Timeout; }
    U32 getSrtSemiAggressiveD3Timeout() const { return mSrtSemiAggressiveD3Timeout; }
    U32 getSrtF1Latency() const { return mSrtF1Latency; }
    U32 getSrtAggressiveCleanAreaSize() const { return mSrtAggressiveCleanAreaSize; }
    U32 getSrtCacheCleaningD3Timeout() const { return mSrtCacheCleaningD3Timeout; }

    void initEventQueue();
    static void setInstance(RaidIsm* instance) { _instance = instance; }
    static RaidIsm* getInstance(void) { return _instance; }
private:

#ifdef HW_XOR
    bool aauOperational;                // AAU available + all good status so far
    ISM_DMA_ID aauDmaId;                // DMA Id for issuing AAU Xor requests
public:
    void setAauOperational(bool b) {aauOperational = b;}
    bool aauIsOperational() {return aauOperational;}
    ISM_DMA_ID getAauDmaId() {return aauDmaId;}
private:
#endif

    EVENT_PROLOG_H_NO_ARG( readConfigReply );
    void readConfigReply();

    EVENT_PROLOG_H_NO_ARG(nvCacheMgrSuspended);
    void nvCacheMgrSuspended();
    EVENT_PROLOG_H_NO_ARG(nvCacheMgrInitDone);
    void nvCacheMgrInitDone();

    EVENT_PROLOG_H_NO_ARG(suspendedForReadConfig);
    void suspendedForReadConfig();
    EVENT_PROLOG_H_NO_ARG(updateRaidPtl);
    void updateRaidPtl();
    EVENT_PROLOG_H_NO_ARG(removeUpdatedRaidDone);
    void removeUpdatedRaidDone();
    EVENT_PROLOG_H_NO_ARG(updateRaidPtlDone);
    void updateRaidPtlDone();
    EVENT_PROLOG_H_NO_ARG(readAndUpdateDone);
    void readAndUpdateDone();
    EVENT_PROLOG_H_NO_ARG(nvCachingResumed);
    void nvCachingResumed();
    EVENT_PROLOG_H_NO_ARG(nvmUpdatesComplete);
    void nvmUpdatesComplete();

    void createReqBlocks();
    void forceOutOfMem();
    bool notEnoughCachedMem(int size);

    bool bbmSupported;  // Whether BBM functionality is supported in this instance
    bool g2TbDiskSupported; // Set when >2TB disk is supported by OROM
    bool trimRaid0Supported;         // Set when trim for RAID0 is indicated by OROM as supported

    U32 premiumFeatures;                // contains the register value from the PFB
                                        // Premium Feature Block

#define AOAC_DEFAULT_CACHING_TIMER 10   // default for how long we stay in AOAC caching mode
#define AOAC_CACHING_MAX_TIMER     900  // max that an agent can set the AOAC timer for
    U32  aoacRegistryOverride;
    U32  aoacDefaultCachingModeTime;
    bool aoacPlatformSupport;

    ArraySemReq nvSeparableCacheArraySemReq;

#if !defined(FREE_BUILD) && (EVT_TRACING != 0)
    EventTraceQ *eventTraceQueue; // Provide an easy handle to get from 
                                  // within the debugger
#endif // !defined(FREE_BUILD) && (EVT_TRACING != 0)

    //  shutdown stuff
private:
    int currentIos;
    U32 ticksWithNoIo;       // How many tick have elapsed with no IO
    U32 secondsWithNoIo;     // How many seconds have elapsed with no 
                             //  new I/O requests

    U32 upTime;              // Number of seconds since RaidIsm was created
    U32 upTimeAtLastEnum;    // Value of upTime at completion of most recent
                             //  device re-enumeration (readConfig sequence)
public:
    MemberDiskReqPool* getFreeMdrs() {return &freeMdrs;}
    MemberDiskReqPool* getFreeMdrsSaved() {return &freeMdrsSaved;}

    bool getBbmSupported() {return bbmSupported;}   
    bool  get2TbDiskSupported(){ return g2TbDiskSupported;}

    // The driver features are also cached in initParms.driverFeatures
    bool getRAID0TrimSupported() { return trimRaid0Supported;}

    // AOAC PUIS
    U32 getAoacRegistryOverride() { return aoacRegistryOverride; }
    U32 getAoacDefaultCachingModeTime() { return aoacDefaultCachingModeTime; }
    bool getAoacPlatformSupport() { return aoacPlatformSupport; }
    PuisVolState initAoacPuis();
    bool updateAoacPuis(int newTime);
    void updateDiskStates();
    bool setPuisPolicy();
    void wakePuisDisks();

    bool getFastEnumSupported() { return initParms.fastEnumSupported; }
    bool getFastEnumEnabled() { return initParms.fastEnumEnabled; }
    void setFastEnumDisabled() { initParms.fastEnumEnabled = false; }
    bool getFfsEnabled() { return initParms.ffsEnabled; }
    U32 getSystemDramSizeInMb() { return (ISM_GB_TO_MB(initParms.systemDramSizeinGb)); }
    bool getNvcMultiFrameSupported() { return initParms.nvcMultiFrameSupported; }

    void decrIsmIos();
    void updateIdleSeconds() {
        secondsWithNoIo += SHUTDOWN_POLL_PERIOD;
    }
    U32 getIdleSeconds() {return secondsWithNoIo;}
    //  end shutdown
  
    void incrIsmIos() {currentIos+=1;}
    void resetIdleCounters() {secondsWithNoIo = 0; ticksWithNoIo = 0;}
    void updateIdleTicks(U32 numTicks) {ticksWithNoIo += numTicks;}
    U32 getIdleTicks() {return ticksWithNoIo;}

    static bool smartIntervalEH(ISM_OBJ_CONTEXT context, ISM_ARG arg);
    bool smartInterval(ISM_ARG arg);
    EVENT_PROLOG_H( smartIntervalDone, CfgDisk* );
    void smartIntervalDone(CfgDisk* dev);
    EVENT_PROLOG_H( smartAttributesDone, CfgDisk* );
    void smartAttributesDone(CfgDisk* dev);
    void getSmartStatusFromDisk(CfgDisk* cdisk);
    static bool storeMpbIntervalEH(ISM_OBJ_CONTEXT context, ISM_ARG arg);
    bool storeMpbInterval(ISM_ARG arg);
    EVENT_PROLOG_H(suspend, Event*);
    void suspend(Event* comp);
    void suspendArrays();
    EVENT_PROLOG_H_NO_ARG(arraySuspended);
    void arraySuspended();
    EVENT_PROLOG_H_NO_ARG(resumeIo);
    void resumeIo();
    EVENT_PROLOG_H_NO_ARG(handlePuisShutDown);
    void handlePuisShutDown();
    static bool setAcPowerEH(ISM_OBJ_CONTEXT context, ISM_ARG arg);
    bool RaidIsm::setAcPower(ISM_ARG arg);
    void setNeverSpinDownHdd(bool neverSpinDown);
    EVENT_PROLOG_H(ismHasLostAcPower, bool);
    void ismHasLostAcPower(bool lostAcPower);
    EVENT_PROLOG_H(nonArrayDiskPwrUpdated, Disk::PowerState);
    void nonArrayDiskPwrUpdated(Disk::PowerState);
    EVENT_PROLOG_H( nvSeparatedCacheInfo, PNVSEPARATED_CACHE_INFO );
    void nvSeparatedCacheInfo( PNVSEPARATED_CACHE_INFO ); 
    EVENT_PROLOG_H(nvSeparatedCacheWbDisable, PNVSEPARATED_CACHE_INFO);
    void nvSeparatedCacheWbDisable( PNVSEPARATED_CACHE_INFO );
    EVENT_PROLOG_H(nvSeparatedCacheWbDisableAcquireLock, PNVSEPARATED_CACHE_INFO);
    void nvSeparatedCacheWbDisableAcquireLock( PNVSEPARATED_CACHE_INFO );
    EVENT_PROLOG_H(nvSeparatedCacheWbDisableTrimFreeList, PNVSEPARATED_CACHE_INFO);
    void nvSeparatedCacheWbDisableTrimFreeList( PNVSEPARATED_CACHE_INFO );
    EVENT_PROLOG_H(nvSeparatedCacheWbRevert, PNVSEPARATED_CACHE_INFO);
    void nvSeparatedCacheWbRevert( PNVSEPARATED_CACHE_INFO );
    EVENT_PROLOG_H(nvSeparatedCacheWbRevertAcquireLock, PNVSEPARATED_CACHE_INFO);
    void nvSeparatedCacheWbRevertAcquireLock( PNVSEPARATED_CACHE_INFO );
    EVENT_PROLOG_H(nvSeparatedCacheWbRevertTrimFreeList, PNVSEPARATED_CACHE_INFO);
    void nvSeparatedCacheWbRevertTrimFreeList( PNVSEPARATED_CACHE_INFO );
    EVENT_PROLOG_H(connectedStandbyNotify, RaidCsState csState);
    void connectedStandbyNotify(RaidCsState csState);

    U32 getUpTime() {return upTime;}
    U32 getUpTimeAtLastEnum() {return upTimeAtLastEnum;}
    void resume();

    void setPremiumFeatures(U32 pf) {premiumFeatures = pf;}
public:

    RaidIsm(void* hostContext, RAID_ISM_INIT_PARMS* initParms);
    bool init();
    void completeInit();

    EVENT_PROLOG_H_NO_ARG( nop );
    EVENT_PROLOG_H_NO_ARG( printState );
    void printState();
    RaidDev* getRaidDev(int i) const;
    RaidDev* getRaidDev(ISM_PATH_TARGET_LUN ptl) const;
    RaidDev* getRaidDev(char* serialNo) const;
    RaidDev* getRaidDev(char* serialNo, int i) const;
    RaidDev* getNvcRaidDev();
    RaidDev* getAccelRaidDev() const;
    int getRaidDevOrd(RaidDev* raidDev);
    RaidDev* firstRaidDev(int& iter) const {iter=0; return nextRaidDev(iter);}
    RaidDev* nextRaidDev(int& iter) const;
    DiskTable* getDiskTable() {return &diskTable;}
    MemoryMgr* getMemoryMgr() {return memoryMgr;}
    MemorySet* getMemoryMgr(MemoryType mst) {
        return memoryMgr->getMemorySet(mst);
    }
    CoalMgr* getCoalMgr() { return coalMgr; }
    CacheMgr* getCacheMgr() { return cacheMgr; }
    NvCacheMgr* getNvCacheMgr() { return nvCacheMgr; }
    Disk* getNvCacheTarget();
    bool hasEnoughGenlMigrResources();
    void updateNumActiveGenlMigrs(int i);
    RaidMpbMgr* getMpbMgr() {return mpbMgr;}
    RaidCfgMgr* getCfgMgr() {return cfgMgr;}
    EVENT_PROLOG_H(diskAdded, DiskIdentityData*);
    Disk* diskAdded(DiskIdentityData* diskId);
    EVENT_PROLOG_H(claimDisk, CfgDisk*);
    void claimDisk(CfgDisk* cdisk);
    EVENT_PROLOG_H(makeAutoSpareDisk, CfgDisk*);
    void makeAutoSpareDisk(CfgDisk* cdisk);
    EVENT_PROLOG_H_NO_ARG(enumComplete);
    void enumComplete();
    EVENT_PROLOG_H(diskRemoved, void*);
    void diskRemoved(void*);
    void* getHostDrvrContext() {return hostDrvrContext;}
    void extractIsmSerialNumber(
        char* dest,                     ///< [out] destination string - will be null terminated
        size_t destSize,                ///< [in] size of destination string, including space for null termination
        const DiskIdentityData& diskId, ///< [in] disk identification data
        BOOL swapBytes                  ///< [in] whether to swap the source string byte order as in ATA IDENTIFY data
        );
private:
    void extractRightmostNonblankSerialInternal(
        char* dest,         ///< [out] destination string - will be null terminated
        const char* src,    ///< [in] source string - not null terminated
        size_t destSize,    ///< [in] size of destination string, including space for null termination
        size_t srcLen,      ///< [in] length of source
        BOOL swapBytes      ///< [in] whether to swap the source string byte order as in ATA IDENTIFY data
        );

public:
    int processVolumeName(char* dest, char* src);
    void* globalNewCached(size_t sz);

    RaidDev* createRaidDev(CfgRaidDev* cfgRaidDev);
    EVENT_PROLOG_H(deleteRaidDev, RaidDev*);
    void deleteRaidDev(RaidDev* raidDev);
    EVENT_PROLOG_H(volumeDeletedDone, RaidDev*);
    void volumeDeletedDone(RaidDev* raidDev);
    Disk* getDisk(ISM_PTL ptl) {return diskTable.getDisk(ptl);}
    Disk* getDisk(char* serialNum) {return diskTable.getDisk(serialNum);}
    Disk* getDiskByContext(void* devContext) {
        return diskTable.getDiskByContext(devContext);
    }
    bool isDiskPtrValid(Disk* ptr) 
        {return diskTable.isDiskPtrValid(ptr);}
    U16 getAdapterTid(U16 i) {return adapterTids[i];}
    int getNumScsiAdapters() {return numScsiAdapters;}
    void updateLeds(U16 adapterId, U8 scsiId, U32 configuredStatus);
    U16 getSioReqStatus() {return sioReqStatus;}
    U16 getSioDetStatus() {return sioDetStatus;}
    void setSioStatus(U16 reqStat, U16 detStat) {
        sioReqStatus = reqStat;
        sioDetStatus = detStat;
    }
    void readyNotify();
    void freeEventQueue();
    void killEventQueue();
    bool eventQueueRunning();
    void restartEventQueue();
    void stallEventQueue();
    void queueEvent(const Event* event);
    void queueEvent(EventFifo& eventFifo, const Event& comp);
    void postEvent(const Event& ev) {
        if (ev.handler != NULL) {
            mEventQueue.queue(&ev);
        }
    }
    void postEvent(Event& ev, ISM_ARG val) {
        ev.arg = val;
        postEvent(ev);
    }
    void postEvents(EventFifo& eventFifo);
    void setTimer(TimerEvent* te) {
        postEvent(Event(IntervalTimer::addEventEH, intervalTimer, (ISM_ARG)te));
    }
    void removeTimer(TimerEvent* te) {
        postEvent(Event(IntervalTimer::removeEventEH, intervalTimer,
                        (ISM_ARG)te));
    }
    void getReq(RaidReqType reqType, Event* getReqComp);
    void getReq(RaidReqType reqType, Event* comp,
                EVENT_H(compEH,context,arg)) {
        comp->handler = compEH;
        comp->context = context;
        comp->arg = arg;
        getReq(reqType, comp);
    }
    void freeReq(RaidReqBase* raidReq, bool forcePost=false); 

    void postXor(XorReq* xorReq) { 
#ifdef HW_XOR
        if (aauOperational)
            xorReq->doAauOp();
        else
#endif
            xorReq->doSwXor();
    }

    static void xferSgl2Sgl(ISM_SG_ELEMENT* src, ISM_SG_ELEMENT* dest);
    void xferSgl2Sgl(ISM_SG_ELEMENT* src, ISM_SG_ELEMENT* dest,
                     EVENT_H_NO_ARG(compEH, ctxt)) {
        xferSgl2Sgl(src, dest);
        postEvent(Event(compEH, ctxt, NULL));
    }
    static void xferSgl2Sgl(ISM_SG_ELEMENT* src, int srcOffset,
                            ISM_SG_ELEMENT* dest, int destOffset, int byteCount);
    void xferSgl2Sgl(ISM_SG_ELEMENT* src, int srcOffset,
                     ISM_SG_ELEMENT* dest, int destOffset, int byteCount,
                     EVENT_H_NO_ARG(compEH, ctxt)) {
        xferSgl2Sgl(src, srcOffset, dest, destOffset, byteCount);
        postEvent(Event(compEH, ctxt, NULL));
    }
    static int copySglFragment(ISM_SG_ELEMENT* sSgl, ISM_SG_ELEMENT* dSgl,
                               U32 dSglSpace, int skipCount, int copyCount);
    static bool buildSglWithBbEntries(ISM_SG_ELEMENT* srcSgl,
                                      ISM_SG_ELEMENT* destSgl,
                                      U32 dSglSpace, int byteCount, U64 mask,
                                      int bytesPerMaskBit, U32& numSglWords,
                                      U32 initialOffset = 0);
    static void getSglInfo(ISM_SG_ELEMENT* sgl, U32& sglCount, 
                           U32& sglWords, ISM_SG_ELEMENT*& lastElement);
;

    MemberDiskReq* getFreeMemberDiskReq(MapReq* mr) {
        MemberDiskReq* mdr = freeMdrs.get();
        if (mdr) { // PREFix
            mdr->init(mr);
            numFreeMdrs--;
        }
        return mdr;
    }

    void putFreeMemberDiskReq(MemberDiskReq* mdr) {
        mdr->markEmpty();
        freeMdrs.put(mdr);
        numFreeMdrs++;
    }

    MemberDiskReq* allocNewMdr(int maxSglWords=MINI_MDR_SGL_WORDS) {
        // Warning MemberDiskReq will automatically use its subdivide
        //  function to fit an I/O into the disk's max size, subdivide uses 
        //  the MDR's own SGL space, any MDR that may subdivide must be
        //  of maxSglWords = FULL_MDR_SGL_WORDS to have enough SGL space
        return new (this) MemberDiskReq(this, maxSglWords);
    }

    CkptMgrPool* getFreeCkptMgrPool() {return freeCkptMgrPool;}
    DsMgrPool* getFreeDsMgrPool() {return freeDsMgrPool;}
    FsMgrPool* getFreeFsMgrPool() {return freeFsMgrPool;}
    int getNumFreeMdrs() {return numFreeMdrs;}
    int getMinMdrs3050() {return numReserved3050Mdrs;}
    void updateVolMaxReqCounts();
    int getReqCountPct(int i) {return reqCountPct[i];}
    MapReqList* getMapReqsPendingMdrs() {return &mapReqsPendingMdrs;}
    int getMaxDisks() {return initParms.maxDisks;}
    int getMaxArrays() {return initParms.maxArrays;}
    int getMaxRaidDevs() {return initParms.maxRaidDevs;}
    int getMaxRaidMpbSize();
    PowerSource getSystemPowerSource() { return systemPowerSource; }
    bool getNeverSpinDownHdd() { return neverSpinDownHdd; }
    void systemPowerToggled();
    EVENT_PROLOG_H_NO_ARG(updateDiskPowerStates);
    void updateDiskPowerStates();
    ISM_STATUS getPwrCycleCount(RaidDev* rdev, U32* powerCycleCount);
    
    int isRaidLevelSupported (int raidLevel);
    int isMigrPrioritySupported (RaidDev::MigrPriority migrPriority);
    
    EVENT_PROLOG_H(getSetParms, GET_SET_PARAMS*);
    void getSetParms(GET_SET_PARAMS* params);

    ISM_STATUS setField(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                        ISM_ADDR pValue);
    ISM_STATUS getField(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                        ISM_ADDR pValue);
    ISM_STATUS setVolume(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                         ISM_ADDR pValue);
    ISM_STATUS getVolume(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                         ISM_ADDR pValue);
    ISM_STATUS setDiskParms(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                            ISM_ADDR pValue);
    ISM_STATUS getDiskParms(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                            ISM_ADDR pValue);
    ISM_STATUS getPartition(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                            ISM_ADDR pValue);
    ISM_STATUS setFieldInvalid(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                               ISM_ADDR pValue);
    ISM_STATUS setRaidDevField(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                               ISM_ADDR pValue);
    ISM_STATUS getRaidDevField(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                               ISM_ADDR pValue);
    ISM_STATUS getRaidDevVol(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                               ISM_ADDR pValue);
    ISM_STATUS getRaidDevMap(U32* instanceIds, ISM_ADDR pKey,  U32 fieldIdx,
                               ISM_ADDR pValue);
    ISM_STATUS getArray(U32* instanceIds, ISM_ADDR pKey, U32 fieldIdx,
                        ISM_ADDR pValue);
    ISM_STATUS setArray(U32* instanceIds, ISM_ADDR pKey, U32 fieldIdx,
                        ISM_ADDR pValue);
    ISM_STATUS getArrayDisk(U32* instanceIds, ISM_ADDR pKey, U32 fieldIdx,
                            ISM_ADDR pValue);
    ISM_STATUS getArrayRaidDev(U32* instanceIds, ISM_ADDR pKey, U32 fieldIdx,
                               ISM_ADDR pValue);
    ISM_STATUS getRaidDevErlField(U32* instanceIds, ISM_ADDR pKey,
                                  U32 fieldIdx, ISM_ADDR pValue);
    ISM_STATUS getNvCachePolicyStats(U32* instanceIds, ISM_ADDR pKey,
                                     U32 fieldIdx, ISM_ADDR pValue);
    ISM_STATUS getNvCacheStats(U32* instanceIds, ISM_ADDR pKey,
                               U32 fieldIdx, ISM_ADDR pValue);
    ISM_STATUS setNvCacheStats(U32* instanceIds, ISM_ADDR pKey,
                               U32 fieldIdx, ISM_ADDR pValue);
    ISM_STATUS getNvCacheInfo(U32* instanceIds, ISM_ADDR pKey,
                              U32 fieldIdx, ISM_ADDR pValue);
    ISM_STATUS setNvCacheInfo(U32* instanceIds, ISM_ADDR pKey,
                              U32 fieldIdx, ISM_ADDR pValue);
    ISM_STATUS getVolNvCacheInfo(U32* instanceIds, ISM_ADDR pKey,
                                 U32 fieldIdx, ISM_ADDR pValue);
    ISM_STATUS setVolNvCacheInfo(U32* instanceIds, ISM_ADDR pKey,
                                 U32 fieldIdx, ISM_ADDR pValue);
    ISM_STATUS getNvCacheLbaInfo(U32* instanceIds, ISM_ADDR pKey,
                                 U32 fieldIdx, ISM_ADDR pValue);
    ISM_STATUS getNvCache(U32* instanceIds, ISM_ADDR pKey, NvCache*& nvCache);
    ISM_STATUS refreshPartition(U32* instanceIds, ISM_ADDR pKey, U32 fieldIdx, ISM_ADDR pval);
#ifdef ISM_TEST_CODE_DEBUG_EVENT_LOGGING
    ISM_STATUS setRaidDevErlField(U32* instanceIds, ISM_ADDR pKey,
                                  U32 fieldIdx, ISM_ADDR pValue);
#endif

    ISM_STATUS RaidIsm::getAoacInfo(U32* instanceIds, ISM_ADDR pKey,
                                       U32 fieldIdx, ISM_ADDR pValue);
    ISM_STATUS RaidIsm::setAoacInfo(U32* instanceIds, ISM_ADDR pKey,
                                       U32 fieldIdx, ISM_ADDR pValue);
    
    void getPuisStatistics(void* context, void * srb, Event* returnEvent);
    EVENT_PROLOG_H(nothing, ISM_ARG);
    U32 getReadParamsReqs();
    bool isConfigInitialized() {return configInitialized;} 

    bool isSelfSuspending() { return selfSuspending; }
    void setSuspendReason(SuspendReason r) {
        suspendReason = r;
    }
    SuspendReason getSuspendReason() { return suspendReason; }

    EventFifo* getFreeEvents() { return &freeEvents; }
    Event* getFreeEvent();

    bool startShutdown();
    void powerMgmt(Disk::PowerState powerUp, const Event& comp);
    void diskStartIoSuspend(Disk*, bool b);
    void diskPwrStateChangeNotify();
    EVENT_PROLOG_H_NO_ARG(updateNonArrayDiskPwr);
    void updateNonArrayDiskPwr();

    int initParity(char* raidSerialNo, Pba firstUnitNum=0);
    int disableParity(char* raidSerialNo);
    int checkParity(char* raidSerialNo, bool withFixup, Pba firstUnitNum=0);
    int rebuild(char* raidSerialNo, Disk* failedDev, Disk* spareDev,
                Pba firstUnitNum=0);
    int replace(char* raidSerialNo, Disk* failedDev, Disk* spareDev,
                Pba firstUnitNum=0);
    int migrate(CfgRaidDev* cdev);
    int migrateSafe(RaidDev* raidDev);
    RAID_ISM_INIT_PARMS* getInitParms() {return &initParms;}
    IntervalTimer* getIntervalTimer() { return intervalTimer; }

    bool isSystemIdle();
    bool areWritesDisabled() { return (disableAllDiskWrites != false); }
    bool isSuspended() { return (selfSuspending | suspended); }
    static U32 getNumMemFrags(UINT_PTR addr, U32 length) {
        return (PAGE_OFFSET(addr) + length + 
                       HOST_PAGE_SIZE - 1) / HOST_PAGE_SIZE;
    }
    static U32 getNumSglFrags(ISM_SG_ELEMENT* sglPtr) {
        return getNumMemFrags((UINT_PTR)sglPtr->u.Simple[0].PhysicalAddress,
                              sglPtr->u.Simple[0].FlagsCount.Count);
    }
    static void getNumSglFrags(ISM_SG_ELEMENT* sglPtr, U32 byteOffset,
                               U32& first, U32& second) {
        first = getNumMemFrags((UINT_PTR)sglPtr->u.Simple[0].PhysicalAddress,
                               byteOffset);
        second = getNumMemFrags((UINT_PTR)sglPtr->u.Simple[0].PhysicalAddress
                                + byteOffset,
                                sglPtr->u.Simple[0].FlagsCount.Count -
                                byteOffset);
    }

    U32 getMaxDiskSglMemFrags() { return maxDiskSglMemFrags; }
    static void noOpEH(ISM_OBJ_CONTEXT /*dummy1*/, ISM_ARG /*dummy2*/) {}

    bool isPatrolEnabled() { return initParms.patrolEnabled; }
    bool isRohiEnabled() { return initParms.rohiEnabled; }
    void patrolPolicyChanged();
    bool isNvCachedVolIdEmpty();
    bool isNvCachedVolPresent();
    bool volAndNvCacheMatch(RaidDev* raidDev);
    bool getNvmSupported() {
        return initParms.nvmSupported || initParms.minimizeSize;
    }
    ISM_PATH_TARGET_LUN generatePtl(CfgRaidDev * cfgRaidDev);
    bool shouldAllocateNvcMemory();        
};
        
        """
        
        return ccs