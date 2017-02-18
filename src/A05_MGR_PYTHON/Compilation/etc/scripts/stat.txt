#!/bin/bash
KGR_STATUS=`ps -ef | grep 'bin/x86Linux/KGRServer' | awk '{total+=1} END{print total-1}'`
if [ $KGR_STATUS == "0" ] 
	then
		echo 'KGRServer(CPP) is STOPPED'
	else
		KGR_PID=`ps -ef | grep 'bin/x86Linux/KGRServer' | grep -v 'grep' | awk '{print $2}'`
		echo 'KGRServer(CPP) is STARTED, PID: '$KGR_PID 
fi
KGR_STATUS=`ps -ef | grep 'Dactivemq.home' | awk '{total+=1} END{print total-1}'`
if [ $KGR_STATUS == "0" ] 
	then
		echo 'ActiveMQ is STOPPED'
	else
		KGR_PID=`ps -ef | grep 'Dactivemq.home' | grep -v 'grep' | awk '{print $2}'`
		echo 'ActiveMQ is STARTED, PID: '$KGR_PID 
fi
KGR_STATUS=`ps -ef | grep 'rvd' | awk '{total+=1} END{print total-1}'`
if [ $KGR_STATUS == "0" ] 
	then
		echo 'Randezvoud is STOPPED'
	else
		KGR_PID=`ps -ef | grep 'rvd' | grep -v 'grep' | awk '{print $2}'`
		echo 'Randezvous is STARTED, PID: '$KGR_PID 
fi
KGR_STATUS=`ps -ef | grep 'kgr.configuration.kgrserver' | awk '{total+=1} END{print total-1}'`
if [ $KGR_STATUS == "0" ] 
	then
		echo 'KGRServer(java) is STOPPED'
	else
		KGR_PID=`ps -ef | grep 'kgr.configuration.kgrserver' | grep -v 'grep' | awk '{print $2}'`
		echo 'KGRServer(java) is STARTED, PID: '$KGR_PID 
fi
KGR_STATUS=`ps -ef | grep 'kgr.application.server.name=kgrserver' | awk '{total+=1} END{print total-1}'`
if [ $KGR_STATUS == "0" ]
	then
                echo 'KGRWebServer is STOPPED'
        else
                KGR_PID=`ps -ef | grep 'kgr.application.server.name=kgrserver' | grep -v 'grep' | awk '{print $2}'`
                echo 'KGRWebServer is STARTED, PID: '$KGR_PID 
fi
