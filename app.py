import streamlit as st

st.set_page_config(
    page_title="우리반 청소 도우미",
    page_icon="🧹",
    layout="wide"
)

# --------------------
# 데이터
# --------------------
NOTICES = [
    "📢 금요일은 특별 대청소가 있습니다.",
    "📢 분리수거함 정리를 꼼꼼히 해주세요.",
    "📢 창문 청소 시 안전에 주의하세요."
]

CLEANING_AREAS = {
    "교실 바닥 청소": "김민준",
    "칠판 정리": "이서연",
    "창문 청소": "박지호",
    "분리수거 정리": "최유진",
    "복도 청소": "정하준"
}

# --------------------
# 제목
# --------------------
st.title("🏫 우리반 청소 도우미")
st.caption("우리 반 청소를 쉽고 즐겁게 관리해보세요!")

# --------------------
# 오늘의 안내
# --------------------
st.success("✨ 오늘도 깨끗한 교실 만들기 프로젝트 진행 중!")

# --------------------
# 공지사항
# --------------------
st.subheader("📢 공지사항")

for notice in NOTICES:
    st.info(notice)

st.divider()

# --------------------
# 당번표
# --------------------
st.subheader("👨‍🎓 오늘의 청소 당번")

col1, col2 = st.columns(2)

areas = list(CLEANING_AREAS.items())

for i, (area, student) in enumerate(areas):

    if i % 2 == 0:
        with col1:
            st.write(f"🧹 **{area}**")
            st.write(f"담당: {student}")
            st.write("")
    else:
        with col2:
            st.write(f"🧹 **{area}**")
            st.write(f"담당: {student}")
            st.write("")

st.divider()

# --------------------
# 체크리스트
# --------------------
st.subheader("✅ 청소 완료 체크")

completed = 0
total = len(CLEANING_AREAS)

try:

    for area in CLEANING_AREAS.keys():
        checked = st.checkbox(area)

        if checked:
            completed += 1

    progress = completed / total

    st.divider()

    st.metric(
        label="청소 진행률",
        value=f"{completed}/{total}"
    )

    st.progress(progress)

    if completed == total:
        st.balloons()
        st.success("🎉 오늘 청소를 모두 완료했습니다!")

except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")

# --------------------
# 하단 메시지
# --------------------
st.divider()

st.markdown(
    """
### 🌟 청소 습관 만들기

- 맡은 구역을 책임감 있게 청소하기
- 분리수거 정확하게 하기
- 책상과 의자 정리하기
- 사용한 물건 제자리에 두기

깨끗한 교실은 우리 모두가 함께 만듭니다!
"""
)
