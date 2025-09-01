# Microtask: Kubernetes Microservices Demo

This repository contains two microservices deployed on Kubernetes with:

- **MySQL** for data storage
- **Kafka** for pub/sub messaging
- **Dapr** for service-to-service communication
- **Open Policy Agent (OPA)** for service communication policies
- **APISIX** as API Gateway

## Structure


## Deployment Instructions

1. Clone the repository in your Kubernetes environment:

```bash
git clone https://github.com/Damasmikee/microservice.git
cd microservices

kubectl apply -f k8s/
kubectl apply -f dapr/
kubectl apply -f opa/

kubectl get pods
kubectl get svc
