set cm=current-2017.05.26.W.2--WMT-300--track-table-added

set b0=current-2017.05.26.W.2
set b1=current-2017.05.26.W.3

rem set b0=prod-2.0.0.16
rem set b1=prod-2.0.0.17



cls

cd C:\lkd\wmtgit\v06\scate-dashboard
git push origin  %b0%

cd C:\lkd\wmtgit\v06\scate-admin-dashboard
git push origin  %b0%

cd C:\lkd\wmtgit\v06\scate-backend
git push origin  %b0%

cd C:\lkd\wmtgit\v06\artifactory-connector
git push origin  %b0%


rem cd C:\lkd\wmtgit\v06\scripts\perf20\perf20docker
rem git add -A
rem git checkout master
rem git merge  %b0%
rem  git push origin  master


cd C:\lkd\wmtgit\v06\scate-admin-dashboard

gitk

rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-gp.bat

rem skarzynskiego 3f/21


rem tail -f C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt
rem Clear-Content "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt"
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt" -Wait
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.err.txt" -Wait
rem php /bin/composer.phar dump-autoload -o
rem localhost:89/apps_portal/lkduni/src
rem
rem
