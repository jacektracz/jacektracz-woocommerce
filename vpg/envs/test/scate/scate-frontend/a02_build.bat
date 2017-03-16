cp config/local/doctrine.local.php config/local/doctrine.local.php.bat
cp src/db/configs/test/config/local/doctrine.local.php config/local/doctrine.local.php
chmod 777 /var/www/scate-backend/cache/

tail -f /var/www/scate-backend/src/Core/logs/log-2.txt.err.txt

vi /var/www/scate-backend/config/local/doctrine.local.php

cp ../environment.txt config/environment.js

ls /var/www/ember/dist/scate

ember build -o /var/www/ember/dist/scate


git -c http.sslVerify=false pull

cp config/environment.js ../environment_test.txt
ember build -e test -o /var/www/ember/dist/scate
ember build -o /var/www/ember/dist/scate
