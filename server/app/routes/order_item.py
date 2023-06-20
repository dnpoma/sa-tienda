from flask import jsonify, Blueprint, request
from app.model.order_item import db, OrderItem

orderItem = Blueprint('orderItem', __name__)

@orderItem.route('/order_items', methods=['GET'])
def get_order_items():
    order_items = OrderItem.query.all()
    result = []
    for order_item in order_items:
        result.append(order_item_to_dict(order_item))
    return jsonify(result)


@orderItem.route('/order_items/<int:order_item_id>', methods=['GET'])
def get_order_item(order_item_id):
    order_item = OrderItem.query.get(order_item_id)
    if not order_item:
        return jsonify({'error': 'Order item not found'}), 404
    return jsonify(order_item_to_dict(order_item))


@orderItem.route('/order_items', methods=['POST'])
def create_order_item():
    data = request.get_json()
    order_item = OrderItem(
        name=data['name'],
        qty=data['qty'],
        image=data['image'],
        price=data['price'],
        product_id=data['product_id'],
        order_id=data['order_id']
    )
    db.session.add(order_item)
    db.session.commit()
    return jsonify(order_item_to_dict(order_item)), 201


@orderItem.route('/order_items/<int:order_item_id>', methods=['PUT'])
def update_order_item(order_item_id):
    order_item = OrderItem.query.get(order_item_id)
    if not order_item:
        return jsonify({'error': 'Order item not found'}), 404
    data = request.get_json()
    order_item.name = data['name']
    order_item.qty = data['qty']
    order_item.image = data['image']
    order_item.price = data['price']
    order_item.product_id = data['product_id']
    order_item.order_id = data['order_id']
    db.session.commit()
    return jsonify(order_item_to_dict(order_item))


@orderItem.route('/order_items/<int:order_item_id>', methods=['DELETE'])
def delete_order_item(order_item_id):
    order_item = OrderItem.query.get(order_item_id)
    if not order_item:
        return jsonify({'error': 'Order item not found'}), 404
    db.session.delete(order_item)
    db.session.commit()
    return jsonify({'message': 'Order item deleted'})


# Resto de las rutas de la API...

def order_item_to_dict(order_item):
    return {
        'id': order_item.id,
        'name': order_item.name,
        'qty': order_item.qty,
        'image': order_item.image,
        'price': order_item.price,
        'product_id': order_item.product_id,
        'order_id': order_item.order_id
    }