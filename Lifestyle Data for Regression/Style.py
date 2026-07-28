import streamlit as st


def load_css():

    st.markdown("""
    <style>

    /* =========================================
       PROFESSIONAL DARK THEME
    ========================================= */

    :root {
        --bg-main: #0B1220;
        --bg-secondary: #111827;
        --bg-card: #172033;

        --primary: #38BDF8;
        --primary-dark: #0284C7;

        --text-main: #F8FAFC;
        --text-secondary: #CBD5E1;

        --border: #293548;
    }


    /* =========================================
       MAIN APP
    ========================================= */

    [data-testid="stAppViewContainer"] {
        background:
        linear-gradient(
            135deg,
            #0B1220,
            #111827
        );
    }

    .block-container {
        max-width: 1250px;

        padding-top: 2.5rem;

        padding-bottom: 3rem;
    }


    /* =========================================
       TEXT
    ========================================= */

    [data-testid="stAppViewContainer"] p,
    [data-testid="stAppViewContainer"] span,
    [data-testid="stAppViewContainer"] li,
    [data-testid="stAppViewContainer"] label {
        color: #CBD5E1 !important;
    }

    h1 {
        color: #F8FAFC !important;

        font-size: 42px;

        font-weight: 800;

        letter-spacing: -1px;
    }

    h2 {
        color: #38BDF8 !important;

        font-size: 30px;

        font-weight: 750;

        margin-top: 35px;
    }

    h3 {
        color: #7DD3FC !important;

        font-weight: 700;
    }


    /* =========================================
       SIDEBAR
    ========================================= */

    [data-testid="stSidebar"] {
        background:
        linear-gradient(
            180deg,
            #111827,
            #080D17
        );

        border-right:
        1px solid #293548;
    }

    .sidebar-title {
        color: #F8FAFC;

        text-align: center;

        font-size: 25px;

        font-weight: 800;

        padding-top: 15px;
    }

    .sidebar-subtitle {
        color: #94A3B8;

        text-align: center;

        font-size: 13px;

        margin-bottom: 20px;
    }


    /* Navigation */

    [data-testid="stSidebarNav"] a {

        color: #CBD5E1 !important;

        font-size: 16px;

        font-weight: 600;

        border-radius: 12px;

        padding: 12px 15px;

        margin: 7px 10px;

        transition: 0.2s;

    }

    /* Hover */

    [data-testid="stSidebarNav"] a:hover {

        background-color:
        rgba(56, 189, 248, 0.12);

        color:
        #FFFFFF !important;

        transform:
        translateX(4px);

    }

    /* Active page */

    [data-testid="stSidebarNav"] a[aria-current="page"] {

        background:
        linear-gradient(
            90deg,
            #0284C7,
            #38BDF8
        );

        color:
        #FFFFFF !important;

        box-shadow:
        0 5px 16px
        rgba(56, 189, 248, 0.20);

    }


    /* =========================================
       CARDS
    ========================================= */

    .custom-card {

        background-color:
        #172033;

        border:
        1px solid #293548;

        border-radius:
        16px;

        padding:
        22px;

        box-shadow:
        0 8px 25px
        rgba(0, 0, 0, 0.25);

        margin-bottom:
        20px;

    }


    /* =========================================
       METRICS
    ========================================= */

    [data-testid="stMetric"] {

        background-color:
        #172033;

        border:
        1px solid #293548;

        border-radius:
        15px;

        padding:
        18px;

        box-shadow:
        0 7px 20px
        rgba(0, 0, 0, 0.20);

    }

    [data-testid="stMetricLabel"] {

        color:
        #94A3B8 !important;

    }

    [data-testid="stMetricValue"] {

        color:
        #38BDF8 !important;

    }


    /* =========================================
       BUTTONS
    ========================================= */

    .stButton > button {

        width:
        100%;

        border:
        none;

        border-radius:
        11px;

        padding:
        11px;

        background:
        linear-gradient(
            90deg,
            #0284C7,
            #38BDF8
        );

        color:
        white !important;

        font-size:
        16px;

        font-weight:
        700;

        transition:
        0.2s;

    }

    .stButton > button:hover {

        transform:
        translateY(-2px);

        box-shadow:
        0 7px 18px
        rgba(56, 189, 248, 0.25);

    }


    /* =========================================
       INPUTS
    ========================================= */

    input {

        background-color:
        #111827 !important;

        color:
        white !important;

        border:
        1px solid #334155 !important;

        border-radius:
        10px !important;

    }

    [data-baseweb="select"] {

        background-color:
        #111827;

        border-radius:
        10px;

    }


    /* =========================================
       DATAFRAME
    ========================================= */

    [data-testid="stDataFrame"] {

        border:
        1px solid #293548;

        border-radius:
        13px;

        overflow:
        hidden;

        box-shadow:
        0 7px 20px
        rgba(0, 0, 0, 0.20);

    }


    /* =========================================
       EXPANDER
    ========================================= */

    [data-testid="stExpander"] {

        background-color:
        #172033;

        border:
        1px solid #293548;

        border-radius:
        12px;

    }


    /* =========================================
       ALERTS
    ========================================= */

    [data-testid="stAlert"] {

        border-radius:
        12px;

    }


    /* =========================================
       DIVIDER
    ========================================= */

    hr {

        border-color:
        #293548;

        margin-top:
        30px;

        margin-bottom:
        30px;

    }


    /* =========================================
       CODE BLOCK
    ========================================= */

    pre {

        background-color:
        #080D17 !important;

        border:
        1px solid #293548;

        border-radius:
        12px;

    }


    /* =========================================
       FOOTER
    ========================================= */

    .footer {

        text-align:
        center;

        color:
        #94A3B8 !important;

        font-size:
        14px;

        padding:
        20px;

    }

    </style>
    """, unsafe_allow_html=True)