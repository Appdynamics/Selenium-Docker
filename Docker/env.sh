#!/bin/bash

if [ -z "${EC2_REGION}" ]; then
	export EC2_REGION="Oregon";
fi

if [ -z "${UNIQUE_ID}" ]; then
	export UNIQUE_ID="docker_selenium_node";
fi
