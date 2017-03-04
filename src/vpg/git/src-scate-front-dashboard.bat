
pause

set ver=v06
set pst=
set proot=c:\lkd\wmtgit

cd %proot%
mkdir %proot%\%ver%%pst%
cd %proot%\%ver%%pst%

git clone https://github.intel.com/jtracz/scate-front-dashboard.git

git clone https://github.intel.com/jtracz/scate-front-backend.git

mkdir %proot%\%ver%%pst%\scate-front-dashboard
cd %proot%\%ver%%pst%\scate-front-dashboard
git checkout -b init-%ver%-dashboard.DEVF

mkdir %proot%\%ver%%pst%\scate-front-backend
cd %proot%\%ver%%pst%\scate-front-backend
git checkout -b init-%ver%-backend.DEVF

rem cd C:\lkd\wmtgit\w2_2\vpg\git\
rem & C:\lkd\wmtgit\w2_2\vpg\git\src-scate-front-dashboard.bat
