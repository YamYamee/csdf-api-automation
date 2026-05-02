import streamlit as st
import pandas as pd
import json
from pathlib import Path

# 경로 설정
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CSV_PATH = BASE_DIR / "data" / "azure_api_specs_complete.csv"

st.set_page_config(layout="wide", page_title="Azure API Forensics Browser", page_icon="🕵️")

@st.cache_data
def load_data():
    return pd.read_csv(CSV_PATH, encoding='utf-8-sig')

# --- [개선] JSON 스키마를 계층형 텍스트로 변환하는 함수 ---
def schema_to_text(schema, level=0):
    text = ""
    indent = "　" * level # 가독성을 위한 전각 공백
    
    if not isinstance(schema, dict): return text

    # allOf 처리 (상속 구조 합치기)
    if 'allOf' in schema:
        for sub in schema['allOf']:
            text += schema_to_text(sub, level)

    properties = schema.get('properties', {})
    for key, info in properties.items():
        p_type = info.get('type', 'object')
        # 타입별 이모지
        icon = {"string": "📄", "integer": "🔢", "number": "📈", "boolean": "🔳", "array": "📦", "object": "📁"}.get(p_type, "🔹")
        desc = info.get('description', '설명 없음').replace('\n', ' ')
        
        text += f"{indent}{icon} **{key}** `({p_type})` : {desc}\n\n"
        
        # 하위 구조 탐색
        if 'properties' in info:
            text += schema_to_text(info, level + 1)
        elif 'items' in info and isinstance(info['items'], dict):
            text += f"{indent}　　↳ *Array Items:*\n"
            text += schema_to_text(info['items'], level + 2)
            
    return text

# --- 파라미터 표 렌더링 ---
def render_parameters(params):
    if not params or not isinstance(params, list):
        st.write("파라미터 정보가 없습니다.")
        return
    md = "| 이름 | 위치 | 필수 | 타입 | 설명 |\n| :--- | :--- | :--- | :--- | :--- |\n"
    for p in params:
        name = p.get('name', '-')
        location = p.get('in', '-')
        req = "🔴 필수" if p.get('required') else "선택"
        p_type = p.get('type', 'object')
        desc = p.get('description', '-').replace('\n', ' ')
        md += f"| **{name}** | `{location}` | {req} | `{p_type}` | {desc} |\n"
    st.markdown(md)

# --- [개선] 응답 상세 렌더링 (JSON 대신 텍스트 트리) ---
def render_responses(responses):
    if not responses or not isinstance(responses, dict):
        st.write("응답 정보가 없습니다.")
        return

    codes = sorted(list(responses.keys()))
    tabs = st.tabs([f"Status {code}" for code in codes])

    for i, code in enumerate(codes):
        with tabs[i]:
            res = responses[code]
            st.info(f"**Description:** {res.get('description', '-')}")
            
            schema = res.get('schema') or res.get('content')
            if schema:
                st.markdown("#### 📋 Data Structure (Readable)")
                readable_view = schema_to_text(schema)
                if readable_view:
                    st.markdown(readable_view)
                else:
                    st.write("기본 타입이거나 상세 구조가 정의되지 않았습니다.")
                
                with st.expander("🛠️ Raw JSON View (Technical)"):
                    st.json(schema)

# --- 메인 실행 ---
st.title("🕵️ Azure API Forensics Browser")
st.markdown("---")

try:
    df = load_data()
except:
    st.error("데이터를 찾을 수 없습니다. extract.py를 먼저 실행하세요.")
    st.stop()

# 필터링 및 페이지네이션 (이전과 동일)
search_query = st.sidebar.text_input("🔍 검색", "")
selected_service = st.sidebar.selectbox("📂 서비스", ["전체"] + sorted(df['Service_Path'].unique().astype(str)))
filtered_df = df.copy()
if selected_service != "전체": filtered_df = filtered_df[filtered_df['Service_Path'] == selected_service]
if search_query:
    filtered_df = filtered_df[filtered_df['Endpoint'].str.contains(search_query, case=False) | 
                              filtered_df['Service_Path'].str.contains(search_query, case=False)]

items_per_page = st.sidebar.select_slider("표시 개수", [10, 20, 50], 20)
total_pages = max(1, (len(filtered_df) // items_per_page) + 1)
current_page = st.sidebar.number_input(f"페이지", 1, total_pages, 1)

page_df = filtered_df.iloc[(current_page-1)*items_per_page : current_page*items_per_page]

for _, row in page_df.iterrows():
    m_color = {"GET": "blue", "POST": "green", "PUT": "orange", "DELETE": "red"}.get(row['Method'], "grey")
    with st.expander(f":{m_color}[**{row['Method']}**] `{row['Endpoint']}`"):
        in_tab, out_tab = st.tabs(["📥 Input", "📤 Output"])
        with in_tab: render_parameters(json.loads(row['Parameters']))
        with out_tab: render_responses(json.loads(row['Response']))