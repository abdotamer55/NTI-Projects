# 🚢 Titanic Survival Analysis

<p align="center">

![Python](https://img.shields.io/badge/Python-Data%20Analysis-blue?style=for-the-badge\&logo=python)

![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge\&logo=pandas)

![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?style=for-the-badge\&logo=numpy)

![Matplotlib](https://img.shields.io/badge/Matplotlib-Data%20Visualization-orange?style=for-the-badge)

![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualization-blue?style=for-the-badge)

![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Data%20Preprocessing-orange?style=for-the-badge\&logo=scikitlearn)

</p>

---

## 📌 Project Overview

The sinking of the RMS Titanic is one of the most well-known maritime disasters in history. This project performs a complete **Exploratory Data Analysis (EDA)** on the Titanic passenger dataset to identify the demographic, social, and economic factors associated with passenger survival.

The project follows a complete data analysis workflow, starting with data understanding and quality assessment, followed by data cleaning, feature engineering, exploratory analysis, visualization, and data preparation for future machine learning models.

The analysis focuses on answering important questions such as:

* Did gender influence survival?
* Did passenger class affect survival chances?
* Were children more likely to survive?
* Did ticket fare influence survival?
* How did family size affect survival?
* Did social titles provide additional information about survival?
* Did cabin availability have a relationship with survival?

---

## 🎯 Project Objectives

The main objectives of this project are to:

* Understand the structure and quality of the Titanic dataset.
* Identify and handle missing values.
* Detect duplicate records and logical data anomalies.
* Analyze relationships between passenger characteristics and survival.
* Create meaningful features from the original data.
* Visualize important patterns and trends.
* Identify the strongest factors associated with passenger survival.
* Prepare the dataset for future machine learning classification models.

---

## 📂 Dataset

The dataset contains information about Titanic passengers, including demographic details, travel information, family relationships, and survival status.

### 🎯 Target Variable

* **Survived**

  * `0` → Passenger did not survive.
  * `1` → Passenger survived.

### 📥 Original Features

* `PassengerId` — Unique passenger identifier.
* `Pclass` — Passenger ticket class.
* `Name` — Passenger name.
* `Sex` — Passenger gender.
* `Age` — Passenger age.
* `SibSp` — Number of siblings or spouses aboard.
* `Parch` — Number of parents or children aboard.
* `Ticket` — Ticket number.
* `Fare` — Ticket fare.
* `Cabin` — Cabin number.
* `Embarked` — Port of embarkation.

---

## 🧹 Data Cleaning and Preprocessing

The following data preparation steps were performed:

* Removed duplicate records.
* Checked for duplicate passenger IDs.
* Identified missing values.
* Filled missing `Age` values using the median.
* Filled missing `Embarked` values using the most frequent value.
* Created a cabin availability indicator before removing the sparse `Cabin` column.
* Handled missing `Fare` values using the median.
* Removed unnecessary columns.
* Removed extra spaces from text values.
* Standardized gender values.
* Converted embarkation codes into readable port names.
* Checked for invalid ages and logical anomalies.
* Checked for negative family counts and invalid fare values.
* Investigated zero-fare passenger records.
* Detected and analyzed outliers using the **IQR method**.

---

## ⚙️ Feature Engineering

Several new features were created to improve the analysis and provide more meaningful insights.

### 👨‍👩‍👧 Family Features

* **FamilySize**

```text
FamilySize = SibSp + Parch + 1
```

Represents the total number of family members traveling together, including the passenger.

* **IsAlone**

Indicates whether a passenger was traveling alone.

### 👤 Passenger Title

Passenger titles were extracted from the `Name` column, such as:

* Mr
* Mrs
* Miss
* Master
* Rare Titles

The `Title` feature provides useful information related to age, gender, and social status.

### 🎂 Age Groups

Passengers were grouped into age categories to better analyze age-related survival patterns.

Examples include:

* Child
* Young Adult
* Adult
* Senior

### 💰 Fare per Person

```text
Fare_per_Person = Fare / FamilySize
```

This feature provides a more meaningful estimate of the travel cost associated with each passenger.

### 🛏️ Cabin Availability

* **Has_Cabin**

  * `1` → Cabin information is available.
  * `0` → Cabin information is missing.

This feature helps preserve useful information from the original `Cabin` column without using the sparse raw values.

---

## 📊 Exploratory Data Analysis

The project includes several visualizations to explore the relationship between passenger characteristics and survival.

### Visualizations Included

* Overall Survival Distribution
* Survival Rate by Gender
* Survival Rate by Passenger Class
* Correlation Heatmap
* Age Distribution by Survival Status
* Fare Distribution by Survival Status
* Family Size vs Survival
* Traveling Alone vs Survival
* Passenger Title vs Survival

---

## 🔍 Key Insights

### 1. Gender Was the Strongest Survival Factor

Female passengers had a significantly higher survival rate than male passengers.

This pattern is consistent with the historical **“women and children first”** evacuation policy.

### 2. Passenger Class Had a Major Impact

Survival rates decreased from First Class to Third Class.

Passengers in First Class generally had better access to lifeboats and more favorable evacuation conditions.

### 3. Children Had a Survival Advantage

Survivors were generally younger, and young children had better survival chances than many adult passengers.

Age alone was not the strongest predictor, but it became more useful when combined with age groups and passenger titles.

### 4. Higher Fares Were Associated with Higher Survival

Passengers who paid higher fares generally had higher survival rates.

Fare acted as an indicator of passenger class, wealth, and cabin location.

### 5. Family Size Had a Non-Linear Effect

Passengers traveling in small families generally had better survival rates.

Passengers traveling alone and those traveling in very large families had lower survival rates.

### 6. Passenger Titles Added Valuable Information

Titles such as **Mrs** and **Miss** showed higher survival rates.

The **Master** title, commonly associated with young boys, had a better survival rate than **Mr**.

The **Mr** title had the lowest survival rate among the main passenger title groups.

### 7. Cabin Availability Was Informative

Passengers with recorded cabin information generally had better survival outcomes.

The `Has_Cabin` feature provided useful information while avoiding the high number of missing values in the original `Cabin` column.

---

## 📈 Executive Summary

The analysis indicates that **Gender** and **Passenger Class** were the strongest factors associated with survival.

The highest-risk passenger profile was generally:

> An adult male traveling in Third Class, traveling alone or with a very large family, paying a low fare, and having no recorded cabin information.

The most valuable engineered features were:

* `Title`
* `FamilySize`
* `IsAlone`
* `AgeGroup`
* `Fare_per_Person`
* `Has_Cabin`

These features can be used as important inputs for a future machine learning classification model.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Jupyter Notebook

---

## 📁 Project Structure

```text
Titanic-Project/
│
├── data/
│   └── titanic-1.csv
│
├── notebook/
│   └── Titanic_Analysis_Updated.ipynb
│
└── README.md

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Titanic-Survival-Analysis.git
```

### 2. Open the Project Folder

```bash
cd Titanic-Survival-Analysis
```

### 3. Install the Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

### 5. Open the Notebook

```text
Titanic_Analysis_Updated.ipynb
```

---

## 🚀 Future Improvements

* Build machine learning models to predict passenger survival.
* Compare multiple classification algorithms.
* Apply cross-validation.
* Perform hyperparameter tuning.
* Analyze feature importance.
* Evaluate models using accuracy, precision, recall, F1-score, and ROC-AUC.
* Deploy the final model using Streamlit.
* Add an interactive dashboard for exploring survival patterns.

---

## 👨‍💻 Author

### Abdelrhman Tamer

AI Engineer & Data Analyst

Passionate about:

* Artificial Intelligence
* Machine Learning
* Data Analysis
* Python Development

---

## ⭐ If you found this project useful, consider giving it a Star on GitHub!
