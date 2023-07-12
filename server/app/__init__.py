from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo



db = SQLAlchemy()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@172.20.10.13:5432/sa_tienda'

     # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://grupo7:grupo7@master-1:5432/sa_tienda'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zuka:zukaritas@postgresql-master:5432/sa_tienda'

    db.init_app(app)


    app.config['MONGO_URI'] = 'mongodb://localhost:27017/amazona'

    mongo.init_app(app)

    return app


app = create_app()
