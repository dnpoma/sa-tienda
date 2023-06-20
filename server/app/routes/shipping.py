from flask import jsonify, Blueprint, request
from app.model.shipping import db, Shipping


shipping = Blueprint('shipping', __name__)


@shipping.route('/shipping', methods=['GET'])
def get_shipping():
    shippings = Shipping.query.all()
    result = []
    for shipping in shippings:
        result.append(shipping_to_dict(shipping))
    return jsonify(result)


@shipping.route('/shipping/<int:shipping_id>', methods=['GET'])
def get_shipping_by_id(shipping_id):
    shipping = Shipping.query.get(shipping_id)
    if not shipping:
        return jsonify({'error': 'Shipping not found'}), 404
    return jsonify(shipping_to_dict(shipping))


@shipping.route('/shipping', methods=['POST'])
def create_shipping():
    data = request.get_json()
    shipping = Shipping(
        address=data['address'],
        city=data['city'],
        postal_code=data['postal_code'],
        country=data['country']
    )
    db.session.add(shipping)
    db.session.commit()
    return jsonify(shipping_to_dict(shipping)), 201


@shipping.route('/shipping/<int:shipping_id>', methods=['PUT'])
def update_shipping(shipping_id):
    shipping = Shipping.query.get(shipping_id)
    if not shipping:
        return jsonify({'error': 'Shipping not found'}), 404
    data = request.get_json()
    shipping.address = data['address']
    shipping.city = data['city']
    shipping.postal_code = data['postal_code']
    shipping.country = data['country']
    db.session.commit()
    return jsonify(shipping_to_dict(shipping))


@shipping.route('/shipping/<int:shipping_id>', methods=['DELETE'])
def delete_shipping(shipping_id):
    shipping = Shipping.query.get(shipping_id)
    if not shipping:
        return jsonify({'error': 'Shipping not found'}), 404
    db.session.delete(shipping)
    db.session.commit()
    return jsonify({'message': 'Shipping deleted'})


def shipping_to_dict(shipping):
    return {
        'id': shipping.id,
        'address': shipping.address,
        'city': shipping.city,
        'postal_code': shipping.postal_code,
        'country': shipping.country
    }