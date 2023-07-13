from flask import jsonify, Blueprint
from app.model.product import db, Product

tienda = Blueprint('tienda', __name__)

# Rutas de la API

@tienda.route('/')
def hello():
    return '¡Hola, bienvenido a la mejor tienda virtual!'