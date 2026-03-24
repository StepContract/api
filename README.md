# StepContract Gateway API
StepContract is a gateway API that allows you to track your physical activities and provides a gamified user experience through a quest and level system.
(Currently in development, not yet deployed)

## Features
- Track and analyze your activities (runs, walks, workouts, etc.)
- Increase your game level through a gamified experience
- Complete daily and weekly quests according to your objectives
- Receive bonuses or penalties based on your quest completion

Access the public API documentation here [https://api.step-contract.fr/docs](https://api.step-contract.fr/docs)

## Context
This is a personal project that is very important to me. My objectives with StepContract are :
- Provide a service that helps users to stay motivated to practice physical activities according to their goals.
- Improve and showcase the skills I learned during my studies and my professional experience.
- Build a complete production-ready application (Infrastructure, CI/CD, Deployment, Frontend, API, Database, Testing).

## Gateway API tech stack

### Api
- Python
- FastAPI

### Database
- MariaDB
- SQLAlchemy
- Alembic
- Redis

### Infrastructure
- Docker
- Docker Compose (development environment)
- Kubernetes (planned for production)

### Production and deployment
- Rocky Linux
- Apache HTTP server (httpd)
- GitHub Actions (CI/CD)
- [Gladhost](https://gladhost.cloud/) (Reliable hosting provider) 

## Run it locally
First, clone the repository, then run :

With make :
```bash
make up
```
or manually using docker compose: 
```bash
docker compose up app
```

This will build the project using the Dockerfile and start the required services defined in the docker-compose configuration.

Then, access the API documentation at: [http://localhost:8000/docs](http://localhost:8000/docs)
