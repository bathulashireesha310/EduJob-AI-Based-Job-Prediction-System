# 🎓 EduJob: AI-Based Job Prediction System

## 📌 Project Overview
EduJob is an AI-powered job prediction system that helps students identify suitable career paths based on their academic performance and skills.  
The system uses Machine Learning (Random Forest Classifier) to analyze inputs such as CGPA, programming skills, internships, and certifications.

---

## 🚀 Features
- 🔐 User Registration & Login System  
- 📊 Interactive Dashboard  
- 🧠 AI-based Job Prediction (Top 3 results with probability)  
- 📈 Graph visualization of job roles & skills  
- 📜 Prediction history tracking  
- 🎨 Attractive UI using Streamlit  

---

## 🧠 Machine Learning Model
- Algorithm Used: Random Forest Classifier  
- Handles categorical and numerical data  
- Provides high accuracy and reduces overfitting  

Process:
- Data preprocessing using one-hot encoding  
- Train-test split (80% / 20%)  
- Model training and prediction  

---

## ⚙️ Tech Stack
- Frontend: Streamlit  
- Backend: Python  
- Libraries:
  - pandas  
  - scikit-learn  
  - matplotlib  
  - streamlit  

---

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

---

## 📊 How It Works
1. User logs in or registers  
2. Enters academic and skill details  
3. Data is processed and encoded  
4. Model predicts job roles  
5. Top 3 job roles are displayed  

---

## 🖥️ Screenshots

### 🔐 Login Page
![Login](images/01_login.jpeg)

### 📊 Dashboard
![Dashboard](images/02_dashboard.jpeg)

### 📄 Student Details
![Details](images/03_details.jpeg)

### 🤖 Prediction Result
![Prediction](images/04_prediction.jpeg)

### 📈 Graph Distribution
![Graph](images/05_graph_distribution.jpeg)

### 📜 View History
![History](images/06_view_history.jpeg)

---

## ▶️ How to Run the Project

### Clone Repository
```bash
git clone https://github.com/bathulashireesha310/EduJob-AI-Based-Job-Prediction-System.git
cd EduJob-AI-Based-Job-Prediction-System
```

### Install Requirements
```bash
pip install -r requirements.txt
```

### Run Application
```bash
streamlit run app.py
```

---

## 📦 Requirements
```
streamlit
pandas
scikit-learn
matplotlib
```

---

## 🎯 Key Highlights
- Real-time job prediction using AI  
- User-friendly interface  
- Data visualization  
- Practical ML implementation  

---

## 🔮 Future Enhancements
- Add more ML models  
- Improve dataset  
- Deploy online  
- Resume-based prediction  

---

## 👨‍💻 Author
Bathula Shireesha  

---

## ⭐ Conclusion
This project shows how Machine Learning helps students choose better career paths.

---

## ⭐ Support
If you like this project, give it a ⭐ on GitHub!
