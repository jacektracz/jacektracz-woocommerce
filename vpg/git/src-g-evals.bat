set ii0=0
set /a "ii1=%ii0%+1"
set /a "ii2=%ii0%+2"
set /a "ii3=%ii0%+3"
echo "ROOT_OF_CALC_START"

echo %ii1%
echo "ROOT_OF_CALC_END"

set cm=current-2017.06.16.HM.%ii0%.berta-start

set b0=current-2017.06.16.HM.%ii0%
set b1=current-2017.06.16.HM.%ii1%
set b2=current-2017.06.16.HM.%ii2%
set b3=current-2017.06.16.HMN.%ii3%


rem =====================================================


cls
c:
cd C:\lkd\ht\apps_jhipster\eval-1\eval-a2
git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b3%
dir
git status 
rem  current-2017.05.2.h.0
rem git checkout current-2017.05.7.h.0

c:
cd C:\lkd\ht\apps_jhipster\eval-1\eval-b2
git init

git checkout -b %b0%
git add -A
git commit -m %cm%
git checkout -b %b1%
git checkout -b %b2%
git checkout -b %b3%
dir
git status 

rem cd C:\lkd\wmtgit\v06\w2\gitp\vpg\git
rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-g-evals.bat

