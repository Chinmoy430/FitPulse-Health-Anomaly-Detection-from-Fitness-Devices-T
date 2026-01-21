import streamlit as st


def load_css():
    # ✅ Load CSS only once per session
    if st.session_state.get("_css_loaded", False):
        return
    st.session_state["_css_loaded"] = True

    # ✅ FontAwesome CDN
    st.markdown("""
    <link rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
      crossorigin="anonymous" referrerpolicy="no-referrer" />
    """, unsafe_allow_html=True)

    # ✅ ONE premium CSS for entire website
    st.markdown("""
    <style>

    /* =========================
       ✅ GLOBAL APP THEME
       ========================= */
    .stApp {
        background: radial-gradient(circle at top left, #0b1220, #070A12 55%, #05060a) !important;
        color: #e5e7eb !important;
    }

    div[data-testid="stAppViewContainer"] { background: transparent !important; }
    .main, .main p, .main span, .main div { color: #e5e7eb !important; }

    /* Fix random white blocks */
    div[data-testid="stVerticalBlock"],
    div[data-testid="stBlock"] { background: transparent !important; }

    /* Page padding */
    .block-container { padding-top: 1.1rem; padding-bottom: 2rem; }

    /* =========================
       ✅ TOP STREAMLIT NAVBAR (remove white strip)
       ========================= */
    header[data-testid="stHeader"] {
        background: rgba(5, 6, 10, 0.95) !important;
        border-bottom: 1px solid rgba(255,255,255,0.06) !important;
    }
    header[data-testid="stHeader"] * {
        color: #e5e7eb !important;
        fill: #e5e7eb !important;
    }
    div[data-testid="stToolbar"] { background: transparent !important; }

    /* =========================
       ✅ PREMIUM APP HEADER CARD
       ========================= */
    .topbar{
        padding: 18px 22px;
        border-radius: 18px;
        background: linear-gradient(90deg, #1d4ed8, #9333ea);
        border: 1px solid rgba(255,255,255,0.06);
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.35);
        margin-bottom: 18px;
    }
    .topbar h2 { margin: 0; font-weight: 900; }
    .topbar p  { margin: 2px 0 0 0; opacity: 0.85; }

    /* =========================
       ✅ GLASS + KPI CARDS
       ========================= */
    .glass{
        background: rgba(17, 24, 39, 0.65);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 18px;
        padding: 16px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.30);
        color: #e5e7eb;
    }

    .kpi{
        border-radius: 18px;
        padding: 16px;
        background: linear-gradient(135deg, rgba(59,130,246,0.12), rgba(168,85,247,0.10));
        border: 1px solid rgba(255,255,255,0.06);
        box-shadow: 0 10px 25px rgba(0,0,0,0.25);
        color: #e5e7eb;
    }
    .kpi-title { font-size: 13px; opacity: 0.85; }
    .kpi-value { font-size: 26px; font-weight: 900; line-height: 1.1; margin-top: 6px; }
    .kpi-sub   { font-size: 12px; opacity: 0.70; margin-top: 5px; }

    /* Insights */
    .insight{
        border-left: 6px solid #ef4444;
        background: rgba(239,68,68,0.10);
        padding: 12px 14px;
        border-radius: 14px;
        margin-bottom: 10px;
        color: #fca5a5;
    }
    .ok{
        border-left: 6px solid #22c55e;
        background: rgba(34,197,94,0.10);
        padding: 12px 14px;
        border-radius: 14px;
        margin-bottom: 10px;
        color: #86efac;
    }

    /* =========================
       ✅ SIDEBAR PREMIUM BLACK
       ========================= */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #05060a, #0b0f19 60%, #05060a) !important;
        border-right: 1px solid rgba(255,255,255,0.06);
    }
    section[data-testid="stSidebar"] .stSidebarContent {
        padding-top: 18px;
    }

    /* Sidebar user card */
    .user-card{
        background: rgba(17, 24, 39, 0.75);
        padding: 14px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.06);
        box-shadow: 0 10px 25px rgba(0,0,0,0.35);
    }
    .user-name{ font-weight: 900; color: #f8fafc; }
    .user-sub { opacity: 0.75; font-size: 12px; color: #cbd5e1; }
    .badge{
        display: inline-block;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 12px;
        background: rgba(59,130,246,0.18);
        border: 1px solid rgba(59,130,246,0.25);
        margin-top: 8px;
        color: #bfdbfe;
    }

    /* Sidebar navigation styling */
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        padding: 10px 12px !important;
        border-radius: 12px !important;
        color: #cbd5e1 !important;
        background: transparent !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        transition: 0.18s ease-in-out !important;
    }
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
        background: rgba(59, 130, 246, 0.12) !important;
        color: #f8fafc !important;
        transform: translateX(2px);
        border: 1px solid rgba(59,130,246,0.18);
    }
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] li[data-selected="true"] a {
        background: linear-gradient(90deg, rgba(59,130,246,0.22), rgba(168,85,247,0.18)) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        box-shadow: 0 10px 18px rgba(0,0,0,0.25);
    }

    /* =========================
       ✅ INPUTS / BUTTONS / UPLOADER
       ========================= */
    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] > div {
        background: rgba(17, 24, 39, 0.80) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        color: #f1f5f9 !important;
        border-radius: 14px !important;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #111827, #1f2937) !important;
        color: #f8fafc !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
        padding: 0.65rem 1rem !important;
        transition: 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        transform: translateY(-1px);
        border: 1px solid rgba(59,130,246,0.40) !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.35);
    }

    section[data-testid="stFileUploaderDropzone"] {
        background: rgba(17, 24, 39, 0.65) !important;
        border: 1px dashed rgba(255,255,255,0.15) !important;
        border-radius: 16px !important;
        color: #e5e7eb !important;
    }
    section[data-testid="stFileUploaderDropzone"] button {
        background: linear-gradient(90deg, #111827, #1f2937) !important;
        color: #f8fafc !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
    }

    /* Alerts + tables */
    div[data-testid="stAlert"] {
        background: rgba(17, 24, 39, 0.75) !important;
        border: 1px solid rgba(255,255,255,0.06) !important;
        border-radius: 14px !important;
        color: #e5e7eb !important;
    }

    div[data-testid="stDataFrame"] {
        background: rgba(17, 24, 39, 0.55) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255,255,255,0.06) !important;
    }

    </style>
    """, unsafe_allow_html=True)


def header():
    st.markdown("""
    <div class="topbar">
        <h2><i class="fa-solid fa-heart-pulse"></i> Detecting Unusual Health Patterns</h2>
        <p><i class="fa-solid fa-gauge-high"></i> Premium Streamlit Dashboard | Module 1 → 2 → 3 Integration</p>
    </div>
    """, unsafe_allow_html=True)


def sidebar_profile(name="Demo User", role="Fitness Watch User"):
    st.sidebar.markdown(f"""
    <div class="user-card">
        <div class="user-name"><i class="fa-solid fa-user"></i> {name}</div>
        <div class="user-sub">{role}</div>
        <div class="badge"><i class="fa-solid fa-cloud"></i> Streamlit Cloud</div>
    </div>
    """, unsafe_allow_html=True)


def kpi(title, value, sub=""):
    st.markdown(f"""
    <div class="kpi">
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-sub">{sub}</div>
    </div>
    """, unsafe_allow_html=True)


# ✅ Aliases (to match app.py + pages imports)
load_premium_css = load_css
render_header = header
sidebar_user_card = sidebar_profile
kpi_card = kpi
