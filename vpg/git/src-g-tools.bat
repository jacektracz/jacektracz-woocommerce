set ii0=2
set /a "ii1=%ii0%+1"
set /a "ii2=%ii0%+2"
echo "ROOT_OF_CALC_START"

echo %ii1%
echo "ROOT_OF_CALC_END"

set cm=current-2017.06.08.WH.%ii0%


set b0=current-2017.06.08.WH.%ii0%
set b1=current-2017.06.08.WH.%ii1%

rem set b2=current-2017.04.25.26
rem set b3=current-2017.04.25.27

rem set b0=prod-2.0.0.0
rem set b1=prod-2.0.0.1


rem cls

c:
cd C:\lkd\ht\apps_tools\BS_2015
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

c:
cd C:\lkd\ht\apps_tools\lkdt_2015
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

c:

cd C:\lkd\wmtgit\v06\w2\gitp
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

rem c:
rem cd C:\lkd\ht\apps_jhipsterg\src\app
rem git add -A
rem git commit -m %cm%
rem git checkout -b %b0%
rem git checkout -b %b1%
rem c:
rem git status 

rem git checkout -b %b2%
rem git checkout -b %b3%

rem cd C:\lkd\ht\apps_jhipster\eval-1\eval-a1
rem git init
rem git add -A
rem git commit -m %cm%
rem git checkout -b %b0%
rem git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
rem git status 

rem cd C:\lkd\ht\apps_jhipster\eval-1\eval-a2
rem git init
rem git add -A
rem git commit -m %cm%
rem git checkout -b %b0%
rem git checkout -b %b1%
rem git checkout -b %b2%
rem git checkout -b %b3%
rem git status 

rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-g-tools.bat

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
