
import sys
import os
from ... DBG_AdapterBase import *
from ... fields.DBG_FieldsMapper import *
from ... appsrc.mmio.DBG_MMIO_Types import *
from ... appcore.memory.DBG_Utils import *

class DBG_Mmio_Py(DBG_AdapterBase):
        def __init__(self, spar, pparent):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_Mmio_Py::__init__::m_in::")
                
                self.xx_set_class_name ( "DBG_Mmio_Py" )
                self.xx_set_full_class_name ( "iastora!DBG_Mmio_Py" )
                
                self.m_fields = DBG_FieldsMapper("DBG_Mmio_Py", self)
                self.xx_dbg("DBG_Mmio_Py::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_Mmio_Py::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_Mmio_Py::prepare_object_internal::")                
                
                if(self.xx_obj_valid() == 1 ):
                        self.clear_messages()
                        self.m_fields.set_fields_parent(self)
                        #self.m_fields.prepare_object()
                        self.parse_ahci_mmio()
                                                
                self.xx_dbg("DBG_Mmio_Py::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("DBG_Mmio_Py::self.print_object")
                        
        def print_object_internal(self,sdbg=""):
                try:
                        self.xx_dbg("DBG_Mmio_Py::print_object_internal::m_in::")
                        #self.prepare_object()                
                        self.xx_print_ptr("")
                        if(self.xx_obj_valid() == 1 ):                                
                                self.m_fields.print_object()
                                
                        self.xx_dbg("DBG_Mmio_Py::print_object_internal::m_out::")
                except:
                        self.xx_exception("DBG_Mmio_Py::print_object_internal")

        def xx_obj_valid(self):
                self.xx_dbg("DBG_Mmio_Py::xx_obj_valid::m_in::")
                #i_valid = self.xx_is_object()
                i_valid = 1
                self.xx_dbg("DBG_Mmio_Py::xx_obj_valid::m_out::" + str(i_valid))
                return i_valid
        
        
        def parse_ahci_mmio(self):
                try:
                        self.xx_dbg("DBG_Mmio_Py::parse_ahci_mmio::m_in::")
                        self.add_raw_str(  'ACHI controller mmio')
                        
                        i_check = DBG_Utils().xx_dbgCommandCheck_Out01('!pci 140 0 17 0')
                        
                        if(i_check != 1):
                                self.add_raw_str('Crash dump mode')
                                return
                        
                        ahci_pci_cs = DBG_Utils().xx_dbgCommand('!pci 140 0 17 0')
                        list = ahci_pci_cs.split()
                        abar = None
                        for i,line in enumerate(list):
                                if line == 'BAR5':
                                    abar = list[i+1]
                                    break
                        if abar:
                                self.add_raw_str(  'abar '+ abar )
                        abar_hex = 0x0
                        try:
                                abar_hex = int(abar,16)
                        except:
                                self.add_raw_str('Crash dump mode')
                                return
                        
                        Port1_offset = 0x180
                        CAP_offset = 0x0
                        CAP2_offset = 0x24
                        PxCMD_offset = 0x18
                        PxSSTS_offset = 0x28
                        PxSCTL_offset = 0x2C
                        PxDEVSLP_offset = 0x44
                        PxSACT_offset = 0x34
                        PxCI_offset = 0x38
                        
                        self.add_raw_str(  'ABAR:')
                        self.add_raw_str(  str(abar_hex))
                        value_hex_string = self.read_32_bits_mmio(abar_hex+CAP_offset)
                        self.add_raw_str(  'CAP:')
                        
                        cap = CAP()
                        cap.asbyte = int(value_hex_string,16)
                        self.print_bitfield(cap)
                        self.add_raw_str(  '' )
                        
                        value_hex_string = self.read_32_bits_mmio(abar_hex+CAP2_offset)
                        self.add_raw_str(  'CAP2:')
                        cap2 = CAP2()
                        cap2.asbyte = int(value_hex_string,16)
                        self.print_bitfield(cap2)
                        self.add_raw_str(  '')
                        
                        value_hex_string = self.read_32_bits_mmio(abar_hex+Port1_offset+PxCMD_offset)
                        self.add_raw_str(  'CMD:')
                        pxcmd = PxCMD()
                        pxcmd.asbyte = int(value_hex_string,16)
                        self.print_bitfield(pxcmd)
                        self.add_raw_str(  '')
                        
                        value_hex_string = self.read_32_bits_mmio(abar_hex+Port1_offset+PxSSTS_offset)
                        self.add_raw_str(  'PxSSTS:')
                        pxssts = PxSSTS()
                        pxssts.asbyte = int(value_hex_string,16)
                        self.print_bitfield(pxssts)
                        self.add_raw_str(  '')
                        
                        value_hex_string = self.read_32_bits_mmio(abar_hex+Port1_offset+PxSCTL_offset)
                        self.add_raw_str(  'PxSCTL:')
                        pxsctl = PxSCTL()
                        pxsctl.asbyte = int(value_hex_string,16)
                        self.print_bitfield(pxsctl)
                        self.add_raw_str(  '')
                        
                        value_hex_string = self.read_32_bits_mmio(abar_hex+Port1_offset+PxDEVSLP_offset)
                        self.add_raw_str(  'PxDEVSLP:')
                        pxdevslp = PxDEVSLP()
                        pxdevslp.asbyte = int(value_hex_string,16)
                        self.print_bitfield(pxdevslp)
                        self.add_raw_str(  '')
                        
                        value_hex_string = self.read_32_bits_mmio(abar_hex+Port1_offset+PxSACT_offset)
                        self.add_raw_str(  'PxSACT:')
                        pxsact = PxSACT()
                        pxsact.asbyte = int(value_hex_string,16)
                        self.print_bitfield(pxsact)
                        self.add_raw_str(  '')
                        
                        value_hex_string = self.read_32_bits_mmio(abar_hex+Port1_offset+PxCI_offset)
                        self.add_raw_str(  'PxCI:')
                        pxci = PxCI()
                        pxci.asbyte = int(value_hex_string,16)
                        self.print_bitfield(pxci) 
                        self.add_raw_str(  '')
                        
                        self.add_raw_str(  'Device Sleep related registers:')
                        
                        self.add_raw_str(  'PxCI : ' + str(pxci.b.CI_command_issued) )
                        self.add_raw_str(  'PxSACT : '+ str(pxsact.b.DS_device_status ))
                        self.add_raw_str(  'PxDEVSLP.ADSE : '+ str(pxdevslp.b.ADSE_aggresive_device_sleep_enable))
                        self.add_raw_str(  'CAP2.SDS : ' + str(cap2.b.SDS_supports_device_sleep))
                        self.add_raw_str(  'CAP2.SADM : ' + str(cap2.b.SADM_supports_aggressive_device_sleep_management))
                        self.add_raw_str(  'PxDEVSLP.DSP : ' + str(pxdevslp.b.DSP_device_sleep_present))
                        self.add_raw_str(  'PxSCTL.IPM : ' + str(pxsctl.b.IPM_interface_power_management_transitions_allowed))
                        self.add_raw_str(  'PxSSTS.IPM : ' + str(pxssts.b.IPM_interface_power_management))
                        self.xx_dbg("DBG_Mmio_Py::parse_ahci_mmio::m_out::")
                except:
                        self.xx_exception("DBG_Mmio_Py::print_object_internal")

        def read_32_bits_mmio(self, address):
                try:
                        self.xx_dbg("DBG_Mmio_Py::read_32_bits_mmio::m_in::")
                        address_hex_string = hex(address).strip('L')
                        #self.add_raw_str(  '!dd '+address_hex_string+' L 1'
                        value_hex_string = dbgCommand('!dd '+ address_hex_string+' L 1').split(' ')[1]
                        #self.add_raw_str(  value_hex_string
                        self.xx_dbg("DBG_Mmio_Py::read_32_bits_mmio::m_in::")
                        return value_hex_string
                except:
                        self.xx_exception("DBG_Mmio_Py::print_object_internal")        
                        
        def add_raw_str(self,tt):
                if(tt == ""):
                        tt = "EMPTY_LINE"
                self.m_fields.add_raw_str(tt)


        def print_bitfield(self,bit_field):
                try:
                        for i in bit_field.b._fields_:
                            self.add_raw_str(  str(i[0]) +' ' + str(getattr(bit_field.b,i[0])) )               
                except:
                        self.xx_exception("DBG_Mmio_Py::print_bitfield::exception::")
                        
        def print_object_global(self):
            self.x_dbg("DBG_Mmio_Py::print_object_global::out::")                  
            self.prepare_object()        
            self.print_object()
            self.x_dbg("DBG_Mmio_Py::print_object_global::out::")
                        
