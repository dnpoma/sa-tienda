## Ejecuta el siguiente comando para construir la imagen de Docker:

docker build -t flask-app .

Una vez que se haya construido la imagen, puedes ejecutar un contenedor basado en ella utilizando el siguiente comando:
docker run -p 5000:5000 flask-app

http://localhost:5000

docker-compose up -d

docker exec -it #### bash

## To

docker build -t server-app .

## In docker container terminal:

pip install flask-cors

pip install pymongo

pip install flask_pymongo

python -m pip install -U pymongo

## To postgrest

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:adminpassword@tienda-pgpool-1:5432/sa_tienda'

## To mongo

app.config['MONGO_URI'] = 'mongodb://localhost:27018/amazona'
