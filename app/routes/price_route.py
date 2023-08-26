from flask import Blueprint, jsonify
from app.services.price_service import get_price

price_bp = Blueprint('price', __name__)


@price_bp.route('/price/<path:ticker>', methods=["GET"])
def fetch_price(ticker):
    return get_price(ticker)
