#!/bin/bash

source /jenkins/jt_dev/tools/python/A05_MGR_PYTHON/Compilation/setenv_cmr_dev.txt

cd /jenkins/jt_dev/cmr/cmr_khepri_v2/kgr-khepri/src/java/kgr-server

#mvn -f ${WORKSPACE}/pom.xml -e -s ${WORKSPACE}/src/java/settings.xml -Dmaven.test.skip=true -Ddist.dir=${WORKSPACE}/install -Dkns.src.dir=${KGRCPP} -P release,generated-libs,default,package clean install

mvn -f ${WORKSPACE}/src/java/kgr-server/pom.xml -e -s ${WORKSPACE}/src/java/settings.xml -Dmaven.test.skip=true -Ddist.dir=${WORKSPACE}/install -Dkns.src.dir=${KGRCPP} -P release,generated-libs,default,package clean install	