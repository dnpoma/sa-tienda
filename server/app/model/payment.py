from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from app import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_method = db.Column(db.String(255), nullable=False)