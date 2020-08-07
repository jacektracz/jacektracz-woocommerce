import sys
import os
from createswipper.lkdcore.LKD_CopyFiles import *
from createswipper.lkdcore.LKD_CopyFilesMd import *
from createswipper.lkdcore.LKD_CopyFilesExec import *
from createswipper.lkdcore.LKD_CreateFiles import *
from createswipper.lkdcore.LKD_FinAnalysis import *
from createswipper.lkdcore.LKD_CreateImages import *
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py
# 600 446 066 Rafal tel

class LKD_MainExec:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_MainExec::__init__::in::")
                self.xx_dbg("LKD_MainExec::__init__::out:")

        def xx_dbg(self, tt):
                "" ""
                print ( tt )

        def refill_swipper(self, tt):
                dd = LKD_CopyFilesExec("")
                dd.refill_full_swipper()

        def create_one_swipper(self, tt):
                dd = LKD_CopyFilesExec("")
                dd.cpy_one_swipper_all_files()

        def create_md(self, tt):
                ddh = LKD_CopyFilesMd("")
                ddh.create_md()

        def create_md_all(self, tt):
                ddh = LKD_CopyFilesMd("")
                ddh.create_md_all(tt,1, 6000)

        def refill_full_copy_one(self, tt):
                ddh = LKD_CopyFilesExec("")
                ddh.refill_full_copy_one()

if __name__ == "__main__":

        ddh = LKD_MainExec("")
        ddh.refill_full_copy_one("")

        # ddh.create_one_swipper("")
        # ddh.create_md("")
        # ddh.create_md_all("")

        #ddh.refill_swipper("")

        # ddcr = LKD_CreateFiles("")
        # ddcr.execute_main()

        # nn

        #######################################
        # COPY SWIPPER START >>>>>
        #######################################

        # dd = LKD_CopyFilesExec("")
        #dd.refill_full_swipper()

        # dd.exec_cpy_to_all_swippers_catsup_without0()
        # dd.exec_cpy_to_all_swippers()
        # dd.cpy_one_swipper_all_files()

        #dd.exec_cpy_list_of_catsup()
        #dd.exec_cpy_to_all_swippers_api()
        #dd.exec_cpy_to_all_swippers_includes_and_main()
        #dd.exec_cpy_to_all_swippers_main()
        


        #dd.exec_cpy_to_all_swippers_splashes()
        #dd.exec_cpy_to_all_swippers_short(300)
        #dd.exec_cpy_to_all_swippers_splashes_css()
        #dd.exec_cpy_one()
        #######################################
        # <<<<<COPY SWIPPER END
        #######################################



        #######################################
        # COPY SWIPPER MD START >>>>>
        #######################################

        #dd.exec_populate_mds()
        #dd.exec_cpy_mds()        


        #dd.exec_cpy_mds()
        #dd.exec_cpy_contents_mds()
        #dd.exec_cpy_one(4480)
        #dd.exec_cpy_one(4522)
        #dd.exec_cpy_one(4524)
        #dd.exec_cpy_one(4526)
        #dd.exec_cpy_one(4531)

        #######################################
        # <<<<<COPY SWIPPER MD END
        #######################################


        #######################################
        # COPY FILES MD START >>>> 
        #######################################

        #hh_md = LKD_CopyFilesMd("")     
        #hh_md.exec_cpy_many

        #dd.generate_refcat(4677, 4700, "phd-thesis=article")
        # modules/mod_ep_swipper_tree_artmenu_tm7
        #######################################
        # <<<<< COPY FILES MD END
        #######################################


        #######################################
        # FIN START >>>>>
        #######################################
        # dd_fin = LKD_FinAnalysis("")
        # dd_fin.print_data()
        #######################################
        # <<<< FIN END
        #######################################



        #######################################
        # CREATE IMAGES START >>>>>
        #######################################

        # dd_img = LKD_CreateImages("")
        # dd_img.exec_images()
        # dd_img.move_digital_images_to_md()

        #######################################
        # <<<< CREATE IMAGES END
        #######################################
