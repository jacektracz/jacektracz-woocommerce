rem cd C:\lkd\wmtgit\v06\w2\gitp\vpg\git\
rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-g-bs.bat


set ii0=12
set dt=31
set dtm=12
set comment=tools-start
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


rem set b2=current-2017.04.25.26
rem set b3=current-2017.04.25.27

rem set b0=prod-2.0.0.0
rem set b1=prod-2.0.0.1


rem cls

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
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

cd C:\lkd\ht\apps_jhipster\eval-1\eval-a2
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
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
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

d:
cd d:\lkd\ht\apps_portal\lkduni
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
rem git checkout -b %b2%
rem git checkout -b %b3%
dir
git status 

