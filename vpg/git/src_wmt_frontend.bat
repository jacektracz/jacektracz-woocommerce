
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
rem mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%
git clone https://github.intel.com/wmt/wmt-dashboard
cd %proot%\%ver%%pst%\wmt-dashboard
git checkout -b %ver%.DEVF

rem & D:\lkd\komodo\w2_2\dat\env\cpphy\src_wmt.bat