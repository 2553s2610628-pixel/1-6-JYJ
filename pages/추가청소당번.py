import streamlit as st
import random
import time

st.set_page_config(
    page_title="우리반 청소 당번 앱",
    page_icon="🧹",
    layout="centered"
)

st.title("🧹 우리반 청소 당번 앱")
st.markdown("### 결석자가 생기면 추가 청소 당번을 룰렛으로 뽑아보세요!")

# 기본 학생 명단
default_students = """김민준
이서준
박지호
최도윤
정예은
한지민
윤서연
강하준
오수아
김도현"""

st.subheader("1️⃣ 학생 명단 입력")

student_text = st.text_area(
    "한 줄에 한 명씩 입력",
    value=default_students,
    height=200
)

students = [s.strip() for s in student_text.split("\n") if s.strip()]

if len(students) < 2:
    st.warning("학생을 2명 이상 입력해주세요.")
    st.stop()

st.subheader("2️⃣ 오늘의 청소 당번")

cleaners = st.multiselect(
    "청소 당번 선택",
    students
)

if len(cleaners) == 0:
    st.info("청소 당번을 선택해주세요.")
    st.stop()

st.subheader("3️⃣ 결석한 청소 당번")

absent_cleaners = st.multiselect(
    "결석한 당번 선택",
    cleaners
)

missing_count = len(absent_cleaners)

if missing_count == 0:
    st.success("현재 결석한 청소 당번이 없습니다.")
    st.stop()

st.subheader("4️⃣ 추가 청소 당번 룰렛")

available_students = [
    s for s in students
    if s not in cleaners
]

if len(available_students) < missing_count:
    st.error(
        "추가 당번을 뽑을 학생 수가 부족합니다."
    )
    st.stop()

if st.button("🎡 룰렛 돌리기", use_container_width=True):

    roulette_area = st.empty()

    for _ in range(25):
        roulette_area.markdown(
            f"# 🎡 {random.choice(available_students)}"
        )
        time.sleep(0.08)

    selected = random.sample(
        available_students,
        missing_count
    )

    roulette_area.empty()

    st.balloons()

    st.success("추가 청소 당번이 선정되었습니다!")

    for i, student in enumerate(selected, start=1):
        st.markdown(
            f"### {i}. 🧹 {student}"
        )

    st.divider()

    st.subheader("최종 청소 당번")

    final_cleaners = [
        s for s in cleaners
        if s not in absent_cleaners
    ] + selected

    for student in final_cleaners:
        st.write(f"✅ {student}")

    st.info(
        f"결석자 {missing_count}명 → 추가 당번 {missing_count}명 선발 완료"
    )
