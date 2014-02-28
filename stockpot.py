from flask import Flask, render_template
import requests
import json


app = Flask(__name__)


@app.route("/")
def index():
    r = requests.get("https://api.fool.com/premium/recommendations/tmfuniverse/?apikey=J6tv7JMuX6DRTqgWbhFIR8pKEww4YV81")
    stocks = json.loads(r.content)
    print stocks
    return render_template('index.html', stocks=stocks)


@app.route("/universe")
def api():
    r = requests.get("https://api.fool.com/premium/recommendations/tmfuniverse/?apikey=J6tv7JMuX6DRTqgWbhFIR8pKEww4YV81")
    return r.content


if __name__ == "__main__":
    app.run()
