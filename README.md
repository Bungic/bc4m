# My Flask API Project

## Overview

This project contains a Flask API that is containerized using Docker and deployed on a Kubernetes cluster.

## Setup Instructions

1. **Docker Setup**:
    - Build the Docker image:
      ```bash
      docker build -t my-flask-app .
      ```
    - Run the Docker container:
      ```bash
      docker run -p 5000:5000 my-flask-app
      ```

2. **Kubernetes Setup**:
    - Start Minikube:
      ```bash
      minikube start --driver=docker
      ```
    - Apply Kubernetes configurations:
      ```bash
      kubectl apply -f deployment.yaml
      kubectl apply -f service.yaml
      ```

## Configuration Files

- **Dockerfile**: Containerizes the Flask API application.
- **deployment.yaml**: Defines the deployment of the Flask application.
- **service.yaml**: Defines the service to expose the Flask application.

## Health Checks

The liveness probe checks the `/health` endpoint to ensure the application is running correctly. If the endpoint is not healthy, Kubernetes will restart the container.

## Troubleshooting

- **Error**: `ImagePullBackOff` or `ErrImagePull`
  - **Solution**: Verify the image tag and repository are correct. Ensure the image is pushed to Docker Hub.

- **Error**: Service not available
  - **Solution**: Check if the pods are running with `kubectl get pods` and if there are any errors.

