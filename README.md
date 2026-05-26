# Full-Stack Football Training Tracker

A lightweight, containerized full-stack web application designed to track a 4-week football development plan. This project utilizes a decoupled client-server architecture managed entirely through Docker Compose, allowing local and local-network (mobile) interaction.

## Architecture Overview

The system consists of two core decoupled microservices running on an isolated virtual Docker bridge network:

1. **Frontend Server (`nginx:alpine`)**: Serves the user interface on port `9010`. Uses a bind mount to deliver the reactive dashboard dynamically.
2. **Backend API (`python:3.10-slim`)**: A Flask-based REST API running on port `5010` that handles data intake, parsing, and persistence.

Data is persisted dynamically via a local host bind mount, generating a `data.json` database file inside the project directory seamlessly.

## Getting Started

### Prerequisites
- Docker Desktop installed on macOS
- Git

### Installation & Deployment

1. Clone the repository to your local machine:
   ```bash
   git clone <your-github-repo-url>
   cd image_layers.dir

2. Boot the environment in detached mode using Docker Compose:
   ```Bash
   docker compose up -d

3. Open your browser and navigate to:
     Frontend Dashboard: http://localhost:9010
     Backend Health Check: http://localhost:5010/api/logs

### Multi-Device / Hotspot Networking. 
 To access the tracker from a mobile device (e.g., iPhone over Personal Hotspot):
 Retrieve your Mac's internal IP address using ipconfig getifaddr en0.
 Update the fetch() network target addresses within the frontend JavaScript block to reflect your Mac's IP.
 Access http://<your-mac-ip>:9010 via your mobile browser.

---
