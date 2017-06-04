set cm=completion-finished

set b0=prod-1.0.0.202
set b1=prod-1.0.0.203

set b2=prod-1.0.0.196
set b3=prod-1.0.0.197

cls

cd C:\lkd\wmtgit\v06\scate-dashboard
git push origin  %b0%

cd C:\lkd\wmtgit\v06\scate-admin-dashboard
git push origin  %b0%

cd C:\lkd\wmtgit\v06\scate-backend
git push origin  %b0%

cd C:\lkd\wmtgit\v06\scate-admin-dashboard
gitk

rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\src-gp.bat

rem skarzynskiego 3f/21

rem C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqld.exe

rem tail -f C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt" -Wait
rem php /bin/composer.phar dump-autoload -o

