
import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. appcore.config.DBG_PrintConfig import *
#from .. appsrc.acpi.DBG_DRIVER_OBJECT import *
from .. driver.DBG_RemapInfo_PyArray import *
from .. driver.DBG_BOOT_LOCATION import *
class DBG_CrashHiberMemoryDescriptor(DBG_AdapterBase):
		def __init__(self,spar, pparent):
				DBG_AdapterBase.__init__(self, spar)
				self.xx_dbg("DBG_CrashHiberMemoryDescriptor::__init__::m_in::")
				
				self.xx_set_class_name ( "CrashHiberMemoryDescriptor" )
				self.xx_set_full_class_name ( "iastora!Wcdl::CrashHiberMemoryDescriptor" )
				
				self.m_fields = DBG_FieldsMapper("DBG_CrashHiberMemoryDescriptor", self)
				self.init_object_fields()
				
				self.m_remap_array = DBG_RemapInfo_PyArray("DBG_CrashHiberMemoryDescriptor",self)
				self.mBootLocation = DBG_BOOT_LOCATION("DBG_CrashHiberMemoryDescriptor",self)
				self.xx_dbg("DBG_CrashHiberMemoryDescriptor::__init__::m_out::")


		def init_object_fields(self):
				self.xx_dbg("DBG_CrashHiberMemoryDescriptor::init_object_fields::in::")                                
				self.m_fields.add_fields_asstr_ints(
						[
						 "mNvCacheMemorySize"
						 ,"mDriverMemorySize"
						 ])
				
				if(DBG_PrintConfig().getItem().m_print_volport_main == 0):
					self.m_fields.add_fields_asstr_addr("mAllocatorMemory")
					self.m_fields.add_fields_asstr_addr("mAllocatorMemorySize")
					
				self.m_fields.add_fields_asstr_addr("mNvCacheMemory")
				self.m_fields.add_fields_asstr_addr("mDriverMemory")
				self.xx_dbg("DBG_CrashHiberMemoryDescriptor::init_object_fields::m_out::")

		def prepare_object(self):
				try:
						self.prepare_object_internal(self)
				except:
						self.xx_exception("DBG_CrashHiberMemoryDescriptor::prepare_object::exc::")
										
		def prepare_object_internal(self, pparent):
				self.xx_dbg("DBG_CrashHiberMemoryDescriptor::prepare_object_internal::")                                
				if(self.xx_obj_valid() == 1 ):
						self.clear_messages()
						self.m_fields.set_fields_parent(self)
						self.m_fields.prepare_object()
						
						#self.m_remap_array.xx_set_full_class_name (  )
						#self.m_remap_array.set_addr(self,"SELF")
						#self.m_remap_array.set_range(3)
						#self.m_remap_array.prepare_object()
						if (DBG_PrintConfig().getItem().m_handle_remapinfo == "1"):
								s_base = "iastora!Wcdl::CrashHiberMemoryDescriptor"
								self.initialize_arr_by_addr(self.m_remap_array, self, s_base, 3)
						self.mBootLocation.set_addr_arr(self,"mBootLocation")
						self.mBootLocation.prepare_object()
						
				self.xx_dbg("DBG_CrashHiberMemoryDescriptor::prepare_object::m_out::")
				
		def print_object(self,sdbg=""):
				try:
						self.xx_print_start("")
						self.print_object_internal(sdbg)
						self.xx_print_end("")
				except:
						self.xx_exception("DBG_CrashHiberMemoryDescriptor::print_object")
						
		def print_object_internal(self,sdbg=""):
				self.xx_dbg("DBG_CrashHiberMemoryDescriptor::print_object::m_in::")
				self.prepare_object()                
				self.xx_print_ptr("")
				if(self.xx_obj_valid() == 1 ):                                                        
						self.m_fields.print_object()
						if (DBG_PrintConfig().getItem().m_handle_remapinfo == "1"):
								self.m_remap_array.print_object()
						self.mBootLocation.print_object()
														
				self.xx_dbg("DBG_CrashHiberMemoryDescriptor::print_object::m_out::")

		def xx_obj_valid(self):
				self.xx_dbg("DBG_CrashHiberMemoryDescriptor::xx_obj_valid::m_in::")
				i_valid = self.xx_is_object()
				self.xx_dbg("DBG_CrashHiberMemoryDescriptor::xx_obj_valid::m_out::" + str(i_valid))
				return i_valid
		
