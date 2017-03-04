ls /var/www/ember/dist/scate
ember build -o /var/www/ember/dist/scate
cp config/environment.js ../environment_test.txt

git -c http.sslVerify=false pull

cp ../environment_test.txt config/environment.js
ember build -e test -o /var/www/ember/dist/scate
