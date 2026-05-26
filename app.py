# app.py

import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="체중 관리 앱",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ 체중 관리 앱")

# 세션 상태 초기화
if "weights" not in st.session_state:
    st.session_state.weights = []

# 입력 폼
with st.form("weight_form"):
    weight = st.number_input(
        "체중 입력 (kg)",
        min_value=1.0,
        max_value=300.0,
        step=0.1
    )

    record_date = st.date_input(
        "날짜 선택",
        value=date.today()
    )

    submitted = st.form_submit_button("저장")

    if submitted:
        st.session_state.weights.append({
            "날짜": record_date,
            "체중": weight
        })
        st.success("체중이 저장되었습니다!")

# 데이터 표시
if st.session_state.weights:

    df = pd.DataFrame(st.session_state.weights)

    st.subheader("📋 기록 목록")
    st.dataframe(df, use_container_width=True)

    st.subheader("📈 체중 변화 그래프")

    chart_df = df.sort_values("날짜")
    chart_df = chart_df.set_index("날짜")

    st.line_chart(chart_df["체중"])

else:
    st.info("아직 저장된 체중 기록이 없습니다.")
