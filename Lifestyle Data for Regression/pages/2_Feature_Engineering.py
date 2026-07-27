import streamlit as st
import pandas as pd
from pathlib import Path
from Style import load_css


# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="Feature Engineering | Insurance Prediction",
    page_icon="⚙️",
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
# Page Header
# =====================================

st.title("⚙️ Feature Engineering")

st.markdown("""
Feature Engineering is the process of transforming raw data
into meaningful features that help the Machine Learning model
learn patterns and make better predictions.
""")

st.divider()


# =====================================
# Feature Engineering Overview
# =====================================

st.subheader("🎯 Engineering Pipeline")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Original Features",
    df.shape[1] - 1
)

col2.metric(
    "New Features",
    "5"
)

col3.metric(
    "Final Features After Encoding",
    "18"
)

col4.metric(
    "Target",
    "Charges"
)

st.divider()


# =====================================
# Create Features
# =====================================

df_engineered = df.copy()


# =====================================
# 1. BMI Category
# =====================================

st.subheader("1️⃣ BMI Category")

st.markdown("""
BMI was converted into health categories to help the model
capture non-linear relationships between body weight and
insurance charges.
""")


df_engineered["bmi_category"] = pd.cut(
    df_engineered["bmi"],

    bins=[
        0,
        18.5,
        25,
        30,
        float("inf")
    ],

    labels=[
        "Underweight",
        "Normal",
        "Overweight",
        "Obese"
    ]
)


st.dataframe(
    df_engineered[
        [
            "bmi",
            "bmi_category"
        ]
    ].head(10),

    use_container_width=True,

    hide_index=True
)


# =====================================
# 2. Obesity Feature
# =====================================

st.subheader("2️⃣ Obesity Indicator")

st.markdown("""
A binary feature was created to indicate whether the person
is obese.
""")


df_engineered["is_obese"] = (
    df_engineered["bmi"] >= 30
).astype(int)


st.dataframe(
    df_engineered[
        [
            "bmi",
            "is_obese"
        ]
    ].head(10),

    use_container_width=True,

    hide_index=True
)


# =====================================
# 3. Age Groups
# =====================================

st.subheader("3️⃣ Age Groups")

st.markdown("""
Age was grouped into meaningful ranges to help identify
different risk levels across age categories.
""")


df_engineered["age_group"] = pd.cut(
    df_engineered["age"],

    bins=[
        18,
        30,
        45,
        60,
        float("inf")
    ],

    labels=[
        "19-30",
        "31-45",
        "46-60",
        "60+"
    ]
)


st.dataframe(
    df_engineered[
        [
            "age",
            "age_group"
        ]
    ].head(10),

    use_container_width=True,

    hide_index=True
)


# =====================================
# 4. Interaction Features
# =====================================

st.subheader("4️⃣ Interaction Features")

st.markdown("""
Interaction features were created to capture the combined
effect of smoking with BMI and age.
""")


# Encode smoker temporarily

smoker_encoded = (
    df_engineered["smoker"]
    .map({
        "yes": 1,
        "no": 0
    })
)


# BMI × Smoker

df_engineered[
    "smoker_bmi_interaction"
] = (
    smoker_encoded
    *
    df_engineered["bmi"]
)


# Age × Smoker

df_engineered[
    "age_smoker_interaction"
] = (
    smoker_encoded
    *
    df_engineered["age"]
)


interaction_df = df_engineered[
    [
        "age",
        "bmi",
        "smoker",
        "smoker_bmi_interaction",
        "age_smoker_interaction"
    ]
].head(10)


st.dataframe(
    interaction_df,

    use_container_width=True,

    hide_index=True
)


# =====================================
# 5. Encoding
# =====================================

st.subheader("5️⃣ Categorical Encoding")

st.markdown("""
Categorical variables were converted into numerical values
so they can be used by the Linear Regression model.
""")


encoding_col1, encoding_col2 = st.columns(2)


with encoding_col1:

    st.markdown(
        "### Binary Encoding"
    )

    st.code("""
smoker:
yes → 1
no  → 0

sex:
male   → 1
female → 0
""")


with encoding_col2:

    st.markdown(
        "### One-Hot Encoding"
    )

    st.code("""
region:
northwest
southeast
southwest

age_group:
19-30
31-45
46-60
60+

bmi_category:
Normal
Overweight
Obese
""")


st.divider()


# =====================================
# Final Features
# =====================================

st.subheader("📋 Final Model Features")

final_features = [

    "age",

    "bmi",

    "children",

    "is_obese",

    "smoker_bmi_interaction",

    "age_smoker_interaction",

    "smoker_encoded",

    "sex_encoded",

    "region_northwest",

    "region_southeast",

    "region_southwest",

    "age_group_19-30",

    "age_group_31-45",

    "age_group_46-60",

    "age_group_60+",

    "bmi_category_Normal",

    "bmi_category_Overweight",

    "bmi_category_Obese"

]


features_df = pd.DataFrame({

    "Feature Number":
    range(
        1,
        len(final_features) + 1
    ),

    "Feature Name":
    final_features

})


st.dataframe(

    features_df,

    use_container_width=True,

    hide_index=True

)


# =====================================
# Engineering Summary
# =====================================

st.divider()

st.subheader("✅ Feature Engineering Summary")

st.success("""
The raw dataset was transformed using:

• BMI categories

• Obesity indicator

• Age groups

• Smoking interaction features

• Binary encoding

• One-Hot encoding

These transformations provide more meaningful information
to the Linear Regression model and help improve prediction
performance.
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