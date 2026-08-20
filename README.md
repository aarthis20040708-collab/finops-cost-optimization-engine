# 💰 FinOps Cloud Cost Optimization & Anomaly Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg?logo=streamlit)](https://streamlit.io)
[![SQL Models](https://img.shields.io/badge/SQL-Transformations-blue.svg)](finops_transformations/models.sql)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Automated multi-cloud billing telemetry ingestion pipeline, SQL transformation models for idle compute anomaly detection, FastAPI microservice, and Streamlit executive spend dashboard delivering up to 28% cloud cost reduction.**

---

## 📌 Executive Summary

As enterprise cloud infrastructure scales across GCP, AWS, and Azure, unmanaged compute instances, over-provisioned databases, and idle resources lead to significant cloud cost leakage.

**FinOps Cost Optimization Engine** provides an automated data pipeline to:
1. **Normalize Multi-Cloud Telemetry:** Ingests heterogeneous billing logs across Compute Engine (GCE), Spanner, BigQuery, AWS EC2, and Azure VMs.
2. **Execute SQL Transformation Models:** Identifies underutilized instances (<15% CPU utilization) and evaluates rightsizing / shutdown opportunities.
3. **Quantify Financial Impact:** Automatically calculates projected monthly and annualized savings.
4. **FastAPI Microservice & Streamlit UI:** Delivers live REST API endpoints and executive spend analytics.

---

## 🏗️ System Architecture

```mermaid
flowchart LR
    A[GCP / AWS / Azure Billing Logs] -->|Python Ingestion Engine| B[src/data_gen.py / ETL]
    B -->|Normalized Records| C[SQL Transformation Models (models.sql)]
    C -->|Idle Anomaly Rules (<15% CPU)| D[Cost Optimization Pipeline]
    D -->|REST Endpoints| E[FastAPI Microservice (api.py)]
    D -->|Executive BI Views| F[Streamlit Dashboard (app.py)]
```

---

## 🛠️ Tech Stack & Key Technologies

| Category | Technologies |
|---|---|
| **Data Pipelines & Processing** | Python 3.10+, Pandas, NumPy, ETL Pipelines |
| **SQL & Data Modeling** | SQL Transformation Views, Aggregate Cost Models, DuckDB |
| **Backend & Microservices** | FastAPI, Uvicorn, RESTful OpenAPI |
| **Frontend & Visualization** | Streamlit, Bar Charts, Metric Cards |
| **Cloud Target Environments** | Google Cloud (BigQuery/GCE), AWS EC2, Azure VMs |

---

## 🚀 Quickstart Guide

### 1. Clone Repository & Install Dependencies
```bash
git clone https://github.com/aarthis20040708-collab/finops-cost-optimization-engine.git
cd finops-cost-optimization-engine
pip install -r requirements.txt
```

### 2. Run Streamlit Spend & Optimization Dashboard
```bash
streamlit run app.py
```
Open `http://localhost:8501`.

### 3. Run FastAPI Microservice
```bash
uvicorn api:app --host 0.0.0.0 --port 8002 --reload
```
Interactive Swagger API documentation: `http://localhost:8002/docs`.

---

## 📡 API Reference

### `GET /api/v1/finops/report`
Generates comprehensive cost optimization and anomaly detection report.

#### Response (200 OK):
```json
{
  "status": "success",
  "total_resources_evaluated": 200,
  "idle_resources_count": 32,
  "monthly_savings_usd": 30307.69,
  "top_anomalies": [
    {
      "resource_id": "res_0042",
      "service_name": "Compute Engine (GCE)",
      "environment": "staging",
      "cpu_utilization_pct": 6.4,
      "daily_cost_usd": 380.50
    }
  ]
}
```

---

## 👤 Author
**Aarthi S** — AI & Data Pipelines Engineer  
* B.Tech in Artificial Intelligence & Data Science, Panimalar Engineering College  
* 📧 Email: [aarthi784197@gmail.com](mailto:aarthi784197@gmail.com)  
* 💼 LinkedIn: [linkedin.com/in/s-aarthi-](https://www.linkedin.com/in/s-aarthi-)  
* 🌐 Portfolio: [aarthis20040708-collab.github.io](https://aarthis20040708-collab.github.io/)
