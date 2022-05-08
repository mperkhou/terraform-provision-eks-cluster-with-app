from ipaddress import ip_address
from flask import Flask, render_template
import platform
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():

    # Current OS version, date, time, and IP address
    OS_type = platform.system()
    OS_version = platform.version()
    OS_output = f"{OS_type} {OS_version}"

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    date_time = datetime.now()
    vars = {
        "OS_info": OS_output,
        "ip_address": ip_address,
        "date_time": date_time
        }
    
    
    return render_template('index.html', vars = vars)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')