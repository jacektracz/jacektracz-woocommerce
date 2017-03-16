
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
mkdir %proot%\%ver%%pst%\scripts\perf20
cd %proot%\%ver%%pst%\scripts\perf20

git clone https://github.intel.com/WMT/perf20docker
cd %proot%\%ver%%pst%\scripts\perf20\perf20dockers
git checkout -b %ver%.DEVB

rem & C:\lkd\wmtgit\w2_2\vpg\git\src-scripts.bat
rem cd C:\lkd\wmtgit\v06\scripts\perf20\perf20docker