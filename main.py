import streamlit as st
import pandas as pd
import base64
import os
import sys
from datetime import datetime
from streamlit_option_menu import option_menu

# Add local modules path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Local imports
from foundation_module.foundation_app import render as render_foundation
from payroll.app import render_payroll_tool
from employeedata.app.data_migration_tool import render_employee_v2

# ✅ Streamlit page config
st.set_page_config(
    page_title="DaSH Migration Plan - Optimized",
    layout="wide",
    page_icon="🚀",
    initial_sidebar_state="expanded"
)

# Hide Streamlit footer, header
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Initialize session state routing
if "page" not in st.session_state:
    st.session_state.page = "Home"
# 🔘 Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Solutions", "Launch Demo"],
        icons=["house", "wrench", "rocket"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f9fa"},
            "icon": {"color": "black", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#02ab21", "color": "white"},
        },
    )
    st.session_state.page = selected
if st.session_state.page == "Home":
    st.markdown("## 🚀 Pioneering the Future of SAP HCM Transformations")

    # 🔹 Background Banner Image
    with open("pexels-googledeepmind-17483873.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <div style="
            background-image: url('data:image/jpg;base64,{encoded_string}');
            background-size: cover;
            background-position: center;
            padding: 6rem 2rem;
            border-radius: 1.5rem;
            color: white;
            text-align: center;
            font-size: 2rem;
            font-weight: 600;">
            Your partner in SAP SuccessFactors data migration & transformation.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 🔹 Icon Grid - Benefits
    st.markdown("### ⚡ Why Quantumela?")
    cols = st.columns(3)
    cols[0].info("✅ Faster Implementation")
    cols[1].info("🔍 Accurate Mapping & Cleansing")
    cols[2].info("📦 Seamless Data Validation")

    # 🔹 SAP Services Block
    st.markdown("### 💼 Built for SAP & SuccessFactors")
    st.markdown("""
        <div style="background-color: #e1f0ff; padding: 2rem; border-radius: 12px; text-align: center;">
            <h4>💡 Services We Offer</h4>
            <ul style="text-align:left; max-width:600px; margin:auto;">
                <li>📁 Foundation Object Migration</li>
                <li>🧍 Employee Data Cleansing</li>
                <li>🧾 Payroll Mapping & Validation</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # 🔹 Solutions Overview Prompt
    st.markdown("---")
    st.markdown("### 🔍 Explore Solutions via the sidebar to view live demos.")
elif st.session_state.page == "Solutions":
    st.markdown("## 🛠️ Our Migration Solutions")

    st.markdown("Use the toggles below to explore our SAP → SuccessFactors data transformation offerings.")

    # 🔹 Data Migration Section
    with st.expander("📁 Foundation Object Migration", expanded=False):
        st.write("""
            Automate and validate your Foundation Object mapping across SAP HCM and SuccessFactors.
            Includes support for complex org structures, associations, and transformation logic.
        """)
        st.image("pexels-divinetechygirl-1181263.jpg", use_column_width=True)

    # 🔹 Employee Data Section
    with st.expander("🧍 Employee Data Cleansing", expanded=False):
        st.write("""
            Clean and transform employee master data with validation rules and fallback handling.
            Identify discrepancies, assign default values, and preview changes in real time.
        """)
        st.image("pexels-divinetechygirl-1181340.jpg", use_column_width=True)

    # 🔹 Variance Monitoring Section
    with st.expander("🧾 Variance Monitoring & Payroll Mapping", expanded=False):
        st.write("""
            Cross-check pre- and post-migration payroll data using intelligent mapping sheets.
            Detect anomalies, view statistical summaries, and export aligned reports.
        """)
        st.image("pexels-divinetechygirl-1181341.jpg", use_column_width=True)
elif st.session_state.page == "Launch Demo":
    st.markdown("## 🚀 Launch Your Migration Demo")

    st.markdown("Choose a transformation module to explore below:")

    b1, b2, b3 = st.columns(3)

    with b1:
        if st.button("📁 Foundation Objects"):
            render_foundation()
    with b2:
        if st.button("🧍 Employee Data"):
            render_employee_v2()
    with b3:
        if st.button("🧾 Payroll Mapping"):
            render_payroll_tool()
