set cm=current-2017.05.31.W.24-WMT-348-SYNC_FULL

set b0=current-2017.05.31.W.24-WMT-348-SYNC_FULL
set b1=current-2017.05.31.W.25-WMT-348-SYNC_FULL

rem set cm=prod-2.0.0.36-WMT-348
rem set b0=prod-2.0.0.36
rem set b1=prod-2.0.0.37

rem =====================================================

cls

cd C:\lkd\wmtgit\v06\scate-dashboard
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
rem ember server --port 4500
git status 

cd C:\lkd\wmtgit\v06\scate-admin-dashboard
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 


cd C:\lkd\wmtgit\v06\scate-operation-dashboard
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 

cd C:\lkd\wmtgit\v06\scate-backend
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status


cd C:\lkd\wmtgit\v06\w2\gitp
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%

git status 

cd C:\lkd\wmtgit\v06\artifactory-connector
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 

cd C:\lkd\ht\apps_portal\lkduni
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 

cd C:\lkd\wmtgit\v06-01\w2_2
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 


cd C:\lkd\ht\apps_tools\BS_2015
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 


cd C:\lkd\ht\apps_tools\lkdt_2015
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 

rem cd C:\lkd\wmtgit\v06\w2\gitp\
rem cd C:\lkd\wmtgit\v06\w2\gitp\vpg\git
rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-g-long.bat
rem localhost:89/phpMyAdmin-v2/index.php
rem C:\lkd\servers\httpd-2.bat

rem tail -f C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt
rem cd C:\lkd\wmtgit\v06\scate-dashboard
rem Clear-Content "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt"
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt" -Wait
rem notepad "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt"


