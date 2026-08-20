import pandas as pd
from typing import Dict, Any, List

class FinOpsOptimizationPipeline:
    """
    Analyzes cloud consumption logs to identify idle compute resources and cost anomalies.
    """
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_idle_resources(self, threshold_cpu: float = 15.0) -> pd.DataFrame:
        """
        Identifies resources running below target CPU threshold costing high daily spend.
        """
        idle = self.df[self.df["cpu_utilization_pct"] < threshold_cpu]
        return idle.sort_values(by="daily_cost_usd", ascending=False)

    def get_cost_by_service(self) -> pd.DataFrame:
        return self.df.groupby("service_name")["daily_cost_usd"].sum().reset_index()

    def get_savings_estimate(self, threshold_cpu: float = 15.0) -> float:
        idle_df = self.get_idle_resources(threshold_cpu)
        # Assuming 70% rightsizing or shutdown savings
        return float(idle_df["daily_cost_usd"].sum() * 0.70 * 30)
