#!/bin/bash

export KREDITNETHOME=/home/kdeveloper/FR/CMR
export KREDITNET_CONFIG_PATH=/home/kdeveloper/FR/CMR/config
export KREDITNETLOG=/home/kdeveloper/FR/CMR/log
export FREETDS=/home/kdeveloper/FR/CMR/3rdparty/freetds
export FREETDSCONF=/home/kdeveloper/FR/CMR/config/freetds.conf
export ARCH=x86Linux

export LD_LIBRARY_PATH=${FREETDS}/lib/${ARCH}:$LD_LIBRARY_PATH
export PATH=${FREETDS}/bin/${ARCH}:$PATH

export KGRCPP=/jenkins/jt_dev/cmr/cmr_trunk_v1/kgr-trunk/src/cpp
export WORKSPACE=/jenkins/jt_dev/cmr/cmr_trunk_v1/kgr-trunk/
export KGRCPP=/jenkins/jt_dev/cmr/cmr_trunk_v1/kgr-trunk/src/cpp

#mvn -f ${WORKSPACE}/pom.xml -e -s ${WORKSPACE}/src/java/settings.xml -Dmaven.test.skip=true -Ddist.dir=${WORKSPACE}/install -Dkns.src.dir=${KGRCPP} -P release,generated-libs,default,package clean install
#scons generation
#scons --no-cache -j 8 > build.txt 2>&1
