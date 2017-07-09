

pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
rem mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%
git clone https://github.intel.com/jtracz/scate-dockers
cd %proot%\%ver%%pst%\scate-dockers
git checkout -b %ver%.DEVF

rem & C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src_scate_dockers.bat

cd c:\lkd\wmtgit\v06\scate-dockers