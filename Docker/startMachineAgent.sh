#!/bin/bash

source /appdynamics/env.sh

java -Dappdynamics.agent.uniqueHostId=\'${UNIQUE_ID}\' -jar /appdynamics/MachineAgent/machineagent.jar  &
