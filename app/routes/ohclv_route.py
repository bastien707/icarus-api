from flask import Blueprint, jsonify
import ccxt

binance = ccxt.binance()
from_ts = binance.parse8601('2022-11-11 12:42:11')
ohlcv = binance.fetch_ohlcv('ETH/USD', '1m', since=from_ts, limit=1)

ohclv_bp = Blueprint('ohclv', __name__)


@ohclv_bp.route('/ohclv', methods=["GET"])
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
