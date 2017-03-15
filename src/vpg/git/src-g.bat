set cm=completions
set b0=xph-1.0.03.16.6
set b1=xph-1.0.03.16.7

cls

cd C:\lkd\wmtgit\v06\scate-dashboard
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git status 

cd C:\lkd\wmtgit\v06\scate-admin-dashboard
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git status 

cd C:\lkd\wmtgit\v06\scate-backend
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git status 

cd C:\lkd\ht\apps_tools\BS_2015
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git status 

cd C:\lkd\w2\gitp
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git status 

rem C:\lkd\w2\gitp\src\vpg\git\src-g.bat