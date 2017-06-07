set cm=artifactory-2017.04.14.12

set b0=current-2017.04.14.12
set b1=current-2017.04.14.13
set b2=current-2017.04.14.14
set b3=current-2017.04.14.15


rem set b0=prod-2.0.0.0
rem set b1=prod-2.0.0.1


rem set b0=prod-1.0.0.208
rem set b1=prod-1.0.0.209

rem set b0=prod-1.0.0.204
rem set b1=prod-1.0.0.205

set b2=current-1.0.0.206
set b3=current-1.0.0.207

cls


cd C:\lkd\wmtgit\v06\scripts\perf20\perf20docker
git add -A
git checkout master
git merge  %b0%
git push origin  master


cd C:\lkd\wmtgit\v06\scate-admin-dashboard

gitk

rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-gp.bat

rem skarzynskiego 3f/21


rem tail -f C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt
rem Clear-Content "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt"
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt" -Wait
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.err.txt" -Wait
rem php /bin/composer.phar dump-autoload -o

