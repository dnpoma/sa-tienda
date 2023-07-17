from flask import jsonify, Blueprint, request
from app import mongo, client
from bson import json_util, ObjectId
import json
from app.routes.user import getUser


orden = Blueprint('orden', __name__)



@orden.route('/orders/', methods=['GET'])
def get_orders():
    orders = client.sa_tienda.order.find()
    orders_with_user = []

    for order in orders:
        user_id = order['user']
        user = getUser(user_id)
        order['user'] = user
        orders_with_user.append(order)
    return json.loads(json_util.dumps((orders_with_user)))            

@orden.route("/orders/mine", methods=['GET'])
def get_ordens():
  orders =  client.sa_tienda.order.find({'user': request.headers.get('user_id')}) 
  return json_util.dumps(list(orders))


@orden.route('/orders/orders', methods=['GET'])
def get_order():
    order = list(client.sa_tienda.order.find())  # Obtener todos los documentos de la colección "order"
    ordersComplete = json.loads(json_util.dumps(order))

    return jsonify({'orders': ordersComplete})

@orden.route('/orders/<id>', methods=['GET'])
def get_order_by_id(id):
    order = client.sa_tienda.order.find_one({'_id': id})
    if order:
        return json_util.dumps(order)
    else:
        return "Order Not Found.", 404
  
@orden.route('/orders/<id>', methods=['DELETE'])
def delete_order(id):
    order = client.sa_tienda.order.find_one({'_id': id})
    if order:
        deleted_order = client.sa_tienda.order.delete_one({'_id': id})
        return json_util.dumps(order)
    else:
        return "Order Not Found.", 404
  
@orden.route('/orders/', methods=['POST'])
def create_order():
    new_order = {
        'orderItems': request.json['orderItems'],
        'user': request.headers.get('user_id'),
        'shipping': request.json['shipping'],
        'payment': request.json['payment'],
        'itemsPrice': request.json['itemsPrice'],
        'taxPrice': request.json['taxPrice'],
        'shippingPrice': request.json['shippingPrice'],
        'totalPrice': request.json['totalPrice']
    }
    result = client.sa_tienda.order.insert_one(new_order)
    created_order = client.sa_tienda.order.find_one({'_id': result.inserted_id})
    return jsonify(message="New Order Created", data=json_util.dumps(created_order)), 201

@orden.route('/orders/<id>/pay', methods=['PUT'])
def pay_order(id):
    order = client.sa_tienda.order.find_one({'_id': id})
    if order:
        order['isPaid'] = True
        order['paidAt'] = datetime.datetime.now()
        order['payment'] = {
            'paymentMethod': 'paypal',
            'paymentResult': {
                'payerID': request.json['payerID'],
                'orderID': request.json['orderID'],
                'paymentID': request.json['paymentID']
            }
        }
        client.sa_tienda.order.update_one({'_id': id}, {'$set': order})
        updated_order =  client.sa_tienda.order.find_one({'_id': id})
        return jsonify(message='Order Paid.', order=json_util.dumps(updated_order))
    else:
        return jsonify(message='Order not found.'), 404