────────────────────────────────────────────────────────────

GitHub Organization ETL Pipeline

Production-Ready Data Engineering Project

Python • PostgreSQL • SQLAlchemy • Pandas • APScheduler

────────────────────────────────────────────────────────────


# GitHub Organization ETL Pipeline

> A production-ready ETL Pipeline that extracts repositories from GitHub Organizations, transforms the data, incrementally loads it into PostgreSQL, tracks metadata, sends email notifications, and runs automatically on a schedule.

---

## Project Overview

This project demonstrates how a real-world Data Engineer builds an automated ETL pipeline.

The pipeline extracts repository data from multiple GitHub Organizations using the GitHub REST API, cleans and transforms the data with Pandas, loads only newly updated repositories into PostgreSQL using Incremental Loading, tracks the pipeline execution through a metadata table, sends execution reports via email, and runs automatically with APScheduler.

---

## Architecture

```
                  GitHub API
                       │
                       ▼
                 Extract Data
                       │
                       ▼
               Transform Data
                       │
                       ▼
            Incremental Filter
                       │
                       ▼
              Batch Load (SQLAlchemy)
                       │
                       ▼
                 PostgreSQL
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
 Metadata Tracking             Email Notification
                       │
                       ▼
                  APScheduler
```

---

## Features

- Extract repositories from multiple GitHub Organizations
- GitHub REST API Integration
- Pagination Support
- Generator-based Data Extraction
- Data Cleaning & Transformation using Pandas
- Incremental Loading
- Batch Insert using SQLAlchemy
- PostgreSQL Integration
- Metadata Tracking
- Email Notifications
- APScheduler Automation
- Logging
- Retry Decorator
- Environment Variables (.env)
- Production Project Structure

---

## Project Structure

```text
github_organization_pipeline/

│
├── decorators/
│   ├── logger.py
│   ├── retry.py
│   └── timer.py
│
├── notifications/
│   └── email_notification.py
│
├── tests/
│   └── test.py
│
├── config.py
├── extract.py
├── transform.py
├── load.py
├── metadata.py
├── notification.py
├── scheduler.py
├── init_db.py
├── main.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Transformation |
| Requests | GitHub API |
| SQLAlchemy | Database Operations |
| PostgreSQL | Data Storage |
| APScheduler | Scheduling |
| SMTP | Email Notification |
| Logging | Monitoring |
| dotenv | Configuration Management |

---

# Pipeline Workflow

1. Connect to GitHub REST API
2. Extract repositories
3. Handle Pagination
4. Transform JSON into DataFrame
5. Clean the Data
6. Apply Incremental Loading
7. Batch Insert into PostgreSQL
8. Update Metadata Table
9. Send Email Notification
10. Wait for the Next Scheduled Run

---

# Database Tables

### github_repositories

Stores all GitHub repositories.

Columns:

- repo_id
- repo_name
- owner_login
- language
- stargazers_count
- forks_count
- created_at
- updated_at
- pushed_at
- organization_login

---

### metadata_pipeline

Tracks pipeline execution.

Columns:

- pipeline_name
- last_run

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/github_organization_pipeline.git

cd github_organization_pipeline
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file using `.env.example`

```env
DATABASE_URL=

GITHUB_TOKEN=

GITHUB_ORGS=

REQUEST_TIMEOUT=

PER_PAGE=

SCHEDULE_HOUR=

SCHEDULE_MINUTE=

TIME_ZONE=

EMAIL_ADDRESS=

EMAIL_APP_PASSWORD=

EMAIL_RECEIVER=
```

---

# Running the Pipeline

Run once

```bash
python main.py
```

Run automatically

```bash
python scheduler.py
```

---

# Email Notification

The pipeline automatically sends an email after every execution.

The email contains:

- Pipeline Status
- Loaded Rows
- Execution Time
- Pipeline Message

---

# Testing

Run tests

```bash
pytest
```

---

# Future Improvements

- Docker
- Apache Airflow
- AWS Deployment
- CI/CD
- GitHub Actions
- Great Expectations
- Prometheus
- Grafana
- Data Validation
- Docker Compose

---

# Concepts Demonstrated

- ETL Pipeline
- REST APIs
- Pagination
- Python Generators
- Data Transformation
- Incremental Loading
- Metadata Tracking
- SQLAlchemy
- PostgreSQL
- Batch Insert
- Scheduler
- Email Automation
- Logging
- Retry Pattern
- Clean Code
- Project Structure

---

# Screenshots

Coming Soon

- Pipeline Running
- PostgreSQL Tables
- Email Notification
- Architecture Diagram

---

# Author

**Khaled Elsayed**

Aspiring Data Engineer

GitHub:
https://github.com/khaledalsyad

---

# If you found this project useful, don't forget to give it a star.
