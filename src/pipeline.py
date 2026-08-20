import os
import json
import re
import urllib.request
import pandas as pd
from typing import Dict, Any, Optional, List

class FinOpsOptimizationPipeline:
    """
    Analyzes cloud consumption telemetry to identify idle compute resources,
    cost anomalies, and uses Groq AI to synthesize executive FinOps recommendations.
    """
    def __init__(self, df: Optional[pd.DataFrame] = None, api_key: Optional[str] = None):
        self.df = df if df is not None else pd.DataFrame()
        self.api_key = api_key or os.getenv("GROQ_API_KEY")

    def ingest_logs(self, df: pd.DataFrame):
        self.df = df

    def get_idle_resources(self, threshold_cpu: float = 15.0) -> pd.DataFrame:
        if self.df.empty:
            return pd.DataFrame()
        idle = self.df[self.df["cpu_utilization_pct"] < threshold_cpu]
        return idle.sort_values(by="daily_cost_usd", ascending=False)

    def get_cost_by_service(self) -> pd.DataFrame:
        if self.df.empty:
            return pd.DataFrame()
        return self.df.groupby("service_name")["daily_cost_usd"].sum().reset_index()

    def get_savings_estimate(self, threshold_cpu: float = 15.0) -> float:
        idle_df = self.get_idle_resources(threshold_cpu)
        if idle_df.empty:
            return 0.0
        return float(idle_df["daily_cost_usd"].sum() * 0.70 * 30)

    def get_ai_recommendation(self, idle_count: int, monthly_savings: float) -> str:
        """
        Synthesizes executive cloud cost reduction steps using Groq LLM.
        """
        if self.api_key:
            try:
                url = "https://api.groq.com/openai/v1/chat/completions"
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0"
                }
                prompt = (
                    f"You are a FinOps Cloud Optimization Expert. We detected {idle_count} idle compute resources "
                    f"resulting in an estimated potential monthly savings of ${monthly_savings:,.2f}.\n"
                    "Provide 3 concise, highly actionable FinOps recommendations for engineering leadership."
                )
                payload = {
                    "model": "qwen/qwen3.6-27b",
                    "messages": [
                        {"role": "system", "content": "You are a professional FinOps advisor. Be concise and structured."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.2
                }
                req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    raw_content = data["choices"][0]["message"]["content"]
                    clean_content = re.sub(r"<think>.*?</think>", "", raw_content, flags=re.DOTALL).strip()
                    return clean_content
            except Exception:
                pass

        return (
            f"1. Automatically snapshot and terminate the {idle_count} compute instances identified with <15% average CPU.\n"
            f"2. Right-size development and staging database instances to capture ${monthly_savings:,.2f}/mo in immediate run-rate savings.\n"
            "3. Enforce automated shutdown schedules outside business hours for non-production environments."
        )

    def generate_cost_optimization_report(self, threshold_cpu: float = 15.0) -> Dict[str, Any]:
        idle = self.get_idle_resources(threshold_cpu)
        savings = self.get_savings_estimate(threshold_cpu)
        ai_rec = self.get_ai_recommendation(len(idle), savings)
        return {
            "total_resources_evaluated": len(self.df),
            "idle_resources_count": len(idle),
            "monthly_savings_usd": round(savings, 2),
            "ai_finops_recommendation": ai_rec,
            "top_anomalies": idle.head(5).to_dict(orient="records") if not idle.empty else []
        }

FinOpsDataPipeline = FinOpsOptimizationPipeline
