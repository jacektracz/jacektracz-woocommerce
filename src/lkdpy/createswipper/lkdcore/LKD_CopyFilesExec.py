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
                dd_md.cpy_all("3937", "3966")
                dd_md.cpy_all("3937", "3967")
                dd_md.cpy_all("3937", "3968")
                dd_md.cpy_all("3937", "3969")
                dd_md.cpy_all("3937", "3970")
                dd_md.cpy_all("3937", "3971")

        def exec_cpy_swipper(self):

                dd = LKD_CopyFiles("")                
                #dd.cpy_all("tree_v8","treecnt_tc8")
                #dd.cpy_all("treeart_ta8","treeon_to8")
                #dd.cpy_all("services_u7","catsall_ca9")
                dd.cpy_all("treeon_to8","treegrid_tg8")
                