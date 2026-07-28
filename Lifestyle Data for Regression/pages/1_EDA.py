import streamlit as st
import pandas as pd
from pathlib import Path
from Style import load_css


# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="EDA | Insurance Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load shared CSS
load_css()

# =====================================
# Load Dataset
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

data_path = BASE_DIR / "data" / "insurance.csv"


@st.cache_data
def load_data():

    return pd.read_csv(data_path)


# Check if dataset exists
if not data_path.exists():

    st.error("❌ Dataset file was not found.")

    st.code(str(data_path))

    st.stop()


# Load dataset
df = load_data()


# =====================================
# Page Header
# =====================================

st.title("📊 Exploratory Data Analysis")

st.markdown("""
Explore the dataset structure, data types, missing values,
statistical summaries, and the first records before building
the Machine Learning model.
""")


st.divider()


# =====================================
# Dataset Overview
# =====================================

st.subheader("📌 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Rows",
    f"{df.shape[0]:,}"
)

col2.metric(
    "Total Columns",
    df.shape[1]
)

col3.metric(
    "Missing Values",
    int(df.isnull().sum().sum())
)

col4.metric(
    "Duplicate Rows",
    int(df.duplicated().sum())
)


st.divider()


# =====================================
# First Five Rows
# =====================================

st.subheader("🔍 First Five Rows")

st.write(
    "A preview of the first five records in the dataset."
)

st.dataframe(
    df.head(),
    use_container_width=True
)


st.divider()


# =====================================
# Dataset Information
# =====================================

st.subheader("🧾 Dataset Information")

left, right = st.columns(2)

with left:

    st.markdown(
        "### Column Names"
    )

    columns_df = pd.DataFrame({

        "Column": df.columns,

        "Data Type":
        df.dtypes.astype(str).values

    })

    st.dataframe(
        columns_df,
        use_container_width=True,
        hide_index=True
    )


with right:

    st.markdown(
        "### Missing Values"
    )

    missing_df = pd.DataFrame({

        "Column":
        df.columns,

        "Missing Values":
        df.isnull().sum().values

    })

    st.dataframe(
        missing_df,
        use_container_width=True,
        hide_index=True
    )


st.divider()


# =====================================
# Statistical Summary
# =====================================

st.subheader("📈 Statistical Summary")

st.write(
    "Summary statistics for the numerical features."
)

st.dataframe(
    df.describe(),
    use_container_width=True
)


st.divider()


# =====================================
# Data Quality
# =====================================

st.subheader("🧹 Data Quality Check")

quality_col1, quality_col2 = st.columns(2)

with quality_col1:

    if df.isnull().sum().sum() == 0:

        st.success(
            "✅ No missing values were found."
        )

    else:

        st.warning(
            "⚠️ Missing values were found."
        )


with quality_col2:

    if df.duplicated().sum() == 0:

        st.success(
            "✅ No duplicate rows were found."
        )

    else:

        st.warning(
            "⚠️ Duplicate rows were found."
        )


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