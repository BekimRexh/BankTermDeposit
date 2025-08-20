# 📊 Bank Term Deposit Prediction – Kaggle to AWS Fargate

This project leverages the **Bank Term Deposit dataset** from Kaggle to build a machine learning model that predicts whether a customer will subscribe to a term deposit.  
The solution is built with **FastAPI**, containerized with **Docker**, and deployed to **AWS Fargate** behind a **load balancer**, making the model accessible as a scalable, production-ready API.

---

## 🚀 Features
- 🔍 **Data Analysis & Modeling** – Exploratory data analysis and ML model training in a Jupyter notebook.  
- ⚡ **FastAPI** – Lightweight REST API serving the trained ML model.  
- 📦 **Containerization** – Packaged with Docker for consistent and reproducible environments.  
- ☁️ **Cloud Deployment** – Deployed on AWS Fargate with an Application Load Balancer.  
- 🌐 **REST API** – Accessible `/predict` endpoint for term deposit predictions.  

---

## 🛠️ Tech Stack
- **Python** / **Jupyter Notebook**  
- **FastAPI**, **Uvicorn**  
- **scikit-learn**, **pandas**  
- **Docker**  
- **AWS ECS Fargate**, **Application Load Balancer**  

---

## 📂 Project Structure
```bash
.
├── notebooks/          # Kaggle-style EDA & model training notebooks
├── app/                # FastAPI application code
├── Dockerfile          # Container definition
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

```

---

## ⚡ Deployment Workflow

1. Train model locally (Kaggle notebook → export model).  
2. Build and containerize the app with Docker.  
3. Push image to Amazon ECR.  
4. Deploy on **AWS Fargate**.  
5. Expose endpoint via **Load Balancer**.  

---

## 🌐 API Usage

### Endpoint
`POST http://bankterm-alb-768401147.eu-west-2.elb.amazonaws.com/predict`

### Example Request
```json
{
  "id": 101,
  "age": 45,
  "job": "management",
  "marital": "married",
  "education": "tertiary",
  "default": "no",
  "balance": 2200,
  "housing": "yes",
  "loan": "no",
  "contact": "cellular",
  "day": 15,
  "month": "dec",
  "duration": 100,
  "campaign": 2,
  "pdays": -1,
  "previous": 0,
  "poutcome": "failure"
}
```

### Example Response
A percentage: e.g. for the above, "10.4%"


## 📈 Next Steps
- Start a **new project** focused on deploying a **user-friendly web application** that anyone can easily use.  
- Design the app with an accessible front-end and connect it to a production-ready backend API.  
- Implement a **CI/CD pipeline** with **GitHub Actions** to automate testing, container builds, and deployment.  
- Deploy the app on **AWS (Fargate / Elastic Beanstalk / Lambda)** for scalability.  
- Add monitoring, logging, and error tracking for a smooth user experience.  

