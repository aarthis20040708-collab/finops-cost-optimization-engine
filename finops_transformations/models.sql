-- FinOps Cloud Cost Transformation Models (PostgreSQL / DuckDB / BigQuery Compatible)

-- 1. Identify Idle Compute Nodes (CPU < 15% with daily spend > $50)
CREATE OR REPLACE VIEW v_idle_compute_resources AS
SELECT
    resource_id,
    service_name,
    environment,
    region,
    ROUND(AVG(cpu_utilization_pct), 2) AS avg_cpu_pct,
    ROUND(SUM(daily_cost_usd), 2) AS total_spend_30d,
    ROUND(SUM(daily_cost_usd) * 0.70, 2) AS potential_monthly_savings
FROM billing_raw_logs
WHERE cpu_utilization_pct < 15.0
GROUP BY resource_id, service_name, environment, region
ORDER BY potential_monthly_savings DESC;

-- 2. Environmental Spend Breakdown
CREATE OR REPLACE VIEW v_environment_cost_summary AS
SELECT
    environment,
    COUNT(DISTINCT resource_id) AS total_resources,
    ROUND(SUM(daily_cost_usd), 2) AS total_cost_usd,
    ROUND(AVG(cpu_utilization_pct), 2) AS avg_cluster_cpu
FROM billing_raw_logs
GROUP BY environment
ORDER BY total_cost_usd DESC;
