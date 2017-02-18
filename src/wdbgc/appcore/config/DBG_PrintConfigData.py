import sys
import os
import ConfigParser
from ... appcore.logging.DBG_ExceptionPrinter import *
from ... appcore.config.DBG_Version import *
from ... appcore.config.DBG_EnvSettings import *

#from ... appcore.config.DBG_PrintConfig import *
#p_all = DBG_PrintConfig().getItem().m_print_ahci_port_fields

class DBG_PrintConfigData:
	
	def __init__(self):
		self.m_print_miniport_params = "0"
		self.m_print_all_targets = 0
		self.m_print_driver = 1
		self.m_print_transports = 1
		self.m_print_raidism = 1
		self.m_print_raid_transport = 1
		self.m_print_raid_target = 1
		self.m_print_raid_targets = 1
		self.m_print_raid_rtargets = 1
		self.m_print_all_errors = 1
		self.m_print_ahci_port_fields = 0
		self.m_print_all_ahci_ports = 0
		self.m_log_all_errors = 0
		self.m_exit_on_exception = 0		
		self.m_system_target = 0
		self.m_drive = DBG_EnvSettings().get_env_drive()
		self.m_root_dir = self.m_drive +":/lkd/komodo/w2_2/apps/driver/"
		self.m_prefix = "iastora2.conf"
		self.m_version = "14"
		self.m_raid_targets_arr = "3d"
		#conf file selector
		self.m_file = "15"
		self.m_out_file_name = "iastoraN"
		self.m_store_errors = 1
		self.m_max_g_stored_errors = 10
		self.m_max_obj_stored_errors = 2
		self.m_dbg_all = 0
		self.m_dbg_all_logger = 0
		self.m_config = None
		self.m_verbose_check = 0
		self.m_skip_check = 0
		self.m_print_all_remap_transports = 0
		self.m_is_inbox = 0
		self.m_is_dump = 0
		self.m_print_raid_lock = 0
		self.m_print_remapport_main = 1
		self.m_print_raidport_main = 1
		self.m_print_volport_main = 0
		self.m_print_mmio_main = 1
		self.m_ver_obj = DBG_Version()
		self.m_version_1 =0
		self.m_version_2 =0
		self.m_version_3 =0
		self.m_handle_devices_in_transport_path =0
		self.m_env_selector = ""
		self.m_print_wdgb_symbols = 0
		self.m_print_stacks = 0
		self.m_handle_global_drivers = 0		
		self.m_handle_info = 1
		self.m_handle_env = 1
		
		self.m_handle_exc = 1
		self.m_sys_name = ""
		self.m_is_handled_lun = 1
		self.m_is_handled_d3 = 1
		self.m_dbg_printer = ""
		#check this only for 13
		self.m_handle_remapinfo = 0
		self.m_handle_methods = 0
		self.m_print_field_out = 1
		self.m_handle_srt_data = 1
		
		self.m_is_soft_remap = 1
		self.m_show_lg_address = 0
		self.m_handle_mdrFifo = 0 #some errors
		self.m_handle_mpb_diskTbl = 0
		self.m_handle_frames = 0
		#new_paths_64
		
		self.m_handle_transport_paths = 0
		
	def is_below(self, v_0,v_1=0,v_2=0,v_3 =0):
		is_below = 1
		is_above = self.self_is_above_or_equal(v_0, v_1, v_2, v_3 )
		if(is_above == 1 ):
			is_below = 0		
		return is_below
		
	def self_is_above_or_equal(self, v_0,v_1=0,v_2=0,v_3 =0):
		ddv = DBG_Version()
		ddv.set_vv(0,v_0)
		ddv.set_vv(1,v_1)
		ddv.set_vv(2,v_2)
		ddv.set_vv(3,v_3)
		is_ab = self.m_ver_obj.self_is_above_or_equal(ddv)
		return is_ab
	
		
	def get_config_full_file_path(self):
		return self.get_root_dir() +  self.m_file + ".txt"
	
	def get_root_dir(self):
		return self.m_root_dir
	
	def get_print_raid_rtargets(self):
		return self.m_print_raid_rtargets
	
	def get_print_raid_lock(self):
		return self.m_print_raid_lock
	
	def get_max_g_stored_errors(self):
		return self.m_max_g_stored_errors
	
	def get_max_obj_stored_errors(self):
		return self.m_max_obj_stored_errors
	
	def set_file(self,tt):
		try:
			self.m_file = tt
		except:
				self.xx_exception("DBG_PrintConfig::set_file::excp")
	
	def get_print_driver(self):
		return self.m_print_driver
	
	def get_print_stacks(self):
		return self.m_print_stacks
	
	def get_print_transports(self):
		return self.m_print_transports

	def get_print_raidism(self):
		return self.m_print_raidism
		
	def get_print_raid_transport(self):
		return self.m_print_raid_transport
	
	def get_print_raid_target(self):
		return self.m_print_raid_target

	def get_print_raid_targets(self):
		return self.m_print_raid_targets
	
	
	def get_system_target(self):
		return self.m_system_target
	
	def get_raid_targets_arr(self):
		return self.m_raid_targets_arr
	
	def set_raid_targets_arr(self,tt):
		self.m_raid_targets_arr = tt
	
	def get_version(self):
		return self.m_version
	
	def set_version(self,tt):
		self.m_version = tt
		
	def get_handle_devices_in_transport_path(self):
		return self.m_handle_devices_in_transport_path
	
	def write_config(self):
			try:
					self.xx_dbg("DBG_PrintConfigData::write_config::in::")
					sf = self.get_config_full_file_path()
					print "create_default_config -  start " + sf
					config = ConfigParser.RawConfigParser()
					
					config.add_section('mainconfig')
					config.set('mainconfig', 'm_out_file_name',self.m_out_file_name)
					config.set('mainconfig', 'm_version', self.m_version)
					config.set('mainconfig', 'm_log_all_errors',self.m_log_all_errors)
					config.set('mainconfig', 'm_exit_on_exception',self.m_exit_on_exception)
					config.set('mainconfig', 'm_system_target',self.m_system_target)					
					config.set('mainconfig', 'm_root_dir',self.m_root_dir)
					config.set('mainconfig', 'm_prefix',self.m_prefix)
					config.set('mainconfig', 'm_file',self.m_file)					
					config.set('mainconfig', 'm_raid_targets_arr',self.m_raid_targets_arr)										
					config.set('mainconfig', 'm_store_errors',self.m_store_errors)
					config.set('mainconfig', 'm_max_g_stored_errors',self.m_max_g_stored_errors)
					config.set('mainconfig', 'm_max_obj_stored_errors',self.m_max_obj_stored_errors)
					config.set('mainconfig', 'm_print_all_targets',self.m_print_all_targets)
					config.set('mainconfig', 'm_dbg_all',self.m_dbg_all)
					config.set('mainconfig', 'm_dbg_all_logger',self.m_dbg_all_logger)
					config.set('mainconfig','m_print_ahci_port_fields',self.m_print_ahci_port_fields)
					config.set('mainconfig','m_print_all_ahci_ports',self.m_print_all_ahci_ports)
					config.set('mainconfig','m_verbose_check',self.m_verbose_check)
					config.set('mainconfig','m_skip_check',self.m_skip_check)
					config.set('mainconfig','m_print_all_remap_transports',self.m_print_all_remap_transports)
					config.set('mainconfig','m_is_inbox',self.m_is_inbox)										
					
					config.set('mainconfig','m_print_raid_targets',self.m_print_raid_targets)
					config.set('mainconfig','m_print_raid_rtargets',self.m_print_raid_rtargets)
					config.set('mainconfig','m_print_raid_lock',self.m_print_raid_lock)
					
					with open(sf, 'w') as configfile:
							config.write(configfile)
							
					print "create_default_config -  success"
					self.xx_dbg("DBG_PrintConfigData::write_config::out::")
			except:
					self.xx_exception("DBG_PrintConfigData::write_config::excp")
					
	def read_config(self):
			try:
				self.xx_dbg("DBG_PrintConfigData::read_config::in::")
				
				self.m_config = ConfigParser.RawConfigParser()
				sf = self.get_config_full_file_path()
				
				if(os.path.isfile(sf)):
					
					self.m_config.read( sf )  
					self.m_version = self.config_get(
						'm_version'
						,self.m_version)
					
					self.m_version_1 = self.config_getint(
						'm_version_1'
						,self.m_version_1)
					
					self.m_version_2 = self.config_getint(
						'm_version_2'
						,self.m_version_2)
					
					self.m_version_3 = self.config_getint(
						'm_version_3'
						,self.m_version_3)
					
					self.m_ver_obj.set_vv(0,int(self.m_version))
					self.m_ver_obj.set_vv(1,int(self.m_version_1))
					self.m_ver_obj.set_vv(2,int(self.m_version_2))
					self.m_ver_obj.set_vv(3,int(self.m_version_3))
					
					self.m_log_all_errors =self.config_getint(
						'm_log_all_errors'
						,self.m_log_all_errors)
					
					self.m_exit_on_exception =self.config_getint(
						'm_exit_on_exception'
						,self.m_exit_on_exception)
					
					self.m_system_target =self.config_get(
						'm_system_target'
						,self.m_system_target)
					
					self.m_root_dir = self.config_get(
						'm_root_dir'
						,self.m_root_dir)
					
					self.m_raid_targets_arr =self.config_get(
						'm_raid_targets_arr'
						,self.m_raid_targets_arr)
					
					self.m_out_file_name = self.config_get(
						'm_out_file_name'
						,self.m_out_file_name)
					
					self.m_store_errors = self.config_getint(
						'm_store_errors'
						,self.m_store_errors)
					
					self.m_max_g_stored_errors = self.config_getint(
						'm_max_g_stored_errors'
						,self.m_max_g_stored_errors)
					
					self.m_max_obj_stored_errors = self.config_getint(
						'm_max_obj_stored_errors'
						,self.m_max_obj_stored_errors)
					
					self.m_print_all_targets = self.config_getint(
						'm_print_all_targets'
						,self.m_print_all_targets)
					
					self.m_dbg_all = self.config_getint(
						'm_dbg_all'
						,self.m_dbg_all)
					
					self.m_dbg_all_logger = self.config_getint(
						'm_dbg_all_logger'
						,self.m_dbg_all_logger)
					
					self.m_print_ahci_port_fields = self.config_getint(
						'm_print_ahci_port_fields'
						, self.m_print_ahci_port_fields)
					
					self.m_print_all_ahci_ports = self.config_getint(
						'm_print_all_ahci_ports'
						, self.m_print_all_ahci_ports)
					
					self.m_verbose_check = self.config_getint(
						'm_verbose_check'
						, self.m_verbose_check)					
					
					self.m_skip_check = self.config_getint(
						'm_skip_check'
						, self.m_skip_check)
										
					self.m_print_all_remap_transports = self.config_getint(
						'm_print_all_remap_transports'
						, self.m_print_all_remap_transports)
										
					self.m_is_inbox = self.config_getint(
						'm_is_inbox'
						, self.m_is_inbox)
					
					self.m_print_raid_lock = self.config_getint(
						'm_print_raid_lock'
						, self.m_print_raid_lock)
					
					self.m_print_raid_targets = self.config_getint(
						'm_print_raid_targets'
						, self.m_print_raid_targets)
					
					self.m_print_raid_rtargets = self.config_getint(
						'm_print_raid_rtargets'
						, self.m_print_raid_rtargets)
					
					self.m_print_remapport_main = self.config_getint(
						'm_print_remapport_main'
						, self.m_print_remapport_main)
					
					self.m_print_raidport_main = self.config_getint(
						'm_print_raidport_main'
						, self.m_print_raidport_main)
					
					self.m_print_volport_main = self.config_getint(
						'm_print_volport_main'
						, self.m_print_volport_main)
					
					self.m_print_mmio_main = self.config_getint(
						'm_print_mmio_main'
						, self.m_print_mmio_main)
					
					self.m_handle_devices_in_transport_path = self.config_getint(
						'm_handle_devices_in_transport_path'
						, self.m_handle_devices_in_transport_path)
					
					self.m_env_selector = self.config_get(
						'm_env_selector'
						, self.m_env_selector)

					self.m_is_dump = self.config_getint(
						'm_is_dump'
						, self.m_is_dump)
					
					self.m_print_wdgb_symbols = self.config_getint(
						'm_print_wdgb_symbols'
						, self.m_print_wdgb_symbols)
					
					self.m_sys_name = self.config_get(
						'm_sys_name'
						, self.m_sys_name)
					
					self.m_is_handled_lun = self.config_getint(
						'm_is_handled_lun'
						, self.m_is_handled_lun)
					
					self.m_is_handled_d3 = self.config_getint(
						'm_is_handled_d3'
						, self.m_is_handled_d3)
					
					
					self.m_print_stacks = self.config_getint(
						'm_print_stacks'
						, self.m_print_stacks)

					self.m_dbg_printer = self.config_get(
						'm_dbg_printer'
						, self.m_dbg_printer)

					self.m_handle_global_drivers = self.config_getint(
						'm_handle_global_drivers'
						, self.m_handle_global_drivers)

					self.m_handle_info = self.config_getint(
						'm_handle_info'
						, self.m_handle_info)
					
					self.m_handle_env = self.config_getint(
						'm_handle_env'
						, self.m_handle_env)
					
					self.m_handle_exc = self.config_getint(
						'm_handle_exc'
						, self.m_handle_exc)

					self.m_handle_srt_data = self.config_getint(
						'm_handle_srt_data'
						, self.m_handle_srt_data)
					
					self.m_print_field_out = self.config_getint(
						'm_print_field_out'
						, self.m_print_field_out)

					self.m_is_soft_remap = self.config_getint(
						'm_is_soft_remap'
						, self.m_is_soft_remap)

					self.m_show_lg_address = self.config_getint(
						'm_show_lg_address'
						,	self.m_show_lg_address)
					
					self.m_handle_transport_paths = self.config_getint(
						'm_handle_transport_paths'
						,	self.m_handle_transport_paths)

					self.m_handle_mpb_diskTbl = self.config_getint(
						'm_handle_mpb_diskTbl'
						,	self.m_handle_mpb_diskTbl)

					self.m_handle_frames = self.config_getint(
						'm_handle_frames'
						,	self.m_handle_frames)
					
					#m_handle_mpb_diskTbl
					#m_handle_transport_paths
					
					#m_show_lg_address
					#m_handle_frames
					#print "UUUUUUUUUUUUUUUUUUUUUUUUUUU:" + str(self.m_is_handled_lun)
					#m_handle_srt_data
					#m_print_field_out
					#m_handle_global_drivers
					#self.m_handle_info = 1
					#self.m_handle_env = 1
					#self.m_handle_exc = 1
					
					
				self.xx_dbg("DBG_PrintConfigData::read_config::out::")
			except:
				self.xx_exception("DBG_PrintConfigData::read_config::excp")


	def config_get(self,tt,sdef):
		try:
				self.xx_dbg("DBG_PrintConfigData::config_get::in::" + tt)
				sout = sdef
				if(self.m_config.has_option('mainconfig',tt)):
					sout = self.m_config.get('mainconfig', tt)
				self.xx_dbg("DBG_PrintConfigData::config_get::out::" + str(sout))
				return sout
		except:
				self.xx_exception("DBG_PrintConfigData::read_config::excp")
				return sdef

			
	def config_getint(self,tt,sdef):
		try:
				self.xx_dbg("DBG_PrintConfigData::config_get::in::" + tt)
				sout = sdef
				if(self.m_config.has_option('mainconfig',tt)):
					sout = self.m_config.getint('mainconfig', tt)
				self.xx_dbg("DBG_PrintConfigData::config_get::out::" + str(sout))
				return sout
		except:
				self.xx_exception("DBG_PrintConfigData::read_config::excp")
				return sdef
				
	def get_handle_global_drivers(self):
		self.xx_dbg("DBG_PrintConfigData::get_handle_global_drivers::in::" + str(self.m_handle_global_drivers))
		self.xx_dbg("DBG_PrintConfigData::get_handle_global_drivers::out::" + str(self.m_handle_global_drivers))
		return self.m_handle_global_drivers
	
	def get_path_out(self,tt):
		self.xx_dbg("DBG_PrintConfigData::get_path_out::in::" + tt)
		tt = self.get_root_dir() + self.m_out_file_name + "_out.html"
		self.xx_dbg("DBG_PrintConfigData::get_path_out::out::" + tt)
		return tt
	
	
	def get_path_err(self,tt):
		self.xx_dbg("DBG_PrintConfigData::get_path_err::in::" + tt)
		tt = self.get_root_dir() +  self.m_out_file_name + "_err.txt"
		self.xx_dbg("DBG_PrintConfigData::get_path_err::out::" + tt)
		return tt
	
	def get_path_trace(self,tt):
		self.xx_dbg("DBG_PrintConfigData::get_path_trace::in::" + tt)
		tt = self.get_root_dir() +  self.m_out_file_name + "_trace.txt"
		self.xx_dbg("DBG_PrintConfigData::get_path_trace::out::" + tt)
		return tt
	
	def get_path_logging(self,tt):
		self.xx_dbg("DBG_PrintConfigData::get_path_err::in::" + tt)
		tt = self.get_root_dir() +  self.m_out_file_name + "_logging.txt"
		self.xx_dbg("DBG_PrintConfigData::get_path_err::out::" + tt)
		return tt
	
	
	def set_out_file_name(self,tt):
		self.xx_dbg("DBG_PrintConfigData::set_file_name::in::" + tt)
		self.m_out_file_name = tt
		self.xx_dbg("DBG_PrintConfigData::set_file_name::out::" + tt)        
	
				
	def xx_dbg(self,tt):
		sinfo = ""
		DBG_ExceptionPrinter.xx_dbg(sinfo + tt)
	
	def xx_exception(self,tt):
		sinfo = ""
		DBG_ExceptionPrinter.print_exception(sinfo + tt)

	def check_dbg_filter(self,tt):
		try:
			i_check = 0
			if( self.m_dbg_printer != ""):
				i_idx = tt.find(self.m_dbg_printer)
				if(i_idx >= 0 ):
					i_check == 1
			return i_check
		except:
			return 0
		
	def path_in_range(self,p_ii):
			is_test = 0
			in_range = 0
			if(is_test == 1):
				in_range =  self.path_in_range_test(p_ii)
			else:
				in_range =  self.path_in_range_release(p_ii)
				
			return in_range
		
	def path_in_range_test(self,p_ii):
			
			in_range =0
			if(p_ii == 0):
				in_range =1
			return in_range
		
	def path_in_range_release(self,p_ii):
			
			in_range = 0
			if(p_ii < 4):
					in_range = 1
					
			#in_range = 0		
			if(p_ii > 15 and p_ii < 18) :
					in_range = 1
					
			return in_range
		