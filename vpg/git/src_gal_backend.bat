
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%
git clone https://github.intel.com/wmt/gal-backend

cd %proot%\%ver%%pst%\gal-backend
git checkout -b %ver%.DEVB

rem & C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src_gal_backend.bat