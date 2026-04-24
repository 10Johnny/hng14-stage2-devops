# FIXES

## Fix 1
- File: api/.env
- Problem: A real `.env` file containing runtime configuration was committed to the repository.
- Change made: Removed the committed `.env` file and replaced it with a safe `.env.example` file.
- Why: Real environment files and secret-like values must not be stored in the repository.

## Fix 2
- File: api/main.py
- Problem: Redis host and port were hardcoded as `localhost:6379`.
- Change made: Replaced hardcoded values with environment variables.
- Why: Inside Docker, services communicate using service names, not localhost.

## Fix 3
- File: api/main.py
- Problem: Queue name was hardcoded as `job`.
- Change made: Replaced hardcoded queue name with `QUEUE_NAME` from environment variables.
- Why: Configuration should be environment-driven.

## Fix 4
- File: api/main.py
- Problem: No health endpoint existed.
- Change made: Added `GET /health`.
- Why: Health checks are needed for containers and service readiness.

## Fix 5
- File: worker/worker.py
- Problem: Redis host and port were hardcoded as `localhost:6379`.
- Change made: Replaced hardcoded values with environment variables.
- Why: This allows the worker to connect correctly in Docker Compose.

## Fix 6
- File: worker/worker.py
- Problem: Queue name was hardcoded as `job`.
- Change made: Replaced it with `QUEUE_NAME`.
- Why: Keeps configuration flexible and environment-driven.

## Fix 7
- File: worker/worker.py
- Problem: There was an unused import (`signal`).
- Change made: Removed the unused import.
- Why: Cleans up the code and avoids lint issues.

## Fix 8
- File: frontend/app.js
- Problem: API URL was hardcoded as `http://localhost:8000`.
- Change made: Replaced it with `process.env.API_URL` and a default value.
- Why: In containers, localhost points to the same container, not another service.

## Fix 9
- File: frontend/app.js
- Problem: Frontend port was hardcoded as `3000`.
- Change made: Replaced it with `process.env.FRONTEND_PORT`.
- Why: Configuration must come from environment variables.

## Fix 10
- File: frontend/app.js
- Problem: No health endpoint existed.
- Change made: Added `GET /health`.
- Why: Needed for container health checks.
## Fix 11
- File: frontend/views/index.html
- Problem: The UI assumed every `/submit` response contained `job_id`, so failed submissions displayed `Submitted: undefined`.
- Change made: Added response validation and error handling before displaying the submitted job ID.
- Why: Prevents misleading UI output and makes frontend failures visible during debugging.
## Fix 12
- File: api/Dockerfile
- Problem: The API service had no container build definition for production use.
- Change made: Added a production-ready Dockerfile with a non-root user and a health check.
- Why: Required to containerize the API safely and make it suitable for orchestration.
## Fix 13
- File: worker/Dockerfile
- Problem: The worker service had no container build definition for production use.
- Change made: Added a production-ready Dockerfile with a non-root user and a health check.
- Why: Required to containerize the worker safely and make it suitable for orchestration.
## Fix 14
- File: frontend/Dockerfile
- Problem: The frontend service had no container build definition for production use.
- Change made: Added a production-ready Dockerfile with a non-root user and a health check.
- Why: Required to containerize the frontend safely and make it suitable for orchestration.
## Fix 15
- File: api/.dockerignore
- Problem: Local virtual environment and cache files could be copied into the API image during Docker build.
- Change made: Added a `.dockerignore` file to exclude venv, cache, and local environment files.
- Why: Keeps the image clean and avoids copying unnecessary local files.

## Fix 16
- File: worker/.dockerignore
- Problem: Local virtual environment and cache files could be copied into the worker image during Docker build.
- Change made: Added a `.dockerignore` file to exclude venv, cache, and local environment files.
- Why: Keeps the image clean and avoids copying unnecessary local files.

## Fix 17
- File: frontend/.dockerignore
- Problem: Local `node_modules` and local environment files could be copied into the frontend image during Docker build.
- Change made: Added a `.dockerignore` file to exclude `node_modules`, logs, and local environment files.
- Why: Prevents bloated images and avoids copying machine-specific files.

## Fix 18
- File: docker-compose.yml
- Problem: The application had no orchestration file to run the full stack together in containers.
- Change made: Added a Docker Compose file defining frontend, API, worker, and Redis with a named network, health-based dependencies, environment-driven configuration, and resource limits.
- Why: Required to run the stack consistently and meet the Stage 2 containerization requirements.