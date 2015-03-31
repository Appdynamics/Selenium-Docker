#!/bin/bash

# This is a starup script for the Selenium server

# Set EC2 Region variable
source /appdynamics/env.sh && sed -i "s/EC2_REGION/${EC2_REGION}/g" /appdynamics/SeleniumDemoLoad/seleniumload.sh

# Start MachineAgent
#su - appdynamics -c "source /appdynamics/env.sh && sed -i 's/AGENT_OPTIONS -Dappdynamics.agent.uniqueHostId=/AGENT_OPTIONS -Dappdynamics.controller.hostName=${CONTROLLER} -Dappdynamics.controller.port=${APPD_PORT} -Dappdynamics.agent.uniqueHostId=/g' /appdynamics/MachineAgent/startMachineAgent.sh"
#su - appdynamics -c 'source /appdynamics/MachineAgent/startMachineAgent.sh'

# Start services
cron -f &
#su - appdynamics -c 'source /appdynamics/MachineAgent/startMachineAgent.sh'
#su - appdynamics -c '/appdynamics/SeleniumDemoLoad/seleniumload.sh start'
cd /appdynamics/SeleniumDemoLoad && ./restartSeleniumDemoLoad.sh

exit 0
