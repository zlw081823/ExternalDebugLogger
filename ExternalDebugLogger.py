import serial
import sys
import time
import os
import os.path
from os import path

def main():
    # config COM port
    comPort = serial.Serial()
    comPort.baudrate = 115200
    comPort.port = "/dev/ttyUSB0"
    comPort.timeout = 1
    try:
        comPort.open()
        if comPort.isOpen():
            print("Serial communication is established")
        else:
            print("Serial communication establish failed")
            sys.exit(-1)
    except:
        print("Serial communication establish failed - exception")
        sys.exit(-1)
    
    if (path.exists("/home/pi/Documents/python_workspace/ExternalDebugLogger")):
        print("Working directory is: " + "/home/pi/Documents/python_workspace/ExternalDebugLogger")
    else:
        try:
            os.mkdir("/home/pi/Documents/python_workspace/ExternalDebugLogger")
        except:
            print("Create /home/pi/Documents/python_workspace/ExternalDebugLogger FAILED")
            sys.exit(-1)
        print("Directory created: " + "/home/pi/Documents/python_workspace/ExternalDebugLogger" )
        
    os.chdir(r"/home/pi/Documents/python_workspace/ExternalDebugLogger")
        
    fileCreationTime = time.asctime(time.localtime(time.time()))
    fileName = fileCreationTime.replace(" ", "_").replace(":", "_") + '.txt'
    print("Save log to: " + fileName)
    file = open(fileName, 'w+')
    file.close()

    specificHeaderForLogMessages = "b'\\x12"
    forever = 1
    while forever:
        response = comPort.readline()
        localtime = time.asctime(time.localtime(time.time()))
        print(response)
        if response[0:6]  == specificHeaderForLogMessages:
            file = open(fileName, 'a')
            file.write(localtime + ': ' + str(response.decode("utf-8", "ignore")) + '\n')
            file.close()
    
if __name__ == "__main__":
    main()
