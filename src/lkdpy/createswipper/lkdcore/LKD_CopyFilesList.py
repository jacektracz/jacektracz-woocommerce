﻿import sys
import os
import logging
import shutil

class LKD_CopyFilesList:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CopyFiles::__init__::in::")
                self.xx_dbg("LKD_CopyFiles::__init__::out::")
               
        def xx_dbg(self, tt):
                "" ""
                print tt
      
        def get_list_short(self):
                self.xx_dbg("LKD_CopyFiles::prepare_object::in::")
                outlist = []    
                
                outlist.append("prod_splash_ps3")
                outlist.append("prod_intro_pi2")
                outlist.append("prod_opinion_po2")
                outlist.append("prod_flow_pf2")
                outlist.append("prod_goals_pg2")
                outlist.append("prod_team_pt2")
                #outlist.append("prod_delivery_pd2")        
                outlist.append("prod_support_ps2")        
                outlist.append("prod_fund_pf2")
                outlist.append("prod_whatnext_pf2")
                outlist.append("prod_clientrequest_cr2")
                outlist.append("prod_list_pl9")
                outlist.append("prod_tags_pd9")
                outlist.append("prod_tags_pd9")

                outlist.append("prod_support_ps2") 
                outlist.append("prod_fund_pf2") 
                outlist.append("prod_whatnext_pf2") 
                #outlist.append("prod_delivery_pd2") 
                outlist.append("prod_opinion_po2")

                self.xx_dbg("LKD_CopyFiles::prepare_object::out::")
                return outlist

        def get_list(self):
                self.xx_dbg("LKD_CopyFiles::prepare_object::in::")
                outlist = []    

                outlist.append("authorsfoot_h7")
                outlist.append("authorsp_u2")
                outlist.append("authors_x3")
                outlist.append("blogtech_x2")
                outlist.append("blog_x1")
                outlist.append("copyright_k2")
                outlist.append("foot_x7")
                outlist.append("hashover_x3")
                outlist.append("header_h8")
                outlist.append("header_h9")
                outlist.append("main")
                outlist.append("md_x8")
                outlist.append("prod_clientrequest_cr2")
                #outlist.append("prod_delivery_pd2")
                outlist.append("prod_flow_pf2")
                outlist.append("prod_fund_pf2")
                outlist.append("prod_goals_pg2")
                outlist.append("prod_intro_pi2")
                outlist.append("prod_list_pl9")
                outlist.append("prod_opinion_po2")
                outlist.append("prod_searchmenu_ps7")
                outlist.append("prod_splash_ps2")
                outlist.append("prod_splash_ps3")
                outlist.append("prod_support_ps2")
                outlist.append("prod_tags_pd9")
                outlist.append("prod_team_pt2")
                outlist.append("prod_team_pt3")
                outlist.append("prod_whatnext_pf2")
                outlist.append("publications_u1")
                outlist.append("related_all_v9")
                outlist.append("related_v8")
                outlist.append("related_v9")
                outlist.append("search_x9")
                outlist.append("search_y9")
                outlist.append("services_s3")
                outlist.append("services_u6")
                outlist.append("services_u7")
                outlist.append("team_u5")
                outlist.append("team_x5")
                outlist.append("trainingsmenu_m6")
                outlist.append("trainingsmenu_m7")
                outlist.append("trainingsmenu_m8")
                outlist.append("tree_v8")
                outlist.append("v3")
                outlist.append("v4")
                outlist.append("v5")
                outlist.append("v6")
                outlist.append("whatwedo_u9")
                
                self.xx_dbg("LKD_CopyFiles::prepare_object::out::")
                return outlist

        def exec_one(self):
                ll = self.get_list()

                
        def get_list_of_modules(self):
                self.xx_dbg("[METHOD_IN]" + "[get_list_of_modules]")

                dd = []
                dd.append('mod_accordeonck')
                dd.append('mod_acymailing')
                dd.append('mod_articles_archive')
                dd.append('mod_articles_categories')
                dd.append('mod_articles_category')
                dd.append('mod_articles_latest')
                dd.append('mod_articles_news')
                dd.append('mod_articles_popular')
                dd.append('mod_banners')
                dd.append('mod_breadcrumbs')
                dd.append('mod_btslideshow')
                dd.append('mod_bt_contentslider')
                dd.append('mod_custom')
                dd.append('mod_dn')
                dd.append('mod_ep_breadcrumbs_top')
                dd.append('mod_ep_btslideshow')
                dd.append('mod_ep_btslideshow_jtmain')
                dd.append('mod_ep_bts_simplemenu')
                dd.append('mod_ep_category_buttons')
                dd.append('mod_ep_category_buttons_bottom')
                dd.append('mod_ep_category_buttons_path')
                dd.append('mod_ep_category_buttons_path_line')
                dd.append('mod_ep_category_buttons_presentation')
                dd.append('mod_ep_category_presentation')
                dd.append('mod_ep_category_title')
                dd.append('mod_ep_cats_btslider')
                dd.append('mod_ep_cats_btslider_table')
                dd.append('mod_ep_cat_images')
                dd.append('mod_ep_choosed_menus')
                dd.append('mod_ep_colors')
                dd.append('mod_ep_cookie_buttons')
                dd.append('mod_ep_currcats')
                dd.append('mod_ep_currcats_generic')
                dd.append('mod_ep_currcats_parent')
                dd.append('mod_ep_flexslider_cats')
                dd.append('mod_ep_foot')
                dd.append('mod_ep_footer')
                dd.append('mod_ep_foot_bottom')
                dd.append('mod_ep_gk_menu_grid')
                dd.append('mod_ep_grid_childs')
                dd.append('mod_ep_grid_core')
                dd.append('mod_ep_grid_executives')
                dd.append('mod_ep_grid_expertise')
                dd.append('mod_ep_grid_footer')
                dd.append('mod_ep_grid_header')
                dd.append('mod_ep_grid_relations1')
                dd.append('mod_ep_grid_relations2')
                dd.append('mod_ep_grid_relations3')
                dd.append('mod_ep_headerwrap')
                dd.append('mod_ep_include_css')
                dd.append('mod_ep_jt_btslider')
                dd.append('mod_ep_lakida_footer')
                dd.append('mod_ep_lead')
                dd.append('mod_ep_lead_splash')
                dd.append('mod_ep_lib_collapsible_panel_2')
                dd.append('mod_ep_lib_m_slider')
                dd.append('mod_ep_lib_m_slider_v2')
                dd.append('mod_ep_menu')
                dd.append('mod_ep_menu_big_v2')
                dd.append('mod_ep_menu_big_wall')
                dd.append('mod_ep_menu_big_wall_choosed')
                dd.append('mod_ep_pathway')
                dd.append('mod_ep_pathway_bottom')
                dd.append('mod_ep_regions_chooser')
                dd.append('mod_ep_right_title')
                dd.append('mod_ep_selregion_accordeonck')
                dd.append('mod_ep_selregion_lead')
                dd.append('mod_ep_selregion_three_tab_fader_v8')
                dd.append('mod_ep_site_mode')
                dd.append('mod_ep_splash_article')
                dd.append('mod_ep_splash_links')
                dd.append('mod_ep_splash_main')
                dd.append('mod_ep_splash_misy_wall_2')
                dd.append('mod_ep_superfish_category_grid')
                dd.append('mod_ep_superfish_menu_grid')
                dd.append('mod_ep_swipper_authorsfoot_h7')
                dd.append('mod_ep_swipper_authorsp_u2')
                dd.append('mod_ep_swipper_authors_x3')
                dd.append('mod_ep_swipper_blogtech_x2')
                dd.append('mod_ep_swipper_blog_x1')
                dd.append('mod_ep_swipper_catsall_ca9')
                dd.append('mod_ep_swipper_catscompany_cc6')
                dd.append('mod_ep_swipper_catscpub_cp6')
                dd.append('mod_ep_swipper_catsenvs_cev6')
                dd.append('mod_ep_swipper_catsevalscms_ce8')
                dd.append('mod_ep_swipper_catsexpertise_ce7')
                dd.append('mod_ep_swipper_catsfeatured_cf5')
                dd.append('mod_ep_swipper_catsframework_cf5')
                dd.append('mod_ep_swipper_catsgen_cg7')
                dd.append('mod_ep_swipper_catslatest_cl8')
                dd.append('mod_ep_swipper_catsoffer_co2')
                dd.append('mod_ep_swipper_catssolutionsc_cs0')
                dd.append('mod_ep_swipper_catssolutionsc_cs9')
                dd.append('mod_ep_swipper_catstechblog_ctb8')
                dd.append('mod_ep_swipper_catstechtopics_ctt5')
                dd.append('mod_ep_swipper_catstech_ct7')
                dd.append('mod_ep_swipper_catswwd_cw7')
                dd.append('mod_ep_swipper_companywwd_cwd2')
                dd.append('mod_ep_swipper_copyright_k2')
                dd.append('mod_ep_swipper_exciting_wwwd_w8')
                dd.append('mod_ep_swipper_execaction_ea2')
                dd.append('mod_ep_swipper_foot_x7')
                dd.append('mod_ep_swipper_hashover_x3')
                dd.append('mod_ep_swipper_headerarticles_ha3')
                dd.append('mod_ep_swipper_headeroffer_ho2')
                dd.append('mod_ep_swipper_headertop_ht9')
                dd.append('mod_ep_swipper_header_h8')
                dd.append('mod_ep_swipper_headexpertise_he2')
                dd.append('mod_ep_swipper_login_sl9')
                dd.append('mod_ep_swipper_main')
                dd.append('mod_ep_swipper_mdimages_mi6')
                dd.append('mod_ep_swipper_md_x8')
                dd.append('mod_ep_swipper_pathmain_pm2')
                dd.append('mod_ep_swipper_prod_clientrequest_cr2')
                dd.append('mod_ep_swipper_prod_delivery_pd2')
                dd.append('mod_ep_swipper_prod_flow_pf2')
                dd.append('mod_ep_swipper_prod_fund_pf2')
                dd.append('mod_ep_swipper_prod_goals_pg2')
                dd.append('mod_ep_swipper_prod_intro_pi2')
                dd.append('mod_ep_swipper_prod_list_pl9')
                dd.append('mod_ep_swipper_prod_opinion_po2')
                dd.append('mod_ep_swipper_prod_searchmenu_ps7')
                dd.append('mod_ep_swipper_prod_splash_ps2')
                dd.append('mod_ep_swipper_prod_splash_ps3')
                dd.append('mod_ep_swipper_prod_support_ps2')
                dd.append('mod_ep_swipper_prod_tags_pd9')
                dd.append('mod_ep_swipper_prod_team_pt3')
                dd.append('mod_ep_swipper_prod_whatnext_pf2')
                dd.append('mod_ep_swipper_publications_u1')
                dd.append('mod_ep_swipper_related_all_v9')
                dd.append('mod_ep_swipper_related_v8')
                dd.append('mod_ep_swipper_related_v9')
                dd.append('mod_ep_swipper_searchmenu_ps7')
                dd.append('mod_ep_swipper_search_x9')
                dd.append('mod_ep_swipper_search_y9')
                dd.append('mod_ep_swipper_services_s3')
                dd.append('mod_ep_swipper_services_u6')
                dd.append('mod_ep_swipper_services_u7')
                dd.append('mod_ep_swipper_services_x3')
                dd.append('mod_ep_swipper_smallcats_sc2')
                dd.append('mod_ep_swipper_splash_cmp_sc9')
                dd.append('mod_ep_swipper_splash_cmp_sl2')
                dd.append('mod_ep_swipper_splash_cmp_sl3')
                dd.append('mod_ep_swipper_splash_cmp_sl4')
                dd.append('mod_ep_swipper_splash_cmp_sl5')
                dd.append('mod_ep_swipper_splash_cmp_sl6')
                dd.append('mod_ep_swipper_splash_cmp_sl7')
                dd.append('mod_ep_swipper_splash_cmp_sl8')
                dd.append('mod_ep_swipper_splash_cmp_sl9')
                dd.append('mod_ep_swipper_splash_cmp_sm1')
                dd.append('mod_ep_swipper_splash_cmp_sm2')
                dd.append('mod_ep_swipper_splash_cmp_sm3')
                dd.append('mod_ep_swipper_splash_cmp_sm4')
                dd.append('mod_ep_swipper_splash_cmp_sm5')
                dd.append('mod_ep_swipper_splash_cmp_sm6')
                dd.append('mod_ep_swipper_team_u5')
                dd.append('mod_ep_swipper_team_x5')
                dd.append('mod_ep_swipper_titlegrid_tg2')
                dd.append('mod_ep_swipper_titlelist_tl4')
                dd.append('mod_ep_swipper_titlemain_tm2')
                dd.append('mod_ep_swipper_titletop_tt9')
                dd.append('mod_ep_swipper_trainingsmenu_m6')
                dd.append('mod_ep_swipper_trainingsmenu_m7')
                dd.append('mod_ep_swipper_trainingsmenu_m8')
                dd.append('mod_ep_swipper_tree')
                dd.append('mod_ep_swipper_treeart_ta8')
                dd.append('mod_ep_swipper_treecats_ts8')
                dd.append('mod_ep_swipper_treechildsblue_tcb8')
                dd.append('mod_ep_swipper_treechilds_tc9')
                dd.append('mod_ep_swipper_treecnt_tc8')
                dd.append('mod_ep_swipper_treefoot1_tf1')
                dd.append('mod_ep_swipper_treefoot2_tf2')
                dd.append('mod_ep_swipper_treegrand_tg9')
                dd.append('mod_ep_swipper_treegreatg1_tg2')
                dd.append('mod_ep_swipper_treegreatg2_tg3')
                dd.append('mod_ep_swipper_treegreatg3_tg4')
                dd.append('mod_ep_swipper_treegreatg_tt9')
                dd.append('mod_ep_swipper_treegrid_tg8')
                dd.append('mod_ep_swipper_treeon_to8')
                dd.append('mod_ep_swipper_treeparent_tp9')
                dd.append('mod_ep_swipper_treeshort_ts8')
                dd.append('mod_ep_swipper_treetopic_tt8')
                dd.append('mod_ep_swipper_treetopic_tt9')
                dd.append('mod_ep_swipper_tree_v8')
                dd.append('mod_ep_swipper_v3')
                dd.append('mod_ep_swipper_v4')
                dd.append('mod_ep_swipper_v5')
                dd.append('mod_ep_swipper_v6')
                dd.append('mod_ep_swipper_whatwedo_u9')
                dd.append('mod_ep_team_bottom_wall')
                dd.append('mod_ep_team_header')
                dd.append('mod_ep_team_menu_original')
                dd.append('mod_ep_team_wall')
                dd.append('mod_ep_team_wall2')
                dd.append('mod_ep_team_wall_lakida')
                dd.append('mod_ep_test')
                dd.append('mod_ep_three_tab')
                dd.append('mod_ep_three_tab_fader')
                dd.append('mod_ep_three_tab_fader_v2')
                dd.append('mod_ep_three_tab_fader_v4')
                dd.append('mod_ep_three_tab_fader_v6')
                dd.append('mod_ep_three_tab_fader_v8')
                dd.append('mod_ep_three_tab_v2')
                dd.append('mod_ep_three_tab_volv4')
                dd.append('mod_ep_three_titles')
                dd.append('mod_ep_top_menu')
                dd.append('mod_ep_tree')
                dd.append('mod_ep_tree_accordion')
                dd.append('mod_ep_virtuemart')
                dd.append('mod_ep_volvo_three')
                dd.append('mod_ep_wall2')
                dd.append('mod_ep_wall3')
                dd.append('mod_ext_superfish_menu')
                dd.append('mod_ezeeaccordion')
                dd.append('mod_fancypantsaccordion')
                dd.append('mod_feed')
                dd.append('mod_footer')
                dd.append('mod_GI_glassymenu')
                dd.append('mod_gk_register')
                dd.append('mod_hot_accordion')
                dd.append('mod_image_show_gk4')
                dd.append('mod_JGMap')
                dd.append('mod_jv_accordion')
                dd.append('mod_jxtc_contactwall')
                dd.append('mod_jxtc_html')
                dd.append('mod_jxtc_newspro')
                dd.append('mod_jxtc_plugoo')
                dd.append('mod_jxtc_twittix')
                dd.append('mod_k2_comments')
                dd.append('mod_k2_content')
                dd.append('mod_k2_login')
                dd.append('mod_k2_quickicons')
                dd.append('mod_k2_stats')
                dd.append('mod_k2_tools')
                dd.append('mod_k2_user')
                dd.append('mod_k2_users')
                dd.append('mod_languages')
                dd.append('mod_latest')
                dd.append('mod_logged')
                dd.append('mod_login')
                dd.append('mod_maximenuck')
                dd.append('mod_menu')
                dd.append('mod_multilangstatus')
                dd.append('mod_news_pro_gk4')
                dd.append('mod_phocagallery_image')
                dd.append('mod_popular')
                dd.append('mod_quickicon')
                dd.append('mod_random_image')
                dd.append('mod_rapid_contact')
                dd.append('mod_related_items')
                dd.append('mod_s5_horizontal_accordion')
                dd.append('mod_search')
                dd.append('mod_SideBarMenuApplestyle')
                dd.append('mod_stats')
                dd.append('mod_status')
                dd.append('mod_submenu')
                dd.append('mod_swmenufree')
                dd.append('mod_syndicate')
                dd.append('mod_tabs_gk4')
                dd.append('mod_title')
                dd.append('mod_toolbar')
                dd.append('mod_tz_accordion_slideshow')
                dd.append('mod_tz_carousel_slideshow')
                dd.append('mod_tz_categoryname')
                dd.append('mod_tz_latestnew_service')
                dd.append('mod_tz_latestnew_slider')
                dd.append('mod_tz_piecemaker')
                dd.append('mod_tz_portfolio')
                dd.append('mod_tz_slidegallery')
                dd.append('mod_tz_slideshow_nivoslide')
                dd.append('mod_tz_twitterwidget')
                dd.append('mod_users_latest')
                dd.append('mod_virtuemart_cart')
                dd.append('mod_virtuemart_currencies')
                dd.append('mod_virtuemart_manufacturer')
                dd.append('mod_virtuemart_product')
                dd.append('mod_virtuemart_search')
                dd.append('mod_weblinks')
                dd.append('mod_whosonline')
                dd.append('mod_widgetkit')
                dd.append('mod_widgetkit_twitter')
                dd.append('mod_wrapper')
                return dd

        def get_list_of_swippers(self):
                self.xx_dbg("[METHOD_IN]" + "[get_list_of_modules]")

                dd = []
                dd.append('authorsfoot_h7')
                dd.append('authorsp_u2')
                dd.append('authors_x3')
                dd.append('blogtech_x2')
                dd.append('blog_x1')
                dd.append('catsall_ca9')
                dd.append('catscompany_cc6')
                dd.append('catscpub_cp6')
                dd.append('catsenvs_cev6')
                dd.append('catsevalscms_ce8')
                dd.append('catsexpertise_ce7')
                dd.append('catsfeatured_cf5')
                dd.append('catsframework_cf5')
                dd.append('catsgen_cg7')
                dd.append('catslatest_cl8')
                dd.append('catsoffer_co2')
                dd.append('catssolutionsc_cs0')
                dd.append('catssolutionsc_cs9')
                dd.append('catstechblog_ctb8')
                dd.append('catstechtopics_ctt5')
                dd.append('catstech_ct7')
                dd.append('catswwd_cw7')
                dd.append('companywwd_cwd2')
                dd.append('copyright_k2')
                dd.append('exciting_wwwd_w8')
                dd.append('execaction_ea2')
                dd.append('foot_x7')
                dd.append('hashover_x3')
                dd.append('headerarticles_ha3')
                dd.append('headeroffer_ho2')
                dd.append('headertop_ht9')
                dd.append('header_h8')
                dd.append('headexpertise_he2')
                dd.append('login_sl9')
                dd.append('main')
                dd.append('mdimages_mi6')
                dd.append('md_x8')
                dd.append('pathmain_pm2')
                dd.append('prod_clientrequest_cr2')
                dd.append('prod_delivery_pd2')
                dd.append('prod_flow_pf2')
                dd.append('prod_fund_pf2')
                dd.append('prod_goals_pg2')
                dd.append('prod_intro_pi2')
                dd.append('prod_list_pl9')
                dd.append('prod_opinion_po2')
                dd.append('prod_searchmenu_ps7')
                dd.append('prod_splash_ps2')
                dd.append('prod_splash_ps3')
                dd.append('prod_support_ps2')
                dd.append('prod_tags_pd9')
                dd.append('prod_team_pt3')
                dd.append('prod_whatnext_pf2')
                dd.append('publications_u1')
                dd.append('related_all_v9')
                dd.append('related_v8')
                dd.append('related_v9')
                dd.append('searchmenu_ps7')
                dd.append('search_x9')
                dd.append('search_y9')
                dd.append('services_s3')
                dd.append('services_u6')
                dd.append('services_u7')
                dd.append('services_x3')
                dd.append('smallcats_sc2')
                dd.append('splash_cmp_sc9')
                dd.append('splash_cmp_sl2')
                dd.append('splash_cmp_sl3')
                dd.append('splash_cmp_sl4')
                dd.append('splash_cmp_sl5')
                dd.append('splash_cmp_sl6')
                dd.append('splash_cmp_sl7')
                dd.append('splash_cmp_sl8')
                dd.append('splash_cmp_sl9')
                dd.append('splash_cmp_sm1')
                dd.append('splash_cmp_sm2')
                dd.append('splash_cmp_sm3')
                dd.append('splash_cmp_sm4')
                dd.append('splash_cmp_sm5')
                dd.append('splash_cmp_sm6')
                dd.append('team_u5')
                dd.append('team_x5')
                dd.append('titlegrid_tg2')
                dd.append('titlelist_tl4')
                dd.append('titlemain_tm2')
                dd.append('titletop_tt9')
                dd.append('trainingsmenu_m6')
                dd.append('trainingsmenu_m7')
                dd.append('trainingsmenu_m8')
                dd.append('tree')
                dd.append('treeart_ta8')
                dd.append('treecats_ts8')
                dd.append('treechildsblue_tcb8')
                dd.append('treechilds_tc9')
                dd.append('treecnt_tc8')
                dd.append('treefoot1_tf1')
                dd.append('treefoot2_tf2')
                dd.append('treegrand_tg9')
                dd.append('treegreatg1_tg2')
                dd.append('treegreatg2_tg3')
                dd.append('treegreatg3_tg4')
                dd.append('treegreatg_tt9')
                dd.append('treegrid_tg8')
                dd.append('treeon_to8')
                dd.append('treeparent_tp9')
                dd.append('treeshort_ts8')
                dd.append('treetopic_tt8')
                dd.append('treetopic_tt9')
                dd.append('tree_v8')
                dd.append('v3')
                dd.append('v4')
                dd.append('v5')
                dd.append('v6')
                dd.append('whatwedo_u9')
                return dd                

        def get_list_of_splahes(self):
                self.xx_dbg("[METHOD_IN]" + "[get_list_of_modules]")
                dd = []

                dd.append('splash_cmp_sc9')
                dd.append('splash_cmp_sl2')
                dd.append('splash_cmp_sl3')
                dd.append('splash_cmp_sl4')
                dd.append('splash_cmp_sl5')
                dd.append('splash_cmp_sl6')
                dd.append('splash_cmp_sl7')
                dd.append('splash_cmp_sl8')
                dd.append('splash_cmp_sl9')
                dd.append('splash_cmp_sm1')
                dd.append('splash_cmp_sm2')
                dd.append('splash_cmp_sm3')
                dd.append('splash_cmp_sm4')
                dd.append('splash_cmp_sm5')
                dd.append('splash_cmp_sm6')
                dd.append('splash_cmp_sm7')
                dd.append('splash_cmptop_st2')
                return dd
