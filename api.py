from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List, Dict, Any

from src.data_gen import generate_cloud_billing_logs
from src.pipeline import FinOpsOptimizationPipeline

app = FastAPI(
    title="FinOps Cloud Cost Optimization API",
    description="Microservice providing real-time cloud cost analytics, anomaly tracking, and rightsizing recommendations.",
    version="1.0.0"
)

df = generate_cloud_billing_logs(300)
pipeline = FinOpsOptimizationPipeline(df)

@app.get("/health", tags=["Telemetry"])
async def health():
    return {"status": "healthy", "service": "FinOps-Engine-API"}

@app.get("/api/v1/costs/summary", tags=["Cost Analytics"])
async def cost_summary():
    by_service = pipeline.get_cost_by_service().to_dict(orient="records")
    estimated_savings = pipeline.get_savings_estimate()
    return {
        "total_spend_30d": round(float(df["daily_cost_usd"].sum()), 2),
        "potential_monthly_savings": round(estimated_savings, 2),
        "by_service": by_service
    }

@app.get("/api/v1/costs/idle-resources", tags=["Rightsizing"])
async def idle_resources(threshold_cpu: float = 15.0):
    idle = pipeline.get_idle_resources(threshold_cpu)
    return idle.head(20).to_dict(orient="records")

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8003, reload=True)
