
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%

git clone https://github.intel.com/WMT/scate-admin-dashboard.git

git clone https://github.intel.com/WMT/scate-admin-backend.git

cd %proot%\%ver%%pst%\scate-admin-dashboard
git checkout -b init-%ver%-dashboard.DEVF
cd %proot%\%ver%%pst%\scate-admin-backend
git checkout -b init-%ver%-backend.DEVF

rem & D:\lkd\komodo\w2_2\dat\env\cpphy\srcv.bat

rem & C:\lkd\wmtgit\w2_2\vpg\git\src-scate-admin.bat
rem cd c:\lkd\wmtgit\v06\scate-admin-backend