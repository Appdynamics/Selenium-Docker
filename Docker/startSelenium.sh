#!/bin/bash

# This is a script to start Selenium on Docker

# Set variables
EC2_REGION=Oregon
UNIQUE_ID=docker
echo "${EC2_REGION} is the EC2 Region name."

# Pull images
#docker pull appdynamics/selenium:latest

# Start containers 
sudo docker run -d --name selenium -e EC2_REGION=${EC2_REGION} -e UNIQUE_ID=${UNIQUE_ID} --net=host -v /etc/localtime:/etc/localtime:ro appdynamics/selenium:latest

exit 0
