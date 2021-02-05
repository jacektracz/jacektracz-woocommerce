import sys
import os
import logging
import shutil
from LKD_CopyFilesList import *
from LKD_CreateSwipperExec import *
from LKD_CopyFilesMd import *
class LKD_CreateSwippersMain:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CreateSwippersMain::__init__::in::")
                self.xx_dbg("LKD_CreateSwippersMain::__init__::out::")
               
        def xx_dbg(self, tt):
                "" ""
                print (tt)
                      
                

        def exec_cpy_one(self):
                self.xx_dbg("LKD_CreateSwippersMain::exec_cpy_one::start::")
                dd_handler = LKD_CreateSwipperExec("")
                dd_list = LKD_CopyFilesList("")
                ll = dd_list.get_list()
                for item_name in ll:
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::start::__" + item_name + "__")
                        #dd_handler.cpy_one_entity_child("prod_delivery_pd2",item_name)


                
        def exec_populate_mds(self):
                self.xx_dbg("LKD_CreateSwippersMain::exec_cpy_one::start::")
                dd_handler = LKD_CopyFilesMd("")
                dd_list = LKD_CopyFilesList("")
                ll = dd_list.get_list()
                for item_name in ll:
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::start::__" + item_name + "__")
                        dd_handler.populate_one_md("3958","3958",item_name)

        def exec_cpy_mds(self):

	        dd_md = LKD_CopyFilesMd("")                
                dd_md.exec_cpy_mds()

        def exec_cpy_contents_mds(self):
                dd_md = LKD_CopyFilesMd("")                
                dd_md.exec_cpy_contents_mds()

        def cpy_one_swipper_all_files(self):

                dd = LKD_CreateSwipperExec("")      

                #dd.cpy_one_swipper_all_files("tree_v8","treecnt_tc8")
                #dd.cpy_one_swipper_all_files("treeart_ta8","treeon_to8")
                #dd.cpy_one_swipper_all_files("services_u7","catsall_ca9")
                #dd.cpy_one_swipper_all_files("treeon_to8","treegrid_tg8")
                #dd.cpy_one_swipper_all_files("treeon_to8","treetopic_tt8")
                #dd.cpy_one_swipper_all_files("treetopic_tt9","treechilds_tc9")
                #dd.cpy_one_swipper_all_files("treetopic_tt9","treeparent_tp9")                
                #dd.cpy_one_swipper_all_files("treegreatg_tt9","treefoot1_tf1")
                #dd.cpy_one_swipper_all_files("treegreatg_tt9","treefoot2_tf1")
                #dd.cpy_one_swipper_all_files("treegreatg_tt9","treegreatg1_tg2")
                #dd.cpy_one_swipper_all_files("treegreatg_tt9","treegreatg2_tg3")

                # dd.cpy_one_swipper_all_files("treegreatg_tt9","treegreatg3_tg4")

                #dd.cpy_one_swipper_all_files("authorsfoot_h7","headertop_ht9")

                #dd.cpy_one_swipper_all_files("services_u7","headexpertise_he2")

                #dd.cpy_one_swipper_all_files("headexpertise_he2","headeroffer_ho2")
                #dd.cpy_one_swipper_all_files("headeroffer_ho2","execaction_ea2")
                #dd.cpy_one_swipper_all_files("titlemain_tm2","companywwd_cwd2")
                #dd.cpy_one_swipper_all_files("treeon_to8","treechildsblue_tcb8")
                #dd.cpy_one_swipper_all_files("companywwd_cwd2","smallcats_sc2")

                #dd.cpy_one_swipper_all_files("smallcats_sc2","catscompany_cc6")
                # catscompany_cc6
                #dd.cpy_one_swipper_all_files("smallcats_sc2","catsoffer_co2")
                #dd.cpy_one_swipper_all_files("smallcats_sc2","catscpub_cp6")
                #dd.cpy_one_swipper_all_files("smallcats_sc2","catstech_ct7")
                #dd.cpy_one_swipper_all_files("smallcats_sc2","catsframework_cf5")
                #dd.cpy_one_swipper_all_files("titlemain_tm2","titletop_tt9")
                #dd.cpy_one_swipper_all_files("catstech_ct7","catsexpertise_ce7")
                #dd.cpy_one_swipper_all_files("catstech_ct7","catswwd_cw7")
                #dd.cpy_one_swipper_all_files("catstech_ct7","catsgen_cg7")

                #dd.cpy_one_swipper_all_files("catsframework_cf5","catstechblog_ctb8")
                #dd.cpy_one_swipper_all_files("catsframework_cf5","mdimages_mi6")                

                #dd.cpy_one_swipper_all_files("mdimages_mi6","catsfeatured_cf5") 
                #dd.cpy_one_swipper_all_files("mdimages_mi6","catslatest_cl8") 
                #dd.cpy_one_swipper_all_files("catslatest_cl8","exciting_wwwd_w8") 

                #dd.cpy_one_swipper_all_files("catslatest_cl8","splash_cmp_sc9") 
                # mod_ep_swipper_splash_cmp_sl4
                #dd.cpy_one_swipper_all_files("splash_cmp_sc9", "splash_cmp_sl2") 
                #dd.cpy_one_swipper_all_files("splash_cmp_sc9", "splash_cmp_sl3") 
                #dd.cpy_one_swipper_all_files("splash_cmp_sc9", "splash_cmp_sl4") 
                #dd.cpy_one_swipper_all_files("splash_cmp_sc9", "splash_cmp_sl5") 
                #dd.cpy_one_swipper_all_files("splash_cmp_sc9", "splash_cmp_sl6") 
                #dd.cpy_one_swipper_all_files("splash_cmp_sc9", "splash_cmp_sl7") 
                #dd.cpy_one_swipper_all_files("splash_cmp_sc9", "splash_cmp_sl8") 
                #dd.cpy_one_swipper_all_files("splash_cmp_sl4", "splash_cmp_sm4") 
                #dd.cpy_one_swipper_all_files("splash_cmp_sl4", "splash_cmp_sm5") 
                #dd.cpy_one_swipper_all_files("splash_cmp_sl4", "splash_cmp_sm6") 

                #dd.cpy_one_swipper_all_files("splash_cmp_sm6", "splash_cmp_sm7","all") 
                #dd.cpy_one_swipper_all_files("titlemain_tm2", "titlecat_tc2","all") 
                #dd.cpy_one_swipper_all_files("splash_cmp_sl4","titlemain_tm2", "images") 
                #dd.cpy_one_swipper_all_files("catschilds_cc5","catsmenu_cm9", "all")
                #dd.cpy_one_swipper_all_files("catschilds_cc5","search_y9", "all")
                #dd.cpy_one_swipper_all_files("search_y9","search_top_st9", "all")
                #dd.cpy_one_swipper_all_files("splash_cmp_sl4", "splash_cmptop_st2","all")
                #dd.cpy_one_swipper_all_files("catschilds_cc5","catsupone_cu1", "all")
                #dd.cpy_one_swipper_all_files("catschilds_cc5","catsuptwo_cu2", "all")

                #dd.cpy_one_swipper_all_files("catsuptwo_cu2","catsup4_cu4", "all")
                #dd.cpy_one_swipper_all_files("catsup4_cu4","catsup0_cu0", "all")
                #dd.cpy_one_swipper_all_files("catsup4_cu4","catsup5_cu5", "all")
                #dd.cpy_one_swipper_all_files("catsup4_cu4","catsup6_cu6", "all")

                #dd.cpy_one_swipper_all_files("catsup6_cu6","catsup1_cu1", "all")
                #dd.cpy_one_swipper_all_files("catsup6_cu6","catsup2_cu2", "all")
                #dd.cpy_one_swipper_all_files("splash_cmp_sl4", "splash_catspath_sc9","all")

                #dd.cpy_one_swipper_all_files("splash_cmp_sl4", "tree_artcontents_tc9","all")
                #dd.cpy_one_swipper_all_files("search_top_st9", "treetopic_tt8","all")
                #dd.cpy_one_swipper_all_files("treetopic_tt8","tree_artcontents_tc9", "all")
                #dd.cpy_one_swipper_all_files("tree_artcontents_tc9","tree_artmenu_tm7", "all")
                #dd.cpy_one_swipper_all_files("tree_artmenu_tm7","md_artcnt_ma7", "all")
                #dd.cpy_one_swipper_all_files("md_artcnt_ma7","md_treebottom_tb9", "all")

                # dd.cpy_one_swipper_all_files("catsup0_cu0","catslatest_cl2", "all-short")
                # dd.cpy_one_swipper_all_files("catsup0_cu0","catslatest_cl2", "image-title")
                # cat_tagsrel_ctr9

                # dd_md = LKD_CopyFilesMd("")                
                # dd_md.exec_cpy_one(idnew)

                dd.m_override_mode = True
                dd.m_error_on_source_not_exist = False
                # dd.cpy_one_swipper_all_files("catslatest_full_xf7","cat_tagschilds_ctc7", "all")
                # dd.cpy_one_swipper_all_files("catslatest_full_xf7","cat_menu_main_cmm9", "all")
                
                # dd.cpy_one_swipper_all_files("cat_menu_main_cmm9","catslatest_full_xf7", "all")
                # dd.cpy_one_swipper_all_files("catslatest_full_xf7","cat_menu_path_cmp9", "all")
                # dd.cpy_one_swipper_all_files("catslatest_full_xf7","jquery_loader_jq7", "all")
                # dd.cpy_one_swipper_all_files("catsup0_cu0","tree_left_tl2", "all")
                # dd.cpy_one_swipper_all_files("treechilds_tc9","mdxtree_mt2", "all")
                # dd.cpy_one_swipper_all_files("treechilds_tc9","mdxtree_mt2", "all")
                # dd.cpy_one_swipper_all_files("md_x8","mdx_content_mx2", "all")
                # mod_ep_swipper_md_treebottom_tb9
                # dd.cpy_one_swipper_all_files("md_treebottom_tb9","md_treecreator_mc2", "all")

                dd.cpy_one_swipper_all_files("treechilds_tc9","treechildsd_td9", "all")

        def refill_full_swipper( self ):
                dd = LKD_CreateSwipperExec("")                 
                dd.m_override_mode = True
                dd.m_error_on_source_not_exist = True
                dd.cpy_one_swipper_all_files("cat_tags_ct7", "catslatest_full_xf7", "all")

        def copy_from_full( self,new_module ):
                dd = LKD_CreateSwipperExec("")   
                dd.m_override_mode = True
                dd.m_error_on_source_not_exist = True
                dd.cpy_one_swipper_all_files("catslatest_full_xf7", new_module, "all")

        def refill_full_copy_one( self, tt ):
                self.refill_full_swipper()
                #self.copy_from_full("cat_tagschilds_ctc7")
                self.copy_from_full("cat_mdparent_ctp7")

# EPT_swipper_render_mdcontent_create_md_artcnt_ma7
# treestatic EPT_swipper_render_treestatic_md_artcnt_ma7


        def create_full_swipper(self,idnew):                
                dd = LKD_CreateSwipperExec("") 
                dd.m_error_on_source_not_exist = False
                dd.m_override_mode = True
                dd.cpy_one_swipper_all_files("md_artcnt_ma7","catslatest_full_xf7", "all")

                dd.m_error_on_source_not_exist = False
                dd.m_override_mode = True
                dd.cpy_one_swipper_all_files("md_treebottom_tb9","catslatest_full_xf7", "all")

                dd.m_error_on_source_not_exist = False
                dd.m_override_mode = True
                dd.cpy_one_swipper_all_files("mdimages_mi6","catslatest_full_xf7", "all")

                dd.m_override_mode = True
                dd.m_error_on_source_not_exist = False
                dd.cpy_one_swipper_all_files("catslatest_cl2","catslatest_full_xf7", "all")

                dd.m_override_mode = True
                dd.m_error_on_source_not_exist = False
                dd.cpy_one_swipper_all_files("catslatest_full_xf7","catslatest_splash_cs7", "all")
                
                dd.m_override_mode = True
                dd.m_error_on_source_not_exist = True
                dd.cpy_one_swipper_all_files("catslatest_full_xf7","catslatest_splash_cs7", "all")


        def exec_cpy_one(self,idnew):                
                dd_md = LKD_CopyFilesMd("")                
                dd_md.exec_cpy_one(idnew)
        
        def exec_cpy_to_all_swippers(self):
                self.xx_dbg("LKD_CreateSwippersMain::exec_cpy_one::start::")
                
                dd_list = LKD_CopyFilesList("")
                ll = dd_list.get_list_of_swippers()

                dd_handler = LKD_CreateSwipperExec("")
                mod_source = "catsup0_cu0"
                mod_source = "md_x8"

                for item_name in ll:
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::start::__" + item_name + "__")
                        #dd_handler.cpy_one_entity_child("pathmain_pm2",item_name)
                        #dd_handler.cpy_one_entity_child("catsmenu_cm9", item_name, "image-title")
                        if(item_name != mod_source):                                
                                # dd_handler.cpy_one_entity_child(mod_source, item_name, "image-title")
                                dd_handler.cpy_one_entity_child(mod_source, item_name, "image-title-desc")

        def exec_cpy_to_all_swippers_catsup_without0(self):
                self.xx_dbg("LKD_CreateSwippersMain::exec_cpy_one::start::")
                
                dd_list = LKD_CopyFilesList("")
                # ll = dd_list.get_list_of_catsup_wihout0()
                ll = dd_list.get_list_of_swippers()
                mod_source = "catsup1_cu1"
                mod_source = "md_x8"
                dd_handler = LKD_CreateSwipperExec("")
                for item_name in ll:
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::start::__" + item_name + "__")
                        #dd_handler.cpy_one_entity_child("pathmain_pm2",item_name)
                        #dd_handler.cpy_one_entity_child("catsmenu_cm9", item_name, "image-title")
                        if(item_name != mod_source ):                                
                                # dd_handler.cpy_one_entity_child(mod_source, item_name, "window-row")
                                # dd_handler.cpy_one_entity_child(mod_source, item_name, "css-file")

                                dd_handler.cpy_one_entity_child(mod_source, item_name, "image-title-desc")
                                

        def exec_cpy_to_all_swippers_short(self,max_files):
                self.xx_dbg("LKD_CreateSwippersMain::exec_cpy_one::start::")
                dd_handler = LKD_CreateSwipperExec("")

                dd_list = LKD_CopyFilesList("")
                ll = dd_list.get_list_of_swippers()
                ii = 0
                for item_name in ll:
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::start::__" + item_name + "__")
                        if ( ii == max_files ):
                                self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::break_after_3t::__" + item_name + "__")
                                break

                        dd_source = "pathmain_pm2"
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::start::__" + item_name + "__")
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::copy_item::__" + dd_source + "__")
                        if ( item_name == dd_source ):
                                self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::skipe::__" + item_name + "__")
                                continue

                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::executet::__" + item_name + "__")
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::copy_item::__" + dd_source + "__")
                        self.xx_dbg("LKD_CreateSwippersMain::CPY_ITEM::__[" + str(ii) + "]__")
                        #dd_handler.cpy_one_entity_child(dd_source, item_name)
                        ii = ii + 1

        def exec_cpy_to_all_swippers_splashes(self):

                dd_list = LKD_CopyFilesList("")
                ll = dd_list.get_list_of_splahes()
                self.exec_cpy_to_all_swippers_one(1, ll, "splash_cmp_sl5", "EPT_swipper_categories_matrix_")

        def exec_cpy_to_all_swippers_splashes_css(self):

                dd_list = LKD_CopyFilesList("")
                ll = dd_list.get_list_of_splahes()
                self.exec_cpy_to_all_swippers_one(1, ll, "splash_cmptop_st2", "css")

        def exec_cpy_list_of_catsup(self):
                dd_list = LKD_CopyFilesList("")
                ll = dd_list.get_list_of_catsup()
                self.exec_cpy_to_all_swippers_one(1, ll, "catsup0_cu0", "cat_copy")

        def exec_cpy_to_all_swippers_includes_and_main(self):
                dd_list = LKD_CopyFilesList("")
                ll = dd_list.get_list_of_swippers()
                self.exec_cpy_to_all_swippers_one(200, ll, "catsup0_cu0", "selector_main")


        def exec_cpy_to_all_swippers_api(self):
                dd_list = LKD_CopyFilesList("")
                ll = dd_list.get_list_of_swippers()
                self.exec_cpy_to_all_swippers_one(1, ll, "prod_splash_ps3", "c-api")



        def exec_cpy_to_all_swippers_one(self, max_files, plist, dd_source, pfilter):
                self.xx_dbg("LKD_CreateSwippersMain::exec_cpy_one::start::")
                
                dd_handler = LKD_CreateSwipperExec("")

                ll = plist
                ii = 0
                for item_name in ll:
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::start::__" + item_name + "__")
                        if ( ii == max_files ):
                                self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::break_after_3t::__" + item_name + "__")
                                break
                        
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::start::__" + item_name + "__")
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::copy_item::__" + dd_source + "__")
                        if ( item_name == dd_source ):
                                self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::skipe::__" + item_name + "__")
                                continue

                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::executet::__" + item_name + "__")
                        self.xx_dbg("LKD_CreateSwippersMain::cpy_one_entity_child::copy_item::__" + dd_source + "__")
                        self.xx_dbg("LKD_CreateSwippersMain::CPY_ITEM::__[" + str(ii) + "]__")
                        dd_handler.cpy_one_swipper_all_files(dd_source, item_name, pfilter)
                        ii = ii + 1

        def generate_refcat(self, ii_from, ii_to, s_type):
                self.xx_dbg("[METHOD_IN]" + "[generate_refcat]")

                while ii_from <= ii_to:
                        ss = "insert into joo2_catg_refcat(m_rg_refcatid, m_rg_value1) values (" + str(ii_from) + ", '" + s_type + "'); "
                        print(ss)
                        ii_from += 1
                
                self.xx_dbg("[METHOD_OUT]" + "[generate_refcat]")

                