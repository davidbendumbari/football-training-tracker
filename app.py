from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Allows your HTML site to talk to this API safely across your Wi-Fi

DATA_FILE = '/app/data/data.json'

# Helper to read from our "database"
def read_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Helper to write to our "database"
def write_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/api/logs', methods=['GET'])
def get_logs():
    return jsonify(read_data())

@app.route('/api/logs', methods=['POST'])
def save_log():
    new_log = request.json
    current_data = read_data()
    current_data.append(new_log)
    write_data(current_data)
    return jsonify({"status": "success", "data": new_log}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
