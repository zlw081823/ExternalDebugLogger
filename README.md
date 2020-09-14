# ExternalDebugLogger
This is a project runs on Raspberry Pi, and listens to the UART port and logs the received data / information in a log file.

# Prerequisite
1. In raspberry Pi, open terminal
2. $ sudo crontab -e
3. Add the following line to the file opened by previous command:
    ``@reboot python /home/pi/Documents/python_workspace/ExternalDebugLogger/ExternalDebugLogger.py >> ~/cron.log``