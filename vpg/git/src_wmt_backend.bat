
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
rem mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%
git clone https://github.intel.com/wmt/wmt-backend
cd %proot%\%ver%%pst%\wmt-backend
git checkout -b %ver%.DEVB


rem php -S 127.0.0.1:8886 -t .\web\
rem & D:\lkd\komodo\w2_2\dat\env\cpphy\src_wmt_backend.bat
