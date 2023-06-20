from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from app import db

class Shipping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)