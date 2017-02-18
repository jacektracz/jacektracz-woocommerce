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
		self.m_test_mode= "0"
		
	def jx(self,tt):
		return "jxpgen" + tt + "xitem"
		
	def copy_files_generic(self):
		s_root_dst = []
		s_root_dst.append(self.jx("menu"))
		s_root_dst.append(self.jx("rqsctest"))
		self.copy_files_generic_arr(s_root_dst)
	
	def copy_files_generic_arr(self, s_arr):
		try:				
			for s_root_dst in s_arr:
				self.copy_from_generic_3(s_root_dst)
			
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	def copy_from_generic_3( self, p_path_src ):
		try:
			self.copy_from_generic("routes", p_path_src)
			self.copy_from_generic("controllers", p_path_src)
			self.copy_from_generic("templates", p_path_src)
			
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	def copy_from_generic( self, p_type, p_path_src):
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
		self.dbg_info("copy dir:" + src )
		self.dbg_info("to dir  :" + dest )	
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
if __name__ == '__main__':
	#data = intl_create_scate().copy_files_scate()
	#data = intl_create_scate().copy_files_scate_editcreate()
	data = intl_copy_dirs().copy_files_generic()
	
	
# cd C:\lkd\wmtgit\w2_2\src\w2\A05_MGR_PYTHON\MGRV1\MGRPYTHON\	
#!py C:\lkd\wmtgit\w2_2\src\w2\A05_MGR_PYTHON\MGRV1\MGRPYTHON\intl_create_scate.py			
#python C:\lkd\wmtgit\w2_2\src\w2\A05_MGR_PYTHON\MGRV1\MGRPYTHON\intl_create_scate.py

#python C:\lkd\wmt\vpg\pyscr\intl_copy_dirs.py