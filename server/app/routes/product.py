
from flask import jsonify, Blueprint, request
from app.model.product import db, Product
from app.model.order_item import db, OrderItem
from app.model.order import db, Order
from app.model.review import db, Review

producto = Blueprint('producto', __name__)

@producto.route('/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    search_keyword = request.args.get('searchKeyword')
    sort_order = request.args.get('sortOrder')

    query = Product.query
    if category:
        query = query.filter_by(category=category)
    if search_keyword:
        query = query.filter(Product.name.ilike(f"%{search_keyword}%"))

    if sort_order == 'lowest':
        query = query.order_by(Product.price.asc())
    elif sort_order == 'highest':
        query = query.order_by(Product.price.desc())
    else:
        query = query.order_by(Product.id.desc())

    products = query.all()
    return jsonify([product.serialize() for product in products])

@producto.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product:
        return jsonify(product.serialize())
    else:
        return jsonify({'message': 'Product Not Found'}), 404

@producto.route('/products/<id>/reviews', methods=['POST'])
def add_review(id):
    product = collection.find_one({'_id': id})
    if product:
        review = {
            'name': request.json.get('name'),
            'rating': int(request.json.get('rating')),
            'comment': request.json.get('comment')
        }
        product['reviews'].append(review)
        product['num_reviews'] = len(product['reviews'])
        product['rating'] = sum(review['rating'] for review in product['reviews']) / len(product['reviews'])
        
        collection.update_one({'_id': id}, {'$set': product})
        
        return jsonify({
            'data': product['reviews'][-1],
            'message': 'Review saved successfully.'
        }), 201
    else:
        return jsonify({'message': 'Product Not Found'}), 404
    
    
@producto.route('/products/<int:product_id>/reviews', methods=['GET'])
def get_reviews(product_id):
    product = Product.query.get(product_id)

    if product:
        reviews = Review.query.filter_by(product_id=product_id).all()

        serialized_reviews = [review.serialize() for review in reviews]

        return jsonify(serialized_reviews), 200
    else:
        return jsonify({'message': 'Product Not Found'}), 404



@producto.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    if product:
        product.name = request.json.get('name')
        product.price = float(request.json.get('price'))
        product.image = request.json.get('image')
        product.brand = request.json.get('brand')
        product.category = request.json.get('category')
        count_in_stock = request.json.get('count_in_stock')
        product.count_in_stock = int(count_in_stock) if count_in_stock is not None else 0
        product.description = request.json.get('description')
        db.session.commit()
        return jsonify({'message': 'Product Updated', 'data': product.serialize()})
    else:
        return jsonify({'message': 'Product Not Found'}), 404


# @producto.route('/products/<int:id>', methods=['DELETE'])
# def delete_product(id):
#     product = Product.query.get(id)
#     if product:
#         db.session.delete(product)
#         db.session.commit()
#         return jsonify({'message': 'Product Deleted'})
#     else:
#         return jsonify({'message': 'Product Not Found'}), 404

@producto.route('/products', methods=['POST'])
def create_product():
    product = Product(
        name=request.json.get('name'),
        price=float(request.json.get('price', 0)),
        image=request.json.get('image'),
        brand=request.json.get('brand'),
        category=request.json.get('category'),
        count_in_stock=int(request.json.get('count_in_stock')),
        description=request.json.get('description'),
        rating=float(request.json.get('rating', 0)),
        num_reviews=int(request.json.get('num_reviews', 0))
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'New Product Created', 'data': product.serialize()}), 201



# @producto.route('/products', methods=['GET'])
# def get_products():
#     products = Product.query.all()
#     result = []
#     for product in products:
#         result.append({
#             'id': product.id,
#             'name': product.name,
#             'image': product.image,
#             'brand': product.brand,
#             'price': product.price,
#             'category': product.category,
#             'count_in_stock': product.count_in_stock,
#             'description': product.description,
#             'rating': product.rating,
#             'num_reviews': product.num_reviews
#         })
#     return jsonify(result)

# @producto.route('/products/<int:id>', methods=['GET'])
# def get_product(id):
#     product = Product.query.get(id)
#     if product:
#         return jsonify(product_to_dict(product))
#     else:
#         return jsonify({'message': 'Product Not Found.'}), 404

# @producto.route('/products/<category>', methods=['GET'])
# def get_products_by_category(category):
#     products = Product.query.filter_by(category=category).all()
#     result = []
#     for product in products:
#         result.append({
#             'id': product.id,
#             'name': product.name,
#             'image': product.image,
#             'brand': product.brand,
#             'price': product.price,
#             'category': product.category,
#             'count_in_stock': product.count_in_stock,
#             'description': product.description,
#             'rating': product.rating,
#             'num_reviews': product.num_reviews
#         })
#     return jsonify(result)



# @producto.route('/products/<int:product_id>', methods=['GET'])
# def get_product(product_id):
#     product = Product.query.get(product_id)
#     if not product:
#         return jsonify({'error': 'Product not found'}), 404
#     result = {
#         'id': product.id,
#         'name': product.name,
#         'image': product.image,
#         'brand': product.brand,
#         'price': product.price,
#         'category': product.category,
#         'count_in_stock': product.count_in_stock,
#         'description': product.description,
#         'rating': product.rating,
#         'num_reviews': product.num_reviews
#     }
#     return jsonify(result)

# @producto.route('/products', methods=['POST'])
# def create_product():
#     print(request.json)
#     name = request.json.get('name')
#     price = request.json.get('price')
#     image = request.json.get('image')
#     brand = request.json.get('brand')
#     category = request.json.get('category')
#     count_in_stock = request.json.get('count_in_stock')
#     description = request.json.get('description')
#     rating = request.json.get('rating', 0)
#     num_reviews = request.json.get('num_reviews', 0)

#     if not all([name, price, image, brand, category, count_in_stock, description]):
#         return jsonify({'message': 'Missing required fields'}), 400

#     try:
#         product = Product(
#             name=name,
#             price=float(price),
#             image=image,
#             brand=brand,
#             category=category,
#             count_in_stock=int(count_in_stock),
#             description=description,
#             rating=float(rating),
#             num_reviews=int(num_reviews)
#         )
#         db.session.add(product)
#         db.session.commit()
#         return jsonify({'message': 'New Product Created', 'data': product.serialize()}), 201
#     except (TypeError, ValueError):
#         return jsonify({'message': 'Invalid field values'}), 400


# @producto.route('/products', methods=['POST'])
# def create_product():
#     print(request.get_json())
#     data = request.get_json()
#     product = Product(
#         name=data['name'],
#         image=data['image'],
#         brand=data['brand'],
#         price=data['price'],
#         category=data['category'],
#         count_in_stock=data['count_in_stock'],
#         description=data['description'],
#         rating=data['rating'],
#         num_reviews=data['num_reviews']
#     )
#     db.session.add(product)
#     db.session.commit()
#     return jsonify({
#         'message': 'New Product Created',
#         'data': product_to_dict(product)
#     }), 201


# @producto.route('/<int:id>/reviews', methods=['POST'])
# def create_review(id):
#     product = Product.query.get(id)
#     if product:
#         review = {
#             'name': request.json['name'],
#             'rating': int(request.json['rating']),
#             'comment': request.json['comment']
#         }
#         product.reviews.append(review)
#         product.num_reviews = len(product.reviews)
#         product.rating = sum(review['rating'] for review in product.reviews) / product.num_reviews
#         db.session.commit()
#         return jsonify({
#             'data': product.reviews[-1],
#             'message': 'Review saved successfully.'
#         }), 201
#     else:
#         return jsonify({'message': 'Product Not Found'}), 404

# @producto.route('/products/<int:product_id>', methods=['PUT'])
# def update_product(product_id):
#     product = Product.query.get(product_id)
#     if not product:
#         return jsonify({'error': 'Product not found'}), 404
#     data = request.get_json()
#     product.name = data['name']
#     product.image = data['image']
#     product.brand = data['brand']
#     product.price = data['price']
#     product.category = data['category']
#     product.count_in_stock = data['count_in_stock']
#     product.description = data['description']
#     product.rating = data['rating']
#     product.num_reviews = data['num_reviews']
#     db.session.commit()
#     return jsonify({'message': 'Product Updated', 'data': product_to_dict(product)}), 200


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