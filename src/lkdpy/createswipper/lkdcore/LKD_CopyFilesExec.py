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
                dd.cpy_all("companywwd_cwd2","pathmain_pm2")

        def exec_cpy_one(self,idnew):                
                dd_md = LKD_CopyFilesMd("")                
                dd_md.exec_cpy_one(idnew)
        