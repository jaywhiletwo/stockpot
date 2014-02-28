from flask import Flask, send_from_directory, send_static_file
import requests


app = Flask(__name__)


@app.route("/universe")
def index():
    return send_static_file('index.html')


@app.route("/<path:filename>")
def send_static(filename):
    print app.static_folder
    return send_from_directory(app.static_folder, filename)


@app.route("/universe")
def api():
    r = requests.get("https://api.fool.com/premium/recommendations/tmfuniverse/?apikey=J6tv7JMuX6DRTqgWbhFIR8pKEww4YV81")
    return r.content


if __name__ == "__main__":
    app.run()
