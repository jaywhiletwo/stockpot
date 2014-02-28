from flask import Flask
import requests


app = Flask(__name__)


@app.route("/")
def hello():
    r = requests.get("https://api.fool.com/premium/recommendations/tmfuniverse/?apikey=J6tv7JMuX6DRTqgWbhFIR8pKEww4YV81")
    return r.content

if __name__ == "__main__":
        app.run()
