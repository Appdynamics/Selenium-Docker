#!/bin/bash

echo "killing Selenium scripts"

echo `ps -ef | grep SeleniumDemoLoad.py | grep -v grep | awk '{print $2}'`

kill -9 `ps -ef | grep SeleniumDemoLoad.py | grep -v grep | awk '{print $2}'`

echo "killing firefox process"

echo `ps -ef | grep firefox | grep -v grep | awk '{print $2}'`

kill -9  `ps -ef | grep firefox | grep -v grep | awk '{print $2}'`

echo "Killing Chrome Processes" 

echo `ps -ef | grep chromedriver | grep -v grep | awk '{print $2}'`

kill -9  `ps -ef | grep chromedriver | grep -v grep | awk '{print $2}'`

echo "killing phantom process"

echo `ps -ef | grep phantom | grep -v grep | awk '{print $2}'`

kill -9  `ps -ef | grep phantom | grep -v grep | awk '{print $2}'`

echo "killing Xvfb process"

echo `ps -ef | grep Xvfb | grep -v grep | awk '{print $2}'`

kill -9  `ps -ef | grep Xvfb | grep -v grep | awk '{print $2}'`
