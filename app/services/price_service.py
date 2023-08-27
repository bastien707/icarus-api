from flask import jsonify
import ccxt

binance = ccxt.binance()
status = binance.fetch_status()


def get_price(ticker):
    try:
        upper_ticker = ticker.upper()

        price = binance.fetch_ticker(upper_ticker)
        response = {
            "last": price['last'],
            "change": price['change'],
            "percentage": price['percentage']
        }

        return jsonify(response)
    except Exception as e:
        print(f"Error fetching price: {e}")
        return jsonify({"error": "Error while fetching price"}), 500
