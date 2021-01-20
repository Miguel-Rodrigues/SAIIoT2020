#!/bin/bash

#Download
# Create a folder
mkdir /opt/actions-runner
cd /opt/actions-runner

# Download the latest runner package
curl -O -L https://github.com/actions/runner/releases/download/v2.274.2/actions-runner-linux-arm-2.274.2.tar.gz

# Extract the installer
tar xzf ./actions-runner-linux-arm-2.274.2.tar.gz

#Configure
# Create the runner and start the configuration experience
./config.sh --url https://github.com/Miguel-Rodrigues/SAIIoT2020 --token $0

#Last step, run it!
# ./run.sh

#To Install the service
./svc.sh install
./svc.sh start

#To get status:
# sudo ./svc.sh status

#To stop the service:
# sudo ./svc.sh stop

#To uninstall the service:
# sudo ./svc.sh uninstall
