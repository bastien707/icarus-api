from flask import jsonify
import ccxt

binance = ccxt.binance()


def get_price(ticker):
    try:
        upper_ticker = ticker.upper()

        if upper_ticker not in binance.symbols:
            return jsonify({"error": "Invalid ticker"})

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
