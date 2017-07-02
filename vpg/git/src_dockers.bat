
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
mkdir %proot%\%ver%%pst%\dockers
cd %proot%\%ver%%pst%\dockers

git clone https://github.intel.com/WMT/perf20docker
cd %proot%\%ver%%pst%\dockers
git checkout -b %ver%.DEVB

rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src_dockers.bat
rem cd c:\lkd\wmtgit\v06\dockers