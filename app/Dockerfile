// Dockerfile

# ==== CONFIGURE =====
# Use a Node 16 base image
FROM node:16-alpine 

COPY package.json ./

COPY yarn.lock ./

RUN yarn install --frozen-lockfile

# Copy app files
COPY . .

EXPOSE 3000

CMD ["npm", "start"]