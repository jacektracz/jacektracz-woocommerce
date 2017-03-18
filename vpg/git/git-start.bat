set cm=actions-gen-tmp
set b0=xpw-1.0.03.17.0
set b1=xpw-1.0.03.17.1

cls

cd C:\lkd\wmtgit\v06\scate-dashboard
ember server --port 4900

cd C:\lkd\wmtgit\v06\scate-admin-dashboard
ember server --port 4500

cd C:\lkd\wmtgit\v06\scate-backend
php -S 127.0.0.1:8986 -t .\web\

rem C:\lkd\wmtgit\v06\w2\gitp\vpg\git\git-start.bat

