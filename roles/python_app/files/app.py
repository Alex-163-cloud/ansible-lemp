#!/usr/bin/env python3
"""Simple Flask app for Ansible practice."""

import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'status': 'ok',
        'app': 'python_app',
        'hostname': os.uname().nodename,
        'environment': os.environ.get('APP_ENV', 'development'),
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('APP_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
