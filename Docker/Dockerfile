FROM ubuntu

MAINTAINER Jeff Morgan (jeff.morgan@appdynamics.com)

################## BEGIN INSTALLATION ######################

# Update the repository sources list
RUN apt-get update

# Install Packages
RUN apt-get update
RUN apt-get -y install default-jre
RUN apt-get -y install vim
RUN apt-get -y install unzip
RUN apt-get -y install git
RUN apt-get -y install nmap
RUN apt-get -y install wget
RUN apt-get update
RUN apt-get -y install Xvfb
RUN apt-get -y install chromium-browser

# Add appdynamics user and set permissions
RUN mkdir -p /appdynamics

# Selenium
RUN git clone https://github.com/Appdynamics/Selenium-Docker.git /appdynamics/
ADD /seleniumload.sh /appdynamics/SeleniumDemoLoad/
RUN chmod 777 /appdynamics/SeleniumDemoLoad/seleniumload.sh
ADD /restartSeleniumDemoLoad.sh /appdynamics/SeleniumDemoLoad/
RUN chmod 777 /appdynamics/SeleniumDemoLoad/restartSeleniumDemoLoad.sh

# Setup Chrome driver
ADD /chromedriver_linux64.zip /appdynamics/
RUN unzip -o -d /appdynamics /appdynamics/chromedriver_linux64.zip

# Setup Python
ADD /distribute_setup.py /appdynamics/
RUN python /appdynamics/distribute_setup.py
RUN easy_install pip
RUN pip install -U selenium
RUN pip install pyvirtualdisplay
RUN pip install pygeoip

# Install Machine Agent
#ADD /MachineAgent.zip /appdynamics/
#RUN mkdir /appdynamics/MachineAgent
#RUN unzip -o -d /appdynamics/MachineAgent /appdynamics/MachineAgent.zip
#ADD /startMachineAgent.sh /appdynamics/MachineAgent/
#RUN chmod 777 /appdynamics/MachineAgent/startMachineAgent.sh
#ADD /killMachineAgent.sh /appdynamics/MachineAgent/
#RUN chmod 777 /appdynamics/MachineAgent/killMachineAgent.sh

# Setup Cron stuff
ADD /cron.conf /appdynamics/
RUN crontab /appdynamics/cron.conf

# Add startup script
ADD /startup.sh /appdynamics/
RUN chmod 777 /appdynamics/startup.sh
ADD /env.sh /appdynamics/
RUN chmod 777 /appdynamics/env.sh

##################### INSTALLATION END #####################

CMD /appdynamics/startup.sh && tail -F /var/log/dmesg
