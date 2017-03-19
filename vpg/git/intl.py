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
		self.m_dir_root_src = "C:/lkd/wmt/frontend"
		self.m_dir_root_dst = "C:/lkd/wmt/frontendshort"
		self.m_test_mode= "0"
		self.m_move_lib = "1"
		self.m_move_gen = "0"
		self.m_move_common = "1"
		self.m_move_sctest = "1"
		self.m_move_bs_2015 = "0"
		self.m_move_src = "0"
		self.m_move_app_full = "0"
		self.m_move_app_short = "0"
		self.m_selector = "";
		self.m_move_vpg = "1"

	def copy_all_to_full_from_short_in_home(self):
		self.set_short_as_source_in_home()
		self.copy_dir_files_generic_full_libs()
		
	def copy_all_to_short_from_full_in_home(self):
		self.set_full_as_source_in_home()
		self.copy_dir_files_generic_full_libs()
		
	def copy_all_to_short_from_full_in_work(self):
		self.set_root_work_src_is_full()
		self.copy_dir_files_generic_full_libs()
		
	def copy_all_to_full_from_short_in_work(self):
		self.set_root_work_src_is_short()
		self.copy_dir_files_generic_full_libs()

	def set_short_as_source_in_home(self):		
		self.m_dir_root_src = "C:/lkd/wmt/frontendshort"
		self.m_dir_root_dst = "C:/lkd/wmt/frontend"
		
	def set_full_as_source_in_home(self):
		self.m_dir_root_src = "C:/lkd/wmt/frontend"
		self.m_dir_root_dst = "C:/lkd/wmt/frontendshort"
		
	def set_root_work_src_is_full(self):		
		self.m_dir_root_src = "C:/lkd/wmtgit/v06/scate-admin-dashboard"
		self.m_dir_root_dst = "C:/lkd/wmtgit/v06/scate-dashboard"
		
	def set_root_work_src_is_short(self):		
		self.m_dir_root_src = "C:/lkd/wmtgit/v06/scate-dashboard"
		self.m_dir_root_dst = "C:/lkd/wmtgit/v06/scate-admin-dashboard"
		
#python C:\lkd\w2\gitp\src\vpg\pyscr\intl_copy_dirs.py
	# create full from short
	
	def cpy_create_short_from_full_test(self):		
		self.set_full_as_source("")
		self.copy_dir_files_generic_full_test()
	
	def cpy_create_short_from_full(self):
		
		self.set_full_as_source("")
		self.copy_dir_files_generic_full_libs()

	def cpy_create_full_from_short_test(self):		
		self.set_short_as_source("")
		self.copy_dir_files_generic_full_test()
		
	def cpy_create_full_from_short(self):		
		self.set_short_as_source("")
		self.copy_dir_files_generic_full_libs()
		
	def copy_dir_files_generic_full_test(self):
		self.copy_fileL1_3("application")
		
	def copy_dir_files_generic_full_libs(self):
	
		if self.m_move_lib == "1":
			self.copy_dir_from_genericL0('dao')
			self.copy_dir_from_genericL0('helpers')
			self.copy_dir_from_genericL0('xpgen')
			self.copy_dir_from_genericL0('models')
			self.copy_dir_from_genericL0('services')
			self.copy_dir_from_genericL0('helpers')
			
		if self.m_move_common == "1":	
			self.copy_fileL0("tools.js")
			self.copy_fileL1_3("application")
			self.copy_fileL1_3("index")		
			self.copy_dir_from_genericL1("templates", "custom")		
			
		
		if self.m_move_gen == "1":
			self.copy_dir_from_generic_3(self.jx("menu"))
			self.copy_dir_from_generic_3(self.jx("user"))
			self.copy_dir_from_generic_3(self.jx("rquserrole"))			
			self.copy_dir_from_generic_3(self.jx("rqdefcolumn"))
			self.copy_dir_from_generic_3(self.jx("rqdefview"))
			self.copy_dir_from_generic_3(self.jx("rqsctest_completion"))
			self.copy_dir_from_generic_3(self.jx("rqsctest_test"))
		
		if self.m_move_sctest == "1":
			self.copy_dir_from_generic_3(self.jx("rqsctest"))
		
	def jx(self,tt):
		return "jxpgen" + tt + "xitem"
		
	def copy_dir_files_generic_full(self):
		s_root_dst = []
		all = 0
		if( all == 1):
			s_root_dst.append(self.jx("menu"))
			s_root_dst.append(self.jx("rqsctest"))
			s_root_dst.append(self.jx("user"))
			s_root_dst.append(self.jx("rquserrole"))
			self.copy_dir_files_generic_arr(s_root_dst)
			self.copy_dir_from_genericL0('dao')
		self.copy_dir_from_generic_3("menu")
		
		
	def copy_dir_files_generic(self):
		s_root_dst = []
		s_root_dst.append(self.jx("rqdefview"))
		s_root_dst.append(self.jx("rqdefcolumn"))
		self.copy_dir_files_generic_arr(s_root_dst)
	
	def copy_dir_files_generic_arr(self, s_arr):
		try:				
			for s_root_dst in s_arr:
				self.copy_dir_from_generic_3(s_root_dst)
			
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	def copy_dir_from_generic_3( self, p_path_src ):
		try:
			self.copy_dir_from_genericL1("routes", p_path_src)
			self.copy_dir_from_genericL1("controllers", p_path_src)
			self.copy_dir_from_genericL1("templates", p_path_src)
			
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	def copy_dir_from_genericL1( self, p_type, p_path_src):
		try:
			self.dbg_info("type:" + p_type)
			s_root_path = self.m_dir_root_src + "/app/" + p_type +"/" + p_path_src + ""
			s_dest_path = self.m_dir_root_dst + "/app/" + p_type +"/" + p_path_src + ""
			s_source = s_root_path 
			s_dest = s_dest_path 
			#self.copy_directory(s_source, s_dest)
			self.recursive_overwrite(s_source, s_dest, None)
		except OSError as e:
			print('file not copied. Error: %s' % e)
			
	def copy_dir_from_genericL0( self, p_type):
		try:
			self.dbg_info("type:" + p_type)
			s_root_path = self.m_dir_root_src + "/app/" + p_type  + ""
			s_dest_path = self.m_dir_root_dst + "/app/" + p_type +	""
			s_source = s_root_path 
			s_dest = s_dest_path 
			#self.copy_directory(s_source, s_dest)
			self.recursive_overwrite(s_source, s_dest, None)
		except OSError as e:
			print('file not copied. Error: %s' % e)

	def copy_froots( self, p_type, p_path_src):
		try:
			self.dbg_info("type:" + p_type)
			s_root_path = self.m_dir_root_src + "/app/" + p_type +"/" + p_path_src + ""
			s_dest_path = self.m_dir_root_dst + "/app/" + p_type +"/" + p_path_src + ""
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

	def recursive_overwrite_start(self, src, dest, ignore=None):
		self.dbg_info("")
		self.dbg_info("")			
		self.dbg_info("ls " + src )
		self.dbg_info("ls " + dest )	
		
	def recursive_overwrite(self, src, dest, ignore=None):
		self.dbg_info("")
		self.dbg_info("")			
		self.dbg_info("recursive_overwrite: " + src )
		self.dbg_info("recursive_overwrite  :" + dest )	
		
		if os.path.isdir(src):
			if not os.path.isdir(dest):
				if self.m_test_mode == "0":
					os.makedirs(dest)
				else:
					self.dbg_info("test_makedirs" + dest)
					
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
			self.copy_file(src, dest)
			#shutil.copyfile(src, dest)			
			
	def copy_fileL0( self, p_src):
		try:
			
			s_root_path = self.m_dir_root_src + "/app/"
			s_dest_path = self.m_dir_root_dst + "/app/"
			s_source = s_root_path + p_src
			s_dest = s_dest_path + p_src
			self.copy_file(s_source, s_dest)
		except OSError as e:
			print('file not copied. Error: %s' % e)
	
	def copy_fileL1_3( self, p_src):	
		self.copy_fileL1("controllers", p_src + ".js")
		self.copy_fileL1("routes", p_src + ".js")
		self.copy_fileL1("templates", p_src + ".hbs")
		
	def copy_fileL1( self, p_dir0, p_src):
		try:
			
			s_root_path = self.m_dir_root_src + "/app/" + p_dir0 + "/"
			s_dest_path = self.m_dir_root_dst + "/app/" + p_dir0 + "/"
			s_source = s_root_path + p_src
			s_dest = s_dest_path + p_src
			self.copy_file(s_source, s_dest)
		except OSError as e:
			print('file not copied. Error: %s' % e)
	
	def copy_file(self, src, dest):
		try:
			self.dbg_info("")
			self.dbg_info("")			
			self.dbg_info("cp:    " + src )
			self.dbg_info("to:    " + dest )
			
			if self.m_test_mode == "0":
				self.dbg_info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" )
				self.dbg_info("real_copy_mode" )
				shutil.copyfile(src, dest)
				self.dbg_info("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<" )
			else:
				self.dbg_info("test_mode" )
			
		except OSError as e:
			print('file not copied. Error: %s' % e)

			
	def sync_full_libs_work( self ):
		self.m_move_gen = "0"
		self.m_move_sctest = "1"
		self.m_move_common = "1"
		self.m_move_lib = "1"
		self.copy_all_to_full_from_short_in_work()

		
	def sync_short_gens_work( self ):
		self.m_move_gen = "1"
		self.m_move_sctest = "1"
		self.m_move_lib = "0"
		self.m_move_common = "0"
		self.copy_all_to_short_from_full_in_work()

	def sync_full_libs_home( self ):
		self.m_move_gen = "0"
		self.m_move_sctest = "1"
		self.m_move_common = "1"
		self.m_move_lib = "1"
		self.copy_all_to_full_from_short_in_home()
		
	def sync_short_gens_home( self ):
		self.m_move_gen = "1"
		self.m_move_sctest = "1"
		self.m_move_lib = "0"
		self.m_move_common = "0"
		self.copy_all_to_short_from_full_in_home()
		
	def copy_to_home(self,p_sel):
		
		self.m_selector = "2017_03_14__1800"		
		self.m_selector = p_sel
		dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\full\\app"
		dir_dest = "C:\\lkd\\wmt\\frontend\\app"
		self.recursive_overwrite(dir_s,dir_dest,None);
		
		dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\short\\app"
		dir_dest = "C:\\lkd\\wmt\\frontendshort\\app"
		self.recursive_overwrite(dir_s,dir_dest,None);

		dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\php\\src"
		dir_dest = "C:\\lkd\\wmt\\backend\\src"
		self.recursive_overwrite(dir_s,dir_dest,None);
		
		dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\gen\\BS_40_PRJ_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\EmberPhp"		
		dir_dest = "C:\\lkd\\ht\\apps_tools\\BS_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\EmberPhp"
		self.recursive_overwrite(dir_s,dir_dest,None);
		
		dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\gen\\BS_40_PRJ_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\gendata"		
		dir_dest = "C:\\lkd\\ht\\apps_tools\\BS_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\gendata"
		self.recursive_overwrite(dir_s,dir_dest,None);
		
		dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\gen\\BS_40_PRJ_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.GUIStarter\\bin\\UserProjects\\RQS";
		dir_dest = "C:\\lkd\\ht\\apps_tools\\BS_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.GUIStarter\\bin\\UserProjects\\RQS"
		self.recursive_overwrite(dir_s,dir_dest,None);
		
	def copy_to_work(self,	p_sel):		
		self.m_selector = p_sel
		if(self.m_move_app_full == "1"):
			dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\full\\app"
			dir_dest = "C:\\lkd\\wmtgit\\v06\\scate-admin-dashboard\\app"
			self.recursive_overwrite(dir_s,dir_dest,None);
			
		if(self.m_move_app_short == "1"):
			dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\short\\app"
			dir_dest = "C:\\lkd\\wmtgit\\v06\\scate-dashboard\\app"
			self.recursive_overwrite_start(dir_s,dir_dest,None);
			self.recursive_overwrite(dir_s,dir_dest,None);
			
		if(self.m_move_src == "1"):
			dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\php\\src"
			dir_dest = "C:\\lkd\\wmtgit\\v06\\scate-backend\\src"
			self.recursive_overwrite_start(dir_s,dir_dest,None);
			self.recursive_overwrite(dir_s,dir_dest,None);
			
		if(self.m_move_bs_2015 == "1"):
			dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\gen\\BS_40_PRJ_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\EmberPhp"		
			dir_dest = "C:\\lkd\\ht\\apps_tools\\BS_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\EmberPhp"
			self.recursive_overwrite_start(dir_s,dir_dest,None);
			self.recursive_overwrite(dir_s,dir_dest,None);
			
		if(self.m_move_bs_2015 == "1"):
			dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\gen\\BS_40_PRJ_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\gendata"		
			dir_dest = "C:\\lkd\\ht\\apps_tools\\BS_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\gendata"
			self.recursive_overwrite_start(dir_s,dir_dest,None);
			self.recursive_overwrite(dir_s,dir_dest,None);
			
		if(self.m_move_bs_2015 == "1"):		
			dir_s = "C:\\lkd_gen-1\\" + self.m_selector + "\\gen\\BS_40_PRJ_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.GUIStarter\\bin\\UserProjects\\RQS";
			dir_dest = "C:\\lkd\\ht\\apps_tools\\BS_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.GUIStarter\\bin\\UserProjects\\RQS"
			self.recursive_overwrite_start(dir_s,dir_dest,None);
			self.recursive_overwrite(dir_s,dir_dest,None);
		
	def copy_to_flash(self, p_sel,p_disc):
		
		self.m_selector = p_sel
		if(self.m_move_app_short == "1"):
			dir_s = "C:\\lkd\\wmtgit\\v06\\scate-dashboard\\app"
			dir_dest = p_disc + ":\\lkd_gen-1\\" + self.m_selector + "\\short\\app"		
			self.recursive_overwrite(dir_s,dir_dest,None);
		
		if(self.m_move_app_full == "1"):
			dir_s = "C:\\lkd\\wmtgit\\v06\\scate-admin-dashboard\\app"
			dir_dest = p_disc + ":\\lkd_gen-1\\" + self.m_selector + "\\full\\app"		
			self.recursive_overwrite(dir_s,dir_dest,None);
			
		if(self.m_move_src == "1"):
			dir_s = "C:\\lkd\\wmtgit\\v06\\scate-backend\\src"
			dir_dest = p_disc + ":\\lkd_gen-1\\" + self.m_selector + "\\php\\src"
			self.recursive_overwrite(dir_s,dir_dest,None);
			
		if(self.m_move_vpg == "1"):
			dir_s = "C:\\lkd\\wmtgit\\v06\\w2\\gitp\\vpg"
			dir_dest = p_disc + ":\\lkd_gen-1\\" + self.m_selector + "\\vpg"
			self.recursive_overwrite(dir_s,dir_dest,None);
		
		if(self.m_move_bs_2015 == "1"):
			dir_s = "C:\\lkd\\ht\\apps_tools\\BS_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\EmberPhp"
			dir_dest = p_disc + ":\\lkd_gen-1\\" + self.m_selector + "\\gen\\BS_40_PRJ_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\EmberPhp"				
			self.recursive_overwrite(dir_s,dir_dest,None);
		
		if(self.m_move_bs_2015 == "1"):								
			dir_s = "C:\\lkd\\ht\\apps_tools\\BS_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\gendata"
			dir_dest = p_disc + ":\\lkd_gen-1\\" + self.m_selector + "\\gen\\BS_40_PRJ_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.EngineF35\\Generator\\gendata"		
			self.recursive_overwrite(dir_s,dir_dest,None);
		if(self.m_move_bs_2015 == "1"):						
			dir_s = "C:\\lkd\\ht\\apps_tools\\BS_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.GUIStarter\\bin\\UserProjects\\RQS"
			dir_dest = p_disc + ":\\lkd_gen-1\\" + self.m_selector + "\\gen\\BS_40_PRJ_2015\\BS_40_PRJ_2015\\BSGen\\BearcatSoft.BSGen.GUIStarter\\bin\\UserProjects\\RQS";
			self.recursive_overwrite(dir_s,dir_dest,None);
	
		
if __name__ == '__main__':

	#data = intl_copy_dirs().cpy_create_full_from_short()	
	#data = intl_copy_dirs().cpy_create_short_from_full()	
	#intl_copy_dirs().cpy_create_short_from_full_test()
	#ddh.copy_all_to_full_work();
	#ddh.copy_all_to_short_from_full_in_work()
	#ddh.copy_all_to_short_from_full_in_home()
	#ddh.copy_all_to_full_from_short_in_work()
	
	ddh = intl_copy_dirs()
	ddh.m_test_mode = "0"
	ddh.m_move_app_short ="1"
	ddh.m_move_app_full = "1"
	ddh.m_move_src = "1"
	ddh.m_move_bs_2015 = "0"
	ddh.m_move_vpg = "0"
	#ddh.copy_to_work("2017_03_17__1700")
	
	ddh.sync_full_libs_work()	
	
	#ddh.copy_to_flash("2017_03_17__1700","E")
	#ddh.sync_short_gens_work()	

	#ddh.sync_full_libs_home()
	#ddh.sync_short_gens_home()	
	#ddh.copy_to_home()		
	#
	#
	#	work
	#
	
	#
	#home
	#frontend 4900
	#short 4600
	#cd C:\lkd\wmt\frontend
	#cd C:\lkd\wmtgit\v06\scate-dashboard
	#ember server --port 5000
	#python C:\lkd\wmtgit\v06\w2\gitp\vpg\git\intl.py
	
	#cd C:\lkd\wmtgit\v06\scate-admin-dashboard
	#ember server --port 7000
	
	
	
	