#!/bin/bash


source /jenkins/jt_dev/tools/python/A05_MGR_PYTHON/Compilation/setenv_cmr_trunk_v1.sh
cd /jenkins/jt_dev/cmr/cmr_trunk_v1/kgr-trunk/src/cpp

#mvn -f ${WORKSPACE}/pom.xml -e -s ${WORKSPACE}/src/java/settings.xml -Dmaven.test.skip=true -Ddist.dir=${WORKSPACE}/install -Dkns.src.dir=${KGRCPP} -P release,generated-libs,default,package clean install

scons generation
#scons --no-cache -j 8 > build.txt 2>&1
