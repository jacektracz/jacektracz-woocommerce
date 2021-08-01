import sys
import os
from createswipper.lkdcore.LKD_CopyFilesMd import *
from createswipper.lkdcore.LKD_CreateSwippersMain import *
from createswipper.lkdcore.LKD_CreateMdFilesFromProjectsSrc import *
from createswipper.lkdcore.LKD_FinAnalysis import *
from createswipper.lkdcore.LKD_CreateImages import *
from createswipper.lkdcore.LKD_CopyFilesPortal import *
from createswipper.lkdcore.LKD_CreateCatsFromDirectories import *
from createswipper.lkdcore.country_db.LKD_CreateCountryExec import *
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py
#  600 446 066 Rafal tel
# select "cats.append(self.get_item(",id,",","\"",title,"\"","))" from joo2_categories where parent_id = 11178

class LKD_MainExec:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_MainExec::__init__::in::")
                self.xx_dbg("LKD_MainExec::__init__::out:")

        def xx_dbg(self, tt):
                "" ""
                print ( tt )

        def prepare_copy_swippers(self, tt):
                dd = LKD_CopyFilesPortal("")
                dd.create_cpy_portal("")

        def refill_swipper(self, tt):
                dd = LKD_CreateSwippersMain("")
                dd.refill_full_swipper()

        def create_one_swipper(self, tt):
                dd = LKD_CreateSwippersMain("")
                dd.cpy_one_swipper_all_files()

        def create_md(self, tt):
                ddh = LKD_CopyFilesMd("")
                #ddh.create_md()

        def create_md_all(self, tt):
                ddh = LKD_CopyFilesMd("")
                #ddh.create_md_all(tt,1, 6000)

        def refill_full_copy_one(self, tt):
                ddh = LKD_CreateSwippersMain("")
                ddh.refill_full_copy_one("cat_mdparent_ctp7")

        def exec_fin(self, tt):
                dd_fin = LKD_FinAnalysis("")
                #dd_fin.print_data()
                dd_fin.print_data_processed()
        
        def images_create_sequential_ids(self, tt):
                dd_img = LKD_CreateImages("")
                #dd_img.create_sequential_ids()
                max_img_id_source_bucket = 2000
                cat_id_start = 10100
                cat_id_end = 11000

                dd_img.move_digital_images_to_md(
                        max_img_id_source_bucket
                        ,cat_id_start
                        ,cat_id_end)

        def exec_cpy_many_md_files(self, tt):
                dd_mdh = LKD_CopyFilesMd("")
                dd_mdh.exec_cpy_many_md_files(8001,12000,14000) 

        def exec_create_images(self,tt):
                dd_img = LKD_CreateImages("")
                dd_img.exec_images()
                dd_img.move_digital_images_to_md()

        def create_source_files(self,tt):
                ddcr = LKD_CreateMdFilesFromProjectsSrc("")
                ddcr.execute_main_create_from_source()

        def create_cats_from_directories(self,tt):
                ddcr = LKD_CreateCatsFromDirectories("")
                ddcr.execute_main("")

                
        def print_cats_for_dirs_db(self,tt):
                ddcr = LKD_CreateMdFilesFromProjectsSrc("")
                ddcr.print_cats_for_dirs_db("")

        def add_two(self,a,b):
                return a+b

        def get_print_files_to_create(self,tt):
                ddcr = LKD_CreateCatsFromDirectories("")
                pth = "C:/lkd/ht/apps_spring_algorithms/app/src/Algorithms-1/src/main/java/com/williamfiset/algorithms/datastructures"
                pth = "C:/lkd/ht/apps_spring_algorithms/app/src/Algorithms-1/src/main/java/com/williamfiset/algorithms"
                pth = "C:/lkd/ht/apps_spring_eugen/app/src/tutorials"
                ddcr.get_print_files_to_create(pth)
                ddcr.get_crete_files_to_create(pth)

        def create_country(self,tt):
                ddcr = LKD_CreateCountryExec("")
                ddcr.execute_main("")

#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py perform-cat-file
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py perform-src-files
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py print-to-create
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py create-md-files
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py create-one-swipper
#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py create-country
if __name__ == "__main__":

        ddh = LKD_MainExec("")
        # ddh.print_cats_for_dirs_db("")
        if len(sys.argv) > 1:
                s_arg_0 = sys.argv[1]

        if (s_arg_0 == "perform-cat-file"):
                ddh.create_cats_from_directories("")

        if (s_arg_0 == "perform-src-files"):
                ddh.create_source_files("")

        if (s_arg_0 == "print-to-create"):
                ddh.get_print_files_to_create("")

        if (s_arg_0 == "create-md-files"):
                ddh.exec_cpy_many_md_files("")

        #ddh.exec_cpy_many_md_files("")

        if (s_arg_0 == "create-one-swipper"):
                ddh.create_one_swipper("")

        if (s_arg_0 == "create-country"):
                ddh.create_country("")

        # ddh.refill_full_copy_one("")
        # ddh.exec_fin("")

        # ddh.images_create_sequential_ids("")

        # #####################################

        # ddh.create_source_files("")

        # ddh.create_cats_from_directories("") 

        # ddh.create_one_swipper("")

        #ddh.prepare_copy_swippers("")
        # ddh.exec_cpy_many_mds("")

        # ddh.create_md("")
        # ddh.create_md_all("")

        #ddh.refill_swipper("")

        # ddcr = LKD_CreateMdFilesFromProjectsSrc("")
        # ddcr.execute_main()

        # nn

        #######################################
        # COPY SWIPPER START >>>>>
        #######################################

        # dd = LKD_CreateSwippersMain("")
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
