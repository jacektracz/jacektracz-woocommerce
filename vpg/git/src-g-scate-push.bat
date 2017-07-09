

cls
c:
cd C:\lkd\wmtgit\v06\scate-dashboard
rem rem git config --global credential.helper wincred
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
rem git checkout -b %b2%
rem git checkout -b %b3%
rem ember server --port 4500
dir
git status 

c:
cd C:\lkd\wmtgit\v06\scate-admin-dashboard
rem git config --global credential.helper wincred
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

c:
cd C:\lkd\wmtgit\v06\scate-operation-dashboard
rem git config --global credential.helper wincred
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

c:
cd C:\lkd\wmtgit\v06\scate-backend
rem git config --global credential.helper wincred
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status

c:
cd C:\lkd\wmtgit\v06\w2\gitp
rem git config --global credential.helper wincred
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

c:
cd C:\lkd\wmtgit\v06\artifactory-connector
rem git config --global credential.helper wincred
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 


c:
cd C:\lkd\wmtgit\v06\wmt-dashboard
rem git config --global credential.helper wincred
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 


c:
cd C:\lkd\wmtgit\v06\wmt-backend
rem git config --global credential.helper wincred
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

c:
cd C:\lkd\wmtgit\v06\gal-backend
rem git config --global credential.helper wincred
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

c:
cd C:\lkd\wmtgit\v06\gal-dashboard
rem git config --global credential.helper wincred
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

c:
cd C:\lkd\wmtgit\v06\messenger
rem git config --global credential.helper wincred
rem git branch --set-upstream-to=origin/v06.DEV8
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status


rem cd C:\lkd\wmtgit\v06\scate-dashboard
rem git push origin  %b1%

rem cd C:\lkd\wmtgit\v06\scate-admin-dashboard
rem git push origin  %b1%

cd C:\lkd\wmtgit\v06\scate-backend
git push origin  %b1%

rem cd C:\lkd\wmtgit\v06\artifactory-connector
rem git push origin  %b1%

rem cd C:\lkd\wmtgit\v06\messenger
rem git push origin  %b1%

rem cd C:\lkd\wmtgit\v06\gal-dashboard
rem git push origin  %b1%

rem cd C:\lkd\wmtgit\v06\gal-backend
rem git push origin  %b1%


rem cd C:\lkd\wmtgit\v06\wmt-backend
rem git push origin  %b1%

rem cd C:\lkd\wmtgit\v06\wmt-dashboard
rem git push origin  %b1%


rem cd C:\lkd\wmtgit\v06\w2\gitp\
rem cd C:\lkd\wmtgit\v06\w2\gitp\vpg\git
rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-g-short-push.bat
rem localhost:89/phpMyAdmin-v2/index.php
rem C:\lkd\servers\httpd-2.bat

rem tail -f C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt
rem cd C:\lkd\wmtgit\v06\scate-dashboard
rem Clear-Content "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt"
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt" -Wait
rem notepad "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt"


