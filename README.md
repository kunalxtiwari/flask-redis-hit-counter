# my-incident-app
# Distributed Hit Counter: A Microservices Project
## Project Overview
This is a containerized web application designed to demonstrate **Microservices Architecture** and **Service Discovery**. 

As a Major Incident Manager transitioning to SRE, I built this to understand how application components (Web Server + Database) interact within a virtual network and how to automate their deployment using Docker Compose.

## Features
- **Python Flask:** Lightweight web framework handling the frontend logic.
- **Redis:** A high-performance, in-memory data store used for counting page hits.
- **Containerization:** Fully dockerized components for "run anywhere" consistency.
- **Infrastructure as Code (Basic):** Orchestrated via Docker Compose.

## Tech Stack
- **Language:** Python 3.9
- **Database:** Redis (Alpine)
- **DevOps Tools:** Docker, Docker Compose, Git

## Architecture

The project consists of two services:
1. `web`: The Python Flask app (built from a custom Dockerfile).
2. `redis`: The backend database (pulled from the official Redis image).

They communicate over a Docker-managed bridge network using the service name `redis` as the hostname.

## How to Run
Ensure you have **Docker** and **Docker Compose** installed, then:

1. **Clone the repo:**
   git clone <repo-link>
   cd <folder-name>
   Spin up the environment:
docker-compose up -d
Access the app: Open your browser and go to http://localhost:5000

SRE Learning Objectives
Fault Tolerance: Managed connection retries in Python to handle database startup delays.

Scalability: Understanding how to scale the 'web' service horizontally.

Observability: Monitoring container logs to debug service-to-service communication.