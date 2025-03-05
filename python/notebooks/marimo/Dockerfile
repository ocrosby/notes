# Use the official Python image from the Docker Hub
FROM python:3.13-bullseye AS builder

# Install build dependencies and Rust toolchain
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    rustc \
    cargo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY --link requirements.txt .
RUN pip install --upgrade pip --root-user-action=ignore && \
    pip install --no-cache-dir -r requirements.txt --root-user-action=ignore && \
    rm -rf /root/.cache/pip

# Copy the rest of the application code into the container
COPY . .

# Use a smaller base image for the final stage
FROM python:3.13-alpine

# Install build dependencies and Rust toolchain in the final stage
# This is required to run the Marimo server
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    rust \
    cargo

# Set the working directory in the container
WORKDIR /app

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/usr/local/lib/python3.13/site-packages

# Ensure /usr/local/bin is in the PATH
ENV PATH=/usr/local/bin:$PATH

# Copy only the necessary files from the builder stage
COPY --from=builder /app /app

# Install marimo in the final stage
RUN pip install marimo --root-user-action=ignore

# Expose the port that Marimo will use
EXPOSE 8080

# Add a healthcheck to the container
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/health || exit 1

# Define the build argument
ARG NOTEBOOK_NAME

# Print the NOTEBOOK_NAME to verify it's being passed correctly
RUN echo "NOTEBOOK_NAME is ${NOTEBOOK_NAME}"

# Set the environment variable
# The ARG directive in the Dockerfile is only available during the build stage and not at runtime.
# To make NOTEBOOK_NAME available at runtime, you need to set it as an environment variable.
ENV NOTEBOOK_NAME=${NOTEBOOK_NAME}

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint to run marimo
ENTRYPOINT ["/entrypoint.sh"]