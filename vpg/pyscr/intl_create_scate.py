#==================================================================
#
#    Copyright (c) 2016 Intel
#    
#==================================================================

import errno
import shutil
			
class	intl_create_scate:
	
	#==================================================================
	#
	#==================================================================
	
	def __init__ (self):
		#self.m_dir_root = "C:/lkd/wmtgit/v06/scate-dashboard"
		self.m_dir_root = "C:/lkd/wmt/frontend"
		self.m_test_mode= "0"
		

	def copy_directory(src, dest):
		try:
			shutil.copytree(src, dest)
		except OSError as e:
			# If the error was caused because the source wasn't a directory
			if e.errno == errno.ENOTDIR:
				shutil.copy(src, dest)
			else:
				print('Directory not copied. Error: %s' % e)
	#==================================================================
	#
	#==================================================================

	def copy_files_scate(self):
		try:			
			self.copy_from_root3("", "jxsearch", "jxsearch-for-jxlist")
			self.copy_from_root3("", "jxsearch", "jxsearch-for-jxlist-filter")
			self.copy_from_root3("", "jxsearch", "jxsearch-for-rqsctest")
			self.copy_from_root3("", "jxsearch", "jxsearch")
			self.copy_from_root3("", "jxlist", "jxlist")
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	#==================================================================
	#
	#==================================================================
			
	def copy_from_root3( self, p_type, p_src, p_dest ):
		try:
			self.copy_from_root("routes",p_src + ".js", p_dest + ".js")
			self.copy_from_root("controllers",p_src + ".js", p_dest + ".js")
			self.copy_from_root("templates",p_src + ".hbs", p_dest + ".hbs")
		except OSError as e:
			print('file not copied. Error: %s' % e)

	#==================================================================
	#
	#==================================================================
			
	def copy_from_root( self, p_type, p_src, p_dest ):
		try:
			self.dbg_info("type:" + p_type)
			s_root_path = self.m_dir_root + "/app/" + p_type +"/jxpgenrqsctestxitem/"
			s_dest_path = self.m_dir_root + "/app/" + p_type +"/streamtests/"
			s_source = s_root_path + p_src
			s_dest = s_dest_path + p_dest
			self.copy_file(s_source, s_dest)
		except OSError as e:
			print('file not copied. Error: %s' % e)
			

	#==================================================================
	#
	#==================================================================
	def copy_files_scate_generic(self):
		try:
			s_root = "streamtests"
			
			self.copy_from_self_path_3("", "editcreate", "editcreate-for-jxlist", s_root)
			self.copy_from_self_path_3("", "editcreate", "editcreate-for-jxlist-filter", s_root)
			self.copy_from_self_path_3("", "editcreate", "editcreate-for-rqsctest", s_root)
			
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	def copy_from_self_path_3( self, p_type, p_src, p_dest, p_self_path ):
		try:
			self.copy_from_self_path("routes",p_src + ".js", p_dest + ".js",p_self_path)
			self.copy_from_self_path("controllers",p_src + ".js", p_dest + ".js",p_self_path)
			self.copy_from_self_path("templates",p_src + ".hbs", p_dest + ".hbs",p_self_path)
		except OSError as e:
			print('file not copied. Error: %s' % e)			
	#==================================================================
	#
	#==================================================================

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
			
	#==================================================================
	#
	#==================================================================
	
	#==================================================================
	#
	#==================================================================
	
	def copy_files_generic(self):
		try:		
			s_root_src = "jxpgenmenuxitem"
			s_root_dst = "jxpgenmenuxitem"
			self.copy_from_generic_3("", "jximport", "jxopermainfilter", s_root_src, s_root_dst)
			
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	def copy_from_generic_3( self, p_type, p_src, p_dest, p_self_path_src,p_self_path_dst ):
		try:
			self.copy_from_generic("routes",p_src + ".js", p_dest + ".js",p_self_path_src,p_self_path_dst)
			self.copy_from_generic("controllers",p_src + ".js", p_dest + ".js",p_self_path_src,p_self_path_dst)
			self.copy_from_generic("templates",p_src + ".hbs", p_dest + ".hbs",p_self_path_src,p_self_path_dst)
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	def copy_from_generic( self, p_type, p_src, p_dest ,p_self_path_src, p_self_path_dst):
		try:
			self.dbg_info("type:" + p_type)
			s_root_path = self.m_dir_root + "/app/" + p_type +"/" + p_self_path_src + "/"
			s_dest_path = self.m_dir_root + "/app/" + p_type +"/" + p_self_path_dst + "/"
			s_source = s_root_path + p_src
			s_dest = s_dest_path + p_dest
			self.copy_file(s_source, s_dest)
		except OSError as e:
			print('file not copied. Error: %s' % e)
	
			
	def dbg_info(self, tt):
		print ( tt )
			
if __name__ == '__main__':
	#data = intl_create_scate().copy_files_scate()
	#data = intl_create_scate().copy_files_scate_editcreate()
	#data = intl_create_scate().copy_files_generic()
	
	
# cd C:\lkd\wmtgit\w2_2\src\w2\A05_MGR_PYTHON\MGRV1\MGRPYTHON\	
#!py C:\lkd\wmtgit\w2_2\src\w2\A05_MGR_PYTHON\MGRV1\MGRPYTHON\intl_create_scate.py			
#python C:\lkd\wmtgit\w2_2\src\w2\A05_MGR_PYTHON\MGRV1\MGRPYTHON\intl_create_scate.py

#python C:\lkd\wmt\vpg\pyscr\intl_create_scate.py