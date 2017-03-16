set cm=completions
set b0=xph-1.0.03.16.44
set b1=xph-1.0.03.16.45

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

cd C:\lkd\wmtgit\v06\w2\gitp
git add -A
git commit -m %cm%
git checkout -b %b0%
git checkout -b %b1%
git status 

rem C:\lkd\wmtgit\v06\w2\gitp\src\vpg\git\src-g.bat
rem tail -f C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt" -Wait