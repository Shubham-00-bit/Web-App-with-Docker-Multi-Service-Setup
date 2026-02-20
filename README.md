# Production-Grade Multi-Tier Web Application (Cloud Deployed)

This project demonstrates deployment and infrastructure skills by running a multi-service containerized web application on a cloud-based Linux instance using Docker Compose.

## Architecture Overview

- Nginx acts as a reverse proxy and single public entry point (port 8080)
- React frontend served as static files
- FastAPI backend accessible internally via `/api`
- PostgreSQL database isolated within a private Docker network
- Persistent storage handled through Docker volumes

Only Nginx is publicly exposed. Backend and database services remain internal.

## Tech Stack

- Frontend: React (Vite build)
- Backend: FastAPI (Python)
- Database: PostgreSQL 15
- Reverse Proxy: Nginx
- Containerization: Docker, Docker Compose
- Cloud Environment: Linux VM (Ubuntu)
