from flask import Flask, jsonify
from flask_cors import CORS
import psutil

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  

@app.route('/metrics')
def get_metrics():
    cpu_usage = psutil.cpu_percent(interval=1) 
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')  
    network = psutil.net_io_counters()

    return jsonify({
        "cpu": {
            "usage": cpu_usage,
            "cores": psutil.cpu_count(logical=True)
        },
        "memory": {
            "total": round(memory.total / (1024 ** 3), 2),  
            "used": round(memory.used / (1024 ** 3), 2),
            "free": round(memory.free / (1024 ** 3), 2),
            "percent": memory.percent
        },
        "disk": {
            "total": round(disk.total / (1024 ** 3), 2),  
            "used": round(disk.used / (1024 ** 3), 2),
            "free": round(disk.free / (1024 ** 3), 2),
            "percent": disk.percent
        },
        "network": {
            "sent": round(network.bytes_sent / 1024, 2), 
            "received": round(network.bytes_recv / 1024, 2)
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False) 
