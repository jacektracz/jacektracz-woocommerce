#!/bin/bash

export KREDITNETHOME=/home/kdeveloper/FR/CMR
export KREDITNET_CONFIG_PATH=/home/kdeveloper/FR/CMR/config
export KREDITNETLOG=/home/kdeveloper/FR/CMR/log
export FREETDS=/home/kdeveloper/FR/CMR/3rdparty/freetds
export FREETDSCONF=/home/kdeveloper/FR/CMR/config/freetds.conf
export ARCH=x86Linux

export LD_LIBRARY_PATH=${FREETDS}/lib/${ARCH}:$LD_LIBRARY_PATH
export PATH=${FREETDS}/bin/${ARCH}:$PATH

