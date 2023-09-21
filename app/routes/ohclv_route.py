from flask import Blueprint, jsonify, request
import requests
import ccxt

binance = ccxt.binance()

ohclv_bp = Blueprint('ohclv', __name__)


@ohclv_bp.route('/ohclv', methods=["POST"])
# params: ticker, date
# ticker format: BTC/USDT
# date format: DD-MM-YYYY HH:MM:SS
def ohclv():
    try:
        data = request.json
        ticker = data.get('ticker')
        date = data.get('date')

        from_ts = binance.parse8601(date)
        ohlcv = binance.fetch_ohlcv(ticker, '1m', since=from_ts, limit=1)
        return jsonify(
            {
                "open": ohlcv[0][1],
                "high": ohlcv[0][2],
                "low": ohlcv[0][3],
                "close": ohlcv[0][4],
                "volume": ohlcv[0][5],
                "timestamp": ohlcv[0][0]
            }
        )
    except Exception as e:
        print(f"Error fetching ohclv: {e}")
        return jsonify(f"error: Error while fetching ohclv"), 500
