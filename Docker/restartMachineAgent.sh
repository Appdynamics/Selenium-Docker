#!/bin/bash

LOG_FILE="/tmp/restartMachineAgent.log"
MACHINE_AGENT_HOME="$HOME/MachineAgent"

echo `date` > $LOG_FILE
echo "Restart Machine Agent" >> $LOG_FILE

echo "APP_ID = " $APP_ID >> $LOG_FILE
echo "EVENT_TIME = " $EVENT_TIME >> $LOG_FILE
echo "EVENT_ID = " $EVENT_ID >> $LOG_FILE
echo "EVENT_TYPE = " $EVENT_TYPE >> $LOG_FILE
echo "ENV_STARTUP_ARGS = " $ENV_STARTUP_ARGS >> $LOG_FILE
echo "ENV_SYSTEM_PROPERTIES = " $ENV_SYSTEM_PROPERTIES >> $LOG_FILE
echo "AFFECTED_ENTITY = " $AFFECTED_ENTITY >> $LOG_FILE

echo "Stopping Machine Agent..." >> $LOG_FILE
$MACHINE_AGENT_HOME/killMachineAgent.sh >> $LOG_FILE
echo "Starting Machine Agent..." >> $LOG_FILE
$MACHINE_AGENT_HOME/startMachineAgent.sh >> $LOG_FILE

exit 0

