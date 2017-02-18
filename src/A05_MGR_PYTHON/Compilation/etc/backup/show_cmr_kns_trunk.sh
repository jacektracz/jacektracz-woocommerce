getprocess=`ps -ef | grep -i kgrserver | grep -i x86`
echo $getprocess
set $getprocess 
pid=$2
echo $pid
#kill -9 $pid