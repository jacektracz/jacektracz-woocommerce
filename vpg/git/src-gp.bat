set ii0=14
set /a "ii1=%ii0%+1"
set /a "ii2=%ii0%+2"
echo "ROOT_OF_CALC_START"

echo %ii1%
echo "ROOT_OF_CALC_END"

set cm=current-2017.06.05.WW.%ii0%


set b0=current-2017.06.05.WW.%ii0%
set b1=current-2017.06.05.WW.%ii1%


rem =====================================================

rem $ git config credential.helper store
rem $ git push https://github.intel.com/WMT/scate-dashboard.git
rem $ git push https://github.intel.com/WMT/scate-admin-dashboard.git
rem git config --global credential.helper 'cache --timeout 7200'

rem Username for 'https://github.com': <USERNAME>
rem Password for 'https://USERNAME@github.com': <PASSWORD>

cls
rem echo '.....'
rem pause

rem cd C:\lkd\wmtgit\v06\scate-dashboard
rem git push https://jtracz:Alinghi2008!@github.intel.com/WMT/scate-dashboard.git origin  %b0%

rem pause

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
