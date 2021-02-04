#!/bin/bash

# https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-on-a-raspberry-pi/
echo "== Purge old installation =="
service AccelKartServer stop
service apache2 stop
rm -r /var/www/AccelkartServer

echo "== Install/Update dependencies =="
apt-get install matchbox-keyboard apache2-dev apache2 python3 git nodejs npm -y
pip3 install virtualenv

echo "== Create Root folder =="
mkdir /var/www/AccelkartServer
chmod 775 /var/www/AccelkartServer

echo "== Install Django Server =="
\cp -r ./ /var/www/AccelkartServer
cd /var/www/AccelkartServer

echo "== Install python virtual environment =="
virtualenv env
source ./env/bin/activate
pip install -r ./requirements.txt
pip install RPi.GPIO
cd ./WebProject
chmod 775 ./manage.py
./manage.py collectstatic --noinput
./manage.py migrate
./manage.py makemigrations
cd ..
deactivate

echo "== install static dependencies =="
cd ./WebProject/static/AccelKartServer/
npm install
cd ../../../

echo "== Create Daphne daemon =="
mv ./AccelKartServer.local.conf /etc/apache2/sites-available
mv ./AccelKartServer.service /etc/systemd/system

echo "== Configure permissions =="
chmod g+w /var/www/AccelkartServer/WebProject/db.sqlite3
chmod g+w /var/www/AccelkartServer/WebProject
chmod g+w /var/www/AccelkartServer
chown :www-data /var/www/AccelkartServer/WebProject/db.sqlite3
chown :www-data /var/www/AccelkartServer/WebProject
chown :www-data /var/www/AccelkartServer
usermod -a -G gpio www-data

echo "== Enable mods and website =="
a2enmod proxy
a2enmod proxy_http
a2enmod proxy_balancer
a2enmod lbmethod_byrequests
a2ensite AccelKartServer.local

echo "== Restart apache2 server =="
service AccelKartServer start
service apache2 start

echo "All done! You may need to Reboot..."
