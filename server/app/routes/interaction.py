from flask import jsonify, Blueprint, request
from app import mongo, client
from bson import json_util, ObjectId
import json
from app.routes.user import getUser


interaction = Blueprint('interaction', __name__)

@interaction.route('/interactions/', methods=['GET'])
def get_interactions():
    interactions = client.sa_tienda.interactions.find()
    if interactions:
        return json_util.dumps(interactions), 200
    else:
        return jsonify(message='No interactions found'), 404

@interaction.route('/interaction/ip/<ip>', methods=['GET'])
def get_interaction_by_ip(ip):
    interaction = client.sa_tienda.interactions.find_one({'ip': ip})
    if interaction:
        return json_util.dumps(interaction), 200
    else:
        return jsonify(message='IP not found'), 404

@interaction.route('/interaction/user/<int:user_id>', methods=['GET'])
def get_interaction_by_user(user_id):
    interaction = client.sa_tienda.interactions.find_one({'user_id': user_id})
    if interaction:
        return json.loads(json_util.dumps((interaction))) 
    else:
        return jsonify(message=f'User with ID {user_id} not found'), 404
    
@interaction.route('/interaction/id/<_id>', methods=['GET'])
def get_interaction_by_id(_id):
    interaction = client.sa_tienda.interactions.find_one({'_id': ObjectId(_id)})
    if interaction:
        return json.loads(json_util.dumps(interaction))
    else:
        return jsonify(message=f'Interaction with ID {_id} not found'), 404


@interaction.route('/interaction/', methods=['POST'])
def create_interaction():
  interaction = client.sa_tienda.interactions.find_one({'_id': ObjectId(_id)})
  if interaction:
      new_products = [request.json['products']]
      client.sa_tienda.interactions.update_one(
          {'_id': ObjectId(_id)},
          {'$push': {'products': {'$each': new_products}}}
      )
      updated_interaction = client.sa_tienda.interactions.find_one({'_id': ObjectId(_id)})
      return jsonify(message="Products Added", data=json_util.dumps(updated_interaction))
  else:
      return jsonify(message='Interaction not found'), 404



@interaction.route('/interaction_user/', methods=['POST'])
def create_interaction_user():
    new_interaction = {
        'user_id': request.json['user'],
        'products': request.json['products'],
        'ip': request.json['ip']
    }
    result = client.sa_tienda.interactions.insert_one(new_interaction)
    created_order = client.sa_tienda.interactions.find_one({'_id': result.inserted_id})
    return jsonify(message="New Interaction Created", data=json_util.dumps(created_order)), 201

@interaction.route('/products_interaction/<_id>', methods=['POST'])
def add_products(_id):
    interaction = client.sa_tienda.interactions.find_one({'_id': ObjectId(_id)})
    if interaction:
        new_products = [request.json['products']]
        client.sa_tienda.interactions.update_one(
            {'_id': ObjectId(_id)},
            {'$push': {'products': {'$each': new_products}}}
        )
        updated_interaction = client.sa_tienda.interactions.find_one({'_id': ObjectId(_id)})
        return jsonify(message="Products Added", data=json_util.dumps(updated_interaction))
    else:
        return jsonify(message='Interaction not found'), 404