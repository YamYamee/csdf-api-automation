import streamlit as st
import pandas as pd
import json
import re
from pathlib import Path

# --- [1] 경로 및 설정 ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CSV_PATH = BASE_DIR / "data" / "aws_api_specs_complete.csv"

st.set_page_config(layout="wide", page_title="AWS API FORENSICS", page_icon=None)

# --- [2] Navy & White Minimal CSS ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stApp { color: #0f172a; font-family: 'Inter', sans-serif; }
    .system-title {
        color: #0f172a; font-size: 1.5rem; font-weight: 800;
        border-left: 4px solid #1e3a8a; padding-left: 12px; margin-bottom: 20px;
    }
    .method-badge {
        padding: 2px 6px; border-radius: 2px; font-weight: 600;
        font-family: 'JetBrains Mono', monospace; font-size: 0.7rem;
        border: 1px solid #cbd5e1; background-color: #f8fafc;
    }
    [data-testid="stSidebar"] { background-color: #0f172a; border-right: 1px solid #1e293b; }
    [data-testid="stSidebar"] * { color: #f8fafc !important; }
    .stExpander { border: 1px solid #e2e8f0 !important; border-radius: 0px !important; }
    .stTabs [data-baseweb="tab"] { background-color: #f8fafc; border: 1px solid #e2e8f0; }
    thead tr th { background-color: #f1f5f9 !important; color: #0f172a !important; font-size: 0.8rem; }
    </style>
""", unsafe_allow_html=True)

# --- [3] 유틸리티: HTML 태그 제거 ---
def clean_html(raw_html):
    if not raw_html: return "-"
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext.strip()

# --- [4] 데이터 로드 ---
@st.cache_data
def load_data():
    if not CSV_PATH.exists(): return pd.DataFrame()
    try:
        return pd.read_csv(CSV_PATH, encoding='utf-8-sig').fillna("")
    except:
        return pd.DataFrame()

# --- [5] 파라미터 렌더링 (Structure/Members 대응) ---
def render_params(params_raw):
    if not params_raw or params_raw in ["", "[]", "{}"]:
        st.text("SPECIFICATION: NO PARAMETERS DEFINED")
        return

    try:
        # 데이터가 문자열로 두 번 감싸져 있을 경우를 대비한 처리
        data = json.loads(params_raw) if isinstance(params_raw, str) else params_raw
        if isinstance(data, str): data = json.loads(data)

        normalized = []

        # Case 1: Structure 기반 (주신 데이터 형식)
        if isinstance(data, dict) and "members" in data:
            members = data.get("members", {})
            resolved = data.get("resolved_members", {})
            required_list = data.get("required", [])

            for field, info in members.items():
                res_info = resolved.get(field, {})
                normalized.append({
                    "FIELD": field,
                    "TYPE": res_info.get("type") or info.get("shape") or "string",
                    "REQUIRED": "TRUE" if field in required_list else "FALSE",
                    "DESCRIPTION": clean_html(info.get("documentation", "-"))
                })

        # Case 2: 일반적인 리스트 기반 (Swagger)
        elif isinstance(data, list):
            for p in data:
                normalized.append({
                    "FIELD": p.get('name') or p.get('key') or "unknown",
                    "TYPE": p.get('type') or "object",
                    "REQUIRED": "TRUE" if p.get('required') is True else "FALSE",
                    "DESCRIPTION": p.get('description') or "-"
                })

        if normalized:
            st.table(pd.DataFrame(normalized))
        else:
            st.text("NO RENDERABLE PARAMETERS FOUND")
            with st.expander("VIEW RAW"):
                st.json(data)

    except Exception as e:
        st.error(f"PARSING ERROR: {str(e)}")

# --- [6] 메인 실행 ---
st.markdown('<div class="system-title">AWS API FORENSICS ANALYSIS</div>', unsafe_allow_html=True)

df = load_data()
if df.empty:
    st.error("DATA NOT FOUND: CHECK CSV PATH")
    st.stop()

# 사이드바 필터
st.sidebar.markdown("### SYSTEM FILTER")
search_query = st.sidebar.text_input("SEARCH ENDPOINT")
services = ["ALL SERVICES"] + sorted(df['Service_Path'].unique().tolist())
selected_service = st.sidebar.selectbox("SERVICE DOMAIN", services)

filtered_df = df
if selected_service != "ALL SERVICES":
    filtered_df = filtered_df[filtered_df['Service_Path'] == selected_service]
if search_query:
    filtered_df = filtered_df[filtered_df['Endpoint'].str.contains(search_query, case=False)]

# 결과 리스트
items_per_page = 15
total_pages = max(1, (len(filtered_df) // items_per_page) + 1)
page = st.select_slider("PAGE SELECTION", options=range(1, total_pages + 1), value=1)

page_df = filtered_df.iloc[(page-1)*items_per_page : page*items_per_page]

for _, row in page_df.iterrows():
    with st.expander(f"{row['Method']} | {row['Endpoint']}"):
        st.caption(f"SERVICE: {row['Service_Path']}")
        t1, t2, t3 = st.tabs(["PARAMETERS", "RESPONSE", "RAW"])
        
        with t1:
            render_params(row['Parameters'])
        with t2:
            st.json(json.loads(row['Response']) if row['Response'] else {})
        with t3:
            st.json({"parameters": row['Parameters'], "response": row['Response']})