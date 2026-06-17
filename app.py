import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="우리반 청소 안내",
    page_icon="🧹",
    layout="wide"
)

# ------------------------
# Gemini 설정
# ------------------------
api_key = st.secrets.get("GEMINI_API_KEY", None)

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash-lite")
    except Exception:
        model = None
else:
    model = None

# ------------------------
# 공지사항 저장
# ------------------------
if "notices" not in st.session_state:
    st.session_state.notices = [
        "금요일은 특별 대청소가 진행됩니다.",
        "분리수거는 반드시 종류별로 구분해주세요."
    ]

# ------------------------
# 체크리스트
# ------------------------
checklist = [
    "책상 정리하기",
    "의자 정리하기",
    "바닥 쓰레기 줍기",
    "분리수거 하기",
    "창문 닫기 확인"
]

# ------------------------
# 제목
# ------------------------
st.title("🏫 우리반 청소 안내")

st.markdown("""
### 깨끗한 교실은 우리 모두의 책임입니다.

이 앱은 우리 반 학생들이 청소 활동에 적극적으로 참여할 수 있도록 만들어졌습니다.

#### 이용 방법
- 공지사항 확인
- 청소 체크리스트 활용
- AI 청소 도우미에게 질문하기
""")

st.divider()

# ------------------------
# 공지사항
# ------------------------
st.subheader("📢 공지사항")

for idx, notice in enumerate(st.session_state.notices):

    col1, col2 = st.columns([8, 1])

    with col1:
        st.info(notice)

    with col2:
        if st.button("❌", key=f"delete_{idx}"):
            st.session_state.notices.pop(idx)
            st.rerun()

new_notice = st.text_input(
    "새 공지 입력",
    placeholder="공지사항을 입력하세요"
)

if st.button("공지 추가"):

    if new_notice.strip():
        st.session_state.notices.append(new_notice.strip())
        st.success("공지사항이 추가되었습니다.")
        st.rerun()

st.divider()

# ------------------------
# 체크리스트
# ------------------------
st.subheader("✅ 청소 체크리스트")

completed = 0

for item in checklist:

    if st.checkbox(item):
        completed += 1

progress = completed / len(checklist)

st.metric(
    "완료 현황",
    f"{completed}/{len(checklist)}"
)

st.progress(progress)

if completed == len(checklist):
    st.balloons()
    st.success("🎉 모든 체크리스트를 완료했습니다!")

st.divider()

# ------------------------
# AI 청소 도우미
# ------------------------
st.subheader("🤖 AI 청소 도우미")

question = st.text_area(
    "궁금한 점을 입력하세요",
    placeholder="예) 칠판을 깨끗하게 지우는 방법은?"
)

if st.button("질문하기"):

    if not question.strip():
        st.warning("질문을 입력해주세요.")

    elif model is None:
        st.error(
            "AI를 사용할 수 없습니다.\n"
            "GEMINI_API_KEY가 설정되어 있는지 확인해주세요."
        )

    else:

        try:

            prompt = f"""
            당신은 학교 청소 도우미입니다.

            학생이 이해하기 쉽게 답변하세요.

            질문:
            {question}
            """

            response = model.generate_content(prompt)

            st.success("답변")

            st.write(response.text)

        except Exception as e:

            st.error(
                f"AI 응답 중 오류가 발생했습니다.\n{e}"
            )

st.divider()

st.caption("🧹 우리 모두가 함께 만드는 깨끗한 교실")
