import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
from Style import load_css


# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="Prediction | Insurance Prediction",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()


# =====================================
# Project Paths
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "linear_regression_model.pkl"
)

SCALER_PATH = (
    BASE_DIR
    / "models"
    / "scaler.pkl"
)


# =====================================
# Load Model and Scaler
# =====================================

@st.cache_resource
def load_model():

    model = joblib.load(MODEL_PATH)

    scaler = joblib.load(SCALER_PATH)

    return model, scaler


# =====================================
# Check Model Files
# =====================================

if not MODEL_PATH.exists():

    st.error("❌ Model file was not found.")

    st.code(str(MODEL_PATH))

    st.stop()


if not SCALER_PATH.exists():

    st.error("❌ Scaler file was not found.")

    st.code(str(SCALER_PATH))

    st.stop()


# Load model and scaler
model, scaler = load_model()


# =====================================
# Feature Engineering Function
# =====================================

def prepare_input(
    age,
    sex,
    bmi,
    children,
    smoker,
    region
):

    input_data = pd.DataFrame({

        # Basic Features
        "age": [age],

        "bmi": [bmi],

        "children": [children],


        # Obesity Feature
        "is_obese": [
            int(bmi >= 30)
        ],


        # Interaction Features
        "smoker_bmi_interaction": [
            bmi if smoker == "yes"
            else 0
        ],

        "age_smoker_interaction": [
            age if smoker == "yes"
            else 0
        ],


        # Binary Encoding
        "smoker_encoded": [
            1 if smoker == "yes"
            else 0
        ],

        "sex_encoded": [
            1 if sex == "male"
            else 0
        ],


        # Region Encoding
        "region_northwest": [
            1 if region == "northwest"
            else 0
        ],

        "region_southeast": [
            1 if region == "southeast"
            else 0
        ],

        "region_southwest": [
            1 if region == "southwest"
            else 0
        ],


        # Age Group Encoding
        "age_group_19-30": [
            1 if 19 <= age <= 30
            else 0
        ],

        "age_group_31-45": [
            1 if 31 <= age <= 45
            else 0
        ],

        "age_group_46-60": [
            1 if 46 <= age <= 60
            else 0
        ],

        "age_group_60+": [
            1 if age > 60
            else 0
        ],


        # BMI Category Encoding
        "bmi_category_Normal": [
            1 if 18.5 <= bmi < 25
            else 0
        ],

        "bmi_category_Overweight": [
            1 if 25 <= bmi < 30
            else 0
        ],

        "bmi_category_Obese": [
            1 if bmi >= 30
            else 0
        ]

    })

    return input_data


# =====================================
# Page Header
# =====================================

st.title("🤖 Insurance Charges Prediction")

st.markdown("""
Enter your basic information, and the Machine Learning model
will estimate your expected annual medical insurance charges.
""")

st.divider()


# =====================================
# Input Form
# =====================================

st.subheader("📝 Enter Your Information")

with st.form("prediction_form"):

    col1, col2 = st.columns(2)


    # =====================================
    # Left Column
    # =====================================

    with col1:

        age = st.number_input(
            "🎂 Age",
            min_value=18,
            max_value=100,
            value=25,
            step=1
        )

        bmi = st.number_input(
            "⚖️ BMI",
            min_value=10.0,
            max_value=60.0,
            value=25.0,
            step=0.1
        )

        children = st.number_input(
            "👨‍👩‍👧 Number of Children",
            min_value=0,
            max_value=10,
            value=0,
            step=1
        )


    # =====================================
    # Right Column
    # =====================================

    with col2:

        sex = st.selectbox(
            "👤 Gender",
            options=[
                "male",
                "female"
            ]
        )

        smoker = st.selectbox(
            "🚬 Smoking Status",
            options=[
                "no",
                "yes"
            ]
        )

        region = st.selectbox(
            "📍 Region",
            options=[
                "northeast",
                "northwest",
                "southeast",
                "southwest"
            ]
        )


    submitted = st.form_submit_button(
        "🔮 Predict Insurance Charges"
    )


# =====================================
# Prediction
# =====================================

if submitted:

    try:

        # Create all engineered features
        input_df = prepare_input(
            age=age,
            sex=sex,
            bmi=bmi,
            children=children,
            smoker=smoker,
            region=region
        )


        # =====================================
        # Feature Order
        # Must Match Training Data
        # =====================================

        feature_order = [

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


        # Arrange columns
        input_df = input_df[
            feature_order
        ]


        # =====================================
        # Scaling
        # =====================================

        input_scaled = scaler.transform(
            input_df
        )


        # =====================================
        # Prediction
        # =====================================

        prediction = model.predict(
            input_scaled
        )[0]


        # Prevent negative values
        prediction = max(
            prediction,
            0
        )


        # =====================================
        # Display Prediction
        # =====================================

        st.divider()

        st.subheader(
            "📊 Prediction Result"
        )


        result_col1, result_col2 = st.columns(
            [2, 1]
        )


        with result_col1:

            st.success(
                "✅ Prediction completed successfully!"
            )

            st.markdown(
                f"""
                <div class="custom-card">

                <h3>
                Estimated Annual Insurance Cost
                </h3>

                <h1>
                ${prediction:,.2f}
                </h1>

                </div>
                """,
                unsafe_allow_html=True
            )


        with result_col2:

            st.metric(
                "Estimated Charges",
                f"${prediction:,.2f}"
            )

            st.metric(
                "Model R² Score",
                "0.886"
            )


        # =====================================
        # Personalized Recommendations
        # =====================================

        st.divider()

        st.subheader(
            "💡 Personalized Recommendations"
        )

        tips = []


        # =====================================
        # Smoking Recommendation
        # =====================================

        if smoker == "yes":

            tips.append(
                {
                    "title": "🚭 Smoking Recommendation",

                    "text": """
                    Smoking is one of the strongest factors
                    associated with higher insurance charges.

                    Reducing or quitting smoking may improve
                    long-term health and could help reduce
                    insurance costs depending on the insurer
                    and policy.
                    """
                }
            )

        else:

            tips.append(
                {
                    "title": "✅ Great Job!",

                    "text": """
                    Being a non-smoker is a positive health
                    factor and may contribute to lower
                    insurance costs.
                    """
                }
            )


        # =====================================
        # BMI Recommendation
        # =====================================

        if bmi >= 30:

            tips.append(
                {
                    "title": "⚖️ BMI Recommendation",

                    "text": """
                    Your BMI is in the obesity range.

                    Gradual weight management through balanced
                    nutrition and regular physical activity
                    may improve long-term health.
                    """
                }
            )

        elif bmi >= 25:

            tips.append(
                {
                    "title": "🏃 Stay Active",

                    "text": """
                    Your BMI is in the overweight range.

                    Regular exercise and balanced nutrition
                    may help improve your overall health.
                    """
                }
            )

        else:

            tips.append(
                {
                    "title": "🌟 Healthy BMI",

                    "text": """
                    Your BMI is within a generally healthy range.

                    Continue maintaining balanced nutrition
                    and regular physical activity.
                    """
                }
            )


        # =====================================
        # Age Recommendation
        # =====================================

        if age >= 45:

            tips.append(
                {
                    "title": "🩺 Preventive Care",

                    "text": """
                    Regular health checkups and preventive
                    screenings can help identify health
                    concerns early.
                    """
                }
            )


        # =====================================
        # Display Tips
        # =====================================

        tip_columns = st.columns(
            min(
                len(tips),
                3
            )
        )


        for index, tip in enumerate(tips):

            with tip_columns[
                index % len(tip_columns)
            ]:

                st.markdown(
                    f"""
                    <div class="custom-card">

                    <h3>
                    {tip["title"]}
                    </h3>

                    <p>
                    {tip["text"]}
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # =====================================
        # Disclaimer
        # =====================================

        st.caption(
            """
            ⚠️ These recommendations are general educational
            guidance and are not medical advice. They do not
            guarantee lower insurance premiums. Actual insurance
            costs depend on the insurer, policy, location,
            coverage, and other factors.
            """
        )


    except Exception as error:

        st.error(
            "❌ An error occurred during prediction."
        )

        st.exception(
            error
        )


# =====================================
# Model Information
# =====================================

st.divider()

st.subheader(
    "🧠 Model Information"
)

info1, info2, info3 = st.columns(3)

info1.metric(
    "Model",
    "Linear Regression"
)

info2.metric(
    "Test R²",
    "0.886"
)

info3.metric(
    "User Inputs",
    "6"
)


# =====================================
# Footer
# =====================================

st.divider()

st.markdown("""
<div class="footer">

Insurance Charges Prediction Project<br>

Developed by <b>Abdo Tamer</b> 💻

</div>
""", unsafe_allow_html=True)