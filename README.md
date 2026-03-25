🎓 EduJob: AI-Based Job Prediction System
📌 Project Overview

EduJob is an AI-powered job prediction system that analyzes student academic and skill-based data to predict the most suitable job roles.
It uses Machine Learning (Random Forest Classifier) to recommend career paths based on user inputs like CGPA, skills, internships, and certifications.

🚀 Features
🔐 User Authentication
Registration & Login system using CSV storage
Email and password validation
📊 Interactive Dashboard
Displays dataset insights
Shows total students, job roles, and skills
🧠 AI-Based Prediction
Predicts Top 3 job roles with probability scores
Highlights best match
📈 Data Visualization
Job role distribution graph
Programming skill demand graph
📜 Prediction History
Stores and displays user prediction history
🧠 Machine Learning Model
Algorithm Used: Random Forest Classifier
Why Random Forest?
Handles categorical + numerical data well
High accuracy and robustness
Reduces overfitting
Training Details:
Train-test split: 80% / 20%
Encoded categorical data using one-hot encoding
Label encoding for target variable
Output:
Top 3 predicted job roles with probability (%)
⚙️ Tech Stack
Frontend: Streamlit
Backend: Python
Libraries:
pandas
scikit-learn
matplotlib
streamlit
Storage:
CSV files (users, dataset, history)

## 📂 Project Structure

```
EduJob-AI-Based-Job-Prediction-System/
│
├── app.py
├── job_dataset_enhanced.csv
├── users.csv
├── history.csv
│
├── images/
│   ├── 01_login.jpeg
│   ├── 02_dashboard.jpeg
│   ├── 03_details.jpeg
│   ├── 04_prediction.jpeg
│   ├── 05_graph_distribution.jpeg
│   └── 06_view_history.jpeg
│
├── README.md
└── requirements.txt
```

📊 How It Works
User Input → Data Preprocessing → Model Training → Prediction → Output Display
User enters academic & skill details
Data is preprocessed (encoding applied)
Model predicts job role probabilities
Top 3 job roles are displayed
🖥️ Screenshots
🔐 Login Page
![1_login](https://github.com/user-attachments/assets/8e249190-a064-4fde-a0b9-6885224aca21)

📊 Dashboard
![2_dashboard](https://github.com/user-attachments/assets/438e0c75-1819-428f-b4b6-dff68d4da6be)

📄 Student Details
![3_details](https://github.com/user-attachments/assets/e1516022-d8dd-42cf-aea3-cfa0feb7f89c)

🤖 Prediction Result
![4_prediction](https://github.com/user-attachments/assets/d3669179-ccff-4761-b4a9-877ccde341f2)

📈 Graph Distribution
![5_graph_distribution](https://github.com/user-attachments/assets/a0308393-d30d-4be5-a1e1-e918f5fee418)

📜 View History
![6_view_history](https://github.com/user-attachments/assets/ed9cbec1-b784-4df1-8988-06b371e2450d)

▶️ How to Run the Project
## 🔗 Project Link
https://github.com/bathulashireesha310/EduJob-AI-Based-Job-Prediction-System
cd EduJob-AI-Based-Job-Prediction-System
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the App
streamlit run app.py
📦 Requirements

Create a requirements.txt file with:

streamlit
pandas
scikit-learn
matplotlib
🎯 Key Highlights
Real-time job prediction using AI
User-friendly interface with Streamlit
Data visualization for better insights
Practical implementation of ML concepts
📌 Future Enhancements
🔹 Deploy on Streamlit Cloud
🔹 Add more ML models for comparison
🔹 Improve dataset size and accuracy
🔹 Add resume-based prediction (NLP)
👨‍💻 Author

Bathula Shireesha
AI & Data Science Student

⭐ Conclusion

This project demonstrates how Machine Learning can be used to guide students in career decisions by analyzing their skills and academic performance.
