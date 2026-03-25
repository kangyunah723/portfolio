import os
from flask import Flask, send_from_directory, abort

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(BASE_DIR, "intro", "public")  # ✅ 여기 핵심

app = Flask(__name__)

def serve_public(filename):
    full = os.path.join(PUBLIC_DIR, filename)
    if not os.path.isfile(full):
        abort(404, description=f"File not found: {full}")
    return send_from_directory(PUBLIC_DIR, filename)

@app.route("/ping")
def ping():
    return "pong"

@app.route("/")
def home():
    return serve_public("index.html")

@app.route("/project")
def project():
    return serve_public("project.html")

@app.route("/research")
def research():
    return serve_public("research.html")

# public 안의 css/js/img 파일들 제공
@app.route("/<path:filename>")
def static_files(filename):
    return serve_public(filename)

if __name__ == "__main__":
    print("✅ running:", __file__)
    print("✅ public dir:", PUBLIC_DIR)
    app.run(debug=True, use_reloader=False)