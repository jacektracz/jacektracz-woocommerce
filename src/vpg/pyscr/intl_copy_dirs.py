#==================================================================
#
#    Copyright (c) 2016 Intel
#    
#==================================================================
import os
import errno
import shutil
			
class	intl_copy_dirs:
	
	#==================================================================
	#
	#==================================================================
	
	def __init__ (self):
		#self.m_dir_root = "C:/lkd/wmtgit/v06/scate-dashboard"
		self.m_dir_root = "C:/lkd/wmt/frontend"
		self.m_dir_dest = "C:/lkd/wmt/frontendshort"
		self.m_test_mode= "1"

	def cpy_shorts_libs(self):
		self.m_test_mode= "0"
		self.short_source("")
		self.copy_files_generic_full_libs()
		
	def short_source(self,tt):
		self.m_dir_dest = "C:/lkd/wmt/frontend"
		self.m_dir_root = "C:/lkd/wmt/frontendshort"
		
	def jx(self,tt):
		return "jxpgen" + tt + "xitem"
		
	def copy_files_generic_full(self):
		s_root_dst = []
		all = 0
		if( all == 1):
			s_root_dst.append(self.jx("menu"))
			s_root_dst.append(self.jx("rqsctest"))
			s_root_dst.append(self.jx("user"))
			s_root_dst.append(self.jx("rquserrole"))
			self.copy_files_generic_arr(s_root_dst)
			self.copy_from_genericL0('dao')
		self.copy_from_generic_3("menu")
		
	def copy_files_generic_full_libs(self):
		self.copy_from_genericL0('dao')
		self.copy_from_genericL0('helpers')
		self.copy_from_genericL0('xpgen')
		self.copy_from_genericL0('models')
		self.copy_from_genericL0('services')
		self.copy_from_genericL0('helpers')
		self.copy_fileL0("tools.js")
		self.copy_from_generic_3(self.jx("menu"))
		
	def copy_files_generic(self):
		s_root_dst = []
		s_root_dst.append(self.jx("rqdefview"))
		s_root_dst.append(self.jx("rqdefcolumn"))
		self.copy_files_generic_arr(s_root_dst)
	
	def copy_files_generic_arr(self, s_arr):
		try:				
			for s_root_dst in s_arr:
				self.copy_from_generic_3(s_root_dst)
			
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	def copy_from_generic_3( self, p_path_src ):
		try:
			self.copy_from_genericL1("routes", p_path_src)
			self.copy_from_genericL1("controllers", p_path_src)
			self.copy_from_genericL1("templates", p_path_src)
			
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	def copy_from_genericL1( self, p_type, p_path_src):
		try:
			self.dbg_info("type:" + p_type)
			s_root_path = self.m_dir_root + "/app/" + p_type +"/" + p_path_src + ""
			s_dest_path = self.m_dir_dest + "/app/" + p_type +"/" + p_path_src + ""
			s_source = s_root_path 
			s_dest = s_dest_path 
			#self.copy_directory(s_source, s_dest)
			self.recursive_overwrite(s_source, s_dest, None)
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	def copy_from_genericL0( self, p_type):
		try:
			self.dbg_info("type:" + p_type)
			s_root_path = self.m_dir_root + "/app/" + p_type  + ""
			s_dest_path = self.m_dir_dest + "/app/" + p_type +	""
			s_source = s_root_path 
			s_dest = s_dest_path 
			#self.copy_directory(s_source, s_dest)
			self.recursive_overwrite(s_source, s_dest, None)
		except OSError as e:
			print('file not copied. Error: %s' % e)

	def copy_froots( self, p_type, p_path_src):
		try:
			self.dbg_info("type:" + p_type)
			s_root_path = self.m_dir_root + "/app/" + p_type +"/" + p_path_src + ""
			s_dest_path = self.m_dir_dest + "/app/" + p_type +"/" + p_path_src + ""
			s_source = s_root_path 
			s_dest = s_dest_path 
			#self.copy_directory(s_source, s_dest)
			self.recursive_overwrite(s_source, s_dest, None)
		except OSError as e:
			print('file not copied. Error: %s' % e)

			
	def copy_directory(self, src, dest):
		try:
			self.dbg_info("")
			self.dbg_info("")			
			self.dbg_info("copy dir:" + src )
			self.dbg_info("to dir  :" + dest )
			if self.m_test_mode == "0":
				shutil.copytree(src, dest)
				
		except OSError as e:
			if e.errno == errno.ENOTDIR:
				shutil.copy(src, dest)
			else:
				print('Directory not copied. Error: %s' % e)
			
			
	def dbg_info(self, tt):
		print ( tt )
		
	def recursive_overwrite(self, src, dest, ignore=None):
		self.dbg_info("")
		self.dbg_info("")			
		self.dbg_info("recursive_overwrite:" + src )
		self.dbg_info("recursive_overwrite  :" + dest )	
		if os.path.isdir(src):
			if not os.path.isdir(dest):
				os.makedirs(dest)
			files = os.listdir(src)
			if ignore is not None:
				ignored = ignore(src, files)
			else:
				ignored = set()
			for f in files:
				if f not in ignored:
					self.recursive_overwrite(os.path.join(src, f), 
										os.path.join(dest, f), 
										ignore)
		else:
			shutil.copyfile(src, dest)			
			
	def copy_fileL0( self, p_src):
		try:
			
			s_root_path = self.m_dir_root + "/app/"
			s_dest_path = self.m_dir_dest + "/app/"
			s_source = s_root_path + p_src
			s_dest = s_dest_path + p_src
			self.copy_file(s_source, s_dest)
		except OSError as e:
			print('file not copied. Error: %s' % e)
	
	def copy_file(self, src, dest):
		try:
			self.dbg_info("")
			self.dbg_info("")			
			self.dbg_info("copy file" + src )
			self.dbg_info("to file" + dest )
			if self.m_test_mode == "0":
				self.dbg_info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" )
				self.dbg_info("real_copy_mode" )
				shutil.copyfile(src, dest)
				self.dbg_info("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<" )
			else:
				self.dbg_info("test_mode" )
			
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
if __name__ == '__main__':
	#data = intl_create_scate().copy_files_scate()
	#data = intl_create_scate().copy_files_scate_editcreate()
	#data = intl_copy_dirs().copy_files_generic()
	data = intl_copy_dirs().cpy_shorts_libs()
	
	
#python C:\lkd\w2\gitp\src\vpg\pyscr\intl_copy_dirs.py