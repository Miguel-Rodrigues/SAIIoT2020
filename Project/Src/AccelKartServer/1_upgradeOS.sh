#!/bin/bash

# https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-on-a-raspberry-pi/
# install dependency packages
echo "== Purge old installation =="
rm -r /var/www/AccelkartServer

echo "== Upgrade OS =="
apt-get update -y
apt-get dist-upgrade -y
apt-get autoremove -y

echo "== Dependencies installed. Rebooting =="
reboot
