#!/bin/bash
START_FOLDER=`pwd`

print_help() {
  echo 'Usage: '
  echo './CMRStopServers [-s <server1,server2,...>|-a|-h]'
  echo '-s	allows to specify comma-delimited list of servers to stop'
  echo '-a	kills all CMR servers'
  echo '-h      prints this help message'
}

kill_kgrserver_cpp() {
  KGR_STATUS=`ps -ef | grep 'bin/x86Linux/KGRServer' | awk '{total+=1} END{print total-1}'`
  if [ $KGR_STATUS == "0" ] 
	then
		echo 'KGRServer(CPP) is STOPPED, ommitting'
	else
		KGR_PID=`ps -ef | grep 'bin/x86Linux/KGRServer' | grep -v 'grep' | awk '{print $2}'`
		echo 'KGRServer(CPP) is STARTED, PID: '$KGR_PID
		echo 'killing '$KGR_PID
		kill -9 $KGR_PID 
  fi
}
kill_jms(){
  KGR_STATUS=`ps -ef | grep 'Dactivemq.home' | awk '{total+=1} END{print total-1}'`
  if [ $KGR_STATUS == "0" ] 
	then
		echo 'ActiveMQ is STOPPED, ommiting'
	else
		KGR_PID=`ps -ef | grep 'Dactivemq.home' | grep -v 'grep' | awk '{print $2}'`
		echo 'ActiveMQ is STARTED, PID: '$KGR_PID 
		echo 'killing '$KGR_PID
		kill -9 $KGR_PID 
  fi
}
kill_rvd(){
  KGR_STATUS=`ps -ef | grep 'rvd' | awk '{total+=1} END{print total-1}'`
  if [ $KGR_STATUS == "0" ] 
	then
		echo 'Randezvoud is STOPPED, ommiting'
	else
		KGR_PID=`ps -ef | grep 'rvd' | grep -v 'grep' | awk '{print $2}'`
		echo 'Randezvous is STARTED, PID: '$KGR_PID 
		echo 'killing '$KGR_PID
		kill -9 $KGR_PID 
  fi
}
kill_kgrserver_java(){
KGR_STATUS=`ps -ef | grep 'kgr.configuration.kgrserver' | awk '{total+=1} END{print total-1}'`
  if [ $KGR_STATUS == "0" ] 
	then
		echo 'KGRServer(java) is STOPPED, ommiting'
	else
		KGR_PID=`ps -ef | grep 'kgr.configuration.kgrserver' | grep -v 'grep' | awk '{print $2}'`
		echo 'KGRServer(java) is STARTED, PID: '$KGR_PID 
		echo 'killing '$KGR_PID
		kill -9 $KGR_PID 
  fi
}
kill_kgrweb(){
  KGR_STATUS=`ps -ef | grep 'kgr.application.server.name=kgrserver' | awk '{total+=1} END{print total-1}'`
  if [ $KGR_STATUS == "0" ]
	then
                echo 'KGRWebServer is STOPPED, ommiting'
        else
                KGR_PID=`ps -ef | grep 'kgr.application.server.name=kgrserver' | grep -v 'grep' | awk '{print $2}'`
                echo 'KGRWebServer is STARTED, PID: '$KGR_PID 
		echo 'killing '$KGR_PID
		kill -9 $KGR_PID 
  fi
}

if [ $1 == "-s" ]
  then
        arr=$(echo $2 | tr "," "\n")
        for x in $arr
          do
            if [ $x == "KGRServer" ]
              then
		kill_kgrserver_java
		kill_kgrserver_cpp
            elif [ $x == "KGRWeb" ]
              then
		kill_kgrweb
            elif [ $x == "JMS" ]
              then
		kill_jms
            elif [ $x == "RVD" ]
              then
		kill_rvd
            else
                echo 'Unrecognised server: ' $x 
            fi
          done
  elif [ $1 == "-a" ]
    then
    #kill 'em all!
	kill_kgrweb
	kill_kgrserver_java
	kill_kgrserver_cpp
	kill_jms
	kill_rvd
  else
	print_help
fi
