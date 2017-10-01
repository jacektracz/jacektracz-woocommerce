
rem cd C:\lkd\wmtgit\v06\w2\gitp\vpg\git
rem C:\lkd\wmtgit\v06\w2\gitp\lkd\git\
rem C:\lkd\wmtgit\v06\w2\gitp\lkd\git\a-git.bat
rem cd c:/lkd/ht/apps_jee/lkd-jee
rem  curr-2017.09.30.WI.5.generic
rem git checkout curr-2017.09.30.WI.5.generic

set ii0=12
set dt=01
set dtm=10
set comment=working-app-02
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
set b1g=curr-2017.%dtm%.%dt%.WI.%ii1%.generic


rem =====================================================
cd C:\lkd\ht\apps_jee\lkd-jee
rem git config --global credential.helper wincred
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b1g%
git status
rem git checkout -b %b2%
rem git checkout -b %b3%
rem ember server --port 4500


c:
cd C:\lkd\wmtgit\v06\w2\gitp
rem git config --global credential.helper wincred
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git checkout -b %b1g%
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
git checkout -b %b1g%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status



c:
cd C:\lkd\ht\apps_tools\BS_2015
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
cd C:\lkd\ht\apps_tools\lkdt_2015
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b1g%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

c:

cd C:\lkd\wmtgit\v06\w2\gitp
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b1g%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

cd C:\lkd\ht\apps_portal\lkduni
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b1g%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

cd C:/lkd/ht/apps_vm/installed
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b1g%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

rem =====================================================
echo "cd C:\lkd\ht\apps_jee\lkd-jee"
cd C:\lkd\ht\apps_jee\lkd-jee
git status
