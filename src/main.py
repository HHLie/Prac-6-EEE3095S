from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    print(request.form)
    if 'Sensor ON' in request.form:
        print("on")
        pass
    if 'Sensor OFF' in request.form:
        print("off")
        pass
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
