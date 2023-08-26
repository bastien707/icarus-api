from flask import Flask, jsonify, request
import ccxt

binance = ccxt.binance()
from_ts = binance.parse8601('2022-11-11 12:42:11')
ohlcv = binance.fetch_ohlcv('ETH/USD', '1m', since=from_ts, limit=1)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/ohclv', methods=["GET"])
def ohclv():
    ohlcv_data = {
        "open": ohlcv[0][1],
        "high": ohlcv[0][2],
        "low": ohlcv[0][3],
        "close": ohlcv[0][4],
        "volume": ohlcv[0][5],
        "timestamp": ohlcv[0][0] * 1000
    }
    return jsonify(ohlcv_data)
