import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="우리 반 청소 관리 앱",
    page_icon="🧹",
    layout="wide"
)

# 세션 상태 초기화
if "notices" not in st.session_state:
    st.session_state.notices = [
        "금요일은 대청소 날입니다.",
        "분리수거는 반드시 구분해서 버려주세요."
    ]

# 제목
st.title("🧹 우리 반 청소 관리 앱")
st.markdown("---")

# 사이드바
menu = st.sidebar.radio(
    "메뉴 선택",
    ["홈", "공지사항", "청소 체크리스트"]
)

# 홈 화면
if menu == "홈":

    st.header("📚 청소 앱 소개")

    st.info(
        """
        우리 반 청소 관리 앱에 오신 것을 환영합니다!

        이 앱은 학생들이 청소 활동을 쉽고 즐겁게 할 수 있도록 만들어졌습니다.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✨ 청소의 중요성")
        st.write(
            """
            - 깨끗한 환경에서 공부할 수 있어요.
            - 건강을 지킬 수 있어요.
            - 책임감과 협동심을 기를 수 있어요.
            """
        )

    with col2:
        st.subheader("🏫 오늘의 청소 구역")

        cleaning_areas = [
            "교실 바닥",
            "복도",
            "창문",
            "분리수거",
            "칠판 정리"
        ]

        for area in cleaning_areas:
            st.success(area)

    st.markdown("---")

    quotes = [
        "깨끗한 교실은 즐거운 학교생활의 시작입니다.",
        "작은 청소가 큰 변화를 만듭니다.",
        "함께 청소하면 더 빠르고 즐겁습니다.",
        "정리정돈은 좋은 습관입니다.",
        "오늘의 청소가 내일의 쾌적함을 만듭니다."
    ]

    st.subheader("🌟 오늘의 청소 한마디")
    st.warning(random.choice(quotes))

# 공지사항
elif menu == "공지사항":

    st.header("📢 청소 공지사항")

    with st.form("notice_form"):
        notice = st.text_input("새 공지 입력")
        submitted = st.form_submit_button("공지 추가")

        if submitted:
            if notice.strip():
                st.session_state.notices.insert(0, notice.strip())
                st.success("공지가 등록되었습니다.")
            else:
                st.error("공지 내용을 입력해주세요.")

    st.markdown("---")

    st.subheader("공지 목록")

    if st.session_state.notices:
        for idx, item in enumerate(st.session_state.notices, start=1):
            st.info(f"{idx}. {item}")
    else:
        st.warning("등록된 공지가 없습니다.")

# 체크리스트
elif menu == "청소 체크리스트":

    st.header("✅ 청소 체크리스트")

    tasks = [
        "바닥 쓸기",
        "쓰레기 버리기",
        "칠판 닦기",
        "창문 정리",
        "분리수거 정리"
    ]

    completed = 0

    for task in tasks:
        if st.checkbox(task):
            completed += 1

    total = len(tasks)

    st.markdown("---")

    st.subheader("📊 진행 상황")

    progress = completed / total
    st.progress(progress)

    st.write(f"완료: {completed} / {total}")

    if completed == total:
        st.balloons()
        st.success("🎉 모든 청소를 완료했습니다!")
