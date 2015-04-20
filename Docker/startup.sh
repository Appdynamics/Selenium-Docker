#!/bin/bash

# This is a starup script for the Selenium server

# Set EC2 Region variable
source /appdynamics/env.sh && sed -i "s/EC2_REGION/${EC2_REGION}/g" /appdynamics/SeleniumDemoLoad/seleniumload.sh

# Input Ecomm IPs
source /appdynamics/env.sh && find /appdynamics/SeleniumDemoLoad/config/ -type f -name "*.cfg" -exec sed -i'' -e "s/ecommerce1/${ECOMM1}/g" {} +
source /appdynamics/env.sh && find /appdynamics/SeleniumDemoLoad/config/ -type f -name "*.cfg" -exec sed -i'' -e "s/ecommerce2/${ECOMM2}/g" {} +
source /appdynamics/env.sh && find /appdynamics/SeleniumDemoLoad/config/ -type f -name "*.cfg" -exec sed -i'' -e "s/ecommercestaging/${ECOMMSTAGING}/g" {} +

# Input Bundy IPs
source /appdynamics/env.sh && find /appdynamics/SeleniumDemoLoad/config/ -type f -name "*.cfg" -exec sed -i'' -e "s/bundy1/${BUNDY1}/g" {} +
source /appdynamics/env.sh && find /appdynamics/SeleniumDemoLoad/config/ -type f -name "*.cfg" -exec sed -i'' -e "s/bundy2/${BUNDY2}/g" {} +
source /appdynamics/env.sh && find /appdynamics/SeleniumDemoLoad/config/ -type f -name "*.cfg" -exec sed -i'' -e "s/bundystaging/${BUNDYSTAGING}/g" {} +

# Input MovieTix IPs
source /appdynamics/env.sh && find /appdynamics/SeleniumDemoLoad/config/ -type f -name "*.cfg" -exec sed -i'' -e "s/movietix1/${MOVIE1}/g" {} +
source /appdynamics/env.sh && find /appdynamics/SeleniumDemoLoad/config/ -type f -name "*.cfg" -exec sed -i'' -e "s/movietix2/${MOVIE2}/g" {} +
source /appdynamics/env.sh && find /appdynamics/SeleniumDemoLoad/config/ -type f -name "*.cfg" -exec sed -i'' -e "s/movietixstaging/${MOVIESTAGING}/g" {} +

# Start MachineAgent
#su - appdynamics -c "source /appdynamics/env.sh && sed -i 's/AGENT_OPTIONS -Dappdynamics.agent.uniqueHostId=/AGENT_OPTIONS -Dappdynamics.controller.hostName=${CONTROLLER} -Dappdynamics.controller.port=${APPD_PORT} -Dappdynamics.agent.uniqueHostId=/g' /appdynamics/MachineAgent/startMachineAgent.sh"
#su - appdynamics -c 'source /appdynamics/MachineAgent/startMachineAgent.sh'

# Start services
cron -f &
#su - appdynamics -c 'source /appdynamics/MachineAgent/startMachineAgent.sh'
#su - appdynamics -c '/appdynamics/SeleniumDemoLoad/seleniumload.sh start'
cd /appdynamics/SeleniumDemoLoad && ./restartSeleniumDemoLoad.sh

exit 0
