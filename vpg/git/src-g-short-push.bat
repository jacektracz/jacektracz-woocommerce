
rem cd C:\lkd\wmtgit\v06\w2\gitp\vpg\git
rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-g-short-push.bat

set ii0=0
set dt=16
set dtm=07
set comment=scate-dashboard-alpha
set /a "ii1=%ii0%+1"
set /a "ii2=%ii0%+2"
set /a "ii3=%ii0%+3"
echo "ROOT_OF_CALC_START"

echo %ii1%
echo "ROOT_OF_CALC_END"

set cm=curr-2017.%dtm%.%dt%.WI.%ii0%.%comment%


set b0=curr-2017.%dtm%.%dt%.WI.%ii0%.%comment%
set b1=curr-2017.%dtm%.%dt%.WI.%ii1%.%comment%
set b2=curr-2017.%dtm%.%dt%.WI.%ii2%.%comment%
set b3=curr-2017.%dtm%.%dt%.WI.%ii3%.%comment%


rem =====================================================



rem =====================================================


cls
c:
cd C:\lkd\wmtgit\v06\scate-dashboard
rem git config --global credential.helper wincred
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


c:
cd C:\lkd\wmtgit\v06\scate-dockers
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



cd C:\lkd\wmtgit\v06\scate-dashboard
git push origin  %b1%

cd C:\lkd\wmtgit\v06\scate-admin-dashboard
git push origin  %b1%

cd C:\lkd\wmtgit\v06\scate-backend
git push origin  %b1%

cd C:\lkd\wmtgit\v06\artifactory-connector
git push origin  %b1%

cd C:\lkd\wmtgit\v06\messenger
git push origin  %b1%

cd C:\lkd\wmtgit\v06\gal-dashboard
git push origin  %b1%

cd C:\lkd\wmtgit\v06\gal-backend
git push origin  %b1%


cd C:\lkd\wmtgit\v06\wmt-backend
git push origin  %b1%

cd C:\lkd\wmtgit\v06\wmt-dashboard
git push origin  %b1%

cd C:\lkd\wmtgit\v06\scate-dockers
git push origin  %b1%

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


