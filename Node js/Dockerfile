# 1) Use Node.js (this is like getting the engine to run the app)
FROM node:20-alpine

# 2) Go inside a folder inside the container
WORKDIR /app

# 3) Copy package.json first (so we can install packages)
COPY package*.json ./

# 4) Install packages listed in package.json
RUN npm install

# 5) Now copy the rest of the app code
COPY . .

# 6) Tell which port the app uses
EXPOSE 3000

# 7) Start the app
CMD ["npm", "start"]
