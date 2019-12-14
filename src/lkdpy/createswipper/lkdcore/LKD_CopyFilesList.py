import sys
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

                
