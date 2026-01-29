# FitPulse – Health Anomaly Detection from Fitness Devices

Live Application Link:  
https://fitpulse-health-anomaly.streamlit.app

---

## Project Overview

FitPulse is a health analytics application designed to analyze fitness device data and detect abnormal health patterns.  
The system processes physiological and activity-based data such as heart rate, sleep duration, daily steps, and stress levels to generate meaningful insights and predictions.

The project integrates data preprocessing, feature extraction, machine learning models, and an interactive dashboard to provide end-to-end health monitoring and anomaly detection.

---

## Objectives

- Analyze fitness device data for health monitoring  
- Detect abnormal health behavior using machine learning  
- Extract meaningful features from time-series data  
- Forecast future health trends  
- Present insights through an interactive dashboard  

---

## Key Features

- Interactive health analytics dashboard  
- Heart rate, sleep, and activity analysis  
- Time-series forecasting using Prophet  
- Feature extraction using TSFresh  
- Clustering and anomaly detection using DBSCAN  
- Health check page based on dataset patterns  
- Modular and scalable project architecture  

---

## Project Structure

```text
FitPulse-Health-Anomaly-Detection-from-Fitness-Devices-T/
│
├── health-anomaly-dashboard/
│   ├── app.py
│   ├── pages/
│   │   ├── dashboard.py
│   │   ├── heart_rate.py
│   │   ├── sleep.py
│   │   ├── steps.py
│   │   ├── model_insights.py
│   │   ├── reports.py
│   │   └── health_check.py
│   │
│   ├── team_code/
│   │   ├── module1_preprocessing.py
│   │   ├── module2_features_model.py
│   │   └── module3_anomaly_detection.py
│   │
│   ├── utils/
│   │   ├── ui.py
│   │   ├── charts.py
│   │   └── runner.py
│   │
│   ├── requirements.txt
│   └── LICENSE
│
└── README.md


## Technology Stack

Frontend:
- Streamlit
- Plotly
- Custom CSS

Backend and Machine Learning:
- Python
- Pandas, NumPy
- Scikit-learn
- TSFresh
- Prophet
- DBSCAN, PCA

---

## Application Workflow

1. User uploads fitness dataset (CSV format)
2. Data preprocessing and cleaning
3. Feature extraction from time-series data
4. Anomaly detection and clustering
5. Time-series forecasting
6. Visualization through dashboards and reports
7. Health evaluation based on dataset patterns

---

## How to Run the Project Locally

### Step 1: Clone the Repository

### Step 2: Navigate to the Project Directory

### Step 3: Create and Activate Virtual Environment

### Step 4: Install Dependencies

### Step 5: Run the Application


---

## Deployment

The application is deployed using Streamlit Community Cloud.

Live URL:  
https://fitpulse-health-anomaly.streamlit.app

---

## Team Contributions

This project was developed as a collaborative team effort.

- Vinotha M  
  Module 1: Data Collection and Preprocessing

- Prajwal Venkatesh Sortur  
  Module 2: Feature Extraction and Modeling

- Sheethal Karan  
  Module 3: Anomaly Detection and Visualization

- Chinmoy Saikia  
  Module 4: Dashboard Development and Insights

- Mahek Sultana  
  Project support and presentation assistance

---

