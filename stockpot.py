from flask import Flask
import requests
import json


app = Flask(__name__)


@app.route("/universe")
def api():
    r = requests.get("https://api.fool.com/premium/recommendations/tmfuniverse/?apikey=J6tv7JMuX6DRTqgWbhFIR8pKEww4YV81")
    universe = json.loads(r.content)
    return str(universe)


@app.route("/")
def index():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
