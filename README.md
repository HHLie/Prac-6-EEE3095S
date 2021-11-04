# Prac 6 EEE3095S
TCP and Webserver git repo.
LXXHSI007 & VBNREE001.

## Scripts: ##
#### webserver.py ####
This script renders a html web page using the Flask library.
6 hyperlinks will be created with different functionality when clicked.
A TCP connection is made with the sensor node. With this connection, the webserver is able to communicate some function commands to the sensor node

#### tcp_server.py ####
This script, a TCP connection is made with the sensor to receive data.
This data is written into a text file called sensorlogs.txt

## Below is a sped up video of the 6 functions: ##

https://user-images.githubusercontent.com/53212860/140175941-8a39e2a1-ce3c-400b-a160-fe611245175b.mp4

## Screenshots of both Pi devices running: ##
#### Webserver. ####
![webserver_running](https://user-images.githubusercontent.com/53212860/140295539-ec29ec90-f832-4c65-bdda-873f500e6fdb.png)

#### Client. ####
![client_running](https://user-images.githubusercontent.com/53212860/140295550-53253446-6544-4c28-a949-ffcf299db6b6.png)


## Some screenshots of the functions: ##

### Download: ###
#### Click on download. ####
![image](https://user-images.githubusercontent.com/53212860/140176566-ff0551ed-cfa9-490e-b88a-2831b7cfc7e7.png)
File downloaded and opened.
![image](https://user-images.githubusercontent.com/53212860/140176688-a7fdd3d8-1e3f-4d2f-865f-8e2b7d81bd8b.png)

#### Check Logs: ####
Click on Logs_Check.
![image](https://user-images.githubusercontent.com/53212860/140177000-6c32ad18-6fac-4ec2-8d01-66cbeeec94a7.png)
Logs appear.
![image](https://user-images.githubusercontent.com/53212860/140177108-8a27fce1-1376-415b-a804-b77ce17ed5fd.png)

#### Sensor On. ####
![image](https://user-images.githubusercontent.com/53212860/140177785-249a135d-a679-472f-aa9f-c7506094cf06.png)

#### Sensor Off. ####
![image](https://user-images.githubusercontent.com/53212860/140177255-b16a733e-5704-4575-8602-c3e0f5a1b13e.png)

#### Status. ####
When sensor is on.
![image](https://user-images.githubusercontent.com/53212860/140177968-4881cab2-1d0d-4e96-909a-023d3365d0ff.png)

When sensor is off.
![image](https://user-images.githubusercontent.com/53212860/140177521-8ab7e62f-0ca0-4c05-9ab5-69db1bf59d45.png)

