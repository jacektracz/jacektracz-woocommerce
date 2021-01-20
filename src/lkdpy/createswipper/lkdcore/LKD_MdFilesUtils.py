import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *

from LKD_CreateFilesDatabase import *
from LKD_CatItem import *
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py


class LKD_MdFilesUtils:

	def __init__(self,spar):                                
			self.xx_dbg("LKD_CreateImages::__init__::in::")
			self.m_ds = "/"
			self.xx_dbg("LKD_CreateImages::__init__::out::")

	def get_sclass(self):
			return "LKD_MdFilesUtils"
			
	def get_root_for_groups( self, dd_active_cat_id ,dd_file_idx)	:

		sfun = self.get_sclass() + "::get_file_content_by_cat_id_groups::"
		self.xx_dbg( sfun + "start")
		self.xx_dbg( sfun + "active_cat_id" + str(dd_active_cat_id ))

		dd_rest = dd_active_cat_id

		dd_mod_1000 = self.get_int(dd_active_cat_id , 1000)

		dd_rest = dd_rest - ( dd_mod_1000 * 1000)
		self.xx_dbg( sfun + "__resolve_groups__mod_1000__[" + str(dd_mod_1000 )+ "]")
		self.xx_dbg( sfun + "__resolve_groups__mod_1000_rest__[" + str(dd_rest) + "]")

		dd_mod_100 = self.get_int(dd_rest , 100)
		dd_rest = dd_rest - ( dd_mod_100 * 100)

		self.xx_dbg( sfun + "__resolve_groups__mod_100__[" + str(dd_mod_100) + "]")
		self.xx_dbg( sfun + "__resolve_groups__mod_100_rest__[" + str(dd_rest) + "]")

		dd_mod_10 = self.get_int(dd_rest , 10)
		dd_rest = dd_rest - ( dd_mod_10 * 10)

		self.xx_dbg( sfun + "__resolve_groups__mod_10__[" + str(dd_mod_10 )+ "]")
		self.xx_dbg( sfun + "__resolve_groups__mod_10_rest__[" + str(dd_rest) + "]")

		dd_mod_1 = dd_rest

		self.xx_dbg( sfun + "__resolve_groups__mod_1__[" + str(dd_mod_1) + "]")
		
		dd_DS1 =  "/"
		dd_file = ""
		dd_file =  dd_file + "C:"
		dd_file =  dd_file +  dd_DS1 + "lkd"
		dd_file =  dd_file +  dd_DS1 + "ht"
		dd_file =  dd_file +  dd_DS1 + "apps_portal"
		dd_file =  dd_file +  dd_DS1 + "lkduni"
		dd_file =  dd_file +  dd_DS1 +  "app-4" 
		dd_file =  dd_file +  dd_DS1 + "src"
		dd_file =  dd_file  + dd_DS1 + "modules"
		dd_file =  dd_file  + dd_DS1 + "mod_ep_articles"
		dd_file =  dd_file  + dd_DS1 + "content_cats"
		dd_file =  dd_file  + dd_DS1 + "content_markdown"
		dd_file =  dd_file  + dd_DS1 + "content_by_groups"
		dd_file =  dd_file  + dd_DS1 + "cat__" + str(dd_mod_1000) + "000"
		dd_file =  dd_file  + dd_DS1 + "cat__" + str(dd_mod_100) + "00"
		dd_file =  dd_file  + dd_DS1 + "cat__" + str(dd_mod_10) + "0"
		dd_file =  dd_file  + dd_DS1 + "cat__" + str(dd_active_cat_id) + ""
		#dd_file =  dd_file  + dd_DS1 + "content_idx_" + str(dd_file_idx) + "" 
		#dd_file =  dd_file  + dd_DS1 + "content__" + str(dd_file_idx) + ".md"

		self.xx_dbg( sfun + "check_file_parsedown_md_x8::" + dd_file)
		self.xx_dbg( sfun + "end")
		return dd_file
				
	def get_int( self, dd_start_idx, dd_step ):

		sfun = self.get_sclass() + "::get_step::"
		self.xx_dbg( sfun + "start")		

		dd_iout = int(round(dd_start_idx / dd_step))

		self.xx_dbg( sfun + "end")
		return dd_iout


	def xx_dbg(self, tt):
			"" ""
			print ( tt )

	def xx_print( self, tt ):
			"" ""
			print ( tt )       
