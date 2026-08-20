import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_gen import generate_cloud_billing_logs
from src.pipeline import FinOpsOptimizationPipeline

st.set_page_config(
    page_title="FinOps Cloud Cost Engine | AI Optimizer",
    page_icon="⚡",
    layout="wide"
)

@st.cache_data
def load_data():
    df = generate_cloud_billing_logs(300)
    return df

df = load_data()
pipeline = FinOpsOptimizationPipeline(df)

st.title("⚡ FinOps Cloud Cost Optimization & AI Anomaly Engine")
st.caption("Automated multi-cloud spend analytics, SQL transformation pipelines, and Groq-powered AI FinOps recommendations.")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Total 30-Day Spend", f"${df['daily_cost_usd'].sum():,.2f}")
with c2:
    savings = pipeline.get_savings_estimate()
    st.metric("Potential Monthly Savings", f"${savings:,.2f}", delta="-28% waste")
with c3:
    st.metric("Monitored Cloud Resources", f"{len(df)} units")

st.divider()

col_a, col_b = st.columns([1, 1])
with col_a:
    st.subheader("Spend by Cloud Service")
    service_df = pipeline.get_cost_by_service()
    st.bar_chart(service_df.set_index("service_name"))

with col_b:
    st.subheader("⚠️ Idle & Overprovisioned Compute Instances")
    idle_df = pipeline.get_idle_resources()
    st.dataframe(idle_df[["resource_id", "service_name", "environment", "cpu_utilization_pct", "daily_cost_usd"]].head(10), use_container_width=True)

st.divider()

st.subheader("🤖 Groq AI FinOps Executive Advisor")
st.write("Generates actionable remediation playbooks for engineering and finance leadership.")

if st.button("🚀 Generate AI Cost Optimization Playbook", type="primary"):
    with st.spinner("Analyzing telemetry with Groq Cloud LLM..."):
        report = pipeline.generate_cost_optimization_report()
        st.success(f"✓ Analysis Complete! Evaluated {report['total_resources_evaluated']} resources.")
        st.markdown(f"""
        <div style="background-color:#111827; border:1px solid #1f2937; border-radius:10px; padding:20px; margin-top:10px;">
            <h4 style="color:#06d6a0; margin-top:0;">📊 Executive Recommendations</h4>
            <div style="color:#f3f4f6; font-size:14px; line-height:1.7;">
                {report['ai_finops_recommendation']}
            </div>
        </div>
        """, unsafe_allow_html=True)
