from flask import Flask, send_file, render_template
import socket


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/Logs_Check')
def check():
    #TODO: Add code that displays the contents of log file /data/sensorlog.txt
    print("check")

    return render_template('index.html')

@app.route('/download')
def download_file():
    print("download")
    path = "/data/sensorlog.txt"
    return send_file(path, as_attachment=True)
    #TODO: Add code to download the file /data.sensorlog.txt



#TODO Add the remaining functions requested either by adding more pages to the template or get fancy with more templates and better formatting
@app.route('/Sensor_ON')
def sensor_on():
    #TODO: Add code that displays the contents of log file /data/sensorlog.txt
    print("sensor_on")
    return render_template('index.html')

@app.route('/Sensor_OFF')
def sensor_off():
    #TODO: Add code that displays the contents of log file /data/sensorlog.txt
    print("sensor_off")
    return render_template('index.html')

@app.route('/Status')
def status():
    #TODO: Add code that displays the contents of log file /data/sensorlog.txt
    print("status")
    return render_template('index.html')

@app.route('/Exit')
def exit():
    #TODO: Add code that displays the contents of log file /data/sensorlog.txt
    print("exit")
    return render_template('exit.html')


if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5080, debug=True) #Use this line to test basic functionality locally before trying to deploy on Pi
    app.run(host='0.0.0.0', port=80)
