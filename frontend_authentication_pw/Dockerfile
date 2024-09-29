# Use Node.js 20.17 image
FROM node:20.17-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 3000 (HTTPS)
EXPOSE 3000

# Start the app with HTTPS on port 3000
CMD ["npm", "run", "dev"]
