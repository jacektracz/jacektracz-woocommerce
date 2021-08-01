import sys
import os
import logging
import shutil


#  C:/lkd/servers/installed/python27/python C:/lkd/ht/apps_w2_risk/app/src/apps_w2_w2/src/lkdpy/start_cpy.py
# C:/lkd/ht/apps_portal/lkduni/app-4/src/modules/mod_ep_articles/content_cats/content_markdown/content_by_groups/cat__8000/cat__000/cat__00/cat__8000/content_idx_0/content__cats_2_add.md
# C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\createswipper\lkdcore\LKD_CreateCats.py
# cd C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\createswipper\lkdcore\country_db\output-script
# select "cats.append(self.get_item(",id,",","\"",trim(title),"\"","))" from joo2_categories where parent_id = 11770

class LKD_TranslationItem:
	def class_name(self):
		return "LKD_TranslationItem::"

	def xx_dbg_lv1(
		self, tt ):
		s_fun = self.class_name() + "::xx_dbg_lv1::"
		dbg = 0
		if dbg == 1:		
			print tt

	def __init__(
		self,spar):   
		s_fun = self.class_name() + "::create_item::"
		self.xx_dbg_lv1(s_fun + "start")
		self.locale =  "sk"
		self.name=  ""
		self.description=  ""
		self.description_short=  ""
		self.info_box_price=  ""
		self.name_synonyms=  "{}"
		self.badge_label=  ""
		self.info_box_procedures=  ""
		self.info_box_tips=  ""
		self.pk =  0
		self.id =  0
		self.pk_prod =  0
		self.pk_s1 =  0

	def create_item(
		self,
		locale , val_locale,
		name , val_name,
		description , val_description,
		description_short , val_description_short,
		info_box_price ,val_info_box_price ,
		name_synonyms , val_name_synonyms,
		badge_label , val_badge_label,
		info_box_procedures , val_info_box_procedures,
		info_box_tips , val_info_box_tips,
		pk , val_pk):
		s_fun = self.class_name() + "::create_item::"
		self.xx_dbg_lv1(s_fun + "start")

		self.locale=  val_locale
		self.name=  val_name
		self.description=  val_description
		self.description_short=  val_description_short
		self.info_box_price=  val_info_box_price
		self.name_synonyms=  val_name_synonyms
		self.badge_label=  val_badge_label
		self.info_box_procedures=  val_info_box_procedures
		self.info_box_tips= val_info_box_tips
		self.pk=  val_pk


class LKD_TranslationArr:

	def __init__(
		self,spar):
		s_fun = self.class_name() + "::put_item::"
		self.xx_dbg_lv1(s_fun + "start")
		self.items = []
		self.xx_dbg_lv1(s_fun + "end")

	def class_name(self):
		return "LKD_TranslationArr::"

	def xx_dbg_lv1(self, tt ):
		s_fun = self.class_name() + "::xx_dbg_lv1::"
		dbg = 0
		tt = self.get_str_no_lf(tt)
		if dbg == 1:		
			tt = self.get_str_no_lf(tt)
			print tt

	def xx_dbg_items(self, tt ):
		""" """
		dbg = 0
		if dbg == 1:		
			tt = self.get_str_no_lf(tt)
			print tt

	def xx_dbg_lv2 (self, tt ):
		dbg = 0
		if dbg == 1:		
			tt = self.get_str_no_lf(tt)
			print tt

	def xx_dbg_sql (self, tt ):
		dbg = 0
		if dbg == 1:		
			tt = self.get_str_no_lf(tt)			
			print tt

	def xx_dbg_sql_diff (self, tt ):
		dbg = 0
		if dbg == 1:		
			tt = self.get_str_no_lf(tt)			
			print tt

	def xx_dbg_sql_update (self, tt ):
		dbg = 1
		if dbg == 1:					
			print tt

	def aa(self):
		s_fun = self.class_name() + "::put_item::"
		self.xx_dbg_lv1(s_fun + "start")

	def put_item(
		self, out_arr, locale , val_locale,
		name , val_name,
		description , val_description,
		description_short , val_description_short,
		info_box_price ,val_info_box_price ,
		name_synonyms , val_name_synonyms,
		badge_label , val_badge_label,
		info_box_procedures , val_info_box_procedures,
		info_box_tips , val_info_box_tips,
		pk , val_pk):

		s_fun = self.class_name() + "::put_item::"
		self.xx_dbg_lv1(s_fun + "start")

		dd = LKD_TranslationItem("")

		dd.create_item(
			locale , val_locale,
			name , val_name,
			description , val_description,
			description_short , val_description_short,
			info_box_price ,val_info_box_price ,
			name_synonyms , val_name_synonyms,
			badge_label , val_badge_label,
			info_box_procedures , val_info_box_procedures,
			info_box_tips , val_info_box_tips,
			pk , val_pk)

		out_arr.append(dd)

	def put_item_pk(
		self, out_arr, pk , val_pk,
		id , val_id,):

		s_fun = self.class_name() + "::put_item::"
		self.xx_dbg_lv1(s_fun + "start")

		dd = LKD_TranslationItem("")
		dd.pk = val_pk
		dd.id = val_id
		out_arr.append(dd)


	def get_items_pk_prod_by_pk_s1(self, pk_arr_s1, pk_arr_prod):
		for item_s1 in pk_arr_s1:
			self.get_pk_prod_by_pk_s1(
				item_s1.pk
				, item_s1.id
				, item_s1
				, pk_arr_prod)

	def xx_dbg_translation_item(self, tt ,dd):
		s_fun = self.class_name() + "::xx_dbg_translation_item::"
		self.xx_dbg_lv1(s_fun + "pk:" + str(dd.pk))
		self.xx_dbg_lv1(s_fun + "id:" + str(dd.id))
		self.xx_dbg_lv1(s_fun + "name:" + self.get_str_no_lf(str(dd.name)))

	def xx_dbg_translation_items(self, tt ,dd_array):
		s_fun = self.class_name() + "::xx_dbg_translation_item::"
		self.xx_dbg_lv1(s_fun + "start")
		ii = 0
		for item in dd_array:
			self.xx_dbg_translation_item(ii, item)
			ii = ii + 1
		self.xx_dbg_lv1(s_fun + "name:" + self.get_str_no_lf(item.name))

	def get_pk_prod_by_pk_s1(
		self
		, pk_s1
		, id_s1
		, item_s1
		, pk_arr_prod):
		s_fun = self.class_name() + "::get_pk_prod_by_pk_s1::"
		self.xx_dbg_lv1(s_fun + "start")

		out_pk_prod = 0
		out_found_item = None
		for item in pk_arr_prod:
			#if( item.id == id_s1 and item.pk == pk_s1):
			if( item.pk == pk_s1 ):
				out_pk_prod = item.pk
				out_found_item = item
				break

		if out_pk_prod == 0:
			self.xx_dbg_lv1(s_fun + "DIFFERENCE-FOR-ID" 
				+ "[id_s1:" + str(id_s1) + "]" 
				+ "[pk_s1:" + str(pk_s1) + "]" 
				+ "[out_pk_prod:" + str(out_pk_prod) + "]")

		return out_pk_prod

	def get_item_by_pk(self, item_pk, pk_arr):
		s_fun = self.class_name() + "::get_item_by_pk::"
		self.xx_dbg_items(s_fun + "start")
		
		out_item = None
		for item in pk_arr:
			if( item.pk == item_pk ):
				out_item = item

				self.xx_dbg_items(s_fun + "FOUND-IN-ARRAY-YES[" + str(item_pk) + "][" + out_item.name + "]")
				break

		if out_item == None:
			self.xx_dbg_items(s_fun + "FOUND-IN-ARRAY-NO[" + str(item_pk) + "]")

		return out_item


	def get_update_prod_items(
		self
		,  pk_arr_s1
		,  pk_arr_prod
		,  arr_t_s1
		,  arr_t_prod):

		s_fun = self.class_name() + "::get_update_prod_items::"
		self.xx_dbg_lv1(s_fun + "start")

		self.get_dbg_items(pk_arr_s1,"DBG-PK-S1-IN-UPDATE")
		self.get_dbg_items(pk_arr_prod,"DBG-PK-PROD-IN-UPDATE")

		self.get_dbg_items(arr_t_prod,"DBG-T-S1-IN-UPDATE")
		self.get_dbg_items(arr_t_prod,"DBG-T-PROD-IN-UPDATE")
		

		for item_s1 in arr_t_s1:
			self.get_update_prod_item(
				item_s1
				, pk_arr_prod
				, arr_t_prod
				, 0)


		self.xx_dbg_lv1(s_fun + "end")

	def get_update_prod_items_diffs(
		self
		,  pk_arr_s1
		,  pk_arr_prod
		,  arr_t_s1
		,  arr_t_prod):

		s_fun = self.class_name() + "::get_update_prod_items_diffs::"
		self.xx_dbg_lv1(s_fun + "start")

		self.get_dbg_items(pk_arr_s1,"DBG-PK-S1-IN-UPDATE")
		self.get_dbg_items(pk_arr_prod,"DBG-PK-PROD-IN-UPDATE")

		self.get_dbg_items(arr_t_prod,"DBG-T-S1-IN-UPDATE")
		self.get_dbg_items(arr_t_prod,"DBG-T-PROD-IN-UPDATE")
		

		for item_s1 in arr_t_s1:
			self.get_update_prod_item(
				item_s1
				, pk_arr_prod
				, arr_t_prod
				, 0)


		self.xx_dbg_lv1(s_fun + "end")

	def get_update_prod_item(
		self
		, item_s1
		, pk_arr_prod
		, arr_t_prod
		, only_diffs):

		s_fun = self.class_name() + "::get_update_prod_item::"
		self.xx_dbg_lv1(s_fun + "start")

		dbg_mode = 0

		if dbg_mode == 1:
			self.get_dbg_items(arr_t_prod,"DBG-T-PROD-IN-UPDATE-ITEM")
		

		pk_prod = self.get_pk_prod_by_pk_s1(
				item_s1.pk
				, item_s1.id
				, item_s1
				, pk_arr_prod)


		if(pk_prod  == 0):
			
			self.get_dbg_item(
				item_s1
				, pk_prod
				,"NO-ITEM-RET")

			return

		if dbg_mode == 1:
			self.get_dbg_items(
				arr_t_prod,
				"DBG-T-PROD-IN-UPDATE-ITEM-2"
				+ "[" + str(pk_prod) + "]")

		out_found_item =  self.get_item_by_pk(
			pk_prod
			, arr_t_prod)

		if out_found_item == None :
			dbg_item = LKD_TranslationItem("")
			self.get_dbg_sql_item(
				dbg_item
				, pk_prod
				, "NO-ITEM-FOUND-FOR-PROD")
			return

		check_name = 0
		if(check_name == 1):
			if(item_s1.name != out_found_item.name):

				self.xx_dbg_sql_diff("")
				self.xx_dbg_sql_diff(">>>>>>>>>>>>")
				self.get_dbg_sql_item_diff(
					item_s1
					, pk_prod
					, "DIFF_NAME-ITEM-S1")

				self.get_dbg_sql_item_diff(
					out_found_item
					, pk_prod
					, "DIFF-NAME-ITEM-PROD-PROD")

				self.xx_dbg_sql_diff("<<<<<<<<<")
				self.xx_dbg_sql_diff("")

				return

		if(only_diffs == 1):
			return

		toc = 0

		if(item_s1.name!= ""):
			toc = 1
		if(item_s1.description!= ""):
			toc = 1
		if(item_s1.description_short!= ""):
			toc = 1
		if(item_s1.info_box_price!= ""):
			toc = 1
		if(item_s1.name_synonyms!= ""):
			toc = 1
		if(item_s1.badge_label!= ""):
			toc = 1
		if(item_s1.info_box_procedures!= ""):
			toc = 1
		if(item_s1.info_box_tips!= ""):
			toc = 1

		if toc == 0 :
			self.get_dbg_sql_update_item(
				item_s1
				, pk_prod
				,"NO-CHANGES")

		item_prod = self.get_item_by_pk(
			pk_prod
			, arr_t_prod)

		NL = "\r\n"
		ss  = ""
		ss = ss + NL + "update service_translation set"
		#ss = ss + NL + " set locale = " + self.get_str(item_s1.locale)
		to_update = 0
		to_update_box = 0

		if(item_s1.name != item_prod.name):
			ss = ss + NL + "  name = " + self.get_str(item_s1.name)
			to_update = 1
		
		if(item_s1.description != item_prod.description):
			ss = ss + NL + self.SL(to_update) + "  description = " + self.get_str(item_s1.description)
			to_update = 1

		if(item_s1.description_short != item_prod.description_short):
			ss = ss + NL + self.SL(to_update) + "  description_short = " + self.get_str(item_s1.description_short)
			to_update = 1

		if(item_s1.info_box_price != item_prod.info_box_price):
			ss = ss + NL + self.SL(to_update)+ "  info_box_price = " + self.get_str(item_s1.info_box_price)
			to_update = 1

		if(item_s1.name_synonyms != item_prod.name_synonyms):
			ss = ss + NL + self.SL(to_update)+ "  name_synonyms = " + self.get_str_array(item_s1.name_synonyms)
			to_update = 1

		if(item_s1.badge_label != item_prod.badge_label):
			ss = ss + NL + self.SL(to_update)+ "  badge_label = " + self.get_str(item_s1.badge_label)
			to_update = 1

		if(item_s1.info_box_procedures != item_prod.info_box_procedures):
			ss = ss + NL + self.SL(to_update)+ "  info_box_procedures = " + self.get_str(item_s1.info_box_procedures)
			to_update = 1
			to_update_box = 1

		if(item_s1.info_box_tips != item_prod.info_box_tips):
			ss = ss + NL + self.SL(to_update) + "  info_box_tips = " + self.get_str(item_s1.info_box_tips)
			to_update = 1
			to_update_box = 1
		#ss = ss + NL + " where id  = " + str(item_s1.id)
		ss = ss + NL + " where pk = " + str(pk_prod) + ""
		#ss = ss + NL + " and name = " + self.get_str(item_s1.name) + ";"
		ss = ss + NL + " and locale = " + self.get_str(item_s1.locale) + ";"
		
		to_update_no_box = 1
		if(to_update_no_box == 1 and to_update == 1 and to_update_box == 0):
			self.xx_dbg_sql_update(" ")
			self.xx_dbg_sql_update(" ")
			self.get_dbg_sql_update_item(
				item_prod
				, pk_prod
				,"GENERATE-UPDATE-PROD-ITEM")

			self.get_dbg_sql_update_item(
				item_s1
				, pk_prod
				,"GENERATE-UPDATE-NEW-ITEM")

			self.xx_dbg_sql_update(ss)

		to_update_box_var = 0
		if(to_update_box_var == 1 and to_update_box == 1):
			self.xx_dbg_sql_update(" ")
			self.xx_dbg_sql_update(" ")
			self.get_dbg_sql_update_item(
				item_prod
				, pk_prod
				,"GENERATE-UPDATE-PROD-ITEM")

			self.get_dbg_sql_update_item(
				item_s1
				, pk_prod
				,"GENERATE-UPDATE-NEW-ITEM")

			self.xx_dbg_sql_update(ss)


		return 

	def SL(self, to_update):
		if(to_update == 1):
			return ", "
		return " "

	def get_dbg_sql_item_diff(
		self
		, item_s1
		, pk_prod_new
		, dbg_add):

		ss = ""
		ss = ss+ "-- "
		ss = ss + "ID[id_s1:" + str(item_s1.id) + "]"		
		ss = ss + "[pk_s1:" + str(item_s1.pk) + "]"
		ss = ss + "[name_s1:" + self.get_str_no_lf(str(item_s1.name)) + "]" 
		ss = ss + "[pk_prod_new:" + str(pk_prod_new) + "]"
		ss = ss + "[dbg_add:" + str(dbg_add) + "]"
		self.xx_dbg_sql_diff(ss)



	def get_dbg_sql_item(
		self
		, item_s1
		, pk_prod_new
		, dbg_add):

		ss = ""
		ss = ss+ "-- "
		ss = ss + "ID[id_s1:" + str(item_s1.id) + "]"		
		ss = ss + "[pk_s1:" + str(item_s1.pk) + "]"
		ss = ss + "[name_s1:" + self.get_str_no_lf(str(item_s1.name)) + "]" 
		ss = ss + "[pk_prod_new:" + str(pk_prod_new) + "]"
		ss = ss + "[dbg_add:" + str(dbg_add) + "]"
		self.xx_dbg_sql(ss)

	def get_dbg_sql_update_item(
		self
		, item_s1
		, pk_prod_new
		, dbg_add):

		ss = ""
		ss = ss+ "-- "
		ss = ss + "ID[id_s1:" + str(item_s1.id) + "]"		
		ss = ss + "[pk_s1:" + str(item_s1.pk) + "]"
		ss = ss + "[name_s1:" + self.get_str_no_lf(str(item_s1.name)) + "]" 
		ss = ss + "[pk_prod_new:" + str(pk_prod_new) + "]"
		ss = ss + "[dbg_add:" + str(dbg_add) + "]"
		self.xx_dbg_sql_update(ss)


	def get_dbg_item(
		self
		, item_s1
		, pk_prod_new
		, dbg_add):

		ss = ""
		ss = ss+ "-- "
		ss = ss + "ID[id_s1:" + str(item_s1.id) + "]"		
		ss = ss + "[pk_s1:" + str(item_s1.pk) + "]"
		ss = ss + "[name_s1:" + self.get_str_no_lf(str(item_s1.name)) + "]" 
		ss = ss + "[pk_prod_new:" + str(pk_prod_new) + "]"
		ss = ss + "[dbg_add:" + str(dbg_add) + "]"
		self.xx_dbg_lv2(ss)

	def get_dbg_new_items(self, pk_arr_s1, pk_arr_prod, dbg_item):
		s_fun = self.class_name() + "::get_dbg_new_items::"
		self.xx_dbg_lv1(s_fun + "start")

		for item_s1 in pk_arr_s1:
			item_new_on_s1 = self.get_item_by_pk(
				item_s1.pk
				, pk_arr_prod)

			if (item_new_on_s1 == None):
				self.get_dbg_item( 
					item_s1
					, 0
					, "DBG-TABLE" + dbg_item)


		self.xx_dbg_lv1(s_fun + "end")

	def get_dbg_items(self, arr_t, dbg_item):
		s_fun = self.class_name() + "::get_dbg_items::"
		self.xx_dbg_lv1(s_fun + "start")

		for item in arr_t:		
			self.get_dbg_item( 
				item
				, 0
				, "DBG-TABLE-" + dbg_item)

		self.xx_dbg_lv1(s_fun + "end")

	def get_str(self, tt_val):
		return self.get_str_no_lf(tt_val)
		#return "'" + tt_val + "'"

	def get_str_array(self, tt_val):
		return "'{" + tt_val + "}'"

	def get_str_no_lf(self, tt_val):
		#print tt_val
		#tt_val = tt_val.rstrip('\n')
		tt_val = tt_val.replace("\n", "")
		#print tt_val
		return "'" + tt_val + "'"
