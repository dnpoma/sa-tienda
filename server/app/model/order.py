from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from app import db

class Order(db.Model):
    __tablename__ = 'order'
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

    order_items = db.relationship('OrderItem', backref='order', primaryjoin="Order.id == OrderItem.order_id")
  
    def serialize(self):
      return {
          'id': self.id,
          'user_id': self.user_id,
          'items_price': self.items_price,
          'tax_price': self.tax_price,
          'shipping_price': self.shipping_price,
          'total_price': self.total_price,
          'is_paid': self.is_paid,
          'paid_at': self.paid_at.strftime('%Y-%m-%d %H:%M:%S') if self.paid_at else None,
          'is_delivered': self.is_delivered,
          'delivered_at': self.delivered_at.strftime('%Y-%m-%d %H:%M:%S') if self.delivered_at else None,
          'shipping_id': self.shipping_id,
          'payment_id': self.payment_id,
          'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
          'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
      }