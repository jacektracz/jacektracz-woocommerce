set cm=completion-start
set b0=xph-1.0.03.19.28
set b1=xph-1.0.03.19.29
set b2=xph-1.0.03.19.30
set b3=xph-1.0.03.19.31

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
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt" -Wait