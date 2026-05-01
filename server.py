#!/usr/bin/env python3
"""
DeDollar Stock Monitor - Flask Server
Serves the single-page app. All market data is fetched
client-side from Yahoo Finance (no server API keys needed).
"""
from flask import Flask, send_from_directory, jsonify
import os, json, datetime

app = Flask(__name__, static_folder='static')

# In-memory alert store (persists while server is running)
alerts_store = []
watchlist_store = {
    "thresholds": {
        "HBLPOWER.NS":   {"drop5": True, "drop10": True, "drop15": True, "custom": 8},
        "SANDUMA.NS":    {"drop5": True, "drop10": True, "drop15": False, "custom": 12},
        "SHIVALIK.NS":   {"drop5": True, "drop10": True, "drop15": True, "custom": 10},
        "ELECONT.NS":    {"drop5": True, "drop10": False, "drop15": False, "custom": 7},
    }
}

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts_store[-50:])

@app.route('/api/alerts', methods=['POST'])
def post_alert():
    from flask import request
    data = request.get_json()
    data['timestamp'] = datetime.datetime.now().isoformat()
    alerts_store.append(data)
    return jsonify({"ok": True})

@app.route('/api/watchlist', methods=['GET'])
def get_watchlist():
    return jsonify(watchlist_store)

@app.route('/api/watchlist', methods=['POST'])
def post_watchlist():
    from flask import request
    global watchlist_store
    watchlist_store = request.get_json()
    return jsonify({"ok": True})

@app.route('/health')
def health():
    return jsonify({"status": "ok", "time": datetime.datetime.now().isoformat()})

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    print("DeDollar Stock Monitor starting on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
