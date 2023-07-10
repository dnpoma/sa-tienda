Ejecuta el siguiente comando para construir la imagen de Docker:

docker build -t flask-app .

Una vez que se haya construido la imagen, puedes ejecutar un contenedor basado en ella utilizando el siguiente comando:
docker run -p 5000:5000 flask-app

http://localhost:5000

docker-compose up -d

docker exec -it #### bash

In docker container terminal:

pip install flask-cors
