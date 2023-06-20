
from flask import jsonify, Blueprint, request
from app.model.product import db, Product
from app.model.order_item import db, OrderItem
from app.model.order import db, Order


producto = Blueprint('producto', __name__)


@producto.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = []
    for product in products:
        result.append({
            'id': product.id,
            'name': product.name,
            'image': product.image,
            'brand': product.brand,
            'price': product.price,
            'category': product.category,
            'count_in_stock': product.count_in_stock,
            'description': product.description,
            'rating': product.rating,
            'num_reviews': product.num_reviews
        })
    return jsonify(result)


@producto.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    result = {
        'id': product.id,
        'name': product.name,
        'image': product.image,
        'brand': product.brand,
        'price': product.price,
        'category': product.category,
        'count_in_stock': product.count_in_stock,
        'description': product.description,
        'rating': product.rating,
        'num_reviews': product.num_reviews
    }
    return jsonify(result)

@producto.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(
        name=data['name'],
        image=data['image'],
        brand=data['brand'],
        price=data['price'],
        category=data['category'],
        count_in_stock=data['count_in_stock'],
        description=data['description'],
        rating=data['rating'],
        num_reviews=data['num_reviews']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product_to_dict(product)), 201


@producto.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    data = request.get_json()
    product.name = data['name']
    product.image = data['image']
    product.brand = data['brand']
    product.price = data['price']
    product.category = data['category']
    product.count_in_stock = data['count_in_stock']
    product.description = data['description']
    product.rating = data['rating']
    product.num_reviews = data['num_reviews']
    db.session.commit()
    return jsonify(product_to_dict(product))

@producto.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})

def product_to_dict(product):
    return {
        'id': product.id,
        'name': product.name,
        'image': product.image,
        'brand': product.brand,
        'price': product.price,
        'category': product.category,
        'count_in_stock': product.count_in_stock,
        'description': product.description,
        'rating': product.rating,
        'num_reviews': product.num_reviews
    }