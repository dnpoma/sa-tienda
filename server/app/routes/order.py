from flask import jsonify, Blueprint, request
from app.model.order import db, Order

order = Blueprint('order', __name__)
