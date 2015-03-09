#!/bin/bash

source /appdynamics/env.sh

HOME=/appdynamics
CHROMEDRIVER_PATH=$HOME
PATH=$CHROMEDRIVER_PATH:$PATH
SELENIUM_HOME=$HOME/SeleniumDemoLoad
MACHINE_AGENT_HOME=$HOME/MachineAgent
ECOM_SELENIUM_LOG_FILE=/tmp/ecomseleniumdemoload.log
PHP_SELENIUM_LOG_FILE=/tmp/bundyseleniumdemoload.log
MOVIE_SELENIUM_LOG_FILE=/tmp/movieseleniumdemoload.log
ECOM_SELENIUM_CONFIG_FILE=$SELENIUM_HOME/config/DemoLoadEcom${EC2_REGION}.cfg
PHP_SELENIUM_CONFIG_FILE=$SELENIUM_HOME/config/DemoLoadBundy${EC2_REGION}.cfg
MOVIE_SELENIUM_CONFIG_FILE=$SELENIUM_HOME/config/DemoLoadMovie${EC2_REGION}.cfg

_moveSeleniumLog ()
{ 
echo "Moving Selenium Logs" 
rm $ECOM_SELENIUM_LOG_FILE.old
mv $ECOM_SELENIUM_LOG_FILE $ECOM_SELENIUM_LOG_FILE.old
rm $PHP_SELENIUM_LOG_FILE.old
mv $PHP_SELENIUM_LOG_FILE $PHP_SELENIUM_LOG_FILE.old
rm $MOVIE_SELENIUM_LOG_FILE.old
mv $MOVIE_SELENIUM_LOG_FILE $MOVIE_SELENIUM_LOG_FILE.old

}

_startSeleniumDemoLoad ()
{ 

which chromedriver 

echo "Starting Ecom Selenium Demo Load"
nohup python $SELENIUM_HOME/SeleniumDemoLoad.py -c $ECOM_SELENIUM_CONFIG_FILE > $ECOM_SELENIUM_LOG_FILE &

echo "Starting Movie Selenium Demo Load"
nohup python $SELENIUM_HOME/SeleniumDemoLoad.py -c $MOVIE_SELENIUM_CONFIG_FILE > $MOVIE_SELENIUM_LOG_FILE &

echo "Starting PHP Selenium Demo Load"
nohup python $SELENIUM_HOME/SeleniumDemoLoad.py -c $PHP_SELENIUM_CONFIG_FILE > $PHP_SELENIUM_LOG_FILE &

return
}

_stopSeleniumDemoLoad ()
{
echo "Stopping Selenium Demo Load" 
echo "Killing Selenium Python Script" 
echo `ps -ef | grep SeleniumDemoLoad.py | grep -v grep | awk '{print $2}'`
kill -9 `ps -ef | grep SeleniumDemoLoad.py | grep -v grep | awk '{print $2}'`
echo "Killing Phantom Processes" 
echo `ps -ef | grep phantom | grep -v grep | awk '{print $2}'`
kill -9  `ps -ef | grep phantom | grep -v grep | awk '{print $2}'`
echo "Killing Firefox Processes" 
echo `ps -ef | grep firefox | grep -v grep | awk '{print $2}'`
kill -9  `ps -ef | grep firefox | grep -v grep | awk '{print $2}'`
echo "Killing Chrome Driver Processes" 
echo `ps -ef | grep chromedriver | grep -v grep | awk '{print $2}'`
kill -9  `ps -ef | grep chromedriver | grep -v grep | awk '{print $2}'`
echo "Killing Chromium Browser Processes"
echo `ps -ef | grep chromium-browser | grep -v grep | awk '{print $2}'`
kill -9 `ps -ef | grep chromium-browser | grep -v grep | awk '{print $2}'`
echo "Killing Xvfb Processes" 
echo `ps -ef | grep Xvfb | grep -v grep | awk '{print $2}'`
kill -9  `ps -ef | grep Xvfb | grep -v grep | awk '{print $2}'`
return 
}

_cleanTmpDirectory () 
{ 
echo "Cleaning /tmp Directory" 
rm -fr /tmp/tmp*
rm -fr /tmp/server*
rm -fr /tmp/.org.chrom*
rm -fr /tmp/.X*-lock
rm -fr /tmp/restartSelenium*.zip
rm -fr /tmp/.com.google.Chrome*
}


_restartSeleniumDemoLoad ()
{
_stopSeleniumDemoLoad 
_cleanTmpDirectory
_moveSeleniumLog
_startSeleniumDemoLoad
}

################

case $1 in
    start)
        _startSeleniumDemoLoad ;;
    stop)
        _stopSeleniumDemoLoad ;;
    restart) 
        _restartSeleniumDemoLoad ;; 
    *)
        echo "usage: seleniumload.sh [start|stop|restart]" ;;
esac

exit 0
