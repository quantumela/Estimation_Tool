import streamlit as st
import pandas as pd

st.set_page_config(page_title="Estimation Tool", layout="wide")

st.title("📊 Project Estimation Tool")

st.write("This tool helps you plan and estimate project timelines, tasks, and effort.")

with st.form("estimation_form"):
    project_name = st.text_input("Project Name")
    client_name = st.text_input("Client Name")
    deadline = st.date_input("Proposed Deadline")
    estimated_hours = st.number_input("Estimated Total Hours", min_value=0.0, step=1.0)
    hourly_rate = st.number_input("Hourly Rate ($)", min_value=0.0, step=1.0)

    submitted = st.form_submit_button("Generate Estimation")

if submitted:
    total_cost = estimated_hours * hourly_rate
    st.subheader("📄 Estimation Summary")
    st.write(f"**Project:** {project_name}")
    st.write(f"**Client:** {client_name}")
    st.write(f"**Deadline:** {deadline}")
    st.write(f"**Estimated Hours:** {estimated_hours}")
    st.write(f"**Hourly Rate:** ${hourly_rate}")
    st.write(f"**Total Cost:** ${total_cost:,.2f}")
