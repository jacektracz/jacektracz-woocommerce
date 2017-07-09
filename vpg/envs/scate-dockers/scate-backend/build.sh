#!/usr/bin/env bash

export http_proxy=http://proxy-chain.intel.com:911 && export https_proxy=http://proxy-chain.intel.com:911

curl -sS https://getcomposer.org/installer | php -- --install-dir=/bin

cd /var/www/

git config --global http.sslverify false
git clone https://github.intel.com/mlukasze/requests-backend.git
cd /var/www/requests-backend
git checkout release

echo "<?php

namespace config;

class LocalConfig extends GlobalConfig
{
    public function __construct()
    {
        $this->user = 'admin';
        $this->password = '';
        $this->dbname = 'wmt';
        $this->host = 'productionDb';
        $this->isDevMode = false;
    }
}
" > /var/www/requests-backend/config/local/doctrine.local.php

#php /bin/composer.phar install --no-dev -o

ln -s /var/www/requests-backend /var/www/html

a2enmod rewrite

apachectl -k graceful
