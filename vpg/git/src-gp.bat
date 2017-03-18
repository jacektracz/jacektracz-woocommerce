set cm=first-import-run
set b0=xpw-1.0.03.17.14
set b1=xpw-1.0.03.17.15


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


rem tail -f C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt
rem Get-Content -Path "C:\lkd\wmtgit\v06\scate-backend\src\Core\logs\log-2.txt.important.txt" -Wait