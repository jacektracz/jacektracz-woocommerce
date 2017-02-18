source /jenkins/jt_dev/tools/python/A05_MGR_PYTHON/Compilation/setenv_cmr_trunk_v1.sh
source /jenkins/jt_dev/tools/python/A05_MGR_PYTHON/Compilation/kill_cmr_kns_trunk.sh
echo 'killed'
sleep 5s
kh_cp
cd /home/kdeveloper/FR/CMR/etc
./startKNS
#tail -f /home/kdeveloper/FR/CMR/log/KGRServer_master_stdout.log
kh_debkh
