from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from app import db


class Product(db.Model):
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

    order_items = relationship('OrderItem', backref='product')



