import sys
import os
import logging
import shutil
from LKD_CopyFilesList import *
from LKD_CopyFiles import *
from LKD_CopyFilesMd import *
class LKD_CopyFilesExec:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CopyFilesExec::__init__::in::")
                self.xx_dbg("LKD_CopyFilesExec::__init__::out::")
               
        def xx_dbg(self, tt):
                "" ""
                print tt
                      
                

        def exec_cpy_one(self):
                self.xx_dbg("LKD_CopyFilesExec::exec_cpy_one::start::")
                dd_handler = LKD_CopyFiles("")
                dd_list = LKD_CopyFilesList("")
                ll = dd_list.get_list()
                for item_name in ll:
                        self.xx_dbg("LKD_CopyFilesExec::cpy_one_entity_child::start::__" + item_name + "__")
                        #dd_handler.cpy_one_entity_child("prod_delivery_pd2",item_name)


                
        def exec_populate_mds(self):
                self.xx_dbg("LKD_CopyFilesExec::exec_cpy_one::start::")
                dd_handler = LKD_CopyFilesMd("")
                dd_list = LKD_CopyFilesList("")
                ll = dd_list.get_list()
                for item_name in ll:
                        self.xx_dbg("LKD_CopyFilesExec::cpy_one_entity_child::start::__" + item_name + "__")
                        dd_handler.populate_one_md("3958","3958",item_name)

        def exec_cpy_mds(self):

	        dd_md = LKD_CopyFilesMd("")                
                dd_md.exec_cpy_mds()

        def exec_cpy_contents_mds(self):
                dd_md = LKD_CopyFilesMd("")                
                dd_md.exec_cpy_contents_mds()

        def exec_cpy_swipper(self):

                dd = LKD_CopyFiles("")                
                #dd.cpy_all("tree_v8","treecnt_tc8")
                #dd.cpy_all("treeart_ta8","treeon_to8")
                #dd.cpy_all("services_u7","catsall_ca9")
                #dd.cpy_all("treeon_to8","treegrid_tg8")
                #dd.cpy_all("treeon_to8","treetopic_tt8")
                #dd.cpy_all("treetopic_tt9","treechilds_tc9")
                #dd.cpy_all("treetopic_tt9","treeparent_tp9")                
                #dd.cpy_all("treegreatg_tt9","treefoot1_tf1")
                #dd.cpy_all("treegreatg_tt9","treefoot2_tf1")
                #dd.cpy_all("treegreatg_tt9","treegreatg1_tg2")
                #dd.cpy_all("treegreatg_tt9","treegreatg2_tg3")

                # dd.cpy_all("treegreatg_tt9","treegreatg3_tg4")

                #dd.cpy_all("authorsfoot_h7","headertop_ht9")

                #dd.cpy_all("services_u7","headexpertise_he2")

                #dd.cpy_all("headexpertise_he2","headeroffer_ho2")
                #dd.cpy_all("headeroffer_ho2","execaction_ea2")
                #dd.cpy_all("titlemain_tm2","companywwd_cwd2")
                #dd.cpy_all("treeon_to8","treechildsblue_tcb8")
                #dd.cpy_all("companywwd_cwd2","smallcats_sc2")

                #dd.cpy_all("smallcats_sc2","catscompany_cc6")
                # catscompany_cc6
                #dd.cpy_all("smallcats_sc2","catsoffer_co2")
                #dd.cpy_all("smallcats_sc2","catscpub_cp6")
                #dd.cpy_all("smallcats_sc2","catstech_ct7")
                #dd.cpy_all("smallcats_sc2","catsframework_cf5")
                #dd.cpy_all("titlemain_tm2","titletop_tt9")
                #dd.cpy_all("catstech_ct7","catsexpertise_ce7")
                #dd.cpy_all("catstech_ct7","catswwd_cw7")
                #dd.cpy_all("catstech_ct7","catsgen_cg7")

                #dd.cpy_all("catsframework_cf5","catstechblog_ctb8")
                #dd.cpy_all("catsframework_cf5","mdimages_mi6")                

                #dd.cpy_all("mdimages_mi6","catsfeatured_cf5") 
                #dd.cpy_all("mdimages_mi6","catslatest_cl8") 
                dd.cpy_all("catslatest_cl8","catsevalscms_ce8") 


        def exec_cpy_one(self,idnew):                
                dd_md = LKD_CopyFilesMd("")                
                dd_md.exec_cpy_one(idnew)
        