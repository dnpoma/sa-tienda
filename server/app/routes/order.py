from flask import jsonify, Blueprint, request
from app.model.order import db, Order

order = Blueprint('order', __name__)
@order.route("/orders", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.serialize() for order in orders])

@order.route("/orders/mine", methods=["GET"])
def get_user_orders():
    user_id = request.headers.get('user_id')
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([order.serialize() for order in orders])

@order.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = Order.query.get(order_id)
    if order:
        return jsonify(order.serialize())
    else:
        return jsonify({"message": "Order Not Found."}), 404

@order.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify(order.serialize())
    else:
        return jsonify({"message": "Order Not Found."}), 404

@order.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    new_order = Order(
        user_id=data['user_id'],
        order_items=[OrderItem(**item) for item in data['orderItems']],
        shipping_address=data['shipping']['address'],
        shipping_city=data['shipping']['city'],
        shipping_postal_code=data['shipping']['postalCode'],
        shipping_country=data['shipping']['country'],
        payment_method=data['payment']['paymentMethod'],
        items_price=data['itemsPrice'],
        tax_price=data['taxPrice'],
        shipping_price=data['shippingPrice'],
        total_price=data['totalPrice']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "New Order Created", "data": new_order.serialize()}), 201

@order.route("/orders/<int:order_id>/pay", methods=["PUT"])
def pay_order(order_id):
    order = Order.query.get(order_id)
    if order:
        order.is_paid = True
        order.paid_at = datetime.utcnow()
        order.payment_method = 'paypal'
        order.payment_result = {
            'payerID': request.json['payerID'],
            'orderID': request.json['orderID'],
            'paymentID': request.json['paymentID']
        }
        db.session.commit()
        return jsonify({"message": "Order Paid.", "order": order.serialize()})
    else:
        return jsonify({"message": "Order not found."}), 404
