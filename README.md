# BESTCLOUDFOR.ME Assignment 

## Description

This project is a Flask API application designed to run in a Kubernetes environment. It includes endpoints to check the health of the application, configured with liveness and readiness probes to make sure application is running.

## Setup and Deployment

### Prerequisites

- Minikube
- Docker
- Kubernetes CLI (`kubectl`)
- Git

### Running Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Bungic/bc4m.git
   cd bc4m
   ```
2. **Build and Run Docker Image**
  
  ```bash
  docker build -t my-flask-app:latest .
  docker run -p 5000:5000 my-flask-app:latest
  ```
3. **Access the Application**

  Open `http://localhost:5000` in your web browser or use curl to test the endpoints.

### Kubernetes Deployment

1. **Deploy to Kubernetes**

  ```bash
  kubectl apply -f deployment.yaml
  ```
2. **Expose the Service**

  ```bash
  kubectl expose deployment my-flask-app --type=LoadBalancer --port=80 --target-port=5000
  ```
3. **Access the Service**
  Use `kubectl get services` to find the external IP or port for accessing your application.

## Problem Solving and Debugging
### Issue Encountered

The application faced issues where the liveness probe failed, causing the containers to restart continuously . The `/health` endpoint was used to check the application's health status, but the application was not responding correctly, leading to constant restarts.

### Steps Taken to Resolve the Issue
1. **Identify the Problem**

  Observed frequent container restarts.
  Checked `kubectl describe pod` for details, which showed the liveness probe failing with HTTP 500 errors.
2. **Check Application Logs**

  Used `kubectl logs <pod-name>` to look at the logs from the failing containers.
  Logs indicated that the application was having errors when handling requests to the `/health` endpoint.
3. **Verify Probe Configuration**
  Confirmed the liveness and readiness probes in `deployment.yaml` were correctly configured to check the `/health` endpoint on port 5000.
  ```yaml
    livenessProbe:
      httpGet:
        path: /health
        port: 5000
      initialDelaySeconds: 30
      periodSeconds: 10

    readinessProbe:
      httpGet:
        path: /health
        port: 5000
      initialDelaySeconds: 10
      periodSeconds: 5
  ```
4. **Test `/health` Endpoint Locally**
  Ran the application locally and use `curl` to test the `/health` endpoint. Found that the endpoint was working correctly, which suggested an issue with Kubernetes configuration.

5. **Update Kubernetes Configuration**
  The issue happened because the Kubernetes deployment was using an outdated version of the API configuration, which had the `/health` endpoint set to return an unhealthy status to test restarts.
  I forgot to update the Kubernetes configuration with the new API. This caused the application to restart constantly.
  After updating the Kubernetes configuration to use the latest API changes. It resolved the issue.

### Outcome
The problem was resolved by updating the Kubernetes configuration to the latest API version. The `/health` endpoint was correctly configured, and the application no longer experienced unnecessary restarts.
