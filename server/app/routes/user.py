from flask import jsonify, Blueprint,request
from app.model.user import db, User


user = Blueprint('user', __name__)

@user.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user_to_dict(user))
    return jsonify(result)


@user.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user_to_dict(user))


@user.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(
        name=data['name'],
        email=data['email'],
        password=data['password'],
        is_admin=data['is_admin']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user_to_dict(user)), 201


@user.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    user.name = data['name']
    user.email = data['email']
    user.password = data['password']
    user.is_admin = data['is_admin']
    db.session.commit()
    return jsonify(user_to_dict(user))


@user.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})


def user_to_dict(user):
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'password': user.password,
        'is_admin': user.is_admin,
        'created_at': user.created_at,
        'updated_at': user.updated_at
    }
