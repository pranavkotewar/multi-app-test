from flask import Flask, jsonify
import socket

app = Flask(__name__)

PAGE = "<html><head><meta charset='UTF-8'><title>Flask API</title><style>body{font-family:Segoe UI,Arial;background:#0b1220;color:#e2e8f0;text-align:center;padding-top:15vh}h1{color:#34d399}pre{display:inline-block;text-align:left;background:#111827;padding:14px;border-radius:8px}</style></head><body><h1>Flask API</h1><p>Deployed with the Flask template</p><pre id='out'>loading...</pre><script>fetch('api/info').then(function(r){return r.json()}).then(function(d){document.getElementById('out').textContent=JSON.stringify(d,null,2)})</script></body></html>"


@app.route("/")
def home():
    return PAGE


@app.route("/api/info")
def info():
    return jsonify({"service": "demo-api", "framework": "flask", "host": socket.gethostname()})
