import streamlit as st
import pandas as pd
from datetime import datetime

# ✅ Streamlit page config
st.set_page_config(
    page_title="DaSH Migration Plan - Optimized",
    layout="wide",
    page_icon="🚀",
    initial_sidebar_state="expanded"
)

# ✅ Hide Streamlit UI clutter
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ✅ Initialize session state
if 'project_data' not in st.session_state:
    st.session_state.project_data = {
        'project_name': 'SAP HCM Migration',
        'lead_hours': 475,
        'consultant_hours': 320,
        'team_members': 3,
        'days': 60
    }

# ✅ Sidebar: Estimation Inputs
st.sidebar.header("🔧 Project Settings")
st.session_state.project_data['project_name'] = st.sidebar.text_input(
    "Project Name", st.session_state.project_data['project_name']
)
st.session_state.project_data['lead_hours'] = st.sidebar.number_input(
    "Lead Hours", value=st.session_state.project_data['lead_hours'], min_value=0
)
st.session_state.project_data['consultant_hours'] = st.sidebar.number_input(
    "Consultant Hours", value=st.session_state.project_data['consultant_hours'], min_value=0
)
st.session_state.project_data['team_members'] = st.sidebar.number_input(
    "Team Members", value=st.session_state.project_data['team_members'], min_value=1
)
st.session_state.project_data['days'] = st.sidebar.slider(
    "Project Duration (days)", min_value=30, max_value=120, value=st.session_state.project_data['days']
)

# ✅ Dummy data for timeline view (replace with real logic later)
@st.cache_data
def get_task_data():
    return pd.DataFrame({
        "Task": ["Design", "Mapping", "Validation", "Testing", "Go-Live"],
        "Estimated Hours": [50, 100, 80, 60, 30],
        "Assigned To": ["Lead", "Consultant", "QA", "QA", "All"]
    })

task_data = get_task_data()

# ✅ Tabs for planning
tabs = st.tabs(["📊 Overview", "📁 Foundation", "🧍 Employee", "🧾 Payroll", "📅 Timeline"])

# Overview Tab
with tabs[0]:
    st.header("📊 Project Overview")
    st.metric("Lead Hours", st.session_state.project_data['lead_hours'])
    st.metric("Consultant Hours", st.session_state.project_data['consultant_hours'])
    st.metric("Team Members", st.session_state.project_data['team_members'])
    st.metric("Duration (Days)", st.session_state.project_data['days'])

# Foundation Tab
with tabs[1]:
    st.header("📁 Foundation Data")
    st.dataframe(task_data)

# Employee Tab
with tabs[2]:
    st.header("🧍 Employee Data")
    st.info("Add your employee-related planning logic here.")

# Payroll Tab
with tabs[3]:
    st.header("🧾 Payroll Data")
    st.info("Add payroll planning or mappings here.")

# Timeline Tab
with tabs[4]:
    st.header("📅 Project Timeline")
    st.info("Insert Gantt chart, milestones, or planning logic here.")

# Footer
st.markdown("---")
st.markdown("Built by Quantumela · Estimation Tool")
