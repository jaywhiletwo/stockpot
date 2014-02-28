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
    css = "http://newsletters.fool.com/%s/css/product.css" % your_soup['service_id']
    your_picks = ['AAPL', 'MSFT', ]

    picks_in_service = collapsed_universe(service=your_soup['name'])
    pic_check = lambda x: requests.get("http://g.foolcdn.com/art/companylogos/medium/%s.png" % x)
    other_picks = filter(pic_check, picks_in_service.keys()[:5])

    return render_template('soup.html', your_picks=your_picks, other_picks=other_picks, your_soup=your_soup, css=css)


@app.route("/static/<path:filename>")
def show_static(filename):
    return send_from_directory('static', filename)


@app.route("/universe")
def api():
    return str(collapsed_universe())


def collapsed_universe(service='Pro'):
    r = requests.get("https://api.fool.com/premium/recommendations/tmfuniverse/?apikey=J6tv7JMuX6DRTqgWbhFIR8pKEww4YV81")
    uni = {}
    universe_list = sorted(json.loads(r.content), key=lambda x: x['OpenDate'], reverse=True)
    for ticker in universe_list:
        symbol = ticker.get('Symbol')
        if symbol not in uni.keys():
            if not service or service == ticker.get('Service'):
                uni[symbol] = ticker

    return uni


if __name__ == "__main__":
    app.run()
