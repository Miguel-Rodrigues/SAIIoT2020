#!/bin/bash

# https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-on-a-raspberry-pi/
# install dependency packages
apt-get update -y
apt-get upgrade -y
apt-get autoremove
apt-get install apache2-dev apache2-mpm-worker libapache2-mod-wsgi-py3 -y

# install python virtual environment
pip3 install virtualenv
virtualenv env
source ./env/bin/activate
pip install -r ./requirements.txt
deactivate

# TODO: configure apache host
# <VirtualHost *:80>
#     ServerAdmin webmaster@localhost
#     DocumentRoot /var/www/html
#     ErrorLog ${APACHE_LOG_DIR}/error.log
#     CustomLog ${APACHE_LOG_DIR}/access.log combined
#     Alias /static ${rootPath}/static
    
#     <Directory ${rootPath}/static> 
#         Require all granted
#     </Directory>
  
#     <Directory ${rootPath}/${applicationName}>
#         <Files wsgi.py>
#             Require all granted
#         </Files>
#     </Directory>
  
#     WSGIDaemonProcess dvds python-path=${rootPath} python-home=${rootPath}/${env}
#     WSGIProcessGroup dvds
#     WSGIScriptAlias / #{rootPath}/${applicationName}/wsgi.py
# </VirtualHost>

# Configure permissions
chmod g+w ${rootPath}/${applicationName}/db.sqlite3
chmod g+w ${rootPath}/${applicationName}
chown :www-data db.sqlite3
chown :www-data ${rootPath}/${applicationName}

#restart server
service apache2 restart
