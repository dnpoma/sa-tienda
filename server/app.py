from flask import Flask
from flask_cors import CORS
from app.routes.product import producto
from app.routes.user import user
from app.routes.shipping import shipping
from app.routes.review import review
from app.routes.payment import payment
from app.routes.orderRoute import orden     

# from app.routes.order import order
# from app.routes.order_item import orderItem

from app.route import tienda
from app import create_app

app = create_app()
CORS(app)

# Register routes
app.register_blueprint(producto)
app.register_blueprint(tienda)
app.register_blueprint(user)
app.register_blueprint(shipping)
app.register_blueprint(review)
app.register_blueprint(payment)
app.register_blueprint(orden)  

# app.register_blueprint(orderItem)
# app.register_blueprint(order)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
