# 🏥 Insurance Charges Prediction using Machine Learning

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge\&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge\&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-red?style=for-the-badge\&logo=streamlit)

</p>

---

# 📌 Project Overview

Medical insurance costs vary significantly depending on several personal and lifestyle factors. Predicting these charges accurately can help insurance providers, healthcare organizations, and individuals better estimate future medical expenses.

This project develops a complete **Machine Learning Regression Pipeline** that predicts a person's **medical insurance charges** using demographic and health-related information.

The project includes:

* Data Exploration (EDA)
* Data Cleaning
* Feature Engineering
* Data Visualization
* Feature Scaling
* Model Training
* Model Evaluation
* Interactive Prediction Web App using Streamlit

---

# 🎯 Project Objective

The objective of this project is to build an accurate regression model capable of estimating medical insurance charges based on user information such as:

* Age
* BMI
* Number of Children
* Smoking Status
* Gender
* Residential Region

The final model is deployed through an interactive **Streamlit Web Application** where users can enter their information and instantly receive a predicted insurance cost.

---

# 📂 Dataset

The dataset contains demographic and health-related information for insurance customers.

### Target Variable

* **Charges** (Medical Insurance Cost)

### Input Features

* Age
* Sex
* BMI
* Children
* Smoker
* Region

---

# ⚙️ Feature Engineering

Several additional features were created to improve model performance, including:

### Encoded Features

* Sex Encoding
* Smoker Encoding

### Interaction Features

* Smoker × BMI
* Smoker × Age

### Health Indicators

* Obesity Indicator

### Age Categories

* 19–30
* 31–45
* 46–60
* 60+

### BMI Categories

* Normal
* Overweight
* Obese

These engineered features enabled the model to capture more complex relationships within the dataset.

---

# 🤖 Machine Learning Workflow

The complete workflow consists of:

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Cleaning
4. Feature Engineering
5. Feature Scaling using StandardScaler
6. Train/Test Split
7. Linear Regression Model Training
8. Model Evaluation
9. Model Saving
10. Streamlit Deployment

---

# 📊 Model Performance

The trained Linear Regression model achieved the following results:

| Metric   | Train       | Test        |
| -------- | ----------- | ----------- |
| R² Score | **0.835**   | **0.886**   |
| MAE      | **2829.68** | **2845.16** |
| RMSE     | **4749.45** | **4584.57** |

The model demonstrates strong generalization performance with no significant signs of overfitting.

---

# 🌐 Streamlit Application

The application is organized into multiple pages:

🏠 **Home**

Project overview and documentation.

📊 **EDA**

Explore the dataset, statistics, missing values, and sample records.

⚙️ **Feature Engineering**

Understand how new features were generated from the original dataset.

📈 **Visualization**

Interactive charts showing distributions, correlations, and feature relationships.

🤖 **Prediction**

Enter user information and receive an estimated medical insurance charge instantly.

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

---

# 🚀 Future Improvements

* Compare multiple regression algorithms.
* Hyperparameter tuning.
* Cross-validation.
* Feature importance analysis.
* Cloud deployment.
* API integration.

---

# 👨‍💻 Author

**Abdelrhman Tamer**

Machine Learning & Data Science Enthusiast

Developed as an end-to-end Machine Learning Regression project using Python and Streamlit.
