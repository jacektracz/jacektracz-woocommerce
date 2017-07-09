#!/usr/bin/env bash

cd /var/www/scate-backend

git checkout release
git pull

./bin/doctrine orm:clear-cache:query
./bin/doctrine orm:clear-cache:result
./bin/doctrine orm:clear-cache:metadata

apachectl -k graceful
