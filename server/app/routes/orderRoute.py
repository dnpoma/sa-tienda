from flask import jsonify, Blueprint, request
from app import mongo

orden = Blueprint('orden', __name__)

@orden.route('/get_order')
def get_order():
  order_id = request.args.get('64af8e6dcb796f2732d6ca2a')
  try:
        order = mongo.db['amazona.orders'].find_one({'_id': order_id})
        if order:
            return jsonify(order)
        else:
            return jsonify({'error': 'Order not found.'}), 404
  except Exception as e:
      return jsonify({'error': 'An error occurred while retrieving the order.'}), 500
