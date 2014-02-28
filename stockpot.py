from flask import Flask
import requests
import json


app = Flask(__name__)


@app.route("/")
def hello():
    r = requests.get("https://api.fool.com/premium/recommendations/tmfuniverse/?apikey=J6tv7JMuX6DRTqgWbhFIR8pKEww4YV81")
    universe = json.loads(r.content)
    return str(universe)
    

if __name__ == "__main__":
        app.run()
