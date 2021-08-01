import sys
import os
import logging
import shutil

from LKD_CreateCountryTranslationProd import *
from LKD_CreateCountryTranslationS1 import *
from LKD_CreateCountryPkS1 import *
from LKD_CreateCountryPkProd import *
from LKD_CreateCountryLib import *

#  C:/lkd/servers/installed/python27/python C:/lkd/ht/apps_w2_risk/app/src/apps_w2_w2/src/lkdpy/start_cpy.py
# C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles/content_cats/content_markdown/content_by_groups/cat__8000/cat__000/cat__00/cat__8000/content_idx_0/content__cats_2_add.md
# C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\createswipper\lkdcore\LKD_CreateCats.py

# select "cats.append(self.get_item(",id,",","\"",trim(title),"\"","))" from joo2_categories where parent_id = 11770


class LKD_CreateCountryExec:

        def __init__(self,spar):                                
			self.xx_dbg("LKD_CreateCountryExec::__init__::in::")
			#self.m_src = "C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles/content_cats/content_markdown/content_by_groups/cat__8000/cat__000/cat__00/cat__8000/content_idx_0/cats/content__cats_2_add.md"
			self.m_src = "C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles_data/cats/content__cats_2_add.md"
			self.xx_dbg("LKD_CreateCountryExec::__init__::out::")

        def class_name(self):
			return "LKD_CreateCountryExec::"

        def xx_dbg(self, tt ):
			s_fun = self.class_name() + "::set_execute_main_toc::"
			dbg = 0
			if dbg == 1:		
				print tt

        def xx_dbg_1(self, tt ):
			s_fun = self.class_name() + "::set_execute_main_toc::"
			# print tt

        def xx_dbg_line(self, tt ):
			s_fun = self.class_name() + "::set_execute_main_toc::"
			dbg = 0
			if dbg == 1:		
				print tt

        def xx_dbg_translation_items(self, tt ,dd_array):
			s_fun = self.class_name() + "::xx_dbg_translation_item::"
			self.xx_dbg(s_fun + "start")
			LKD_TranslationArr("").xx_dbg_translation_items("", dd_array)
			
        def execute_main(self,  tt ):
			s_fun = self.class_name() + "::execute_main::"
			self.xx_dbg(s_fun + "start")
			#self.execute_main_test(tt)
			self.execute_main_full(tt)

        def execute_main_test(self,  tt ):
			s_fun = self.class_name() + "::execute_main::"
			self.xx_dbg(s_fun + "start")

			producer_t_prod = LKD_CreateCountryTranslationProd("")
			arr_t_prod = []
			test_mode = 0
			producer_t_prod.get_items("arr_t_prod", arr_t_prod, test_mode)
			self.xx_dbg_translation_items("arr_t_prod", arr_t_prod)

        def execute_main_full(self,  tt ):
			s_fun = self.class_name() + "::execute_main::"
			self.xx_dbg(s_fun + "start")
			test_mode = 0
			producer_t_prod = LKD_CreateCountryTranslationProd("")
			arr_t_prod = []
			producer_t_prod.get_items("arr_t_prod", arr_t_prod, test_mode)
			self.xx_dbg_translation_items("arr_t_prod", arr_t_prod)


			producer_t_s1 = LKD_CreateCountryTranslationS1("")
			arr_t_s1 = []
			producer_t_s1.get_items("arr_t_s1", arr_t_s1, test_mode)
			self.xx_dbg_translation_items("arr_t_s1", arr_t_s1)

			producer_pk_s1 = LKD_CreateCountryPkS1("")
			arr_pk_s1 = []
			producer_pk_s1.get_items("arr_pk_s1", arr_pk_s1, test_mode)
			self.xx_dbg_translation_items("arr_pk_s1", arr_pk_s1)

			producer_pk_prod = LKD_CreateCountryPkProd("")
			arr_pk_prod = []
			producer_pk_prod.get_items("arr_pk_prod", arr_pk_prod, test_mode)
			self.xx_dbg_translation_items("arr_pk_prod", arr_pk_prod)

			worker_handler = LKD_TranslationArr("")

			test_0 = 0
			if(test_0 == 1):
				worker_handler.get_items_pk_prod_by_pk_s1(
					arr_pk_s1, 
					arr_pk_prod)

			test_update = 1
			if(test_update == 1):
				worker_handler.get_update_prod_items(
					arr_pk_s1
					, arr_pk_prod
					, arr_t_s1
					, arr_t_prod)

			test_diffs = 0
			if(test_diffs == 1):
				worker_handler.get_update_prod_items_diffs(
					arr_pk_s1
					, arr_pk_prod
					, arr_t_s1
					, arr_t_prod)

			test_2 = 0
			if(test_2 == 1):
				worker_handler.get_dbg_new_items(
					arr_pk_s1
					, arr_t_prod
					, "arr_t_prod")

			test_3 = 0
			if(test_3 == 1):
				worker_handler.get_dbg_items(					
					 arr_t_prod
					, "arr_t_prod_items")


			self.xx_dbg(s_fun + "end")

if __name__ == "__main__":

        ddh = LKD_CreateCats("")
        ddh.execute_main("")
