🚀 Production-Grade Dockerized Web Application (AWS Deployed)

This project demonstrates real-world DevOps skills by deploying a multi-service, containerized web application on AWS EC2 using Docker Compose.

The focus of this project is deployment, networking, and operations, not full-stack feature development.

🧱 Architecture Overview
Browser
   │
   │  :8080
   ▼
Nginx (Reverse Proxy)
   ├── Serves React static files
   └── /api  →  FastAPI Backend
                     │
                     ▼
               PostgreSQL Database

Only Nginx is exposed to the public

Backend and database are isolated inside a private Docker network

Database data is persisted using Docker volumes

🛠️ Tech Stack
Layer	Technology
Frontend	React (Vite, production build)
Backend	FastAPI (Python)
Database	PostgreSQL 15
Reverse Proxy	Nginx
Containerization	Docker & Docker Compose
Cloud	AWS EC2 (Ubuntu)
🎯 What This Project Proves

Docker multi-container orchestration using Docker Compose

Container-to-container communication using Docker DNS

Secure architecture (database not exposed to public network)

Reverse proxy configuration with Nginx

Handling real production issues (ports, MIME types, networking)

Deploying containerized applications on AWS EC2

⚠️ Note: The application code itself is intentionally simple. The goal is to demonstrate deployment and infrastructure skills, not UI complexity.

📁 Project Structure
Docker_Project/
├── docker-compose.yml
├── .env
│
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
│
├── nginx/
│   └── nginx.conf
│
└── volumes/
🔐 Security Design

Only port 8080 is exposed publicly

PostgreSQL runs in a private Docker network

No database ports exposed to the internet

Environment variables managed via .env file

SSH access restricted via AWS Security Groups

🚀 Deployment Steps (AWS EC2)
1️⃣ Launch EC2 Instance

Ubuntu 22.04 LTS

Open inbound port 8080 in Security Group

2️⃣ Install Docker & Compose
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo usermod -aG docker ubuntu
newgrp docker
3️⃣ Run the Application
docker compose up --build -d
4️⃣ Access Application
http://<EC2_PUBLIC_IP>:8080

🧪 Health Check

Backend health endpoint (via Nginx):

curl http://localhost:8080/api/health

Expected response:

{"status": "Backend is healthy 🚀"}

📌 Key Learnings

Rootless Docker cannot bind privileged ports (<1024)

Nginx requires proper MIME configuration for modern frontend apps

Docker service names act as internal DNS

Production deployments require debugging beyond "it works locally"
