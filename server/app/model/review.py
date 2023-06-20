from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from app import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, default=0)
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, default=db.func.now())
