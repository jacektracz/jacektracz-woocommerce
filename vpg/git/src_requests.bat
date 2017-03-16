
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%
git clone https://github.intel.com/wmt/requests-backend
git clone https://github.intel.com/wmt/requests-dashboard
cd %proot%\%ver%%pst%\requests-backend
git checkout -b %ver%.DEVB
cd %proot%\%ver%%pst%\requests-dashboard
git checkout -b %ver%.DEVF

rem & D:\lkd\komodo\w2_2\dat\env\cpphy\src_wmt.bat