
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%

git clone https://github.intel.com/jtracz/admincrud-backend.git
cd %proot%\%ver%%pst%\admincrud-backend
git checkout -b %ver%.DEVF

rem & C:\lkd\wmtgit\w2_2\vpg\git\src-acb.bat

