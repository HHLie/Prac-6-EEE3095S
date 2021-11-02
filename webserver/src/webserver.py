from flask import Flask, send_file, render_template
import socket
import os

#jank coding 1010
TCP_IP = '0.0.0.0'
TCP_PORT = 5050
BUFFER_SIZE = 20
web_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
web_s.bind((TCP_IP, TCP_PORT))
web_s.listen(1)
conn, addr = web_s.accept()

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/Logs_Check')
def check():
    f = open("/data/sensorlog.txt")
    g = f.readlines()
    #TODO: Add code that displays the contents of log file /data/sensorlog.txt
    print("check")
    lastlines = g[2:]
    lastlines = lastlines[-10:]
    temp = ''
    for i in range(len(lastlines)):
        temp = temp + lastlines[i]
    f.close()
    return render_template('index.html', n=temp)

@app.route('/download')
def download_file():
    print("download")
    path = "/data/sensorlog.txt"
    return send_file(path, as_attachment=True, cache_timeout=0)
    #TODO: Add code to download the file /data.sensorlog.txt



#TODO Add the remaining functions requested either by adding more pages to the template or get fancy with more templates and better formatting
@app.route('/Sensor_ON')
def sensor_on():
    conn.send(str(1).encode())
    print("sensor_on")
    return render_template('index.html')

@app.route('/Sensor_OFF')
def sensor_off():
    conn.send(str(2).encode())
    print("sensor_off")
    return render_template('index.html')

@app.route('/Status')
def status():
    conn.send(str(3).encode())
    print("status")
    #print(conn.recv(20).decode())
    stat = conn.recv(20).decode()
    temp = 'Sensor is not sampling'
    if stat == 'True':
        temp = 'Sensor is sampling'

    return render_template('index.html', n=temp)

@app.route('/Connect')
def connect():
    print('Connected by', addr)
    print("connect")
    return render_template('index.html')

@app.route('/Exit')
def exit():
    print("exit")
    return render_template('exit.html')


if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5080, debug=True) #Use this line to test basic functionality locally before trying to deploy on Pi
    app.run(host='0.0.0.0', port=80)
