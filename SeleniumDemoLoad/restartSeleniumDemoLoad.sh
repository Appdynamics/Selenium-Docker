#!/bin/bash

LOG_FILE="/tmp/restartSeleniumDemoLoad.log"
SELENIUM_HOME="$HOME/SeleniumDemoLoad"

echo `date` > $LOG_FILE
echo "Restart Selenium Load" >> $LOG_FILE

echo "APP_ID = " $APP_ID >> $LOG_FILE
echo "EVENT_TIME = " $EVENT_TIME >> $LOG_FILE
echo "EVENT_ID = " $EVENT_ID >> $LOG_FILE
echo "EVENT_TYPE = " $EVENT_TYPE >> $LOG_FILE
echo "ENV_STARTUP_ARGS = " $ENV_STARTUP_ARGS >> $LOG_FILE
echo "ENV_SYSTEM_PROPERTIES = " $ENV_SYSTEM_PROPERTIES >> $LOG_FILE
echo "AFFECTED_ENTITY = " $AFFECTED_ENTITY >> $LOG_FILE

echo "Restarting Selenium Demo Load..." >> $LOG_FILE
$SELENIUM_HOME/seleniumload.sh restart >> $LOG_FILE

exit 0

