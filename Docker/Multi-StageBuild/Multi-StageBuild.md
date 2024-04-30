# Docker Multi-StageBuild

## Problem Description

From https://github.com/moabukar/tech-vault/tree/main/devops-challenges#9-docker-multi-stage-build-exercise

### Context
You're a DevOps engineer working on a Node.js application. Your company is keen on optimising Docker images for production use.

### Objective
Create a Dockerfile that accomplishes the following:

1. Utilizes multi-stage builds for development and production.
2. In the first stage, named `builder`, use a Node.js image to install all dependencies and build the application. Assume that the build command is `npm run build`.
3. In the second stage, named `production`, use a smaller base image like `node:alpine` to set up the production environment. Copy only the essential files and folders from the `builder` stage.
4. Ensure that the production stage runs as a non-root user for added security.
5. Expose port `3000` for the application.
6. Make sure that the application starts with the command `npm start`.

### Constraints
- Your Dockerfile should be optimized for size and security.
- You can assume that a `.dockerignore` file is already set up to exclude unnecessary files.

### Bonus
- Include health checks in your Dockerfile.
- Use BuildKit features for added optimization, if you're familiar with them.

## Solving the Problem

Creating a "Hello World" nodejs image would be very simple to do. However, the goal of this exercise is to do it with a multi-stage build.

For a multi-stage build, I will start with a 'building' phase using a heavier node base image, and then switch for a lighter image in the 'production' phase.

This will also have a simple healthcheck that makes a HTTP request to the running server every 30s to check if it is accessible.

Note that none of this was actually tested, what's important is the concept itself and not that the solution is 100% right.

Dockerfile:

```dockerfile
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
```

