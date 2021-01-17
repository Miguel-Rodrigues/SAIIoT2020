#!/bin/bash

# https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-on-a-raspberry-pi/
# install dependency packages
echo "== Install/Update dependencies =="
apt-get update -y
apt-get upgrade -y
apt-get autoremove -y
apt-get install apache2-dev apache2 libapache2-mod-wsgi-py3 python3 git -y
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
deactivate
mv ./AccelKartServer.local.conf /etc/apache2/sites-available

echo "== Configure permissions =="
chmod g+w /var/www/AccelkartServer/db.sqlite3
chmod g+w /var/www/AccelkartServer
chown :www-data db.sqlite3
chown :www-data /var/www/AccelkartServer

echo "== Restart HTTPD server =="
service apache2 restart

echo "All done! You may need to Reboot..."
