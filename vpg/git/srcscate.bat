
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%

git clone https://github.intel.com/WMT/scate-dashboard.git
rem git clone https://github.intel.com/WMT/scate-backend.git
rem https://github.intel.com/jtracz/admincrud-dashboard
rem cd %proot%\%ver%%pst%\scate-backend
rem git checkout -b %ver%.DEVB
cd %proot%\%ver%%pst%\scate-dashboard
git checkout -b %ver%.DEVF

rem & D:\lkd\komodo\w2_2\dat\env\cpphy\srcv.bat

rem & C:\lkd\wmtgit\w2_2\dat\env\cpphy\srcscate.bat