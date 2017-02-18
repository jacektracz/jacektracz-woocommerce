import sys
import os        
        
class DBG_PortStateMachineMap:
        def __init__(self,spar):                
                self.m_items = []
                self.create_map()
                
        def create_map(self):
            
                self.m_items = [
                        "StateUnknown",
                        "StateEnableFisReceive",
                        "StateClearStart",
                        "StateSpinup",
                        "StateWaitForSpinup",
                        "StateClearSerr",
                        "StateInit",
                        "StateNotRunning",
                        "StateWaitForReady",
                        "StateSetStart",
                        "StateRunning",
                        "StateWaitForDET",
                        "StateWaitWhileDET1",
                        "StateStartDiscovery",
                        "StateDiscoveryDetermineZpoddPort",
                        "StateDiscoveryDetermineZpoddPortWait",
                        "StateDiscoveryIdentifyDeviceType",
                        "StateDiscoveryGetIdentifyData1",
                        "StateDiscoveryGetIdentifyDataWait1",
                        "StateDiscoveryGetIdentifyData2",
                        "StateDiscoveryGetIdentifyDataWait2",
                        "StateDiscoveryGetIdentifyDataLogSataPage",
                        "StateDiscoveryGetIdentifyDataLogSataPageWait",
                        "StateDiscoverySpinUpPuisDisk",
                        "StateDiscoverySpinUpPuisDiskWait",
                        "StateDiscoveryIdle",
                        "StateDiscoveryIdleWait",
                        "StateDiscoveryGetAcpiTaskFile",
                        "StateDiscoveryGetAcpiTaskFileWait",
                        "StateDiscoveryProgramAcpiTaskFile",
                        "StateDiscoveryProgramAcpiTaskFileWait",
                        "StateDiscoveryCompleteEnableInts",
                        "StateDiscoveryConfigurePort1",
                        "StateDiscoveryCompleteConfigurePort",
                        "StateDiscoverySetFeatures",
                        "StateDiscoverySetFeaturesWait",
                        "StateDiscoveryComplete",
                        "StateReset",
                        "StateResetClearStart",
                        "StateResetWait",
                        "StateResetFinish",
                        "StateRecoveryClearStart",
                        "StateRecoverySetStart",
                        "StateRecoverySendReadLog",
                        "StateRecoverySendReadLogWait",
                        "StateRecoveryFailCommand",
                        "StateRecoveryResubmitCommands",
                        "StateStoppedTrying",
                        "StateFailed"]
            
        def get_str(self, smb):
                try:
                        if(smb >=0 and smb < len(self.m_items)):
                                return self.m_items[smb]
                        else:
                                return "Unkonown_DBG_PortStateMachineMap:" + str(smb)
                except:
                        return "Unkonown_DBG_PortStateMachineMap:"
        