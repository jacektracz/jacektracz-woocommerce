#!/bin/sh

getprocess=`ps -ef | grep -i kgrserver | grep -i x86`
#echo $getprocess
if [ -n "$getprocess ]; then

	set $getprocess 
	pid=$2
	echo 'i will kill ...' 
	echo $pid
	
	if [ "$pid" -gt 0 ]; then
		echo 'found  kns and kill'
		kill -9 $pid
	else
		echo 'no kns'
	fi
fi	