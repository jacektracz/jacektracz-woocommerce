
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
rem mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%
git clone https://github.intel.com/wmt/requests-backend

cd %proot%\%ver%%pst%\requests-backend
git checkout -b %ver%.DEVB

rem & D:\lkd\komodo\w2_2\dat\env\cpphy\src_wmt.bat