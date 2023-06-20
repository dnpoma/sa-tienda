from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from app import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items_price = db.Column(db.Float)
    tax_price = db.Column(db.Float)
    shipping_price = db.Column(db.Float)
    total_price = db.Column(db.Float)
    is_paid = db.Column(db.Boolean, default=False)
    paid_at = db.Column(db.TIMESTAMP)
    is_delivered = db.Column(db.Boolean, default=False)
    delivered_at = db.Column(db.TIMESTAMP)
    shipping_id = db.Column(db.Integer, db.ForeignKey('shipping.id'))
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'))
    created_at = db.Column(db.TIMESTAMP, default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, default=db.func.now())

    order_items = db.relationship('OrderItem', backref='order')
