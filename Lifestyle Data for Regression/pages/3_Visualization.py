import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from Style import load_css


# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="Visualization | Insurance Prediction",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()


# =====================================
# Load Dataset
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

data_path = BASE_DIR / "data" / "insurance.csv"


@st.cache_data
def load_data():
    return pd.read_csv(data_path)


if not data_path.exists():

    st.error("❌ Dataset file was not found.")

    st.code(str(data_path))

    st.stop()


df = load_data()


# =====================================
# Plot Style
# =====================================

plt.style.use("dark_background")

sns.set_theme(
    style="darkgrid"
)


# =====================================
# Page Header
# =====================================

st.title("📈 Data Visualization")

st.markdown("""
Explore the distributions, relationships, and patterns
between customer characteristics and medical insurance charges.
""")

st.divider()


# =====================================
# Key Insights
# =====================================

st.subheader("💡 Quick Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 🚬 Smoking

Smokers generally have much higher
insurance charges than non-smokers.
""")

with col2:
    st.info("""
### ⚖️ BMI

Higher BMI values may be associated
with increased medical costs.
""")

with col3:
    st.info("""
### 🎂 Age

Insurance charges generally increase
as age increases.
""")

st.divider()


# =====================================
# 1. Charges Distribution
# =====================================

st.subheader("1️⃣ Insurance Charges Distribution")

st.write("""
This histogram shows how medical insurance charges
are distributed across all customers.
""")

fig, ax = plt.subplots(
    figsize=(11, 5)
)

sns.histplot(
    data=df,
    x="charges",
    bins=30,
    kde=True,
    ax=ax
)

ax.set_title(
    "Distribution of Insurance Charges",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel(
    "Insurance Charges"
)

ax.set_ylabel(
    "Number of Customers"
)

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)

st.divider()


# =====================================
# 2. Charges by Smoker
# =====================================

st.subheader("2️⃣ Insurance Charges by Smoking Status")

st.write("""
This chart compares insurance charges
between smokers and non-smokers.
""")

fig, ax = plt.subplots(
    figsize=(10, 5)
)

sns.boxplot(
    data=df,
    x="smoker",
    y="charges",
    ax=ax
)

ax.set_title(
    "Insurance Charges by Smoking Status",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel(
    "Smoking Status"
)

ax.set_ylabel(
    "Insurance Charges"
)

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)

st.divider()


# =====================================
# 3. Age vs Charges
# =====================================

st.subheader("3️⃣ Age vs Insurance Charges")

st.write("""
This scatter plot shows the relationship
between age and medical insurance charges.
""")

fig, ax = plt.subplots(
    figsize=(11, 5)
)

sns.scatterplot(
    data=df,
    x="age",
    y="charges",
    hue="smoker",
    alpha=0.75,
    ax=ax
)

ax.set_title(
    "Age vs Insurance Charges",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel(
    "Age"
)

ax.set_ylabel(
    "Insurance Charges"
)

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)

st.divider()


# =====================================
# 4. BMI vs Charges
# =====================================

st.subheader("4️⃣ BMI vs Insurance Charges")

st.write("""
This chart shows the relationship between
BMI and insurance charges.
""")

fig, ax = plt.subplots(
    figsize=(11, 5)
)

sns.scatterplot(
    data=df,
    x="bmi",
    y="charges",
    hue="smoker",
    alpha=0.75,
    ax=ax
)

ax.set_title(
    "BMI vs Insurance Charges",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel(
    "BMI"
)

ax.set_ylabel(
    "Insurance Charges"
)

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)

st.divider()


# =====================================
# 5. Charges by Region
# =====================================

st.subheader("5️⃣ Average Charges by Region")

st.write("""
This chart compares the average insurance charges
across different geographical regions.
""")

region_avg = (
    df.groupby("region")["charges"]
    .mean()
    .sort_values(
        ascending=False
    )
)

fig, ax = plt.subplots(
    figsize=(10, 5)
)

sns.barplot(
    x=region_avg.index,
    y=region_avg.values,
    ax=ax
)

ax.set_title(
    "Average Insurance Charges by Region",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel(
    "Region"
)

ax.set_ylabel(
    "Average Charges"
)

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)

st.divider()


# =====================================
# 6. Correlation Heatmap
# =====================================

st.subheader("6️⃣ Correlation Heatmap")

st.write("""
The heatmap shows the correlation between
numerical variables in the dataset.
""")

numeric_df = df.select_dtypes(
    include="number"
)

fig, ax = plt.subplots(
    figsize=(10, 7)
)

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f",
    linewidths=0.5,
    ax=ax
)

ax.set_title(
    "Correlation Between Numerical Features",
    fontsize=16,
    fontweight="bold"
)

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)


# =====================================
# Final Insights
# =====================================

st.divider()

st.subheader("✅ Visualization Summary")

st.success("""
The visual analysis highlights several important patterns:

• Smoking status has a strong impact on insurance charges.

• Insurance charges generally increase with age.

• BMI may have a stronger effect on charges for smokers.

• Regional differences exist but appear less influential.

• The relationship between features and charges supports
the use of feature engineering and interaction features.
""")


# =====================================
# Footer
# =====================================

st.divider()

st.markdown("""
<div class="footer">

Insurance Charges Prediction Project<br>

Developed by <b>Abdelrhman Tamer</b> 💻

</div>
""", unsafe_allow_html=True)