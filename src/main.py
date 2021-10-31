from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
import socket

TCP_IP = '192.168.0.116'
TCP_PORT = 50
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    #global conn, addr
    print(request.method)
    if request.method == 'POST':
        if request.form.get('ON') == 'Sensor ON':
            # pass

            print(addr)
            while 1:
                data = conn.recv(BUFFER_SIZE)
                if not data: break
                print(data)
                conn.send(data)  # echo

            print("Sensor ON")
        elif  request.form.get('OFF') == 'Sensor OFF':
            # pass # do something else
            print("Sensor OFF")
        elif  request.form.get('Status') == 'Status':
            # pass # do something else
            print("Status")
        elif  request.form.get('Check') == 'Log Check':
            # pass # do something else
            print("Check")
        elif  request.form.get('Download') == 'Log Download':
            # pass # do something else
            print("Download")
        elif  request.form.get('Exit') == 'Exit':
            # pass # do something else
            conn.close()
            print("Exit")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
