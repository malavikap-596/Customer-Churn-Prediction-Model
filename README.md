# 🚀 Customer Churn Prediction Model

## 📌 Project Overview

This project focuses on predicting customer churn using machine learning techniques. Churn prediction helps businesses identify customers who are likely to leave their service, enabling proactive retention strategies.

---

## 🎯 Objectives

* Predict whether a customer will churn or not
* Analyze key factors influencing churn
* Provide actionable business insights
* Build an industry-ready ML pipeline

---

## 🧠 Business Problem

Customer retention is critical for business growth. Acquiring new customers is significantly more expensive than retaining existing ones. This project helps in:

* Reducing customer loss
* Improving retention strategies
* Increasing revenue
* Enabling targeted marketing

---

## 📊 Dataset

* **Source:** Kaggle Telco Customer Churn Dataset
* Contains customer demographics, services, billing, and contract details
* Target variable: `Churn`

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* XGBoost
* Jupyter Notebook

---

## 🏗️ Project Architecture

```
Customer Data → Preprocessing → Feature Engineering → Model Training → Prediction → Business Insights
```

---

## 📁 Project Structure

```
Customer-Churn-Prediction/
│
├── data/
├── notebooks/
├── src/
├── models/
├── outputs/
├── images/
├── README.md
├── requirements.txt
└── main.py
```

---

## 🔄 Workflow

1. Data Loading
2. Data Cleaning & Preprocessing
3. Feature Engineering
4. Model Training (Logistic Regression, Random Forest, XGBoost)
5. Model Evaluation
6. Prediction & Insights

---

## 📈 Results

* Built multiple models and compared performance
* Identified key churn drivers such as contract type, tenure, and monthly charges
* Generated insights for customer retention strategies

---

## 📊 Visualizations

* Churn distribution
* Feature distributions
* Correlation heatmap
* Confusion matrix
* ROC curve

---

## 🚀 How to Run

```bash
git clone <your-repo-link>
cd Customer-Churn-Prediction

python -m venv venv
venv\\Scripts\\activate  # Windows

pip install -r requirements.txt

python main.py
```

---

## 💡 Key Insights

* Customers with month-to-month contracts have higher churn
* Higher monthly charges correlate with higher churn
* Long-term customers are less likely to churn

---

## 🎯 Future Improvements

* Hyperparameter tuning
* Deployment using Streamlit
* Real-time prediction API
* Advanced feature engineering

---

## 👨‍💻 Author

MALAVIKA P

---

## ⭐ If you found this useful, consider giving a star!
