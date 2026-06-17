import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="우리반 청소 도우미",
    page_icon="🏫",
    layout="wide"
)

# 데이터
NOTICES = [
    "📢 금요일은 특별 대청소가 있습니다.",
    "📢 분리수거함 정리를 꼼꼼히 해주세요.",
    "📢 창문 청소 시 안전에 주의하세요."
]

CLEANING_AREAS = {
    "교실 바닥": "김민준",
    "칠판 정리": "이서연",
    "창문 청소": "박지호",
    "분리수거": "최유진",
    "복도 청소": "정하준"
}

# 사이드바
menu = st.sidebar.radio(
    "메뉴",
    [
        "홈",
        "공지사항",
        "청소 당번표",
        "청소 체크리스트"
    ]
)

# 홈
if menu == "홈":

    st.title("🏫 우리반 청소 도우미")

    st.success("오늘도 깨끗한 교실을 만들어 봅시다!")

    st.subheader("📅 오늘의 청소 구역")

    for area in CLEANING_AREAS:
        st.write(f"• {area}")

    st.info(
        """
담당 구역을 확인한 후
청소 완료 시 체크리스트를 완료해주세요.
"""
    )

# 공지사항
elif menu == "공지사항":

    st.title("📢 공지사항")

    for notice in NOTICES:
        st.info(notice)

# 청소 당번표
elif menu == "청소 당번표":

    st.title("👨‍🎓 청소 당번표")

    for area, student in CLEANING_AREAS.items():
        st.write(f"**{area}** : {student}")

# 청소 체크리스트
elif menu == "청소 체크리스트":

    st.title("✅ 청소 체크리스트")

    completed = 0
    total = len(CLEANING_AREAS)

    try:
        for area in CLEANING_AREAS:

            if st.checkbox(area):
                completed += 1

        st.divider()

        progress = completed / total

        st.metric(
            "완료 현황",
            f"{completed}/{total}"
        )

        st.progress(progress)

        if completed == total:
            st.balloons()
            st.success("🎉 오늘 청소를 모두 완료했습니다!")

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")
