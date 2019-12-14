import sys
import os
from createswipper.lkdcore.LKD_CopyFiles import *
from createswipper.lkdcore.LKD_CopyFilesMd import *
from createswipper.lkdcore.LKD_CopyFilesExec import *
#python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py
if __name__ == "__main__":

	dd = LKD_CopyFilesExec("")
        #dd.exec_cpy_one()
        #dd.exec_populate_mds()
        #dd.exec_cpy_mds()        
        dd.exec_cpy_swipper()
