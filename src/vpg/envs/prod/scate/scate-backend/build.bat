cp config/local/doctrine.local.php config/local/doctrine.local.php.bat
cp src/db/configs/test/config/local/doctrine.local.php config/local/doctrine.local.php
chmod 777 /var/www/scate-backend/cache
mkdir /var/www/scate-backend/src/Core/logs
chmod 777 /var/www/scate-backend/src/Core/logs
tail -f /var/www/scate-backend/src/Core/logs/log-2.txt.err.txt

vi /var/www/scate-backend/config/local/doctrine.local.php

cp ../environment.txt config/environment.js

ls /var/www/ember/dist/scate

ember build -o /var/www/ember/dist/scate




		GenericLogger::logToFile("LocalConfig::__construct::method::start::");
        $this->user = 'admin';
        $this->password = '4ES0MO7nTyec';
        $this->dbname = 'wmt_test';
        $this->port = '3306';
		$this->host = 'productionDb';
        $this->isDevMode = true;
        $this->isOrmCache = false;
        $this->isMemCache = false;
        $this->logging = true;
		$this->isOrmCache = false;
		$this->isMemCache = false;
		$this->isFileCache = true;
		$this->isMetadataCache = false;
		$this->isQueryCache = false;
		$this->isResultsCache = false;
		$this->isSecondLevelCache = false;
        GenericLogger::logToFile("LocalConfig::__construct::method::end::");

		
		
PROD::SCATE::BACK

	10.237.132.143
	mlukasze
	1024knives!
		
	
	docker run -di --name scatebackprod2 -p 8111:80 -p 8211:443 --add-host productionDb:10.237.132.18 --link perf20memcached:cacheengine --link rabbitmq:queuemng scate-back-test:latest
	docker exec -it scatebackprod2 bash -l
	
	
	