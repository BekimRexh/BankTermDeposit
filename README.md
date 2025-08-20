# 📊 Bank Term Deposit Prediction – Kaggle to AWS Fargate

This project leverages the **Bank Term Deposit dataset** from Kaggle to build a machine learning model that predicts whether a customer will subscribe to a term deposit.  
The solution is fully containerized with Docker and deployed to AWS using **Fargate** behind a **load balancer**, making the model accessible as a scalable, production-ready API.

---

## 🚀 Features
- 🔍 **Data Analysis & Modeling** – Exploratory data analysis and ML model training in a Jupyter notebook.  
- 📦 **Containerization** – Packaged with Docker for consistent and reproducible environments.  
- ☁️ **Cloud Deployment** – Deployed on AWS Fargate with an Application Load Balancer.  
- 🌐 **REST API** – Exposes prediction endpoint for easy integration with external applications.  

---

## 🛠️ Tech Stack
- **Python** / **Jupyter Notebook**  
- **scikit-learn**, **pandas**, **matplotlib**  
- **Docker**  
- **AWS ECS Fargate**, **Application Load Balancer**  

---

## 📂 Project Structure
```bash
.
├── notebooks/          # Kaggle-style EDA & model training notebooks
├── app/                # API application code
├── Dockerfile          # Container definition
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
