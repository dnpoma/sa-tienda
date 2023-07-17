## To start :3

follow the next steps:

npm install
npm audit fix --force
npm start

docker-compose up
docker-compose up --build

## To connect from ther computer

-> package.json
// "proxy": "http://host.docker.internal:5000",

app.config['PROXY'] = 'http://192.168.15.79:5000'
