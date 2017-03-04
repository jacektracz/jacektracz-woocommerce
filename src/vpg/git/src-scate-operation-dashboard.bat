
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%

git clone https://github.intel.com/wmt/scate-operation-dashboard.git

git clone https://github.intel.com/wmt/scate-operation-backend.git

mkdir %proot%\%ver%%pst%\scate-operation-dashboard
cd %proot%\%ver%%pst%\scate-operation-dashboard
git checkout -b init-%ver%-dashboard.DEVF

mkdir %proot%\%ver%%pst%\scate-operation-backend
cd %proot%\%ver%%pst%\scate-operation-backend
git checkout -b init-%ver%-backend.DEVF

rem cd C:\lkd\wmtgit\w2_2\vpg\git\
rem & C:\lkd\wmtgit\w2_2\vpg\git\src-scate-operation-dashboard.bat
