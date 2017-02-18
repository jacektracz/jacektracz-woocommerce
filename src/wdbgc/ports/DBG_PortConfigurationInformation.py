import sys
import os

from .. DBG_AdapterBase import *       
from .. appcore.memory.DBG_WdbgItemsPrinter import *
from .. fields.DBG_FieldsMapper import *

class DBG_PortConfigurationInformation(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_PortConfigurationInformation::__init__::")
                self.xx_set_class_name ( "_PORT_CONFIGURATION_INFORMATION" )                
                self.xx_set_full_class_name ( "iastora!_PORT_CONFIGURATION_INFORMATION" )
                self.m_fields = DBG_FieldsMapper("DBG_PortConfigurationInformation"
                                                 ,self)
                self.m_fields.add_int("MaximumNumberOfTargets")
                self.m_fields.add_int("NumberOfBuses")                
                self.m_fields.add_int("NumberOfAccessRanges")
                self.m_fields.add_int("Dma32BitAddresses")
                self.m_fields.add_int("AdapterInterfaceType")
                self.m_fields.add_int("SlotNumber")
                self.m_fields.add_hex("SlotNumber")
                self.m_fields.add_fields_int_array([
                        "VirtualDevice"
                        ,"SynchronizationModel"
                        ,"InterruptSynchronizationMode"
                        ,"WmiDataProvider"
                        ,"MaximumNumberOfLogicalUnits"
                        ,"BusInterruptLevel2"
                        ,"BusInterruptVector2"
                        ,"DmaChannel2"
                        ,"DmaPort2"
                        ,"DmaWidth2"
                        ,"DmaSpeed2"
                        ,"DeviceExtensionSize"
                        ,"SpecificLuExtensionSize"
                        ,"SrbExtensionSize"
                        ,"Dma64BitAddresses"
                        ,"ResetTargetSupported"
                        ,"MaximumNumberOfLogicalUnits"
                        ,"WmiDataProvider"])
                
                self.xx_dbg("DBG_PortConfigurationInformation::__init__::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_PortConfigurationInformation::print_object_internal::")                                
                self.xx_print_ptr("")
                self.prepare_object()
                if(self.xx_is_object() == 0):
                        return
                self.m_fields.print_object()
                self.xx_dbg("DBG_PortConfigurationInformation::print_object_internal::out::")
                
        def prepare_object(self):
                self.xx_dbg("DBG_PortConfigurationInformation::prepare_object::")
                if(self.xx_is_object() == 0):
                        return                
                self.m_fields.set_parent(self)
                self.m_fields.prepare_object()
                self.xx_dbg("DBG_PortConfigurationInformation::prepare_object::out::")        