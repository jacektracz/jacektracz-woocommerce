set cm=completion-finished

set b0=xph-1.0.03.21.8
set b1=xph-1.0.03.21.9
set b2=xph-1.0.03.21.10
set b3=xph-1.0.03.21.11

rem set b0=prod-1.0.0.62
rem set b1=prod-1.0.0.63
rem set b2=prod-1.0.0.64
rem set b3=prod-1.0.0.65

cls

cd C:\lkd\wmtgit\v06\scate-dashboard
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b3%
git status 

cd C:\lkd\wmtgit\v06\scate-admin-dashboard
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b3%
git status 

cd C:\lkd\wmtgit\v06\scate-backend
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b3%
git status 

cd C:\lkd\ht\apps_tools\BS_2015
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b3%
git status 


cd C:\lkd\wmtgit\v06-01\w2_2
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b3%
git status 



cd C:\lkd\wmtgit\v06\w2\gitp
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b3%

git status 

rem cd C:\lkd\wmtgit\v06\w2\gitp\
rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-g.bat
rem localhost:89/phpMyAdmin-v2/index.php
rem C:\lkd\servers\httpd-2.bat

rem tail -f C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt
rem cd C:\lkd\wmtgit\v06\scate-dashboard

rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt" -Wait
rem notepad "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt"