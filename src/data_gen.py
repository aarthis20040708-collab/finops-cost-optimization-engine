import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_cloud_billing_logs(num_records: int = 200) -> pd.DataFrame:
    """
    Generates synthetic cloud billing logs with compute, storage, and database instances.
    """
    services = ["Compute Engine (GCE)", "Cloud Spanner", "AWS EC2", "Azure VM", "Cloud Storage (GCS)", "BigQuery"]
    environments = ["production", "staging", "dev"]
    regions = ["us-central1", "asia-south1", "us-east-1", "europe-west1"]
    
    np.random.seed(42)
    dates = [datetime.today() - timedelta(days=int(d)) for d in np.random.randint(0, 30, num_records)]
    
    data = {
        "resource_id": [f"res_{i:04d}" for i in range(num_records)],
        "service_name": np.random.choice(services, num_records),
        "environment": np.random.choice(environments, num_records, p=[0.5, 0.3, 0.2]),
        "region": np.random.choice(regions, num_records),
        "cpu_utilization_pct": np.random.uniform(5.0, 95.0, num_records),
        "daily_cost_usd": np.random.uniform(10.0, 450.0, num_records),
        "usage_date": dates
    }
    return pd.DataFrame(data)
