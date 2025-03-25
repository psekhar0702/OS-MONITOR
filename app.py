from flask import Flask, jsonify
import psutil
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/')
def home():
    return "Welcome to OS-Monitor API!"

@app.route('/cpu')
def get_cpu():
    return jsonify({'cpu_usage': psutil.cpu_percent(interval=0)})

@app.route('/memory')
def get_memory():
    mem = psutil.virtual_memory()
    return jsonify({'total': mem.total, 'used': mem.used, 'available': mem.available, 'percent': mem.percent})

@app.route('/disk')
def get_disk():
    disk = psutil.disk_usage('/')
    return jsonify({'total': disk.total, 'used': disk.used, 'free': disk.free, 'percent': disk.percent})

@app.route('/network')
def get_network():
    net = psutil.net_io_counters()
    return jsonify({
        'bytes_sent': net.bytes_sent,
        'bytes_recv': net.bytes_recv
    })

if __name__ == '__main__':
    app.run(debug=True)