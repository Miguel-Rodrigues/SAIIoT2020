#!/bin/bash

# https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-on-a-raspberry-pi/
# install dependency packages
apt-get update -y
apt-get upgrade -y
apt-get autoremove
apt-get install apache2-dev apache2-mpm-worker libapache2-mod-wsgi-py3 python3 git -y

# install python virtual environment
pip3 install virtualenv
virtualenv env
source ./env/bin/activate
pip install -r ./requirements.txt
deactivate

#Virtualhost Manage Script
wget -O virtualhost https://raw.githubusercontent.com/RoverWire/virtualhost/master/virtualhost.sh
chmod +x virtualhost
wget -O virtualhost-nginx https://raw.githubusercontent.com/RoverWire/virtualhost/master/virtualhost-nginx.sh
chmod +x virtualhost-nginx

virtualhost create "accelKartServer.local" cd ..

# Configure permissions
chmod g+w /var/www/accelkartServer/db.sqlite3
chmod g+w /var/www/accelkartServer
chown :www-data db.sqlite3
chown :www-data /var/www/accelkartServer

#restart server
service apache2 restart
