from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from app import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(255), nullable=False)
    count_in_stock = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=0)
    num_reviews = db.Column(db.Integer, default=0)
    created_at = db.Column(db.TIMESTAMP, default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, default=db.func.now())


    reviews = db.relationship('Review', backref='product')
    # order_items = db.relationship('OrderItem', backref='product', foreign_keys='OrderItem.product_id')



    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'brand': self.brand,
            'price': self.price,
            'category': self.category,
            'count_in_stock': self.count_in_stock,
            'description': self.description,
            'rating': self.rating,
            'num_reviews': self.num_reviews
        }