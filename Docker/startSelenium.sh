#!/bin/bash

# This is a script to start Selenium on Docker

# Set variables
EC2_REGION=Oregon
UNIQUE_ID=docker
ECOMM1=
ECOMM2=
ECOMMSTAGING=
BUNDY1=
BUNDY2=
BUNDYSTAGING=
MOVIE1=
MOVIE2=
MOVIESTAGING=
echo "${EC2_REGION} is the EC2 Region name."

# Pull images
#docker pull appdynamics/selenium:latest

# Start containers 
docker run -d --name selenium -e EC2_REGION=${EC2_REGION} -e UNIQUE_ID=${UNIQUE_ID} -e ECOMM1=${ECOMM1} -e ECOMM2=${ECOMM2} -e ECOMMSTAGING=${ECOMMSTAGING} -e BUNDY1=${BUNDY1} -e BUNDY2=${BUNDY2} -e BUNDYSTAGING=${BUNDYSTAGING} -e MOVIE1=${MOVIE1} -e MOVIE2=${MOVIE2} -e MOVIESTAGING=${MOVIESTAGING} --net=host -v /etc/localtime:/etc/localtime:ro appdynamics/selenium:latest

exit 0
