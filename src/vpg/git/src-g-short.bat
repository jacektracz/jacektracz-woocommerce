set cm=current-2017.05.26.W.2--WMT-300--track-table-added

set b0=current-2017.05.26.W.2
set b1=current-2017.05.26.W.3

rem set b0=prod-2.0.0.16
rem set b1=prod-2.0.0.17


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


rem cd C:\lkd\wmtgit\v06\w2\gitp\
rem cd C:\lkd\wmtgit\v06\w2\gitp\vpg\git
rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-g-short.bat
rem localhost:89/phpMyAdmin-v2/index.php
rem C:\lkd\servers\httpd-2.bat

rem tail -f C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt
rem cd C:\lkd\wmtgit\v06\scate-dashboard
rem Clear-Content "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt"
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt" -Wait
rem notepad "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt"


