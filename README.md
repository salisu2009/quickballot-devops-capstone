\# QuickBallot â€” DevOps Capstone



QuickBallot is a containerized voting application built to demonstrate practical DevOps skills using Docker, FastAPI, and PostgreSQL.



\## Project Overview



Users can vote for AWS, Docker, or Kubernetes. The FastAPI backend records votes in PostgreSQL and provides an endpoint for retrieving the results.



\## Architecture



```text

Browser (HTML, CSS, JavaScript)

&#x20;         |

&#x20;         v

Frontend (localhost:5500)

&#x20;         |

&#x20;         v

FastAPI Backend (localhost:8000)

&#x20;         |

&#x20;         v

PostgreSQL Database (localhost:5432)

```



\## Technologies



\- Python

\- FastAPI

\- PostgreSQL 17

\- Docker

\- Docker Compose

\- HTML, CSS, and JavaScript

\- PowerShell

\- Visual Studio Code



\## Features



\- Submit votes for three technology options.

\- Store votes in PostgreSQL.

\- Retrieve current vote totals.

\- Check API health.

\- Run the backend and database in Docker containers.



\## Project Structure



```text

quickballot-devops-capstone/

â”œâ”€â”€ database/

â”‚   â”œâ”€â”€ docker-compose.yml

â”‚   â””â”€â”€ init.sql

â”œâ”€â”€ results-api/

â”‚   â”œâ”€â”€ app/

â”‚   â”‚   â””â”€â”€ main.py

â”‚   â”œâ”€â”€ Dockerfile

â”‚   â””â”€â”€ requirements.txt

â”œâ”€â”€ frontend/

â”‚   â””â”€â”€ index.html

â”œâ”€â”€ docker-compose.yml

â”œâ”€â”€ .env.example

â”œâ”€â”€ .gitignore

â””â”€â”€ README.md

```



\## Prerequisites



\- Docker Desktop

\- Python 3

\- Git

\- Visual Studio Code



\## Run Locally



Start Docker Desktop, then run these commands from the project root:



```powershell

docker compose up -d --build

```



Start the frontend in a separate terminal:



```powershell

py -m http.server 5500 --directory frontend

```



Open the application at:



http://localhost:5500



\## API Endpoints



| Method | Endpoint | Purpose |

|---|---|---|

| GET | `/` | API welcome message |

| GET | `/health` | Health check |

| POST | `/vote` | Submit a vote |

| GET | `/results` | Retrieve vote totals |



API documentation is available at:



http://localhost:8000/docs



\## Useful Docker Commands



Check container status:



```powershell

docker compose ps

```



View logs:



```powershell

docker compose logs

```



Stop the services while retaining the database volume:



```powershell

docker compose down

```



\*\*Warning:\*\* Do not use `docker compose down -v` if you need to preserve the database volume and saved votes.



\## DevOps Learning Goals



\- Containerize an application.

\- Orchestrate multiple services with Docker Compose.

\- Connect an API to a relational database.

\- Test application health and API endpoints.

\- Add automated tests and GitHub Actions CI/CD.

\- Improve container security and configuration management.



\## Author



\*\*Salisu Abubakar\*\*



GitHub: https://github.com/salisu2009



LinkedIn: https://www.linkedin.com/in/salisu-abubakar-688954381/



\## Project Status



The frontend, API, and PostgreSQL database have been tested successfully in the local Docker environment. CI/CD automation and further security improvements are planned.
