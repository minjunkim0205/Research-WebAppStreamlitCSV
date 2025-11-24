import streamlit as st
import pandas as pd
import numpy as np

# Page setting
st.set_page_config(
    page_title="Week11주차 Streamlit CSV Read 팀 프로젝트",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="auto"
)
file = pd.read_csv("./penguins.csv")

# Task 01
st.title("Task 01")
if 'name' not in st.session_state:
    st.session_state['name'] = ''

if 'age' not in st.session_state:
    st.session_state['age'] = 25  # 기본값 25로 세팅

if 'color' not in st.session_state:
    st.session_state['color'] = ''

name_input = st.text_input("이름을 입력하세요.", value=st.session_state['name'])

# ✅ key 제거, value를 session_state 값으로 사용
age_input = st.slider("나이", min_value=0, max_value=100, value=st.session_state['age'])

color_input = st.selectbox("좋아하는 색상", ['red','orange','green','blue','violet'])

agree = st.checkbox("이용 약관에 동의합니다.")

if st.button('제출'):
    st.session_state['name'] = name_input
    st.session_state['age'] = age_input
    st.session_state['color'] = color_input
    st.success("제출이 완료되었습니다!")

# Task 02
st.title("Task 02")
if st.session_state['name']:
    st.write(f"**이름:** {st.session_state['name']}")
    st.write(f"**나이:** {st.session_state['age']}")
    st.write(f"**좋아하는 색상:** {st.session_state['color']}")
# Task 03
st.title("Task 03")
# 막대 그래프 생성
chart_data = pd.DataFrame(
    {
        "X 축": list(range(20)) * 3,
        "Y 축": np.random.randn(60),
        "색": ["A"] * 20 + ["B"] * 20 + ["C"] * 20
    }
)
# 막대 그래프 출력
st.bar_chart(chart_data, x="X 축", y="Y 축", color="색")

# 선 그래프 생성
line_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
# 선 그래프 출력
st.line_chart(line_data)

# 영역 그래프 생성
area_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
# 영역 그래프 출력
st.area_chart(area_data)

# Task 04
st.title("Task 04")

st.subheader("펭귄 데이터")
species_list = file["species"].unique()
island_list = file["island"].unique()

species_filter = st.multiselect(
    "종 선택 (species):",
    options=species_list,
    default=species_list
)
island_filter = st.multiselect(
    "서식지 섬 선택 (island):",
    options=island_list,
    default=island_list
)

min_value, max_value = int(file["bill_length_mm"].min()), int(file["bill_length_mm"].max())
bill_length_range = st.slider(
    "부리 길이 범위 (bill_length_mm):",
    min_value=min_value,
    max_value=max_value,
    value=(min_value, max_value)
)

filtered_file = file[
    (file["species"].isin(species_filter)) &
    (file["island"].isin(island_filter)) &
    (file["bill_length_mm"] >= bill_length_range[0]) &
    (file["bill_length_mm"] <= bill_length_range[1])
]

st.subheader("필터링된 데이터")
st.dataframe(filtered_file)
st.write(f"총 {len(filtered_file)}개 행이 선택되었습니다.")

# Task 05
st.title("Task 05")

st.subheader("데이터 미리보기")
st.dataframe(file)


# Task 06
st.title("Task 06")

# 컬럼 레이아웃 생성
col1, col2, col3 = st.columns(3)

with col1:
    st.header("컬럼 1")
    st.write("첫 번째 컬럼입니다.")
    st.metric(label="펭귄 총 개체수", value=len(file), delta="100%")

with col2:
    st.header("컬럼 2")
    st.write("두 번째 컬럼입니다.")
    st.metric(label="평균 부리 길이", value=f"{file['bill_length_mm'].mean():.2f}mm", delta="1.2mm")

with col3:
    st.header("컬럼 3")
    st.write("세 번째 컬럼입니다.")
    st.metric(label="펭귄 종 수", value=len(file['species'].unique()), delta="3종")

# 탭 생성
tab1, tab2, tab3 = st.tabs(["📊 데이터", "📈 통계", "🐧 정보"])

with tab1:
    st.subheader("펭귄 데이터 테이블")
    st.dataframe(file.head(10))

with tab2:
    st.subheader("기본 통계")
    st.write(file.describe())

with tab3:
    st.subheader("펭귄 종 정보")
    st.write("이 데이터셋에는 Adelie, Chinstrap, Gentoo 세 종의 펭귄이 포함되어 있습니다.")

# Expander 생성
with st.expander("더 많은 정보 보기"):
    st.write("**데이터셋 정보:**")
    st.write(f"- 총 행 수: {len(file)}")
    st.write(f"- 총 열 수: {len(file.columns)}")
    st.write(f"- 결측치: {file.isnull().sum().sum()}개")

# Task 07
st.title("Task 07")

st.subheader("종합 대시보드 - 모든 기능 통합")

# 사이드바에 필터 추가
st.sidebar.header("필터 옵션")
sidebar_species = st.sidebar.multiselect(
    "종 선택:",
    options=file["species"].unique(),
    default=file["species"].unique()
)

sidebar_island = st.sidebar.multiselect(
    "섬 선택:",
    options=file["island"].unique(),
    default=file["island"].unique()
)

# 필터링된 데이터
dashboard_filtered = file[
    (file["species"].isin(sidebar_species)) &
    (file["island"].isin(sidebar_island))
]

# 메인 대시보드
col_a, col_b, col_c, col_d = st.columns(4)

with col_a:
    st.metric("총 개체수", len(dashboard_filtered))

with col_b:
    st.metric("평균 체중", f"{dashboard_filtered['body_mass_g'].mean():.0f}g")

with col_c:
    st.metric("평균 부리 길이", f"{dashboard_filtered['bill_length_mm'].mean():.1f}mm")

with col_d:
    st.metric("평균 날개 길이", f"{dashboard_filtered['flipper_length_mm'].mean():.1f}mm")

# 차트 섹션
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("종별 개체수")
    species_count = dashboard_filtered['species'].value_counts()
    st.bar_chart(species_count)

with chart_col2:
    st.subheader("섬별 분포")
    island_count = dashboard_filtered['island'].value_counts()
    st.bar_chart(island_count)

# 상세 데이터 테이블
with st.expander("필터링된 데이터 보기"):
    st.dataframe(dashboard_filtered)
    st.write(f"총 {len(dashboard_filtered)}개의 행이 표시됩니다.")

# 다운로드 버튼
csv = dashboard_filtered.to_csv(index=False).encode('utf-8')
st.download_button(
    label="필터링된 데이터 다운로드 (CSV)",
    data=csv,
    file_name='filtered_penguins.csv',
    mime='text/csv',
)
