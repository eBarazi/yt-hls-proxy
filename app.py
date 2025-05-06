from flask import Flask, Response
import os
import requests

app = Flask(__name__)
OUTPUT_DIR = "/output"

@app.route("/<stream>.m3u8")
def proxy_m3u8(stream):
    file_path = f"{OUTPUT_DIR}/{stream}.txt"
    if not os.path.exists(file_path):
        return f"Stream '{stream}' not found or not available.", 404

    with open(file_path) as f:
        target_url = f.read().strip()

    try:
        r = requests.get(target_url, stream=True, timeout=10)
        return Response(r.iter_content(chunk_size=4096), content_type=r.headers.get("Content-Type"))
    except Exception as e:
        return f"Failed to proxy stream: {e}", 500