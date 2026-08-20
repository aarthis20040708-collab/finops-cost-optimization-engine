import pandas as pd
from typing import Dict, Any, Optional

class FinOpsOptimizationPipeline:
    """
    Analyzes cloud consumption logs to identify idle compute resources and cost anomalies.
    """
    def __init__(self, df: Optional[pd.DataFrame] = None):
        self.df = df if df is not None else pd.DataFrame()

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

    def generate_cost_optimization_report(self, threshold_cpu: float = 15.0) -> Dict[str, Any]:
        idle = self.get_idle_resources(threshold_cpu)
        savings = self.get_savings_estimate(threshold_cpu)
        return {
            "total_resources_evaluated": len(self.df),
            "idle_resources_count": len(idle),
            "monthly_savings_usd": round(savings, 2),
            "top_anomalies": idle.head(5).to_dict(orient="records") if not idle.empty else []
        }

FinOpsDataPipeline = FinOpsOptimizationPipeline
