import streamlit as st

st.set_page_config(
    page_title="우리반 청소 안내",
    page_icon="🧹",
    layout="wide"
)

# -------------------
# 공지사항
# -------------------
notices = [
    "금요일은 특별 대청소가 진행됩니다.",
    "분리수거는 반드시 종류별로 구분해주세요.",
    "창문 청소 시 안전에 주의하세요."
]

# -------------------
# 체크리스트
# -------------------
checklist = [
    "책상 정리하기",
    "의자 정리하기",
    "바닥 쓰레기 줍기",
    "분리수거 하기",
    "창문 닫기 확인"
]

# -------------------
# 메인 화면
# -------------------
st.title("🏫 우리반 청소 안내")

st.markdown("""
### 깨끗한 교실은 우리 모두의 책임입니다.

이 앱은 우리 반 학생들이 청소 활동에 적극적으로 참여할 수 있도록 만들어졌습니다.

#### 이용 방법
1. 공지사항을 확인합니다.
2. 청소 체크리스트를 확인합니다.
3. 맡은 구역 청소를 진행합니다.
4. 완료된 항목을 체크합니다.

함께 깨끗한 교실을 만들어 봅시다!
""")

st.divider()

# -------------------
# 청소 팁
# -------------------
st.subheader("💡 오늘의 청소 팁")

st.info(
    "청소는 큰 곳보다 작은 곳부터 시작하면 더 빠르고 효율적으로 끝낼 수 있습니다."
)

st.divider()

# -------------------
# 공지사항
# -------------------
st.subheader("📢 공지사항")

for notice in notices:
    st.info(notice)

st.divider()

# -------------------
# 체크리스트
# -------------------
st.subheader("✅ 청소 체크리스트")

completed = 0
total = len(checklist)

try:

    for item in checklist:

        if st.checkbox(item):
            completed += 1

    progress = completed / total

    st.metric(
        "완료 현황",
        f"{completed}/{total}"
    )

    st.progress(progress)

    if completed == total:
        st.balloons()
        st.success("🎉 체크리스트를 모두 완료했습니다!")

except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")

st.divider()

st.caption("우리 모두가 함께 만드는 깨끗한 교실 🧹")
