from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from pymongo import MongoClient

db = SQLAlchemy()
mongo = PyMongo()
client = MongoClient('mongodb://sharded-mongodb-docker-mongos-router0-1:27017')



def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@172.20.10.13:5432/sa_tienda'

     # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://grupo7:grupo7@master-1:5432/sa_tienda'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zuka:zukaritas@postgresql-master:5432/sa_tienda'

    db.init_app(app)

    app.config['MONGO_URI'] = 'mongodb://sharded-mongodb-docker-mongos-router0-1:27017'
    client = MongoClient(app.config['MONGO_URI'])
    mongo.init_app(app)

    try:
    # Check if MongoDB connection is successful
      client.server_info()
      print("Connected to MongoDB successfully.")
    except Exception as e:
      print("Failed to connect to MongoDB:", str(e))


    return  app

app = create_app()
