from flask import Flask, send_file, render_template
import socket
import os
import time

######
#TCP Setup
######
TCP_IP = '0.0.0.0' # Symbolic name meaning all available interfaces
TCP_PORT = 5050
BUFFER_SIZE = 20
web_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind web_s to the host IP and port
web_s.bind((TCP_IP, TCP_PORT))
#open the socket and listen for a connection
web_s.listen(1)
connected = False
conn, addr = web_s.accept()
######

app = Flask(__name__)

#default landing page
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

#displays the contents of log file /data/sensorlog.txt
@app.route('/Logs_Check')
def check():
    #Open file
    f = open("/data/sensorlog.txt")
    #read all the lines in the file
    g = f.readlines()
    print("check")
    #skip the first 2 lines
    lastlines = g[2:]
    #get the last ten entries, if less then ten get all of them
    lastlines = lastlines[-10:]
    temp = ''
    for i in range(len(lastlines)):
        temp = temp + lastlines[i]
    f.close()
    return render_template('index.html', text_display=temp)

#code to download the file /data.sensorlog.txt
@app.route('/download')
def download_file():
    print("download")
    path = "/data/sensorlog.txt"
    #to download the new file (not browser cached version)
    #we set cache_timeout=0
    return send_file(path, as_attachment=True, cache_timeout=0)

#turn the sensor of the node on
@app.route('/Sensor_ON')
def sensor_on():
    #send command to adc.py
    conn.send(str(1).encode())
    print("sensor_on")
    temp = "Sampling started"
    return render_template('index.html', text_display = temp)

#turn the sensor of the node off
@app.route('/Sensor_OFF')
def sensor_off():
    #send command to adc.py
    conn.send(str(2).encode())
    print("sensor_off")
    temp = "Sampling stopped"
    return render_template('index.html', text_display = temp)

#check the status of the sensor
@app.route('/Status')
def status():
    #send command to adc.py
    conn.send(str(3).encode())
    print("status")
    #wait a bit to receive a message
    time.sleep(0.5)
    #receive a command from adc.py
    stat = conn.recv(20).decode()
    print(stat)
    #configure what to display on the webpage
    temp = 'Sensor is not sampling'
    if stat == 'True':
        temp = 'Sensor is sampling'
    return render_template('index.html', text_display = temp)

#redirect the page to an exit html
@app.route('/Exit')
def exit():
    print("exit")
    return render_template('exit.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
