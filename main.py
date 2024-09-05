import streamlit as st
from pdf2image import convert_from_path

@st.cache_data
def load_images(pdf_file):
    return convert_from_path(pdf_file, dpi=150)

# PDF 파일 경로
pdf_file = "refactoring_onboarding.pdf"

# PDF를 이미지로 변환
images = load_images(pdf_file)

# 현재 페이지 인덱스 초기화
if 'page_index' not in st.session_state:
    st.session_state.page_index = 0

# 슬라이드 이동 함수
def go_to_previous_page():
    if st.session_state.page_index > 0:
        st.session_state.page_index -= 1

def go_to_next_page():
    if st.session_state.page_index < len(images) - 1:
        st.session_state.page_index += 1

# 좌우 버튼 추가
col_left, col_center, col_right = st.columns([1, 5, 1])  # 비율로 열을 나누기

with col_left:
    if st.button("◀", key='left_button'):
        go_to_previous_page()

with col_center:
    # 현재 페이지의 이미지 표시
    st.image(images[st.session_state.page_index], use_column_width=True)

with col_right:
    if st.button("▶", key='right_button'):
        go_to_next_page()

# 페이지 번호 중앙 표시
col_page = st.columns([1, 2, 1])  # 비율로 열을 나누기
with col_page[1]:  # 중앙 열에 페이지 번호 표시
    st.write(f"페이지 {st.session_state.page_index + 1} / {len(images)}")

## pdf 전체를 표시
#pdf_viewer(pdf_file) 

## 슬라이드 형태로 이미지 표시
#selected_page = st.slider("슬라이드 선택", 0, len(images) - 1)
#st.image(images[selected_page], use_column_width=True)

