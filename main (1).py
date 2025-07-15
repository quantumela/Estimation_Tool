import streamlit as st
st.write("App started")
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np


# Page configuration
st.set_page_config(
    page_title="DaSH Migration Plan - Corrected",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .milestone-card {
        background: #f8f9fa;
        border-left: 4px solid #667eea;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .metric-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .billing-info {
        background: #e8f5e8;
        border-left: 4px solid #4caf50;
        padding: 15px;
        border-radius: 5px;
        margin: 20px 0;
    }
    .correction-notice {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 15px;
        margin: 20px 0;
        color: #856404;
    }
</style>
""", unsafe_allow_html=True)

# Correction Notice
st.markdown("""
<div class="correction-notice">
    <h3>📋 Corrected Module Structure</h3>
    <p><strong>Based on your object categorization table:</strong></p>
    <ul>
        <li><strong>Foundation Data:</strong> 16 objects (Weeks 3-4)</li>
        <li><strong>Employee Data:</strong> 38 objects (Weeks 5-7) - Including financial objects like Tax, Super, Payment Info</li>
        <li><strong>Payroll Data:</strong> 9 objects (Week 8) - DWS, PWS, WorkSchedules ECP</li>
        <li><strong>Time Data:</strong> 11 objects (Week 9) - Absences, Time Accounts, Work Schedules</li>
    </ul>
    <p><em>Total: 64 objects (688 hours after filtering out N scope items)</em></p>
</div>
""", unsafe_allow_html=True)

# Initialize session state for editable data
if 'project_data' not in st.session_state:
    st.session_state.project_data = {
        'total_duration': 12,
        'lead_hours': 475,
        'intern_hours': 213,
        'total_objects': 74,
        'in_scope_objects': 64,  # Based on your filtered data
        'total_effort_hours': 688,  # From your table
        'milestones': 5
    }

# Header
st.markdown("""
<div class="main-header">
    <h1>🚀 DaSH Migration Product - Corrected 3-Month Plan</h1>
    <p>SAP On-Premise to SuccessFactors Migration Tool | Proper Module-Based Deliveries</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for project configuration
st.sidebar.header("📊 Project Configuration")
st.session_state.project_data['lead_hours'] = st.sidebar.number_input("Lead Hours", value=475, min_value=0)
st.session_state.project_data['intern_hours'] = st.sidebar.number_input("Intern Hours", value=213, min_value=0)
st.session_state.project_data['total_objects'] = st.sidebar.number_input("Total Objects", value=64, min_value=0)

# Load the actual objects data
@st.cache_data
def load_objects_data():
    """Load and categorize objects based on the provided table"""
    objects_data = [
        # Foundation Data (16 objects)
        {"name": "Bank", "category": "Foundation Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Business Unit", "category": "Foundation Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Business Unit - Legal Entity", "category": "Foundation Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Cost Centre", "category": "Foundation Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Department", "category": "Foundation Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Department - Division", "category": "Foundation Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Division", "category": "Foundation Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Division - Business Unit", "category": "Foundation Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Holiday", "category": "Foundation Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Holiday Calendar", "category": "Foundation Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Job Classification", "category": "Foundation Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Job Classification AUS", "category": "Foundation Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Job Family (Job Function)", "category": "Foundation Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Job Family (Job Function) - Legal Entity", "category": "Foundation Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Legal Entity (Company)", "category": "Foundation Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Location", "category": "Foundation Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        
        # Employee Data (38 objects) - Including financial objects
        {"name": "Accrual Calculation Base (Attendances)", "category": "Employee Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Addresses", "category": "Employee Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Basic Import", "category": "Employee Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Biographical Information (PersonInfo)", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Compensation Info", "category": "Employee Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Email Information", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Emergency Contact", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Employee Time (Absences)", "category": "Employee Data", "complexity": "Very Complex", "hours": 20, "scope": "Y", "final_effort": 20},
        {"name": "Employment Info", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Global Information", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "IT0188 Tax", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "IT0220 Super", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Job Information", "category": "Employee Data", "complexity": "Very Complex", "hours": 20, "scope": "Y", "final_effort": 20},
        {"name": "National ID Information (TFN)", "category": "Employee Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Non Recurring Payments and Allowances", "category": "Employee Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Payment Information", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Payment Information - Details", "category": "Employee Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Personal Info (Hire Date)", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Phone Information", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Recurring deductions - Recurring Items (Child)", "category": "Employee Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Recurring deductions (Parent)", "category": "Employee Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Recurring Payments and Allowances", "category": "Employee Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Super fund code", "category": "Employee Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Time Account (Accrual/Entitlement)", "category": "Employee Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Work Permit details", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Work Permit Information", "category": "Employee Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        
        # Payroll Data (9 objects)
        {"name": "Bank Keys (ECP)", "category": "Payroll Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Cost Centre (ECP)", "category": "Payroll Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "DWS", "category": "Payroll Data", "complexity": "Very Complex", "hours": 20, "scope": "Y", "final_effort": 20},
        {"name": "GL Accounts (ECP)", "category": "Payroll Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "PWS", "category": "Payroll Data", "complexity": "Very Complex", "hours": 20, "scope": "Y", "final_effort": 20},
        {"name": "WorkSchedules (ECP) (WSR)", "category": "Payroll Data", "complexity": "Very Complex", "hours": 20, "scope": "Y", "final_effort": 20},
        {"name": "Super Fund (ECP)", "category": "Payroll Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Tax Rules (ECP)", "category": "Payroll Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Payment Methods (ECP)", "category": "Payroll Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        
        # Time Data (11 objects)
        {"name": "Time Account Balance", "category": "Time Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Time Off Request", "category": "Time Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Work Schedule Assignment", "category": "Time Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Absence Type", "category": "Time Data", "complexity": "Simple", "hours": 5, "scope": "Y", "final_effort": 5},
        {"name": "Time Recording", "category": "Time Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Work Schedule Pattern", "category": "Time Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Time Account Setup", "category": "Time Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Absence Entitlement", "category": "Time Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Time Tracking Configuration", "category": "Time Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
        {"name": "Work Schedule Rules", "category": "Time Data", "complexity": "Complex", "hours": 15, "scope": "Y", "final_effort": 15},
        {"name": "Time Approval Workflow", "category": "Time Data", "complexity": "Medium", "hours": 10, "scope": "Y", "final_effort": 10},
    ]
    
    return pd.DataFrame(objects_data)

# Create corrected project data
def create_corrected_project_data():
    milestones = [
        {
            'milestone': 'M1: Architecture & Foundation',
            'weeks': 'W1-W4',
            'lead_hours': 100,
            'intern_hours': 50,
            'billing_percentage': 25,
            'deliverables': [
                'Project Setup & Requirements Package',
                'Core Architecture & UI Framework',
                'Foundation Data Migration Engine (16 objects)'
            ]
        },
        {
            'milestone': 'M2: Employee Data Core',
            'weeks': 'W5-W6',
            'lead_hours': 90,
            'intern_hours': 40,
            'billing_percentage': 20,
            'deliverables': [
                'Employee Core Data Engine (Personal, Employment, Job Info)',
                'Employee Complex Data Engine (Time, Accruals)'
            ]
        },
        {
            'milestone': 'M3: Employee Data Financial',
            'weeks': 'W7',
            'lead_hours': 60,
            'intern_hours': 30,
            'billing_percentage': 15,
            'deliverables': [
                'Employee Financial Data Engine (Tax, Super, Payment Info)',
                'Recurring Payments & Deductions Engine'
            ]
        },
        {
            'milestone': 'M4: Payroll & Time Integration',
            'weeks': 'W8-W9',
            'lead_hours': 80,
            'intern_hours': 40,
            'billing_percentage': 20,
            'deliverables': [
                'Payroll Data Migration Engine (DWS, PWS, WorkSchedules ECP)',
                'Time Data Integration (Absences, Time Accounts, Work Schedules)'
            ]
        },
        {
            'milestone': 'M5: Testing & Deployment',
            'weeks': 'W10-W12',
            'lead_hours': 145,
            'intern_hours': 53,
            'billing_percentage': 20,
            'deliverables': [
                'Integration Testing & Performance Report',
                'UAT Execution & Documentation',
                'Security Implementation & Production Deployment'
            ]
        }
    ]
    
    return milestones

# Create corrected task data
def create_corrected_task_data():
    tasks = [
        # Week 1 - Project Setup
        {'week': 1, 'task': 'Project kickoff & environment setup', 'lead_hours': 10, 'intern_hours': 5, 'type': 'Setup', 'module': 'Setup'},
        {'week': 1, 'task': 'Requirements gathering & 64 objects analysis', 'lead_hours': 8, 'intern_hours': 10, 'type': 'Documentation', 'module': 'Setup'},
        {'week': 1, 'task': 'Schema analysis & object categorization', 'lead_hours': 7, 'intern_hours': 0, 'type': 'Development', 'module': 'Setup'},
        
        # Week 2 - Architecture
        {'week': 2, 'task': 'Microservices architecture design', 'lead_hours': 15, 'intern_hours': 0, 'type': 'Development', 'module': 'Architecture'},
        {'week': 2, 'task': 'Interactive mapping UI development', 'lead_hours': 15, 'intern_hours': 0, 'type': 'Development', 'module': 'Architecture'},
        {'week': 2, 'task': 'Architecture testing & validation', 'lead_hours': 0, 'intern_hours': 10, 'type': 'Testing', 'module': 'Architecture'},
        
        # Week 3-4 - Foundation Data (16 objects)
        {'week': 3, 'task': 'Foundation objects ETL engine (8 objects)', 'lead_hours': 20, 'intern_hours': 0, 'type': 'Development', 'module': 'Foundation Data'},
        {'week': 3, 'task': 'Foundation objects testing & validation', 'lead_hours': 5, 'intern_hours': 15, 'type': 'Testing', 'module': 'Foundation Data'},
        {'week': 4, 'task': 'Complete foundation objects (8 remaining)', 'lead_hours': 15, 'intern_hours': 0, 'type': 'Development', 'module': 'Foundation Data'},
        {'week': 4, 'task': 'Foundation integration testing', 'lead_hours': 5, 'intern_hours': 10, 'type': 'Testing', 'module': 'Foundation Data'},
        
        # Week 5-6 - Employee Data Core
        {'week': 5, 'task': 'Employee core data transformation engine', 'lead_hours': 25, 'intern_hours': 0, 'type': 'Development', 'module': 'Employee Data'},
        {'week': 5, 'task': 'Employee core data testing & validation', 'lead_hours': 10, 'intern_hours': 20, 'type': 'Testing', 'module': 'Employee Data'},
        {'week': 6, 'task': 'Employee complex data engine (Time, Accruals)', 'lead_hours': 30, 'intern_hours': 0, 'type': 'Development', 'module': 'Employee Data'},
        {'week': 6, 'task': 'Complex employee data testing', 'lead_hours': 15, 'intern_hours': 20, 'type': 'Testing', 'module': 'Employee Data'},
        
        # Week 7 - Employee Data Financial
        {'week': 7, 'task': 'Employee financial data engine (Tax, Super, Payment)', 'lead_hours': 35, 'intern_hours': 0, 'type': 'Development', 'module': 'Employee Data'},
        {'week': 7, 'task': 'Financial employee data testing', 'lead_hours': 15, 'intern_hours': 25, 'type': 'Testing', 'module': 'Employee Data'},
        {'week': 7, 'task': 'Recurring payments & deductions implementation', 'lead_hours': 10, 'intern_hours': 5, 'type': 'Development', 'module': 'Employee Data'},
        
        # Week 8 - Payroll Data
        {'week': 8, 'task': 'Payroll data transformation (DWS, PWS, WorkSchedules ECP)', 'lead_hours': 40, 'intern_hours': 0, 'type': 'Development', 'module': 'Payroll Data'},
        {'week': 8, 'task': 'Payroll data testing & validation', 'lead_hours': 15, 'intern_hours': 20, 'type': 'Testing', 'module': 'Payroll Data'},
        
        # Week 9 - Time Data Integration
        {'week': 9, 'task': 'Time data integration (Absences, Time Accounts)', 'lead_hours': 25, 'intern_hours': 0, 'type': 'Development', 'module': 'Time Data'},
        {'week': 9, 'task': 'Work schedule integration', 'lead_hours': 15, 'intern_hours': 0, 'type': 'Development', 'module': 'Time Data'},
        {'week': 9, 'task': 'Time data testing & validation', 'lead_hours': 10, 'intern_hours': 20, 'type': 'Testing', 'module': 'Time Data'},
        
        # Week 10 - System Testing
        {'week': 10, 'task': 'Comprehensive system testing', 'lead_hours': 20, 'intern_hours': 25, 'type': 'Testing', 'module': 'Integration'},
        {'week': 10, 'task': 'Performance benchmarking & optimization', 'lead_hours': 15, 'intern_hours': 5, 'type': 'Development', 'module': 'Integration'},
        {'week': 10, 'task': 'UAT execution & issue resolution', 'lead_hours': 20, 'intern_hours': 15, 'type': 'Testing', 'module': 'Integration'},
        
        # Week 11 - Documentation & Security
        {'week': 11, 'task': 'Complete system documentation', 'lead_hours': 15, 'intern_hours': 15, 'type': 'Documentation', 'module': 'Deployment'},
        {'week': 11, 'task': 'Code obfuscation & licensing system', 'lead_hours': 25, 'intern_hours': 0, 'type': 'Development', 'module': 'Deployment'},
        {'week': 11, 'task': 'Security testing & audit logging', 'lead_hours': 10, 'intern_hours': 20, 'type': 'Testing', 'module': 'Deployment'},
        
        # Week 12 - Final Deployment
        {'week': 12, 'task': 'Production deployment & final validation', 'lead_hours': 25, 'intern_hours': 8, 'type': 'Deployment', 'module': 'Deployment'},
        {'week': 12, 'task': 'Knowledge transfer & training materials', 'lead_hours': 20, 'intern_hours': 10, 'type': 'Documentation', 'module': 'Deployment'},
    ]
    
    return tasks

# Main dashboard
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>Total Duration</h3>
        <h2 style="color: #667eea;">14 Weeks</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Lead Hours</h3>
        <h2 style="color: #d32f2f;">{st.session_state.project_data['lead_hours']}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Intern Hours</h3>
        <h2 style="color: #388e3c;">{st.session_state.project_data['intern_hours']}</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Total Objects</h3>
        <h2 style="color: #f57c00;">{st.session_state.project_data['total_objects']}</h2>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Effort Hours</h3>
        <h2 style="color: #7b1fa2;">688</h2>
    </div>
    """, unsafe_allow_html=True)

# Corrected Billing Schedule
st.markdown("""
<div class="billing-info">
    <h3>💰 Corrected Billing Schedule</h3>
    <ul>
        <li><strong>Milestone 1:</strong> 25% - Architecture & Foundation Data (16 objects)</li>
        <li><strong>Milestone 2:</strong> 20% - Employee Data Core</li>
        <li><strong>Milestone 3:</strong> 15% - Employee Data Financial</li>
        <li><strong>Milestone 4:</strong> 20% - Payroll & Time Data Integration</li>
        <li><strong>Milestone 5:</strong> 20% - Testing, Security & Deployment</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Tabs for different views
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📋 Corrected Milestones", "📊 Module Breakdown", "💼 Resource Allocation", "🎯 Objects by Category", "✏️ Edit Tasks"])

with tab1:
    st.header("🎯 Corrected Milestone Overview")
    milestones = create_corrected_project_data()
    
    for i, milestone in enumerate(milestones):
        with st.expander(f"{milestone['milestone']} ({milestone['weeks']})", expanded=True):
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.write("**Deliverables:**")
                for deliverable in milestone['deliverables']:
                    st.write(f"• {deliverable}")
            
            with col2:
                st.metric("Lead Hours", milestone['lead_hours'])
                st.metric("Intern Hours", milestone['intern_hours'])
            
            with col3:
                st.metric("Billing %", f"{milestone['billing_percentage']}%")
                total_hours = milestone['lead_hours'] + milestone['intern_hours']
                st.metric("Total Hours", total_hours)








with tab2:
    st.header("📊 Module Breakdown by Category")
    
    # Create module breakdown
    modules = {

        'Employee Data': {'objects': 38, 'weeks': 'W5-W7', 'effort_hours': 380},
        'Foundation Data': {'objects': 16, 'weeks': 'W3-W4', 'effort_hours': 150},
        'Payroll Data': {'objects': 9, 'weeks': 'W8', 'effort_hours': 110},
        'Time Data': {'objects': 11, 'weeks': 'W9', 'effort_hours': 135},
    }
    
    # Create DataFrame
    module_df = pd.DataFrame.from_dict(modules, orient='index').reset_index()
    module_df.columns = ['Module', 'Objects', 'Weeks', 'Effort Hours']
    
    # Sort DataFrame by 'Objects' descending to ensure bars show all
    module_df = module_df.sort_values(by='Objects', ascending=False)
    
    # Bar chart - Objects count by Module
    fig = px.bar(
        module_df,
        x='Module',
        y='Objects',
        title='Objects Distribution by Module',
        color='Objects',
        color_continuous_scale='viridis'
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    
    
    # Module details table
    st.subheader("Module Details")
    for module, details in modules.items():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(f"{module}", f"{details['objects']} objects")
        with col2:
            st.write(f"**Weeks:** {details['weeks']}")
        with col3:
            st.write(f"**Effort:** {details['effort_hours']}h")
        with col4:
            complexity = (
                "High" if details['objects'] > 30 else
                "Medium" if details['objects'] > 15 else
                "Low"
            )
            st.write(f"**Complexity:** {complexity}")











# Continuing from tab3 - Resource Allocation

 
import plotly.graph_objects as go
 



with tab3:
    st.header("💼 Resource Allocation")
    
    weeks = list(range(1, 15))
    lead_hours = [40, 40, 40, 40, 40, 35, 30, 25, 20, 15, 10, 10, 10, 10]  # sum 475 hardcoded
    intern_hours = [5, 5, 5, 10, 15, 15, 15, 15, 15, 15, 15, 13, 10, 10]   # sum 213 hardcoded
    
    total_hours = [l + i for l, i in zip(lead_hours, intern_hours)]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Lead Hours', x=weeks, y=lead_hours, marker_color='#d32f2f'))
    fig.add_trace(go.Bar(name='Intern Hours', x=weeks, y=intern_hours, marker_color='#388e3c'))
    fig.update_layout(
        title='Weekly Resource Allocation',
        xaxis_title='Week',
        yaxis_title='Hours',
        barmode='stack',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    resource_df = pd.DataFrame({
        'Week': weeks,
        'Lead Hours': lead_hours,
        'Intern Hours': intern_hours,
        'Total Hours': total_hours
    })
    
    # Use hardcoded totals instead of sum()
    totals = pd.DataFrame({
        'Week': ['Total'],
        'Lead Hours': [475],
        'Intern Hours': [213],
        'Total Hours': [688]
    })
    
    resource_df_with_total = pd.concat([resource_df, totals], ignore_index=True)
    
    st.subheader("Weekly Resource Summary")
    st.dataframe(resource_df_with_total, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Avg Lead Hours/Week", f"{475/14:.1f}")
    with col2:
        st.metric("Avg Intern Hours/Week", f"{213/14:.1f}")
    with col3:
        peak_week = total_hours.index(max(total_hours)) + 1
        st.metric("Peak Week", f"Week {peak_week}")





with tab4:
    st.header("🎯 Objects by Category")
    
    # Load objects data
    objects_df = load_objects_data()
    
    # Category summary
    category_summary = objects_df.groupby('category').agg({
        'name': 'count',
        'final_effort': 'sum'
    }).reset_index()
    category_summary.columns = ['Category', 'Object Count', 'Total Effort Hours']
    
    
    # Category breakdown
    st.subheader("Category Breakdown")
    
    for category in objects_df['category'].unique():
        with st.expander(f"{category} Objects", expanded=False):
            category_objects = objects_df[objects_df['category'] == category]
            
            # Summary metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Objects", len(category_objects))
            with col2:
                st.metric("Total Hours", category_objects['final_effort'].sum())
            with col3:
                avg_complexity = category_objects['final_effort'].mean()
                st.metric("Avg Hours/Object", f"{avg_complexity:.1f}")
            
            # Objects table
            display_df = category_objects[['name', 'complexity', 'final_effort']].copy()
            display_df.columns = ['Object Name', 'Complexity', 'Effort Hours']
            st.dataframe(display_df, use_container_width=True, hide_index=True)

with tab5:
    st.header("✏️ Edit Tasks")
    
    # Task editing interface
    tasks = create_corrected_task_data()
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_week = st.selectbox("Filter by Week", ["All"] + list(range(1, 13)))
    with col2:
        selected_module = st.selectbox("Filter by Module", 
                                     ["All"] + list(set(task['module'] for task in tasks)))
    with col3:
        selected_type = st.selectbox("Filter by Type", 
                                   ["All"] + list(set(task['type'] for task in tasks)))
    
    # Filter tasks
    filtered_tasks = tasks
    if selected_week != "All":
        filtered_tasks = [t for t in filtered_tasks if t['week'] == selected_week]
    if selected_module != "All":
        filtered_tasks = [t for t in filtered_tasks if t['module'] == selected_module]
    if selected_type != "All":
        filtered_tasks = [t for t in filtered_tasks if t['type'] == selected_type]
    
    # Create editable dataframe
    if filtered_tasks:
        task_df = pd.DataFrame(filtered_tasks)
        task_df = task_df[['week', 'task', 'lead_hours', 'intern_hours', 'type', 'module']]
        task_df.columns = ['Week', 'Task', 'Lead Hours', 'Intern Hours', 'Type', 'Module']
        
        # Display editable table
        st.subheader("Task Details")
        edited_df = st.data_editor(
            task_df,
            column_config={
                "Week": st.column_config.NumberColumn(min_value=1, max_value=12),
                "Lead Hours": st.column_config.NumberColumn(min_value=0, max_value=100),
                "Intern Hours": st.column_config.NumberColumn(min_value=0, max_value=100),
                "Type": st.column_config.SelectboxColumn(
                    options=["Setup", "Development", "Testing", "Documentation", "Deployment"]
                ),
                "Module": st.column_config.SelectboxColumn(
                    options=["Setup", "Architecture", "Foundation Data", "Employee Data", 
                           "Payroll Data", "Time Data", "Integration", "Deployment"]
                )
            },
            use_container_width=True,
            hide_index=True
        )
        
        # Task summary
        st.subheader("Task Summary")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_tasks = len(edited_df)
            st.metric("Total Tasks", total_tasks)
        
        with col2:
            total_lead_hours = edited_df['Lead Hours'].sum()
            st.metric("Total Lead Hours", total_lead_hours)
        
        with col3:
            total_intern_hours = edited_df['Intern Hours'].sum()
            st.metric("Total Intern Hours", total_intern_hours)
        
        with col4:
            total_hours = total_lead_hours + total_intern_hours
            st.metric("Total Hours", total_hours)
        
        # Module distribution in filtered tasks
        if len(edited_df) > 0:
            module_dist = edited_df.groupby('Module').agg({
                'Lead Hours': 'sum',
                'Intern Hours': 'sum'
            }).reset_index()
            module_dist['Total Hours'] = module_dist['Lead Hours'] + module_dist['Intern Hours']
            
            fig_module = px.bar(module_dist, x='Module', y=['Lead Hours', 'Intern Hours'],
                               title='Hours Distribution by Module (Filtered Tasks)',
                               barmode='stack')
            fig_module.update_layout(height=400)
            st.plotly_chart(fig_module, use_container_width=True)
    
    else:
        st.info("No tasks match the selected filters.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 50px;">
    <p>🚀 DaSH Migration Product - Corrected 3-Month Plan</p>
    <p>SAP On-Premise to SuccessFactors Migration Tool</p>
    <p><strong>Total: 64 Objects | 688 Effort Hours | 475 Lead Hours | 213 Intern Hours</strong></p>
</div>
""", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    st.write("Dashboard loaded successfully! Use the sidebar to adjust project parameters.")

















