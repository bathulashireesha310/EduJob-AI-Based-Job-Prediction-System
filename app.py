import streamlit as st
import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import os
if not os.path.exists("users.csv"):
    pd.DataFrame(columns=["Name","Email","Password"]).to_csv("users.csv", index=False)
st.set_page_config(page_title="AI Job Prediction System", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    color: white;
}

.metric-card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.4);
    margin-bottom: 10px;
}

/* Force the container and the button to be 100% width */
div.stButton, div.stButton > button {
    width: 100% !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    box-sizing: border-box !important;
}

/* 3D Button Styling */
div.stButton > button {
    background-color: #FFD700;
    color: black !important;
    font-weight: bold;
    border-radius: 8px;
    padding: 12px 20px;
    border: none;
    /* 3D effect thickness */
    box-shadow: 0px 6px 0px #b8860b; 
    transition: all 0.1s ease;
    margin-bottom: 18px; /* Space between buttons */
    text-align: center;
}

/* Hover effect */
div.stButton > button:hover {
    background-color: #FFC300;
    color: black !important;
    transform: translateY(2px);
    box-shadow: 0px 4px 0px #b8860b;
}

/* Click effect */
div.stButton > button:active {
    transform: translateY(6px);
    box-shadow: 0px 0px 0px #b8860b;
}

/* Fix label visibility */
label {
    color: white !important;
    font-weight: 600;
}

/* Dropdown selected text */
div[data-baseweb="select"] span {
    color: black !important;
}

/* Input text field color */
input {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# Email Validation
# ==============================
def valid_gmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email)


# ==============================
# Password Validation
# ==============================
def valid_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    return re.match(pattern, password)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
# Track if student details have been saved
if "details_entered" not in st.session_state:
    st.session_state.details_entered = False

# ==============================
# Initialize student details
# ==============================
for key, default in {
    "degree": None,
    "specialization": None,
    "programming": None,
    "internship": None,
    "cgpa": 7.0,
    "projects": 0,
    "certification": None,
    "problem": None
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# Initialize flag to track if student details are saved
if "details_entered" not in st.session_state:
    st.session_state.details_entered = False



# ==============================
# LOGIN PAGE
# ==============================
def login_page():

    left, center, right = st.columns([2,1,2])

    with center:

        st.title("EduJob Login")

        name = st.text_input("Name", placeholder="Enter your name")
        email = st.text_input("Email", placeholder="Enter your gmail")
        password = st.text_input("Password", placeholder="Enter password", type="password")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Register"):
                if not name:
                    st.error("Enter your name")
                elif not valid_gmail(email):
                    st.error("Enter valid Gmail")
                elif not valid_password(password):
                    st.error("Password must contain:")
                    st.write("• 8 characters")
                    st.write("• 1 capital letter")
                    st.write("• 1 number")
                    st.write("• 1 special symbol")
                else:
                    new_user = pd.DataFrame([[name, email, password]],
                                            columns=["Name","Email","Password"])
                    try:
                        old_users = pd.read_csv("users.csv")
                        if email in old_users["Email"].values:
                            st.error("User already registered")
                            st.stop()
                        users = pd.concat([old_users, new_user], ignore_index=True)
                    except:
                        users = new_user
                    users.to_csv("users.csv", index=False)
                    st.success("Registration Successful ✅")
        with col2:
            if st.button("Login"):

                if not valid_gmail(email):
                    st.error("Enter valid Gmail")
                elif not password:
                    st.error("Enter password")
                else:
                    if not os.path.exists("users.csv"):
                        st.error("No users found. Please register first.")
                        st.stop()
                    users = pd.read_csv("users.csv")
                    email_match = users[users["Email"] == email]
                    if email_match.empty:
                        st.error("Invalid Email ❌")
                    else:
                        name_match = email_match[email_match["Name"] == name]
                        if name_match.empty:
                            st.error("Invalid Username ❌")
                        else:
                            pass_match = name_match[name_match["Password"] == password]
                            if pass_match.empty:
                                st.error("Invalid Password ❌")
                            else:
                                st.session_state.logged_in = True
                                st.session_state.user = name
                                st.success("Login Successful ✅")
                                st.stop()
# ==============================
# Train Model
# ==============================
@st.cache_resource
def train_model(data):

    model_data = data.copy()
    y = model_data['JobRole']
    X = model_data.drop('JobRole', axis=1)
    X = pd.get_dummies(X)
    le_job = LabelEncoder()
    y = le_job.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=20,
        min_samples_split=5,
        random_state=42
    )

    model.fit(X_train, y_train)

    train_acc = model.score(X_train, y_train)
    test_acc = accuracy_score(y_test, model.predict(X_test))

    return model, le_job, X.columns, train_acc, test_acc
# ==============================
# DASHBOARD
# ==============================
def dashboard(): 
    st.sidebar.write(f"Welcome {st.session_state.get('user','User')}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
    
    if "page" not in st.session_state:
        st.session_state.page = "details"
        
    st.title("🎓 AI Based Job Prediction System")
    data = pd.read_csv("job_dataset_enhanced.csv")
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="metric-card"><h2>{len(data)}</h2><p>Total Students</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><h2>{data["JobRole"].nunique()}</h2><p>Job Roles</p></div>', unsafe_allow_html=True)
    with col3:
         st.markdown(f'<div class="metric-card"><h2>{data["Programming"].nunique()}</h2><p>Programming Skills</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Train Model
    model, le_job, X_columns, train_acc, test_acc = train_model(data)

    # Sidebar Menu
    st.sidebar.header("Model Accuracy")
    st.sidebar.write(f"Training Accuracy: {train_acc:.2f}")
    st.sidebar.write(f"Testing Accuracy: {test_acc:.2f}")
    st.sidebar.header("Menu")

    if st.sidebar.button("Enter Student Details"):
        st.session_state.page = "details"
    if st.sidebar.button("Predict Job"):
        st.session_state.page = "predict"
    if st.sidebar.button("Graph Distribution"):
        st.session_state.page = "graphs"
    if st.sidebar.button("View History"):
        st.session_state.page = "history"


    # ==============================
    # PAGE: DETAILS
    # ==============================
    if st.session_state.page == "details":
        st.subheader("Enter Student Details")
        col1, col2 = st.columns(2)

        with col1:
            degree_input = st.selectbox("Degree", data["Degree"].unique())
            spec_input = st.selectbox("Specialization", data["Specialization"].unique())
            prog_input = st.selectbox("Programming Skill", data["Programming"].unique())
            intern_input = st.selectbox("Internship", data["Internship"].unique())
        with col2:
            cgpa_input = st.number_input("CGPA", 1.0, 10.0, 7.0)
            proj_input = st.number_input("Projects", 0, 10, 2)
            cert_input = st.selectbox("Certification", data["Certification"].unique())
            prob_input = st.selectbox("Problem Solving", data["ProblemSolving"].unique())

        if st.button("💾 Save Details"):
            st.session_state.degree = degree_input
            st.session_state.specialization = spec_input
            st.session_state.programming = prog_input
            st.session_state.internship = intern_input
            st.session_state.cgpa = cgpa_input
            st.session_state.projects = proj_input
            st.session_state.certification = cert_input
            st.session_state.problem = prob_input        
            st.session_state.details_entered = True
            st.success("✅ Details saved! You can now go to Predict Job.")

    # ==============================
    # PAGE: PREDICT (Moved outside the 'details' block)
    # ==============================
    if st.session_state.page == "predict":
        if not st.session_state.details_entered:
            st.warning("⚠ Please enter and save student details first.")
        else:
            if st.button("🚀 Predict Job Role", use_container_width=True):
                input_dict = {
                    'Degree': st.session_state.degree,
                    'Specialization': st.session_state.specialization,
                    'CGPA': st.session_state.cgpa,
                    'Programming': st.session_state.programming,
                    'Internship': st.session_state.internship,
                    'Projects': st.session_state.projects,
                    'Certification': st.session_state.certification,
                    'ProblemSolving': st.session_state.problem
                }
                input_df = pd.DataFrame([input_dict])
                input_df = pd.get_dummies(input_df)
                input_df = input_df.reindex(columns=X_columns, fill_value=0)
                input_df = input_df.astype(float)
                probs = model.predict_proba(input_df)[0]
                top_indices = probs.argsort()[-3:][::-1]
                top_jobs = le_job.inverse_transform(top_indices)
                top_scores = probs[top_indices] * 100
                st.markdown("### 🎯 Top Job Predictions")
                for i in range(3):
                    st.write(f"{i+1}. {top_jobs[i]} — {top_scores[i]:.2f}%")
                    st.progress(int(top_scores[i]))
                st.success(f"🏆 Best Match: {top_jobs[0]} ({top_scores[0]:.2f}%)")
                history_data = pd.DataFrame({
                    "User": [st.session_state.get("user", "Unknown")],
                    "Top1": [f"{top_jobs[0]} ({top_scores[0]:.2f}%)"],
                    "Top2": [f"{top_jobs[1]} ({top_scores[1]:.2f}%)"],
                    "Top3": [f"{top_jobs[2]} ({top_scores[2]:.2f}%)"]
                })
                if os.path.exists("history.csv"):
                    old_history = pd.read_csv("history.csv")
                    history_data = pd.concat([old_history, history_data], ignore_index=True)
                history_data.to_csv("history.csv", index=False)


# ==============================
# Job Role Graph
# ==============================
    if st.session_state.page == "graphs":

        graph_col1, graph_col2 = st.columns(2)
        with graph_col1:
            st.subheader("Job Role Distribution")

            job_counts = data['JobRole'].value_counts()
            fig, ax = plt.subplots(figsize=(6,4))
            x_pos = range(len(job_counts))
            ax.bar(x_pos, job_counts.values,               
                   color='#FFD700',
                   width=0.5)

            ax.set_xticks(x_pos)
            ax.set_xticklabels(job_counts.index, rotation=30, ha='right')

            ax.set_ylabel("Count")
            ax.set_xlabel("Job Roles")
            plt.tight_layout()
            st.pyplot(fig)
        with graph_col2:
            st.subheader("Programming Skill Demand")
            skill_counts = data['Programming'].value_counts()
            fig2, ax2 = plt.subplots(figsize=(6,4))
            ax2.bar(skill_counts.index, skill_counts.values,                 
                    color='#FFD700',
                    width=0.4)

            plt.tight_layout()
            st.pyplot(fig2)
    if st.session_state.page == "history":
        st.subheader("📜 Prediction History")
        if os.path.exists("history.csv"):
            history = pd.read_csv("history.csv")
            user_history = history[history["User"] == st.session_state.user]
            if not user_history.empty:
                st.dataframe(user_history[["User", "Top1", "Top2", "Top3"]])
            else:
                st.info("No history found")
        else:
            st.info("No history file found")

# ==============================
# Main App
# ==============================

if st.session_state.logged_in:
    dashboard()
else:
    login_page()