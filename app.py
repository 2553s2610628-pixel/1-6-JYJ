import streamlit as st

st.set_page_config(
    page_title="우리반 청소 도우미",
    page_icon="🧹",
    layout="wide"
)

# ----------------------
# 출석번호 (26번 제외)
# ----------------------
students = [i for i in range(1, 37) if i != 26]

# ----------------------
# 공지사항
# ----------------------
notices = [
    "금요일은 특별 대청소가 있습니다.",
    "분리수거는 반드시 종류별로 구분해주세요.",
    "창문 청소 시 안전에 주의하세요."
]

# ----------------------
# 청소 구역
# ----------------------
cleaning_areas = [
    "교실 바닥 청소",
    "칠판 정리",
    "창문 청소",
    "분리수거 정리",
    "복도 청소"
]

# 담당 번호 자동 배정
duty_assignments = {
    area: students[index]
    for index, area in enumerate(cleaning_areas)
}

# ----------------------
# 제목
# ----------------------
st.title("🏫 우리반 청소 도우미")
st.caption("깨끗한 교실은 우리 모두가 함께 만듭니다.")

# ----------------------
# 안내
# ----------------------
st.success("✨ 오늘의 청소를 시작해보세요!")

# ----------------------
# 공지사항
# ----------------------
st.subheader("📢 공지사항")

for notice in notices:
    st.info(notice)

st.divider()

# ----------------------
# 청소 당번표
# ----------------------
st.subheader("👨‍🎓 오늘의 청소 당번")

col1, col2 = st.columns(2)

items = list(duty_assignments.items())

for idx, (area, number) in enumerate(items):

    text = f"🧹 **{area}**  \n담당 : {number}번"

    if idx % 2 == 0:
        with col1:
            st.write(text)
    else:
        with col2:
            st.write(text)

st.divider()

# ----------------------
# 체크리스트
# ----------------------
st.subheader("✅ 청소 완료 체크")

completed = 0
total = len(cleaning_areas)

try:

    for area in cleaning_areas:

        if st.checkbox(area):
            completed += 1

    progress = completed / total

    st.divider()

    st.metric(
        "청소 진행률",
        f"{completed}/{total}"
    )

    st.progress(progress)

    if completed == total:
        st.balloons()
        st.success("🎉 오늘 청소를 모두 완료했습니다!")

except Exception as error:
    st.error(f"오류가 발생했습니다: {error}")

st.divider()

st.markdown("""
### 🌟 우리반 청소 규칙

- 맡은 구역 책임감 있게 청소하기
- 쓰레기 분리수거 정확히 하기
- 의자와 책상 정리하기
- 청소 후 창문 확인하기

모두가 함께 만드는 깨끗한 교실!
""")
