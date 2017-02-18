#!/bin/bash

source /jenkins/jt_dev/tools/python/A05_MGR_PYTHON/Compilation/setenv_cmr_dist_dev.txt
source /jenkins/jt_dev/tools/python/A05_MGR_PYTHON/Compilation/setenv_cmr_compilation_dev.txt
cd /jenkins/jt_dev/cmr/cmr_khepri_g9/kgr-khepri/cmr/CMR/src/cpp
echo "KGRCPP: $KGRCPP"
echo "WORKSPACE: $WORKSPACE"
scons generation
#scons --no-cache -j 8 > build.txt 2>&1

	