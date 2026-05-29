import streamlit as st

st.title("🧹 청소당번 체크 앱")

st.write("청소를 안 한 학생을 확인합니다.")

# 학생 목록
students = [
    "민수",
    "지훈",
    "서연",
    "하은",
    "유진"
]

not_cleaned = []

st.subheader("청소 참여 체크")

for student in students:
    checked = st.checkbox(f"{student} 청소함")

    if not checked:
        not_cleaned.append(student)

st.divider()

st.subheader("결과")

if len(not_cleaned) == 0:
    st.success("모든 학생이 청소를 했습니다!")
else:
    st.error("청소 안 한 학생")

    for student in not_cleaned:
        st.write(f"❌ {student}")

    st.warning("추가 청소를 하게 하세요.")
