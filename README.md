# Three Tier App

A complete three-tier web application built with Flask, SQLAlchemy, and PostgreSQL.

## Features

- Multiple pages: Home, About, Contact, Add Post
- SQL Database with PostgreSQL
- Docker containerization
- CI/CD pipeline with GitHub Actions
- DevSecOps practices: Unit testing, linting, SAST with SonarQube, image scanning with Trivy
- Deployment to AWS Elastic Beanstalk

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your values
3. For local development with Docker:
   ```bash
   docker-compose up --build
   ```
4. For local development without Docker:
   ```bash
   pip install -r requirements.txt
   python run.py
   ```

## Environment Variables

- `SECRET_KEY`: Flask secret key
- `DATABASE_URL`: PostgreSQL connection string

## CI/CD

The pipeline includes:
- Linting with flake8
- Unit tests with pytest
- SAST with SonarQube
- Image scanning with Trivy
- Deployment to AWS Elastic Beanstalk

Set the following secrets in GitHub:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_ACCOUNT_ID`
- `SONAR_TOKEN`
- `SONAR_HOST_URL`