#!/bin/bash

export KREDITNETHOME=/jenkins/dist/FR/CMR
export KREDITNET_CONFIG_PATH=/jenkins/dist/FR/CMR/config
export KREDITNETLOG=/jenkins/dist/FR/CMR/log
export FREETDS=/jenkins/dist/FR/CMR/3rdparty/freetds
export FREETDSCONF=/jenkins/dist/FR/CMR/config/freetds.conf
export ARCH=x86Linux

export LD_LIBRARY_PATH=${FREETDS}/lib/${ARCH}:$LD_LIBRARY_PATH
export PATH=${FREETDS}/bin/${ARCH}:$PATH


export KGRCPP=/jenkins/jt_dev/cmr/cmr_khepri_v2/kgr-khepri/src/cpp
export WORKSPACE=/jenkins/jt_dev/cmr/cmr_khepri_v2/kgr-khepri/
export KGRCPP=/jenkins/jt_dev/cmr/cmr_khepri_v2/kgr-khepri/src/cpp


#scons generation
#scons --no-cache -j 8 > build.txt 2>&1
#mvn -f ${WORKSPACE}/pom.xml -e -s ${WORKSPACE}/src/java/settings.xml -Dmaven.test.skip=true -Ddist.dir=${WORKSPACE}/install -Dkns.src.dir=${KGRCPP} -P release,generated-libs,default,package clean install

	