# QuickBallot — DevOps Capstone Project

A containerized voting application built to demonstrate DevOps fundamentals using Docker, FastAPI, and PostgreSQL.

## 📌 Project Overview

QuickBallot is a simple voting application that allows users to vote for their preferred technology: AWS, Docker, or Kubernetes. The application stores votes in a PostgreSQL database and provides an API for submitting votes and retrieving results.

This project is developed locally using Docker Desktop and is designed to evolve into a complete DevOps portfolio project with automated testing and CI/CD.

## 🏗️ Architecture

```text
             User's Browser
                    |
                    v
          Frontend (HTML, CSS, JS)
             localhost:5500
                    |
                    | HTTP Requests
                    v
             FastAPI Backend
             localhost:8000
                    |
                    | SQL Queries
                    v
             PostgreSQL Database
               localhost:5432
```

## 🛠️ Technologies Used

- **HTML, CSS, JavaScript** — Frontend
- **Python** — Backend programming language
- **FastAPI** — REST API framework
- **PostgreSQL 17** — Relational database
- **Docker** — Application containerization
- **Docker Compose** — Local multi-container orchestration
- **Docker Desktop** — Local container environment
- **PowerShell** — Windows command-line operations

## ✨ Features

- Cast votes for AWS, Docker, or Kubernetes.
- Store votes persistently in PostgreSQL.
- Retrieve voting results through a REST API.
- Check backend health using a health endpoint.
- Run the backend and database with Docker.
- Access the frontend through a local web server.

## 📂 Project Structure

```text
quickballot-devops-capstone/
│
├── database/
│   ├── docker-compose.yml
│   └── init.sql
│
├── results-api/
│   ├── app/
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── docker-compose.yml
└── README.md
```

*Note: Adjust the structure above if your actual folders or files differ.*

## 🚀 Getting Started

### Prerequisites

Install the following tools:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/quickballot-devops-capstone.git
cd quickballot-devops-capstone
```

Replace `YOUR_USERNAME` with your GitHub username after publishing the repository.

### 2. Start the Application

Ensure Docker Desktop is running, then execute:

```powershell
docker compose up -d --build
```

This starts the services defined in the root Docker Compose file.

### 3. Start the Frontend

From the project root, run:

```powershell
py -m http.server 5500 --directory frontend
```

Keep the terminal open while using the frontend.

### 4. Access the Application

| Component | URL |
|---|---|
| Voting frontend | http://localhost:5500 |
| API root | http://localhost:8000 |
| API health check | http://localhost:8000/health |
| API documentation | http://localhost:8000/docs |
| Voting results | http://localhost:8000/results |

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns the API welcome message |
| GET | `/health` | Checks API health |
| POST | `/vote` | Records a vote |
| GET | `/results` | Returns vote totals |

### Example: Submit a Vote

```http
POST /vote
Content-Type: application/json
```

Request body:

```json
{
  "option": "Docker"
}
```

Example successful response:

```json
{
  "message": "Vote recorded successfully",
  "option": "Docker"
}
```

The accepted voting options are `AWS`, `Docker`, and `Kubernetes`.

### Example: Retrieve Results

```http
GET /results
```

Example response:

```json
{
  "AWS": 4,
  "Docker": 5,
  "Kubernetes": 2
}
```

The numbers above are an example of previously observed results; actual totals change as votes are submitted.

## 🐳 Docker Commands

Check running containers:

```powershell
docker compose ps
```

View service logs:

```powershell
docker compose logs
```

View logs for the API:

```powershell
docker compose logs results-api
```

Restart services:

```powershell
docker compose restart
```

Stop services without deleting the database volume:

```powershell
docker compose down
```

**Important:** Avoid `docker compose down -v` if you want to preserve stored votes, because it can delete the database volume.

## 🧪 Testing

The following checks have been performed during local development:

- API health endpoint returns a healthy status.
- API exposes the expected endpoints.
- Voting requests can be submitted.
- PostgreSQL stores votes.
- Results endpoint returns vote totals.
- Frontend communicates with the backend successfully.

## 🔐 Security Notes

This is a learning project intended for local development.

Before deploying it publicly:

- Move database credentials into environment variables or a secrets manager.
- Avoid committing passwords, tokens, or other secrets to GitHub.
- Restrict database access to trusted services.
- Add automated tests and appropriate input validation.
- Configure production-grade networking and HTTPS.

## 🗺️ Future Improvements

- [ ] Publish the project to GitHub.
- [ ] Add automated API tests with `pytest`.
- [ ] Implement a CI/CD pipeline using GitHub Actions.
- [ ] Add container image scanning and security checks.
- [ ] Improve application configuration and secrets management.
- [ ] Add monitoring and centralized logging.
- [ ] Explore cloud deployment when the environment is available.

## 🎯 Learning Objectives

This project demonstrates practical experience with:

- Containerizing an application.
- Running multiple services with Docker Compose.
- Connecting a Python API to PostgreSQL.
- Building and testing REST API endpoints.
- Troubleshooting containers and application connectivity.
- Preparing an application for CI/CD automation.

## 👨‍💻 Author

**Salisu Abubakar**

GitHub: [salisu2009](https://github.com/salisu2009)

LinkedIn: [Salisu Abubakar](https://www.linkedin.com/in/salisu-abubakar-688954381/)

## 📄 License

This project is available for educational and portfolio purposes. Add a license file if you intend to distribute it under a specific open-source license.
