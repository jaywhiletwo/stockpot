from flask import Flask, render_template, request, send_from_directory
import requests
import json


app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET', 'POST', ])
def index():
    stocks = collapsed_universe()
    return render_template('index.html', stocks=stocks)


@app.route("/soup", methods=['GET', 'POST', ])
def soup():
    picks = request.form.getlist('picks')
    return render_template('soup.html', picks=picks)


@app.route("/static/<path:filename>")
def show_static(filename):
    return send_from_directory('static', filename)


@app.route("/universe")
def api():
    return collapsed_universe()


def collapsed_universe():
    r = requests.get("https://api.fool.com/premium/recommendations/tmfuniverse/?apikey=J6tv7JMuX6DRTqgWbhFIR8pKEww4YV81")
    uni = []
    for ticker in json.loads(r.content):
        uni.append(ticker)
    return uni


if __name__ == "__main__":
    app.run()
