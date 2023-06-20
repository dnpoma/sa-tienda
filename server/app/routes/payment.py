from flask import jsonify, Blueprint, request
from app.model.payment import db, Payment

payment = Blueprint('payment', __name__)

@payment.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    result = []
    for payment in payments:
        result.append(payment_to_dict(payment))
    return jsonify(result)


@payment.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'error': 'Payment not found'}), 404
    return jsonify(payment_to_dict(payment))


@payment.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    payment = Payment(payment_method=data['payment_method'])
    db.session.add(payment)
    db.session.commit()
    return jsonify(payment_to_dict(payment)), 201


@payment.route('/payments/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'error': 'Payment not found'}), 404
    data = request.get_json()
    payment.payment_method = data['payment_method']
    db.session.commit()
    return jsonify(payment_to_dict(payment))


@payment.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'error': 'Payment not found'}), 404
    db.session.delete(payment)
    db.session.commit()
    return jsonify({'message': 'Payment deleted'})


def payment_to_dict(payment):
    return {
        'id': payment.id,
        'payment_method': payment.payment_method
    }