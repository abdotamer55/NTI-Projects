import streamlit as st
from pathlib import Path
from Style import load_css

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="Insurance Charges Prediction",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css() 
# =====================================
# Get Project Path
# =====================================

BASE_DIR = Path(__file__).resolve().parent

banner_path = BASE_DIR / "images" / "banner.jpg"

readme_path = BASE_DIR / "README.md"

# =====================================
# Custom CSS
# =====================================

st.markdown("""
<style>

/* Main page spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Banner frame */
[data-testid="stImage"] {
    border: 3px solid #1f77b4;
    border-radius: 20px;
    padding: 7px;
    background-color: white;
    box-shadow: 0 7px 20px rgba(0, 0, 0, 0.18);
}

/* Banner image */
[data-testid="stImage"] img {
    border-radius: 13px;
}

/* Main headings */
h1 {
    color: #0b3c5d;
    text-align: center;
}

/* Section headings */
h2 {
    color: #1f5f8b;
    margin-top: 35px;
}

/* Better text spacing */
p {
    font-size: 17px;
    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# Banner Image
# =====================================

left, center, right = st.columns([2, 3, 2])

with center:

    if banner_path.exists():

        st.image(
            str(banner_path),
            use_container_width=True
        )

    else:

        st.error(
            "Banner image was not found."
        )

        st.code(
            str(banner_path)
        )

# =====================================
# Space After Image
# =====================================

st.markdown("<br>", unsafe_allow_html=True)

# =====================================
# Read README File
# =====================================

if readme_path.exists():

    readme_content = readme_path.read_text(
        encoding="utf-8"
    )

    # Remove banner image from README
    readme_content = readme_content.replace(
        '<p align="center"><img src="images/banner.jpg" alt="Insurance Charges Prediction Banner" width="100%"></p>',
        ""
    )

    readme_content = readme_content.replace(
        '<p align="center"> <img src="images/banner.jpg" alt="Insurance Charges Prediction Banner" width="100%"> </p>',
        ""
    )

    # Display README
    st.markdown(
        readme_content,
        unsafe_allow_html=True
    )

else:

    st.error(
        "README.md file was not found."
    )

    st.info(
        "Make sure README.md is in the same folder as app.py."
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