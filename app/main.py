from flask import Flask
from app.routes.hello_route import hello_bp
from app.routes.ohclv_route import ohclv_bp
from app.routes.price_route import price_bp

app = Flask(__name__)

app.register_blueprint(hello_bp)
app.register_blueprint(ohclv_bp)
app.register_blueprint(price_bp)
