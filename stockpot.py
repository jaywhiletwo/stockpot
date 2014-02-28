from flask import Flask, render_template, request, send_from_directory
import requests
import json


app = Flask(__name__)
app.debug = True


@app.route("/soup", methods=['GET', 'POST', ])
def soup():
    your_soup = {
        'name': 'Rule Breakers',
        'service_id': 1069,
    }
    your_picks = ['AAPL', 'MSFT', ]
    other_picks = ['GOOG', 'TSLA', ]
    return render_template('soup.html', your_picks=your_picks, other_picks=other_picks, your_soup=your_soup)


@app.route("/static/<path:filename>")
def show_static(filename):
    return send_from_directory('static', filename)


@app.route("/universe")
def api():
    return str(collapsed_universe())


def collapsed_universe():
    r = requests.get("https://api.fool.com/premium/recommendations/tmfuniverse/?apikey=J6tv7JMuX6DRTqgWbhFIR8pKEww4YV81")
    uni = {}
    for ticker in sorted(json.loads(r.content), key=lambda x: x['OpenDate'], reverse=True):
        symbol = ticker.get('Symbol')
        if symbol not in uni.keys():
            uni[symbol] = ticker

    return uni


if __name__ == "__main__":
    app.run()
