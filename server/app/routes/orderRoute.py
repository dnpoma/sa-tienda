from flask import jsonify, Blueprint, request
from app import mongo, client
from bson import json_util, ObjectId
import json

orden = Blueprint('orden', __name__)


@orden.route('/orders', methods=['GET'])
def get_orders():
    orders = list(client.amazona.orders.find())  # Obtener todos los documentos de la colección "orders"
    ordersComplete = json.loads(json_util.dumps(orders))

    return jsonify({'orders': ordersComplete})