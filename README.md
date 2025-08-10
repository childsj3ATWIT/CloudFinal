# CloudFinal
Cloud Computing Final Project 2025 <br/>
Joseph Childs & Cole Fitzgerald

## INTRODUCTION
This project simulates a local cloud environment for a small online guitar shop. It models a modular microservices architecture using Docker Compose to deploy 10 independently managed containers that together provide core cloud-based features such as load balancing, database access, email communication, shared memory caching, file storage, and service authentication.
It was built to demonstrate how to deploy and connect services typically found in real-world cloud platforms, all running locally.

## DESCRIPTION
The system is built around a central Backend-for-Frontend (BFF) service written in FastAPI, which exposes RESTful endpoints to a static HTML frontend and a Python CLI client. This BFF connects to multiple cloud-native components, including:

- A relational database (MySQL)
- Shared memory cache (Redis)
- Shared file system (MinIO)
- Email server (Postfix/Mailhog)
- Identity provider (FastAPI microservice)
- Admin panel backend (FastAPI microservice)
- BFF
- Load balancer (Nginx)
- Static frontend (Nginx)
- CLI driver (Python)

## DESIGN
The architecture uses a service-oriented, layered design:

- The **frontend** (served via Nginx) provides a UI that calls the BFF to display guitars.
- The **BFF** acts as a secure gateway to backend resources, handling login, session cookies, Redis caching, file uploads, and email notifications.
- The **MySQL database** holds the guitar shop schema (products, users, orders).
- The **Admin backend** allows management of products.
- The **Identity service** verifies session tokens issued by the BFF and stores them in Redis.
- The **Redis instance** supports fast in-memory access to session data and cart caching.
- **Postfix/Mailhog** handles outbound email.
- **MinIO** provides shared file storage.
- **Nginx Load Balancer** load balances frontend/API traffic (configurable).
- The **CLI** container allows service access through Python code.

All services run on a shared Docker bridge network, and services use internal DNS (`bff`, `db`, `email`, etc.) to resolve hostnames. External-facing services (e.g., BFF, frontend, MinIO) expose ports on the host for browser or developer access.

## HOW TO RUN

### Prerequisites:
- Docker Desktop installed

### Step 1: Clone the repository
- Download the project/clone project

### Step 2: Build and launch all services
- Change Directory into the CloudProject folder using "cd CloudProject/"
- pip install -r requirements.txt
- docker compose up --build

This launches:
- FasstAPI BFF and admin backends
- MySQL database with your guitar shop schema
- Redis
- Nginx frontend
- Load balancer
- MinIO file server
- Postfix email server
- Identity provider
- CLI driver

### Step 3: Access the services
Service	URL
Frontend	http://localhost:8080
BFF API	http://localhost:8000/products
MinIO	http://localhost:9000 (minioadmin/minioadmin)
Admin API	http://localhost:8001/admin/products

The CLI service runs automatically on startup or can be run manually:
- docker compose run cli
It tests the BFF, login, Redis, MinIO, admin add, and email endpoints.

### Step 4: Shut down
- docker compose down -v

