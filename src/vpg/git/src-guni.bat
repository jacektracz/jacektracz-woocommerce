set cm=current-2017.05.04.w.2

set b0=current-2017.05.04.w.2
set b1=current-2017.05.04.w.3
rem set b2=current-2017.04.25.26
rem set b3=current-2017.04.25.27

rem set b0=prod-2.0.0.0
rem set b1=prod-2.0.0.1


cls


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


cd C:\lkd\wmtgit\v06-01\w2_2
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


cd C:\lkd\ht\apps_portal\lkduni
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 

cd C:\lkd\ht\apps_jhipster\eval-1\eval-2
rem git init
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 

cd C:\lkd\ht\apps_jhipster\eval-1\eval-3
rem git init
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 

cd C:\lkd\ht\apps_jhipster\eval-1\eval-4
rem git init
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 

cd C:\lkd\ht\apps_jhipster\eval-1\eval-6
rem git init
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 

cd C:\lkd\ht\apps_conf\configs\jhipster
git init
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
git status 

rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-guni.bat

rem
rem

rem cd C:\lkd\wmtgit\v06\w2\gitp\

rem localhost:89/phpMyAdmin-v2/index.php
rem C:\lkd\servers\httpd-2.bat

rem tail -f C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt
rem cd C:\lkd\wmtgit\v06\scate-dashboard
rem Clear-Content "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt"
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt" -Wait
rem notepad "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt"
