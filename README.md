# ⚡ FinOps Cloud Cost Optimization & Anomaly Engine

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQL](https://img.shields.io/badge/SQL_Transformations-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

> An automated multi-cloud data pipeline and FastAPI microservice designed to ingest billing telemetry, execute SQL transformations, and identify idle compute resources to reduce unnecessary cloud expenditure.

---

## 🏗️ Architecture & Pipeline Flow

```mermaid
flowchart LR
    A[Cloud Billing Logs / Telemetry] --> B[Ingestion & Normalization (data_gen.py)]
    B --> C[SQL Transformation Models (models.sql)]
    C --> D[Anomaly & Idle Compute Detection Engine]
    D --> E[FastAPI Microservice (api.py)]
    E --> F[Streamlit FinOps Dashboard (app.py)]
```
