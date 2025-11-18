import streamlit as st
import pandas as pd

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

# Task 02
st.title("Task 02")

# Task 03
streamlit.title("Task 03")
#막대 그래프 생성
chart_data = pandas.DataFrame(
    {
        "X 축": list(range(20)) * 3,
        "Y 축": numpy.random.randn(60),
        "색": ["A"] * 20 + ["B"] * 20 + ["C"] * 20
    }
)
#막대 그래프 출력
streamlit.bar_chart(chart_data, x="X 축", y="Y 축", color = "색")
#선 그래프 생성
line_data = pandas.DataFrame(
    numpy.random.randn(20, 3),
    columns=["A", "B", "C"]
)
#선 그래프 출력
streamlit.line_chart(line_data)
#영역 그래프 생성
area_data = pandas.DataFrame(
    numpy.random.randn(20, 3),
    columns=["A", "B", "C"]
)
#영역 그래프 출력
streamlit.area_chart(area_data)

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

# Task 07
st.title("Task 07")
