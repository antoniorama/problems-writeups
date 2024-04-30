# First Stage
FROM node:22 AS builder

WORKDIR /app

COPY package*.json ./

# Install the dependencies
RUN npm install

COPY . .

RUN npm run build

# Second Stage
FROM node:22-alpine AS production

WORKDIR /app

# Set a non-root user
RUN adduser -D appuser
USER appuser

# Copy necessary files from the builder stage
COPY --from=builder /app/build ./build
COPY --from=builder /app/package*.json ./

# Install only production dependencies
RUN npm install --only=production

# Expose the port the app runs on
EXPOSE 3000

# Define healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start_period=5s --retries=3 \
  CMD curl -f http://localhost:3000/ || exit 1

CMD ["npm", "start"]

