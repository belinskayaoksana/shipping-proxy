from flask import Flask, request, jsonify
import urllib.request
import urllib.parse
import json

app = Flask(__name__)

GAS_URL = "https://script.google.com/macros/s/AKfycbwNT493H-rcRoffGmWS08fjT3Qt0ehC-GJ3VCub3bNbU9ip7UMkbYuT-eYjnAZ8CuQ/exec"

@app.route("/")
def shipping():
    country = request.args.get("country", "")
    encoded = urllib.parse.quote(country)
    url = f"{GAS_URL}?country={encoded}"
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=30) as response:
        data = json.loads(response.read())
    
    return jsonify(data)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
