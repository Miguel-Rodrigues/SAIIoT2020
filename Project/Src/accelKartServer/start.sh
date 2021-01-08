#!/bin/bash

apt-get update -y
apt-get upgrade -y
apt-get autoremove
pip3 install virtualenv

source ./env/bin/activate
cd ./WebProject
python3 manage.py runserver