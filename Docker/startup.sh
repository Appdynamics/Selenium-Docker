#!/bin/bash

# This is a starup script for the Bundy Java server

# Edit hosts file
sudo echo "" >> /etc/hosts
sudo echo "54.190.107.43   www.ecommerce1.com" >> /etc/hosts
sudo echo "54.203.78.38    www.ecommerce2.com" >> /etc/hosts
sudo echo "54.202.32.47    www.ecommercestaging.com" >> /etc/hosts
sudo echo "54.214.253.138  www.moviesearch1.com" >> /etc/hosts
sudo echo "54.244.107.80   www.moviesearch2.com" >> /etc/hosts
sudo echo "54.214.146.251  www.moviesearchstaging.com" >> /etc/hosts
sudo echo "54.70.167.208   www.bundyshoes1.com" >> /etc/hosts
sudo echo "54.214.147.9    www.bundyshoes2.com" >> /etc/hosts
sudo echo "54.184.203.176  www.bundyshoesstaging.com" >> /etc/hosts
sudo echo "54.190.170.102  static.twitter.com" >> /etc/hosts
sudo echo "54.190.170.102  static.facebook.com" >> /etc/hosts
sudo echo "54.190.170.102  cdn.bundyshoes.com" >> /etc/hosts

# Set EC2 Region variable
source /appdynamics/env.sh

# Start MachineAgent
#su - appdynamics -c "source /appdynamics/env.sh && sed -i 's/AGENT_OPTIONS -Dappdynamics.agent.uniqueHostId=/AGENT_OPTIONS -Dappdynamics.controller.hostName=${CONTROLLER} -Dappdynamics.controller.port=${APPD_PORT} -Dappdynamics.agent.uniqueHostId=/g' /appdynamics/MachineAgent/startMachineAgent.sh"
#su - appdynamics -c 'source /appdynamics/MachineAgent/startMachineAgent.sh'

# Set crontab
#su - appdynamics -c 'crontab /appdynamics/cron.conf'
#crontab /appdynamics/cron.conf

# Start services
cron -f &
#su - appdynamics -c 'source /appdynamics/MachineAgent/startMachineAgent.sh'
#su - appdynamics -c '/appdynamics/SeleniumDemoLoad/seleniumload.sh start'
cd /appdynamics/SeleniumDemoLoad && ./restartSeleniumDemoLoad.sh

exit 0
